import json

class ServoConfig:
    def __init__(self, name, pin, up_angle=90, press_angle=45):
        self.name = name
        self.pin = pin
        self.up_angle = up_angle
        self.press_angle = press_angle

    def to_dict(self):
        return {
            "name": self.name,
            "pin": self.pin,
            "up_angle": self.up_angle,
            "press_angle": self.press_angle
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            pin=data["pin"],
            up_angle=data.get("up_angle", 90),
            press_angle=data.get("press_angle", 45)
        )


class Action:
    # Supported Actions
    TYPES = [
        "NONE", "LEFT", "RIGHT", "UP", "DOWN", "A",
        "BLINK_LEFT", "BLINK_RIGHT", "BLINK_UP", "BLINK_DOWN"
    ]

    def __init__(self, action_type="NONE", press_duration=200, delay_duration=500):
        self.action_type = action_type if action_type in self.TYPES else "NONE"
        self.press_duration = press_duration  # in ms
        self.delay_duration = delay_duration  # in ms

    def to_dict(self):
        return {
            "action_type": self.action_type,
            "press_duration": self.press_duration,
            "delay_duration": self.delay_duration
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            action_type=data.get("action_type", "NONE"),
            press_duration=data.get("press_duration", 200),
            delay_duration=data.get("delay_duration", 500)
        )


class RobotProfile:
    def __init__(self):
        # Default 6 servos as required
        self.servos = [
            ServoConfig("LEFT", 2, 90, 45),
            ServoConfig("RIGHT", 3, 90, 45),
            ServoConfig("UP", 4, 90, 45),
            ServoConfig("DOWN", 5, 90, 45),
            ServoConfig("SHIFT", 6, 90, 45),
            ServoConfig("A", 7, 90, 45),
        ]
        self.pattern = []  # List of Action objects
        
        # Loop Settings
        self.loop_mode = "INFINITY"  # "INFINITY" or "CUSTOM"
        self.loop_count = 1
        
        # Random Settings
        self.random_delay_enabled = False
        self.random_delay_min = 100
        self.random_delay_max = 1000
        
        # Auto Start Settings
        self.auto_start = False

    def to_dict(self):
        return {
            "servos": [s.to_dict() for s in self.servos],
            "pattern": [a.to_dict() for a in self.pattern],
            "loop_mode": self.loop_mode,
            "loop_count": self.loop_count,
            "random_delay_enabled": self.random_delay_enabled,
            "random_delay_min": self.random_delay_min,
            "random_delay_max": self.random_delay_max,
            "auto_start": self.auto_start
        }

    def load_from_dict(self, data):
        if "servos" in data:
            self.servos = [ServoConfig.from_dict(s) for s in data["servos"]]
        if "pattern" in data:
            self.pattern = [Action.from_dict(a) for a in data["pattern"]]
        self.loop_mode = data.get("loop_mode", "INFINITY")
        self.loop_count = data.get("loop_count", 1)
        self.random_delay_enabled = data.get("random_delay_enabled", False)
        self.random_delay_min = data.get("random_delay_min", 100)
        self.random_delay_max = data.get("random_delay_max", 1000)
        self.auto_start = data.get("auto_start", False)

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)

    def load_from_json(self, json_str):
        data = json.loads(json_str)
        self.load_from_dict(data)
