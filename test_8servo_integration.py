import sys
import os
from pathlib import Path

# Add the 8-servo app directory to the system path
sys.path.append(str(Path(__file__).parent))

from app.models import RobotProfile, Action
from app.connection import SerialConnectionManager
from app.auto_farm.controller import AutoFarmController

def run_tests():
    print("=== START INTEGRATION TESTS FOR 8-SERVO CONFIGURATION ===")

    # Test 1: Profile Initialization
    print("\n[Test 1] Profile & Action Types...")
    profile = RobotProfile()
    assert len(profile.servos) == 8, f"Expected 8 servos, got {len(profile.servos)}"
    expected_servo_names = ["LEFT", "RIGHT", "UP", "DOWN", "A", "SHIFT", "ALT", "SPACE"]
    for i, name in enumerate(expected_servo_names):
        assert profile.servos[i].name == name, f"Servo {i} name expected {name}, got {profile.servos[i].name}"
        assert profile.servos[i].pin == (i + 2), f"Servo {i} pin expected {i+2}, got {profile.servos[i].pin}"
    
    assert "SHIFT" in Action.TYPES
    assert "ALT" in Action.TYPES
    assert "SPACE" in Action.TYPES
    print("Test 1 Passed: 8 servos and new action types successfully initialized!")

    # Test 2: EEPROM config packing & parsing (SerialConnectionManager)
    print("\n[Test 2] EEPROM Config Serializer & Parser...")
    # Change some calibration values to test round-trip integrity
    for idx, s in enumerate(profile.servos):
        s.up_angle = 100 + idx
        s.press_angle = 30 + idx
    
    manager = SerialConnectionManager()
    
    # Simulating upload payload generation
    payload = bytearray()
    for servo in profile.servos:
        payload.append(int(servo.up_angle) & 0xFF)
        payload.append(int(servo.press_angle) & 0xFF)
    
    # Pad settings, pattern size, etc.
    payload.append(0) # auto_start
    payload.append(0) # loop_mode
    payload.extend(b"\x00\x01") # loop_count
    payload.append(0) # random_delay_enabled
    payload.extend(b"\x00\x64") # random_delay_min
    payload.extend(b"\x03\xe8") # random_delay_max
    payload.extend(b"\x00\x78") # blink_init_delay
    payload.extend(b"\x00\xc8") # blink_hold_delay
    payload.extend(b"\x00\x78") # blink_release_delay
    payload.append(0) # random_skip_enabled
    payload.append(0) # pattern size
    
    hex_str = payload.hex().upper()
    print(f"Generated Hex string: {hex_str[:32]}...")

    # Parse round-trip
    parsed_profile = RobotProfile()
    # The default parsed profile has default angles. Let's run parsing.
    manager.parse_config_hex(hex_str, parsed_profile)

    # Verify parsed values match
    for idx in range(8):
        assert parsed_profile.servos[idx].up_angle == 100 + idx, f"UP angle mismatch for servo {idx}"
        assert parsed_profile.servos[idx].press_angle == 30 + idx, f"Press angle mismatch for servo {idx}"
    print("Test 2 Passed: 16-byte calibration round-trip parsing matches perfectly!")

    # Test 3: Controller dynamic key mapping & physical servo routing
    print("\n[Test 3] Controller Key Mapping & Hardware Action Routing...")
    
    class MockConnection:
        def __init__(self):
            self.connected = True
            self.simulation_mode = False
            self.commands_sent = []
        def log(self, msg):
            pass
        def send_command(self, cmd):
            self.commands_sent.append(cmd)

    conn = MockConnection()
    # Set mock calibration
    profile = RobotProfile()
    for idx, s in enumerate(profile.servos):
        s.up_angle = 90
        s.press_angle = 45

    controller = AutoFarmController(conn, profile)
    controller.settings["rune_input_mode"] = "hardware"

    # Map tests:
    # 0: LEFT
    # 1: RIGHT
    # 2: UP
    # 3: DOWN
    # 4: A
    # 5: SHIFT
    # 6: ALT
    # 7: SPACE
    
    # 3a. Index check
    assert controller._get_servo_index_for_key("left") == 0
    assert controller._get_servo_index_for_key("puzzle_left") == 0
    assert controller._get_servo_index_for_key("right") == 1
    assert controller._get_servo_index_for_key("up") == 2
    assert controller._get_servo_index_for_key("down") == 3
    assert controller._get_servo_index_for_key("a") == 4
    
    # Custom key definitions
    controller.settings["interact_key"] = "space"
    controller.settings["blink_key"] = "shift"
    controller.settings["jump_key"] = "alt"
    
    assert controller._get_servo_index_for_key("interact") == 7
    assert controller._get_servo_index_for_key("blink") == 5
    assert controller._get_servo_index_for_key("jump") == 6

    # 3b. Keypress routing tests
    conn.commands_sent.clear()
    controller._press_key("interact")
    # interact maps to space -> Servo 7 -> Pin 9 -> angle 45 then 90
    assert len(conn.commands_sent) == 2
    assert conn.commands_sent[0] == "TEST_SERVO 7 45"
    assert conn.commands_sent[1] == "TEST_SERVO 7 90"

    conn.commands_sent.clear()
    controller._key_down("left")
    assert len(conn.commands_sent) == 1
    assert conn.commands_sent[0] == "TEST_SERVO 0 45"

    conn.commands_sent.clear()
    controller._key_up("left")
    assert len(conn.commands_sent) == 1
    assert conn.commands_sent[0] == "TEST_SERVO 0 90"

    conn.commands_sent.clear()
    controller._press_key("puzzle_up")
    assert len(conn.commands_sent) == 2
    assert conn.commands_sent[0] == "TEST_SERVO 2 45"
    assert conn.commands_sent[1] == "TEST_SERVO 2 90"
    
    print("Test 3 Passed: Key index mapping and physical hardware routing are fully verified!")

    print("\n=== ALL INTEGRATION TESTS PASSED SUCCESSFULLY! ===")

if __name__ == "__main__":
    run_tests()
