# Audit Report

## Syntax & Runtime Errors (pylint)

************* Module apply_fixes
apply_fixes.py:143:0: C0301: Line too long (155/100) (line-too-long)
apply_fixes.py:15:13: W1510: 'subprocess.run' used without explicitly defining the value for 'check'. (subprocess-run-check)
apply_fixes.py:134:13: W1510: 'subprocess.run' used without explicitly defining the value for 'check'. (subprocess-run-check)
apply_fixes.py:3:0: W0611: Unused import os (unused-import)
************* Module audit_report
audit_report.py:23:13: W1510: 'subprocess.run' used without explicitly defining the value for 'check'. (subprocess-run-check)
audit_report.py:47:0: R0914: Too many local variables (16/15) (too-many-locals)
audit_report.py:56:15: W0718: Catching too general exception Exception (broad-exception-caught)
audit_report.py:56:8: W0612: Unused variable 'e' (unused-variable)
audit_report.py:101:15: W0718: Catching too general exception Exception (broad-exception-caught)
audit_report.py:101:8: W0612: Unused variable 'e' (unused-variable)
audit_report.py:11:0: W0611: Unused import difflib (unused-import)
audit_report.py:12:0: W0611: Unused import os (unused-import)
************* Module check_image
check_image.py:9:0: C0301: Line too long (143/100) (line-too-long)
check_image.py:10:10: E1101: Module 'cv2' has no 'imread' member (no-member)
check_image.py:4:0: W0611: Unused Image imported from PIL (unused-import)
************* Module convert_vit_to_onnx
convert_vit_to_onnx.py:16:11: W0718: Catching too general exception Exception (broad-exception-caught)
convert_vit_to_onnx.py:18:8: W0107: Unnecessary pass statement (unnecessary-pass)
convert_vit_to_onnx.py:6:0: W0611: Unused numpy imported as np (unused-import)
************* Module debug_minimap_capture
debug_minimap_capture.py:77:0: C0301: Line too long (121/100) (line-too-long)
debug_minimap_capture.py:11:0: C0413: Import "from lazy_imports import lazy_import" should be placed at the top of the module (wrong-import-position)
debug_minimap_capture.py:15:0: C0413: Import "import time" should be placed at the top of the module (wrong-import-position)
debug_minimap_capture.py:16:0: C0413: Import "from pathlib import Path" should be placed at the top of the module (wrong-import-position)
debug_minimap_capture.py:18:0: C0413: Import "import cv2" should be placed at the top of the module (wrong-import-position)
debug_minimap_capture.py:19:0: C0413: Import "import mss" should be placed at the top of the module (wrong-import-position)
debug_minimap_capture.py:20:0: C0413: Import "import numpy as np" should be placed at the top of the module (wrong-import-position)
debug_minimap_capture.py:21:0: C0413: Import "import pygetwindow as gw" should be placed at the top of the module (wrong-import-position)
debug_minimap_capture.py:34:0: W0702: No exception type(s) specified (bare-except)
debug_minimap_capture.py:32:4: W0702: No exception type(s) specified (bare-except)
debug_minimap_capture.py:56:4: W0621: Redefining name 'w' from outer scope (line 96) (redefined-outer-name)
debug_minimap_capture.py:57:4: W0621: Redefining name 'h' from outer scope (line 96) (redefined-outer-name)
debug_minimap_capture.py:54:11: W0212: Access to a protected member _hWnd of a client class (protected-access)
debug_minimap_capture.py:85:16: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
debug_minimap_capture.py:85:36: E1101: Module 'cv2' has no 'COLOR_BGRA2BGR' member (no-member)
debug_minimap_capture.py:92:4: E1101: Module 'cv2' has no 'imwrite' member (no-member)
debug_minimap_capture.py:93:10: W1309: Using an f-string that does not have any interpolated variables (f-string-without-interpolation)
debug_minimap_capture.py:98:4: E1101: Module 'cv2' has no 'imwrite' member (no-member)
debug_minimap_capture.py:99:10: W1309: Using an f-string that does not have any interpolated variables (f-string-without-interpolation)
debug_minimap_capture.py:104:66: E1101: Module 'cv2' has no 'IMREAD_GRAYSCALE' member (no-member)
debug_minimap_capture.py:105:66: E1101: Module 'cv2' has no 'IMREAD_GRAYSCALE' member (no-member)
debug_minimap_capture.py:106:63: E1101: Module 'cv2' has no 'IMREAD_GRAYSCALE' member (no-member)
debug_minimap_capture.py:112:11: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
debug_minimap_capture.py:112:31: E1101: Module 'cv2' has no 'COLOR_BGR2GRAY' member (no-member)
debug_minimap_capture.py:118:16: E1101: Module 'cv2' has no 'matchTemplate' member (no-member)
debug_minimap_capture.py:118:66: E1101: Module 'cv2' has no 'TM_CCOEFF_NORMED' member (no-member)
debug_minimap_capture.py:119:27: E1101: Module 'cv2' has no 'minMaxLoc' member (no-member)
debug_minimap_capture.py:129:20: E1101: Module 'cv2' has no 'matchTemplate' member (no-member)
debug_minimap_capture.py:129:69: E1101: Module 'cv2' has no 'TM_CCOEFF_NORMED' member (no-member)
debug_minimap_capture.py:130:35: E1101: Module 'cv2' has no 'minMaxLoc' member (no-member)
debug_minimap_capture.py:145:11: R1716: Simplify chained comparison between the operands (chained-comparison)
debug_minimap_capture.py:146:18: W1309: Using an f-string that does not have any interpolated variables (f-string-without-interpolation)
debug_minimap_capture.py:150:12: E1101: Module 'cv2' has no 'imwrite' member (no-member)
debug_minimap_capture.py:151:18: W1309: Using an f-string that does not have any interpolated variables (f-string-without-interpolation)
debug_minimap_capture.py:155:16: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
debug_minimap_capture.py:155:38: E1101: Module 'cv2' has no 'COLOR_BGR2GRAY' member (no-member)
debug_minimap_capture.py:157:28: E1101: Module 'cv2' has no 'matchTemplate' member (no-member)
debug_minimap_capture.py:157:72: E1101: Module 'cv2' has no 'TM_CCOEFF_NORMED' member (no-member)
debug_minimap_capture.py:158:41: E1101: Module 'cv2' has no 'minMaxLoc' member (no-member)
debug_minimap_capture.py:172:18: W1309: Using an f-string that does not have any interpolated variables (f-string-without-interpolation)
debug_minimap_capture.py:175:14: W1309: Using an f-string that does not have any interpolated variables (f-string-without-interpolation)
debug_minimap_capture.py:15:0: C0411: standard import "time" should be placed before first party import "lazy_imports.lazy_import"  (wrong-import-order)
debug_minimap_capture.py:16:0: C0411: standard import "pathlib.Path" should be placed before first party import "lazy_imports.lazy_import"  (wrong-import-order)
debug_minimap_capture.py:18:0: C0411: third party import "cv2" should be placed before first party import "lazy_imports.lazy_import"  (wrong-import-order)
debug_minimap_capture.py:19:0: C0411: third party import "mss" should be placed before first party import "lazy_imports.lazy_import"  (wrong-import-order)
debug_minimap_capture.py:20:0: C0411: third party import "numpy" should be placed before first party import "lazy_imports.lazy_import"  (wrong-import-order)
debug_minimap_capture.py:21:0: C0411: third party import "pygetwindow" should be placed before first party import "lazy_imports.lazy_import"  (wrong-import-order)
debug_minimap_capture.py:15:0: W0611: Unused import time (unused-import)
debug_minimap_capture.py:102:4: W0611: Unused multi_match imported from app.auto_farm.utils (unused-import)
************* Module generate_wiring_pdf
generate_wiring_pdf.py:808:0: C0301: Line too long (102/100) (line-too-long)
generate_wiring_pdf.py:869:0: C0301: Line too long (106/100) (line-too-long)
generate_wiring_pdf.py:1021:0: C0301: Line too long (104/100) (line-too-long)
generate_wiring_pdf.py:1:0: C0302: Too many lines in module (1031/1000) (too-many-lines)
generate_wiring_pdf.py:40:0: C0103: Function name "S" doesn't conform to snake_case naming style (invalid-name)
generate_wiring_pdf.py:42:15: R1735: Consider using '{"fontName": 'Helvetica', "fontSize": 9, "leading": 13, "textColor": C_LIGHT, ... }' instead of a call to 'dict'. (use-dict-literal)
generate_wiring_pdf.py:68:0: C0103: Function name "HR" doesn't conform to snake_case naming style (invalid-name)
generate_wiring_pdf.py:116:4: W0237: Parameter 'availWidth' has been renamed to 'aW' in overriding 'ClearWiringDiagram.wrap' method (arguments-renamed)
generate_wiring_pdf.py:116:4: W0237: Parameter 'availHeight' has been renamed to 'aH' in overriding 'ClearWiringDiagram.wrap' method (arguments-renamed)
generate_wiring_pdf.py:116:19: W0613: Unused argument 'aW' (unused-argument)
generate_wiring_pdf.py:116:23: W0613: Unused argument 'aH' (unused-argument)
generate_wiring_pdf.py:120:4: R0914: Too many local variables (88/15) (too-many-locals)
generate_wiring_pdf.py:123:8: C0103: Variable name "W" doesn't conform to snake_case naming style (invalid-name)
generate_wiring_pdf.py:123:11: C0103: Variable name "H" doesn't conform to snake_case naming style (invalid-name)
generate_wiring_pdf.py:147:8: R0913: Too many arguments (8/5) (too-many-arguments)
generate_wiring_pdf.py:147:8: R0917: Too many positional arguments (8/5) (too-many-positional-arguments)
generate_wiring_pdf.py:154:8: R0913: Too many arguments (7/5) (too-many-arguments)
generate_wiring_pdf.py:154:8: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
generate_wiring_pdf.py:168:8: R0913: Too many arguments (6/5) (too-many-arguments)
generate_wiring_pdf.py:168:8: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
generate_wiring_pdf.py:175:8: C0103: Function name "wire_L" doesn't conform to snake_case naming style (invalid-name)
generate_wiring_pdf.py:175:8: R0913: Too many arguments (7/5) (too-many-arguments)
generate_wiring_pdf.py:175:8: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
generate_wiring_pdf.py:187:8: R0913: Too many arguments (6/5) (too-many-arguments)
generate_wiring_pdf.py:187:8: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
generate_wiring_pdf.py:195:8: R0913: Too many arguments (6/5) (too-many-arguments)
generate_wiring_pdf.py:195:8: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
generate_wiring_pdf.py:120:4: R0915: Too many statements (264/50) (too-many-statements)
generate_wiring_pdf.py:187:8: W0612: Unused variable 'badge' (unused-variable)
generate_wiring_pdf.py:195:8: W0612: Unused variable 'label_pin' (unused-variable)
generate_wiring_pdf.py:218:8: W0612: Unused variable 'left_comp_right' (unused-variable)
generate_wiring_pdf.py:273:12: W0612: Unused variable 'label_text' (unused-variable)
generate_wiring_pdf.py:481:23: W0612: Unused variable 'spin' (unused-variable)
generate_wiring_pdf.py:526:12: W0612: Unused variable 'mid_x' (unused-variable)
generate_wiring_pdf.py:737:0: R0915: Too many statements (59/50) (too-many-statements)
generate_wiring_pdf.py:9:0: W0611: Unused TA_LEFT imported from reportlab.lib.enums (unused-import)
************* Module setup_wallpaper
setup_wallpaper.py:51:11: W0718: Catching too general exception Exception (broad-exception-caught)
************* Module test_coordinates
test_coordinates.py:15:0: R0914: Too many local variables (39/15) (too-many-locals)
test_coordinates.py:21:14: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
test_coordinates.py:21:57: E1101: Module 'cv2' has no 'COLOR_RGB2BGR' member (no-member)
test_coordinates.py:22:4: C0103: Variable name "_REF_IMAGE" doesn't conform to snake_case naming style (invalid-name)
test_coordinates.py:23:14: E1101: Module 'cv2' has no 'imread' member (no-member)
test_coordinates.py:24:4: C0103: Variable name "_TPL_BOX" doesn't conform to snake_case naming style (invalid-name)
test_coordinates.py:35:4: C0103: Variable name "_REF_IMAGE" doesn't conform to snake_case naming style (invalid-name)
test_coordinates.py:36:4: C0103: Variable name "_TPL_BOX" doesn't conform to snake_case naming style (invalid-name)
test_coordinates.py:51:4: C0415: Import outside toplevel (torch.nn.functional) (import-outside-toplevel)
test_coordinates.py:53:12: E1102: F.conv2d is not callable (not-callable)
test_coordinates.py:55:4: C0103: Variable name "C" doesn't conform to snake_case naming style (invalid-name)
test_coordinates.py:55:7: C0103: Variable name "H" doesn't conform to snake_case naming style (invalid-name)
test_coordinates.py:55:10: C0103: Variable name "W" doesn't conform to snake_case naming style (invalid-name)
test_coordinates.py:58:12: E1102: F.conv2d is not callable (not-callable)
test_coordinates.py:59:13: E1102: F.conv2d is not callable (not-callable)
test_coordinates.py:55:7: W0612: Unused variable 'H' (unused-variable)
test_coordinates.py:55:10: W0612: Unused variable 'W' (unused-variable)
************* Module test_lie_detection
test_lie_detection.py:58:0: C0301: Line too long (136/100) (line-too-long)
test_lie_detection.py:75:0: C0301: Line too long (147/100) (line-too-long)
test_lie_detection.py:81:0: C0301: Line too long (101/100) (line-too-long)
test_lie_detection.py:11:0: R0914: Too many local variables (21/15) (too-many-locals)
test_lie_detection.py:33:14: E1101: Module 'cv2' has no 'imread' member (no-member)
test_lie_detection.py:33:31: E1101: Module 'cv2' has no 'IMREAD_GRAYSCALE' member (no-member)
test_lie_detection.py:44:21: E1101: Module 'cv2' has no 'imread' member (no-member)
test_lie_detection.py:44:45: E1101: Module 'cv2' has no 'IMREAD_GRAYSCALE' member (no-member)
test_lie_detection.py:69:33: E1101: Module 'cv2' has no 'resize' member (no-member)
test_lie_detection.py:70:63: E1101: Module 'cv2' has no 'INTER_LANCZOS4' member (no-member)
test_lie_detection.py:64:16: W0612: Unused variable 'h' (unused-variable)
test_lie_detection.py:6:0: W0611: Unused numpy imported as np (unused-import)
************* Module test_onnx_solver
test_onnx_solver.py:33:11: W0718: Catching too general exception Exception (broad-exception-caught)
test_onnx_solver.py:35:8: C0415: Import outside toplevel (traceback) (import-outside-toplevel)
************* Module test_roboflow
test_roboflow.py:21:0: C0301: Line too long (132/100) (line-too-long)
test_roboflow.py:25:0: C0301: Line too long (144/100) (line-too-long)
test_roboflow.py:12:0: C0413: Import "from app.auto_farm.rune_solver.roboflow_client import RoboflowClient" should be placed at the top of the module (wrong-import-position)
test_roboflow.py:39:11: W0718: Catching too general exception Exception (broad-exception-caught)
test_roboflow.py:47:11: W0718: Catching too general exception Exception (broad-exception-caught)
test_roboflow.py:44:45: E1101: Module 'PIL.Image' has no 'LANCZOS' member (no-member)
************* Module test_wide_search
test_wide_search.py:12:0: R0914: Too many local variables (24/15) (too-many-locals)
test_wide_search.py:15:14: E1101: Module 'cv2' has no 'imread' member (no-member)
test_wide_search.py:17:4: C0103: Variable name "_REF_IMAGE" doesn't conform to snake_case naming style (invalid-name)
test_wide_search.py:18:14: E1101: Module 'cv2' has no 'imread' member (no-member)
test_wide_search.py:19:4: C0103: Variable name "_TPL_BOX" doesn't conform to snake_case naming style (invalid-name)
test_wide_search.py:23:10: E1101: Module 'cv2' has no 'matchTemplate' member (no-member)
test_wide_search.py:23:42: E1101: Module 'cv2' has no 'TM_CCOEFF_NORMED' member (no-member)
test_wide_search.py:7:0: W0611: Unused Image imported from PIL (unused-import)
************* Module app.connection
app\connection.py:153:0: C0301: Line too long (101/100) (line-too-long)
app\connection.py:371:0: C0301: Line too long (102/100) (line-too-long)
app\connection.py:389:0: C0301: Line too long (107/100) (line-too-long)
app\connection.py:19:0: R0902: Too many instance attributes (11/7) (too-many-instance-attributes)
app\connection.py:99:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\connection.py:94:12: C0415: Import outside toplevel (random) (import-outside-toplevel)
app\connection.py:112:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\connection.py:114:16: W0107: Unnecessary pass statement (unnecessary-pass)
app\connection.py:112:12: W0612: Unused variable 'e' (unused-variable)
app\connection.py:133:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\connection.py:161:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\connection.py:237:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\connection.py:174:12: C0415: Import outside toplevel (random) (import-outside-toplevel)
app\connection.py:227:16: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
app\connection.py:347:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\connection.py:321:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
app\connection.py:366:4: R0913: Too many arguments (7/5) (too-many-arguments)
app\connection.py:366:4: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
app\connection.py:375:8: W0621: Redefining name 'time' from outer scope (line 5) (redefined-outer-name)
app\connection.py:370:8: W0105: String statement has no effect (pointless-string-statement)
app\connection.py:373:8: C0415: Import outside toplevel (os) (import-outside-toplevel)
app\connection.py:374:8: C0415: Import outside toplevel (subprocess) (import-outside-toplevel)
app\connection.py:375:8: W0404: Reimport 'time' (imported line 5) (reimported)
app\connection.py:375:8: C0415: Import outside toplevel (time) (import-outside-toplevel)
app\connection.py:499:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\connection.py:382:8: R0912: Too many branches (27/12) (too-many-branches)
app\connection.py:382:8: R0915: Too many statements (62/50) (too-many-statements)
app\connection.py:466:26: R1732: Consider using 'with' for resource-allocating operations (consider-using-with)
app\connection.py:366:4: R0915: Too many statements (70/50) (too-many-statements)
************* Module app.driver_manager
app\driver_manager.py:11:0: R0914: Too many local variables (21/15) (too-many-locals)
app\driver_manager.py:85:11: W0718: Catching too general exception Exception (broad-exception-caught)
app\driver_manager.py:48:8: C0415: Import outside toplevel (csv) (import-outside-toplevel)
app\driver_manager.py:49:8: C0415: Import outside toplevel (io) (import-outside-toplevel)
app\driver_manager.py:87:8: W0107: Unnecessary pass statement (unnecessary-pass)
app\driver_manager.py:85:4: W0612: Unused variable 'e' (unused-variable)
app\driver_manager.py:111:4: R0914: Too many local variables (19/15) (too-many-locals)
app\driver_manager.py:179:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\driver_manager.py:111:4: R0912: Too many branches (17/12) (too-many-branches)
app\driver_manager.py:156:26: W0612: Unused variable 'dirs' (unused-variable)
app\driver_manager.py:99:0: R0915: Too many statements (54/50) (too-many-statements)
************* Module app.main
app\main.py:109:0: C0301: Line too long (108/100) (line-too-long)
app\main.py:391:0: C0301: Line too long (101/100) (line-too-long)
app\main.py:7:7: W0718: Catching too general exception Exception (broad-exception-caught)
app\main.py:11:11: W0718: Catching too general exception Exception (broad-exception-caught)
app\main.py:11:4: W0621: Redefining name 'e' from outer scope (line 7) (redefined-outer-name)
app\main.py:13:8: W0107: Unnecessary pass statement (unnecessary-pass)
app\main.py:15:0: C0413: Import "import queue" should be placed at the top of the module (wrong-import-position)
app\main.py:16:0: C0413: Import "import time" should be placed at the top of the module (wrong-import-position)
app\main.py:17:0: C0413: Import "import tkinter as tk" should be placed at the top of the module (wrong-import-position)
app\main.py:18:0: C0413: Import "from tkinter import ttk" should be placed at the top of the module (wrong-import-position)
app\main.py:20:0: C0413: Import "from PIL import Image, ImageTk" should be placed at the top of the module (wrong-import-position)
app\main.py:22:0: C0413: Import "from app.connection import SerialConnectionManager" should be placed at the top of the module (wrong-import-position)
app\main.py:23:0: C0413: Import "from app.models import RobotProfile" should be placed at the top of the module (wrong-import-position)
app\main.py:24:0: C0413: Import "from app.tabs.auto_farm_firmware import AutoFarmFirmwareTab" should be placed at the top of the module (wrong-import-position)
app\main.py:25:0: C0413: Import "from app.tabs.dashboard import DashboardTab" should be placed at the top of the module (wrong-import-position)
app\main.py:26:0: C0413: Import "from app.tabs.pattern import PatternBuilderTab" should be placed at the top of the module (wrong-import-position)
app\main.py:27:0: C0413: Import "from app.tabs.profiles import ProfileManagerTab" should be placed at the top of the module (wrong-import-position)
app\main.py:28:0: C0413: Import "from app.tabs.robot_settings import RobotSettingsTab" should be placed at the top of the module (wrong-import-position)
app\main.py:45:8: C0415: Import outside toplevel (os) (import-outside-toplevel)
app\main.py:56:8: C0415: Import outside toplevel (os) (import-outside-toplevel)
app\main.py:65:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\main.py:78:32: W0212: Access to a protected member _resize_after_id of a client class (protected-access)
app\main.py:79:8: W0212: Access to a protected member _resize_after_id of a client class (protected-access)
app\main.py:81:4: R0914: Too many local variables (22/15) (too-many-locals)
app\main.py:128:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\main.py:138:0: R0902: Too many instance attributes (15/7) (too-many-instance-attributes)
app\main.py:339:21: R1714: Consider merging these comparisons with 'in' by using 'cls in (AutoFarmFirmwareTab, ProfileManagerTab)'. Use a set instead if elements are hashable. (consider-using-in)
app\main.py:352:23: W0718: Catching too general exception Exception (broad-exception-caught)
app\main.py:349:20: C0415: Import outside toplevel (pywinstyles) (import-outside-toplevel)
app\main.py:398:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\main.py:393:12: C0415: Import outside toplevel (pywinstyles) (import-outside-toplevel)
app\main.py:141:4: R0915: Too many statements (79/50) (too-many-statements)
app\main.py:437:12: W0612: Unused variable 'name' (unused-variable)
app\main.py:488:8: W0107: Unnecessary pass statement (unnecessary-pass)
************* Module app.models
app\models.py:77:0: R0902: Too many instance attributes (13/7) (too-many-instance-attributes)
************* Module app.auto_farm.capture
app\auto_farm\capture.py:121:0: C0301: Line too long (107/100) (line-too-long)
app\auto_farm\capture.py:146:0: C0301: Line too long (105/100) (line-too-long)
app\auto_farm\capture.py:211:0: C0301: Line too long (121/100) (line-too-long)
app\auto_farm\capture.py:212:0: C0301: Line too long (114/100) (line-too-long)
app\auto_farm\capture.py:223:0: C0301: Line too long (101/100) (line-too-long)
app\auto_farm\capture.py:251:0: C0301: Line too long (104/100) (line-too-long)
app\auto_farm\capture.py:268:0: C0301: Line too long (112/100) (line-too-long)
app\auto_farm\capture.py:322:0: C0301: Line too long (113/100) (line-too-long)
app\auto_farm\capture.py:326:0: C0301: Line too long (111/100) (line-too-long)
app\auto_farm\capture.py:6:0: C0413: Import "import threading" should be placed at the top of the module (wrong-import-position)
app\auto_farm\capture.py:7:0: C0413: Import "import time" should be placed at the top of the module (wrong-import-position)
app\auto_farm\capture.py:8:0: C0413: Import "from collections import deque" should be placed at the top of the module (wrong-import-position)
app\auto_farm\capture.py:10:0: C0413: Import "import cv2" should be placed at the top of the module (wrong-import-position)
app\auto_farm\capture.py:11:0: C0413: Import "import mss" should be placed at the top of the module (wrong-import-position)
app\auto_farm\capture.py:12:0: C0413: Import "import numpy as np" should be placed at the top of the module (wrong-import-position)
app\auto_farm\capture.py:13:0: C0413: Import "import pygetwindow as gw" should be placed at the top of the module (wrong-import-position)
app\auto_farm\capture.py:17:0: C0413: Import "from app.auto_farm.utils import load_image, multi_match" should be placed at the top of the module (wrong-import-position)
app\auto_farm\capture.py:23:7: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\capture.py:25:4: W0107: Unnecessary pass statement (unnecessary-pass)
app\auto_farm\capture.py:33:7: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\capture.py:29:66: E1101: Module 'cv2' has no 'IMREAD_GRAYSCALE' member (no-member)
app\auto_farm\capture.py:30:66: E1101: Module 'cv2' has no 'IMREAD_GRAYSCALE' member (no-member)
app\auto_farm\capture.py:31:63: E1101: Module 'cv2' has no 'IMREAD_GRAYSCALE' member (no-member)
app\auto_farm\capture.py:37:0: R0902: Too many instance attributes (12/7) (too-many-instance-attributes)
app\auto_farm\capture.py:122:15: W0212: Access to a protected member _hWnd of a client class (protected-access)
app\auto_farm\capture.py:144:4: R0914: Too many local variables (39/15) (too-many-locals)
app\auto_farm\capture.py:151:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\capture.py:157:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\capture.py:157:12: W0621: Redefining name 'e' from outer scope (line 151) (redefined-outer-name)
app\auto_farm\capture.py:181:23: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\capture.py:197:23: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\capture.py:278:23: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\capture.py:208:33: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
app\auto_farm\capture.py:208:58: E1101: Module 'cv2' has no 'COLOR_BGR2GRAY' member (no-member)
app\auto_farm\capture.py:217:32: E1101: Module 'cv2' has no 'matchTemplate' member (no-member)
app\auto_farm\capture.py:218:58: E1101: Module 'cv2' has no 'TM_CCOEFF_NORMED' member (no-member)
app\auto_farm\capture.py:220:43: E1101: Module 'cv2' has no 'minMaxLoc' member (no-member)
app\auto_farm\capture.py:243:32: E1101: Module 'cv2' has no 'matchTemplate' member (no-member)
app\auto_farm\capture.py:244:55: E1101: Module 'cv2' has no 'TM_CCOEFF_NORMED' member (no-member)
app\auto_farm\capture.py:246:47: E1101: Module 'cv2' has no 'minMaxLoc' member (no-member)
app\auto_farm\capture.py:269:23: R1716: Simplify chained comparison between the operands (chained-comparison)
app\auto_farm\capture.py:343:27: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\capture.py:316:44: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
app\auto_farm\capture.py:316:72: E1101: Module 'cv2' has no 'COLOR_BGRA2BGR' member (no-member)
app\auto_farm\capture.py:328:32: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
app\auto_farm\capture.py:328:54: E1101: Module 'cv2' has no 'COLOR_BGR2GRAY' member (no-member)
app\auto_farm\capture.py:332:44: E1101: Module 'cv2' has no 'matchTemplate' member (no-member)
app\auto_farm\capture.py:333:63: E1101: Module 'cv2' has no 'TM_CCOEFF_NORMED' member (no-member)
app\auto_farm\capture.py:335:53: E1101: Module 'cv2' has no 'minMaxLoc' member (no-member)
app\auto_farm\capture.py:348:24: C0415: Import outside toplevel (gc) (import-outside-toplevel)
app\auto_farm\capture.py:144:4: R0912: Too many branches (22/12) (too-many-branches)
app\auto_farm\capture.py:144:4: R0915: Too many statements (140/50) (too-many-statements)
app\auto_farm\capture.py:151:8: W0612: Unused variable 'e' (unused-variable)
app\auto_farm\capture.py:6:0: C0411: standard import "threading" should be placed before first party import "lazy_imports.lazy_import"  (wrong-import-order)
app\auto_farm\capture.py:7:0: C0411: standard import "time" should be placed before first party import "lazy_imports.lazy_import"  (wrong-import-order)
app\auto_farm\capture.py:8:0: C0411: standard import "collections.deque" should be placed before first party import "lazy_imports.lazy_import"  (wrong-import-order)
app\auto_farm\capture.py:10:0: C0411: third party import "cv2" should be placed before first party import "lazy_imports.lazy_import"  (wrong-import-order)
app\auto_farm\capture.py:11:0: C0411: third party import "mss" should be placed before first party import "lazy_imports.lazy_import"  (wrong-import-order)
app\auto_farm\capture.py:12:0: C0411: third party import "numpy" should be placed before first party import "lazy_imports.lazy_import"  (wrong-import-order)
app\auto_farm\capture.py:13:0: C0411: third party import "pygetwindow" should be placed before first party import "lazy_imports.lazy_import"  (wrong-import-order)
app\auto_farm\capture.py:17:0: W0611: Unused multi_match imported from app.auto_farm.utils (unused-import)
************* Module app.auto_farm.controller
app\auto_farm\controller.py:47:0: C0301: Line too long (122/100) (line-too-long)
app\auto_farm\controller.py:61:0: C0301: Line too long (106/100) (line-too-long)
app\auto_farm\controller.py:67:0: C0301: Line too long (103/100) (line-too-long)
app\auto_farm\controller.py:202:0: C0301: Line too long (124/100) (line-too-long)
app\auto_farm\controller.py:214:0: C0301: Line too long (124/100) (line-too-long)
app\auto_farm\controller.py:230:0: C0301: Line too long (117/100) (line-too-long)
app\auto_farm\controller.py:316:0: C0301: Line too long (110/100) (line-too-long)
app\auto_farm\controller.py:337:0: C0301: Line too long (110/100) (line-too-long)
app\auto_farm\controller.py:464:0: C0301: Line too long (118/100) (line-too-long)
app\auto_farm\controller.py:532:0: C0301: Line too long (205/100) (line-too-long)
app\auto_farm\controller.py:546:0: C0301: Line too long (107/100) (line-too-long)
app\auto_farm\controller.py:554:0: C0301: Line too long (118/100) (line-too-long)
app\auto_farm\controller.py:586:0: C0301: Line too long (131/100) (line-too-long)
app\auto_farm\controller.py:595:0: C0301: Line too long (120/100) (line-too-long)
app\auto_farm\controller.py:643:0: C0301: Line too long (110/100) (line-too-long)
app\auto_farm\controller.py:713:0: C0301: Line too long (132/100) (line-too-long)
app\auto_farm\controller.py:739:0: C0301: Line too long (131/100) (line-too-long)
app\auto_farm\controller.py:769:0: C0301: Line too long (106/100) (line-too-long)
app\auto_farm\controller.py:775:0: C0301: Line too long (115/100) (line-too-long)
app\auto_farm\controller.py:853:0: C0301: Line too long (104/100) (line-too-long)
app\auto_farm\controller.py:862:0: C0301: Line too long (110/100) (line-too-long)
app\auto_farm\controller.py:870:0: C0301: Line too long (121/100) (line-too-long)
app\auto_farm\controller.py:878:0: C0301: Line too long (105/100) (line-too-long)
app\auto_farm\controller.py:886:0: C0301: Line too long (109/100) (line-too-long)
app\auto_farm\controller.py:915:0: C0301: Line too long (104/100) (line-too-long)
app\auto_farm\controller.py:931:0: C0301: Line too long (126/100) (line-too-long)
app\auto_farm\controller.py:939:0: C0301: Line too long (121/100) (line-too-long)
app\auto_farm\controller.py:947:0: C0301: Line too long (105/100) (line-too-long)
app\auto_farm\controller.py:984:0: C0301: Line too long (147/100) (line-too-long)
app\auto_farm\controller.py:1110:0: C0301: Line too long (115/100) (line-too-long)
app\auto_farm\controller.py:1:0: C0302: Too many lines in module (1114/1000) (too-many-lines)
app\auto_farm\controller.py:16:0: R0402: Use 'from app.auto_farm import vkeys' instead (consider-using-from-import)
app\auto_farm\controller.py:69:7: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\controller.py:35:20: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
app\auto_farm\controller.py:35:52: E1101: Module 'cv2' has no 'COLOR_BGR2GRAY' member (no-member)
app\auto_farm\controller.py:37:61: E1101: Module 'cv2' has no 'IMREAD_GRAYSCALE' member (no-member)
app\auto_farm\controller.py:38:61: E1101: Module 'cv2' has no 'IMREAD_GRAYSCALE' member (no-member)
app\auto_farm\controller.py:41:52: E1101: Module 'cv2' has no 'IMREAD_GRAYSCALE' member (no-member)
app\auto_farm\controller.py:42:54: E1101: Module 'cv2' has no 'IMREAD_GRAYSCALE' member (no-member)
app\auto_farm\controller.py:65:11: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\controller.py:73:0: R0902: Too many instance attributes (15/7) (too-many-instance-attributes)
app\auto_farm\controller.py:101:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\controller.py:121:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\controller.py:118:21: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
app\auto_farm\controller.py:123:16: W0107: Unnecessary pass statement (unnecessary-pass)
app\auto_farm\controller.py:121:12: W0612: Unused variable 'e' (unused-variable)
app\auto_farm\controller.py:131:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\controller.py:129:17: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
app\auto_farm\controller.py:172:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\controller.py:138:23: W0212: Access to a protected member _hWnd of a client class (protected-access)
app\auto_farm\controller.py:139:16: C0415: Import outside toplevel (win32api) (import-outside-toplevel)
app\auto_farm\controller.py:140:16: C0415: Import outside toplevel (win32con) (import-outside-toplevel)
app\auto_farm\controller.py:141:16: C0415: Import outside toplevel (win32gui) (import-outside-toplevel)
app\auto_farm\controller.py:142:16: C0415: Import outside toplevel (win32process) (import-outside-toplevel)
app\auto_farm\controller.py:145:34: I1101: Module 'win32gui' has no 'GetForegroundWindow' member, but source is unavailable. Consider adding this module to extension-pkg-allow-list if you want to perform analysis based on run-time introspection of living objects. (c-extension-no-member)
app\auto_farm\controller.py:151:23: I1101: Module 'win32gui' has no 'IsIconic' member, but source is unavailable. Consider adding this module to extension-pkg-allow-list if you want to perform analysis based on run-time introspection of living objects. (c-extension-no-member)
app\auto_farm\controller.py:152:24: I1101: Module 'win32gui' has no 'ShowWindow' member, but source is unavailable. Consider adding this module to extension-pkg-allow-list if you want to perform analysis based on run-time introspection of living objects. (c-extension-no-member)
app\auto_farm\controller.py:166:27: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\controller.py:157:38: I1101: Module 'win32process' has no 'GetWindowThreadProcessId' member, but source is unavailable. Consider adding this module to extension-pkg-allow-list if you want to perform analysis based on run-time introspection of living objects. (c-extension-no-member)
app\auto_farm\controller.py:158:37: I1101: Module 'win32api' has no 'GetCurrentThreadId' member, but source is unavailable. Consider adding this module to extension-pkg-allow-list if you want to perform analysis based on run-time introspection of living objects. (c-extension-no-member)
app\auto_farm\controller.py:160:28: I1101: Module 'win32process' has no 'AttachThreadInput' member, but source is unavailable. Consider adding this module to extension-pkg-allow-list if you want to perform analysis based on run-time introspection of living objects. (c-extension-no-member)
app\auto_farm\controller.py:161:28: I1101: Module 'win32gui' has no 'BringWindowToTop' member, but source is unavailable. Consider adding this module to extension-pkg-allow-list if you want to perform analysis based on run-time introspection of living objects. (c-extension-no-member)
app\auto_farm\controller.py:162:28: I1101: Module 'win32gui' has no 'SetForegroundWindow' member, but source is unavailable. Consider adding this module to extension-pkg-allow-list if you want to perform analysis based on run-time introspection of living objects. (c-extension-no-member)
app\auto_farm\controller.py:163:28: I1101: Module 'win32process' has no 'AttachThreadInput' member, but source is unavailable. Consider adding this module to extension-pkg-allow-list if you want to perform analysis based on run-time introspection of living objects. (c-extension-no-member)
app\auto_farm\controller.py:165:28: I1101: Module 'win32gui' has no 'SetForegroundWindow' member, but source is unavailable. Consider adding this module to extension-pkg-allow-list if you want to perform analysis based on run-time introspection of living objects. (c-extension-no-member)
app\auto_farm\controller.py:169:24: I1101: Module 'win32gui' has no 'SetForegroundWindow' member, but source is unavailable. Consider adding this module to extension-pkg-allow-list if you want to perform analysis based on run-time introspection of living objects. (c-extension-no-member)
app\auto_farm\controller.py:166:20: W0612: Unused variable 'e' (unused-variable)
app\auto_farm\controller.py:182:8: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
app\auto_farm\controller.py:176:4: R0911: Too many return statements (7/6) (too-many-return-statements)
app\auto_farm\controller.py:284:12: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
app\auto_farm\controller.py:308:23: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\controller.py:310:20: W0107: Unnecessary pass statement (unnecessary-pass)
app\auto_farm\controller.py:308:16: W0612: Unused variable 'e' (unused-variable)
app\auto_farm\controller.py:405:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\controller.py:387:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\controller.py:383:16: C0415: Import outside toplevel (win32api) (import-outside-toplevel)
app\auto_farm\controller.py:386:20: I1101: Module 'win32api' has no 'keybd_event' member, but source is unavailable. Consider adding this module to extension-pkg-allow-list if you want to perform analysis based on run-time introspection of living objects. (c-extension-no-member)
app\auto_farm\controller.py:402:16: C0415: Import outside toplevel (winsound) (import-outside-toplevel)
app\auto_farm\controller.py:413:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\controller.py:415:12: W0107: Unnecessary pass statement (unnecessary-pass)
app\auto_farm\controller.py:413:8: W0612: Unused variable 'e' (unused-variable)
app\auto_farm\controller.py:426:12: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
app\auto_farm\controller.py:426:36: E1101: Module 'cv2' has no 'COLOR_BGR2GRAY' member (no-member)
app\auto_farm\controller.py:447:15: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
app\auto_farm\controller.py:447:38: E1101: Module 'cv2' has no 'COLOR_BGR2GRAY' member (no-member)
app\auto_farm\controller.py:469:4: R0914: Too many local variables (33/15) (too-many-locals)
app\auto_farm\controller.py:491:23: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\controller.py:538:23: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\controller.py:507:44: E1101: Module 'cv2' has no 'resize' member (no-member)
app\auto_farm\controller.py:510:42: E1101: Module 'cv2' has no 'INTER_LANCZOS4' member (no-member)
app\auto_farm\controller.py:516:44: E1101: Module 'cv2' has no 'resize' member (no-member)
app\auto_farm\controller.py:519:42: E1101: Module 'cv2' has no 'INTER_LANCZOS4' member (no-member)
app\auto_farm\controller.py:527:37: E1101: Module 'cv2' has no 'resize' member (no-member)
app\auto_farm\controller.py:528:67: E1101: Module 'cv2' has no 'INTER_LANCZOS4' member (no-member)
app\auto_farm\controller.py:549:32: E1101: Module 'cv2' has no 'resize' member (no-member)
app\auto_farm\controller.py:550:63: E1101: Module 'cv2' has no 'INTER_AREA' member (no-member)
app\auto_farm\controller.py:552:29: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
app\auto_farm\controller.py:552:57: E1101: Module 'cv2' has no 'COLOR_BGR2GRAY' member (no-member)
app\auto_farm\controller.py:573:41: E1101: Module 'cv2' has no 'resize' member (no-member)
app\auto_farm\controller.py:574:67: E1101: Module 'cv2' has no 'INTER_LANCZOS4' member (no-member)
app\auto_farm\controller.py:471:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
app\auto_farm\controller.py:578:24: R1731: Consider using 'max_score = max(max_score, score)' instead of unnecessary if block (consider-using-max-builtin)
app\auto_farm\controller.py:627:25: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
app\auto_farm\controller.py:627:45: E1101: Module 'cv2' has no 'COLOR_BGR2GRAY' member (no-member)
app\auto_farm\controller.py:469:4: R0912: Too many branches (29/12) (too-many-branches)
app\auto_farm\controller.py:469:4: R0915: Too many statements (115/50) (too-many-statements)
app\auto_farm\controller.py:639:12: W0612: Unused variable 'app' (unused-variable)
app\auto_farm\controller.py:662:4: R0914: Too many local variables (44/15) (too-many-locals)
app\auto_farm\controller.py:952:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\controller.py:715:27: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\controller.py:709:24: E1101: Module 'cv2' has no 'imwrite' member (no-member)
app\auto_farm\controller.py:741:27: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\controller.py:735:24: E1101: Module 'cv2' has no 'imwrite' member (no-member)
app\auto_farm\controller.py:771:27: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\controller.py:762:38: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
app\auto_farm\controller.py:762:60: E1101: Module 'cv2' has no 'COLOR_BGRA2BGR' member (no-member)
app\auto_farm\controller.py:767:24: E1101: Module 'cv2' has no 'imwrite' member (no-member)
app\auto_farm\controller.py:810:34: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
app\auto_farm\controller.py:810:56: E1101: Module 'cv2' has no 'COLOR_BGRA2BGR' member (no-member)
app\auto_farm\controller.py:828:28: R1731: Consider using 'best_score = max(best_score, score)' instead of unnecessary if block (consider-using-max-builtin)
app\auto_farm\controller.py:664:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
app\auto_farm\controller.py:836:20: C0415: Import outside toplevel (collections.Counter) (import-outside-toplevel)
app\auto_farm\controller.py:957:12: C0415: Import outside toplevel (gc) (import-outside-toplevel)
app\auto_farm\controller.py:965:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\controller.py:961:16: C0415: Import outside toplevel (torch) (import-outside-toplevel)
app\auto_farm\controller.py:967:16: W0107: Unnecessary pass statement (unnecessary-pass)
app\auto_farm\controller.py:662:4: R0912: Too many branches (30/12) (too-many-branches)
app\auto_farm\controller.py:662:4: R0915: Too many statements (178/50) (too-many-statements)
app\auto_farm\controller.py:867:24: W0612: Unused variable 'py' (unused-variable)
app\auto_farm\controller.py:969:4: R0912: Too many branches (19/12) (too-many-branches)
app\auto_farm\controller.py:969:4: R0915: Too many statements (94/50) (too-many-statements)
app\auto_farm\controller.py:969:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app\auto_farm\controller.py:593:20: W0201: Attribute 'last_lie_log_time' defined outside __init__ (attribute-defined-outside-init)
app\auto_farm\controller.py:48:8: W0611: Unused import glob (unused-import)
************* Module app.auto_farm.utils
app\auto_farm\utils.py:14:28: W0212: Access to a protected member _MEIPASS of a client class (protected-access)
app\auto_farm\utils.py:18:27: E1101: Module 'cv2' has no 'IMREAD_COLOR' member (no-member)
app\auto_farm\utils.py:21:10: E1101: Module 'cv2' has no 'imread' member (no-member)
app\auto_farm\utils.py:35:15: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
app\auto_farm\utils.py:35:35: E1101: Module 'cv2' has no 'COLOR_BGR2GRAY' member (no-member)
app\auto_farm\utils.py:41:11: E0712: Catching an exception which doesn't inherit from Exception: cv2.error (catching-non-exception)
app\auto_farm\utils.py:40:17: E1101: Module 'cv2' has no 'matchTemplate' member (no-member)
app\auto_farm\utils.py:40:51: E1101: Module 'cv2' has no 'TM_CCOEFF_NORMED' member (no-member)
app\auto_farm\utils.py:67:11: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\utils.py:62:19: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
app\auto_farm\utils.py:62:39: E1101: Module 'cv2' has no 'COLOR_BGR2GRAY' member (no-member)
app\auto_farm\utils.py:65:17: E1101: Module 'cv2' has no 'matchTemplate' member (no-member)
app\auto_farm\utils.py:65:51: E1101: Module 'cv2' has no 'TM_CCOEFF_NORMED' member (no-member)
app\auto_farm\utils.py:67:4: W0612: Unused variable 'e' (unused-variable)
app\auto_farm\utils.py:74:10: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
app\auto_farm\utils.py:74:28: E1101: Module 'cv2' has no 'COLOR_BGR2HSV' member (no-member)
app\auto_farm\utils.py:75:11: E1101: Module 'cv2' has no 'inRange' member (no-member)
app\auto_farm\utils.py:77:15: E1101: Module 'cv2' has no 'bitwise_or' member (no-member)
app\auto_farm\utils.py:77:36: E1101: Module 'cv2' has no 'inRange' member (no-member)
************* Module app.auto_farm.vkeys
app\auto_farm\vkeys.py:1:0: C0301: Line too long (104/100) (line-too-long)
app\auto_farm\vkeys.py:204:0: C0301: Line too long (127/100) (line-too-long)
app\auto_farm\vkeys.py:32:0: C0103: Constant name "_pynput_initialized" doesn't conform to UPPER_CASE naming style (invalid-name)
app\auto_farm\vkeys.py:33:0: C0103: Constant name "keyboard" doesn't conform to UPPER_CASE naming style (invalid-name)
app\auto_farm\vkeys.py:56:12: W0621: Redefining name 'c' from outer scope (line 23) (redefined-outer-name)
app\auto_farm\vkeys.py:37:4: W0603: Using the global statement (global-statement)
app\auto_farm\vkeys.py:58:11: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\vkeys.py:41:8: C0415: Import outside toplevel (pynput.keyboard.Controller, pynput.keyboard.Key) (import-outside-toplevel)
app\auto_farm\vkeys.py:77:4: R0903: Too few public methods (0/2) (too-few-public-methods)
app\auto_farm\vkeys.py:88:4: R0903: Too few public methods (0/2) (too-few-public-methods)
app\auto_farm\vkeys.py:100:4: R0903: Too few public methods (0/2) (too-few-public-methods)
app\auto_farm\vkeys.py:109:4: R0903: Too few public methods (0/2) (too-few-public-methods)
app\auto_farm\vkeys.py:114:4: R0903: Too few public methods (0/2) (too-few-public-methods)
app\auto_farm\vkeys.py:145:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\vkeys.py:151:26: W0613: Unused argument 'vk_code' (unused-argument)
app\auto_farm\vkeys.py:151:35: W0613: Unused argument 'is_up' (unused-argument)
app\auto_farm\vkeys.py:151:48: W0613: Unused argument 'is_extended' (unused-argument)
app\auto_farm\vkeys.py:174:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\vkeys.py:197:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\vkeys.py:207:4: C0415: Import outside toplevel (random) (import-outside-toplevel)
app\auto_farm\vkeys.py:212:8: R1731: Consider using 'actual_down = max(actual_down, 0.01)' instead of unnecessary if block (consider-using-max-builtin)
app\auto_farm\vkeys.py:221:8: R1731: Consider using 'actual_up = max(actual_up, 0.01)' instead of unnecessary if block (consider-using-max-builtin)
************* Module app.auto_farm.rune_solver.hybrid_solver
app\auto_farm\rune_solver\hybrid_solver.py:92:0: C0301: Line too long (104/100) (line-too-long)
app\auto_farm\rune_solver\hybrid_solver.py:118:0: C0301: Line too long (110/100) (line-too-long)
app\auto_farm\rune_solver\hybrid_solver.py:124:0: C0301: Line too long (108/100) (line-too-long)
app\auto_farm\rune_solver\hybrid_solver.py:47:12: C0415: Import outside toplevel (data_vit.build_transforms) (import-outside-toplevel)
app\auto_farm\rune_solver\hybrid_solver.py:54:8: C0415: Import outside toplevel (torch) (import-outside-toplevel)
app\auto_farm\rune_solver\hybrid_solver.py:54:8: W0611: Unused import torch (unused-import)
app\auto_farm\rune_solver\hybrid_solver.py:70:4: R0914: Too many local variables (19/15) (too-many-locals)
app\auto_farm\rune_solver\hybrid_solver.py:73:12: C0415: Import outside toplevel (vit_solver.ViTSolver) (import-outside-toplevel)
app\auto_farm\rune_solver\hybrid_solver.py:75:20: W0212: Access to a protected member _proportional_resize_center_crop of a client class (protected-access)
app\auto_farm\rune_solver\hybrid_solver.py:121:8: C0415: Import outside toplevel (torch) (import-outside-toplevel)
app\auto_farm\rune_solver\hybrid_solver.py:70:40: W0613: Unused argument 'save_debug' (unused-argument)
app\auto_farm\rune_solver\hybrid_solver.py:19:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module app.auto_farm.rune_solver.panel_detect
app\auto_farm\rune_solver\panel_detect.py:73:0: C0301: Line too long (104/100) (line-too-long)
app\auto_farm\rune_solver\panel_detect.py:124:0: C0325: Unnecessary parens after 'not' keyword (superfluous-parens)
app\auto_farm\rune_solver\panel_detect.py:126:0: C0325: Unnecessary parens after 'not' keyword (superfluous-parens)
app\auto_farm\rune_solver\panel_detect.py:39:0: R0914: Too many local variables (21/15) (too-many-locals)
app\auto_farm\rune_solver\panel_detect.py:41:10: E1101: Module 'cv2' has no 'matchTemplate' member (no-member)
app\auto_farm\rune_solver\panel_detect.py:41:44: E1101: Module 'cv2' has no 'TM_CCOEFF_NORMED' member (no-member)
app\auto_farm\rune_solver\panel_detect.py:70:0: R0914: Too many local variables (17/15) (too-many-locals)
app\auto_farm\rune_solver\panel_detect.py:74:10: E1101: Module 'cv2' has no 'matchTemplate' member (no-member)
app\auto_farm\rune_solver\panel_detect.py:74:44: E1101: Module 'cv2' has no 'TM_CCOEFF_NORMED' member (no-member)
app\auto_farm\rune_solver\panel_detect.py:99:0: R0914: Too many local variables (50/15) (too-many-locals)
app\auto_farm\rune_solver\panel_detect.py:102:14: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
app\auto_farm\rune_solver\panel_detect.py:102:57: E1101: Module 'cv2' has no 'COLOR_RGB2BGR' member (no-member)
app\auto_farm\rune_solver\panel_detect.py:105:14: E1101: Module 'cv2' has no 'imread' member (no-member)
app\auto_farm\rune_solver\panel_detect.py:117:8: C0103: Variable name "L" doesn't conform to snake_case naming style (invalid-name)
app\auto_farm\rune_solver\panel_detect.py:120:8: C0103: Variable name "L" doesn't conform to snake_case naming style (invalid-name)
app\auto_farm\rune_solver\panel_detect.py:125:8: C0103: Variable name "L" doesn't conform to snake_case naming style (invalid-name)
app\auto_farm\rune_solver\panel_detect.py:131:8: C0103: Variable name "R" doesn't conform to snake_case naming style (invalid-name)
app\auto_farm\rune_solver\panel_detect.py:134:8: C0103: Variable name "R" doesn't conform to snake_case naming style (invalid-name)
app\auto_farm\rune_solver\panel_detect.py:138:8: C0103: Variable name "R" doesn't conform to snake_case naming style (invalid-name)
app\auto_farm\rune_solver\panel_detect.py:142:10: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
app\auto_farm\rune_solver\panel_detect.py:142:32: E1101: Module 'cv2' has no 'COLOR_BGR2HSV' member (no-member)
app\auto_farm\rune_solver\panel_detect.py:145:11: E1101: Module 'cv2' has no 'inRange' member (no-member)
app\auto_farm\rune_solver\panel_detect.py:147:18: E1101: Module 'cv2' has no 'findContours' member (no-member)
app\auto_farm\rune_solver\panel_detect.py:147:41: E1101: Module 'cv2' has no 'RETR_EXTERNAL' member (no-member)
app\auto_farm\rune_solver\panel_detect.py:147:60: E1101: Module 'cv2' has no 'CHAIN_APPROX_SIMPLE' member (no-member)
app\auto_farm\rune_solver\panel_detect.py:154:15: E1101: Module 'cv2' has no 'contourArea' member (no-member)
app\auto_farm\rune_solver\panel_detect.py:156:25: E1101: Module 'cv2' has no 'boundingRect' member (no-member)
app\auto_farm\rune_solver\panel_detect.py:228:4: C0103: Variable name "H_img" doesn't conform to snake_case naming style (invalid-name)
app\auto_farm\rune_solver\panel_detect.py:228:11: C0103: Variable name "W_img" doesn't conform to snake_case naming style (invalid-name)
app\auto_farm\rune_solver\panel_detect.py:99:0: R0912: Too many branches (26/12) (too-many-branches)
app\auto_farm\rune_solver\panel_detect.py:99:0: R0915: Too many statements (78/50) (too-many-statements)
app\auto_farm\rune_solver\panel_detect.py:133:13: W0612: Unused variable 'ry' (unused-variable)
************* Module app.auto_farm.rune_solver.roboflow_client
app\auto_farm\rune_solver\roboflow_client.py:90:0: C0301: Line too long (110/100) (line-too-long)
app\auto_farm\rune_solver\roboflow_client.py:113:0: C0301: Line too long (126/100) (line-too-long)
app\auto_farm\rune_solver\roboflow_client.py:149:0: C0301: Line too long (103/100) (line-too-long)
app\auto_farm\rune_solver\roboflow_client.py:155:0: C0301: Line too long (102/100) (line-too-long)
app\auto_farm\rune_solver\roboflow_client.py:157:0: C0301: Line too long (104/100) (line-too-long)
app\auto_farm\rune_solver\roboflow_client.py:25:4: R0913: Too many arguments (7/5) (too-many-arguments)
app\auto_farm\rune_solver\roboflow_client.py:25:4: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
app\auto_farm\rune_solver\roboflow_client.py:92:20: R1724: Unnecessary "else" after "continue", remove the "else" and de-indent the code inside it (no-else-continue)
app\auto_farm\rune_solver\roboflow_client.py:103:27: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\rune_solver\roboflow_client.py:115:24: R1724: Unnecessary "else" after "continue", remove the "else" and de-indent the code inside it (no-else-continue)
app\auto_farm\rune_solver\roboflow_client.py:139:31: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\rune_solver\roboflow_client.py:65:4: R0912: Too many branches (18/12) (too-many-branches)
app\auto_farm\rune_solver\roboflow_client.py:65:4: R0915: Too many statements (56/50) (too-many-statements)
app\auto_farm\rune_solver\roboflow_client.py:103:20: W0612: Unused variable 'e' (unused-variable)
app\auto_farm\rune_solver\roboflow_client.py:22:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module app.auto_farm.rune_solver.solver
app\auto_farm\rune_solver\solver.py:72:0: C0301: Line too long (119/100) (line-too-long)
app\auto_farm\rune_solver\solver.py:39:12: C0415: Import outside toplevel (vit_solver.ViTSolver) (import-outside-toplevel)
app\auto_farm\rune_solver\solver.py:63:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\rune_solver\solver.py:51:16: C0415: Import outside toplevel (hybrid_solver.HybridSolver) (import-outside-toplevel)
app\auto_farm\rune_solver\solver.py:82:8: C0415: Import outside toplevel (cv2) (import-outside-toplevel)
app\auto_farm\rune_solver\solver.py:83:8: C0415: Import outside toplevel (PIL.Image) (import-outside-toplevel)
app\auto_farm\rune_solver\solver.py:86:20: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
app\auto_farm\rune_solver\solver.py:86:40: E1101: Module 'cv2' has no 'COLOR_BGRA2BGR' member (no-member)
app\auto_farm\rune_solver\solver.py:87:14: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
app\auto_farm\rune_solver\solver.py:87:34: E1101: Module 'cv2' has no 'COLOR_BGR2RGB' member (no-member)
app\auto_farm\rune_solver\solver.py:95:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\rune_solver\solver.py:106:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\rune_solver\solver.py:27:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module app.auto_farm.rune_solver.vit_solver
app\auto_farm\rune_solver\vit_solver.py:152:0: C0301: Line too long (133/100) (line-too-long)
app\auto_farm\rune_solver\vit_solver.py:190:0: C0301: Line too long (103/100) (line-too-long)
app\auto_farm\rune_solver\vit_solver.py:27:17: E1121: Too many positional arguments for method call (too-many-function-args)
app\auto_farm\rune_solver\vit_solver.py:28:16: E1121: Too many positional arguments for method call (too-many-function-args)
app\auto_farm\rune_solver\vit_solver.py:37:8: W0613: Unused argument 'device' (unused-argument)
app\auto_farm\rune_solver\vit_solver.py:60:8: C0103: Variable name "W" doesn't conform to snake_case naming style (invalid-name)
app\auto_farm\rune_solver\vit_solver.py:60:11: C0103: Variable name "H" doesn't conform to snake_case naming style (invalid-name)
app\auto_farm\rune_solver\vit_solver.py:68:45: E1101: Module 'PIL.Image' has no 'BILINEAR' member (no-member)
app\auto_farm\rune_solver\vit_solver.py:89:45: E1101: Module 'PIL.Image' has no 'LANCZOS' member (no-member)
app\auto_farm\rune_solver\vit_solver.py:101:4: R0914: Too many local variables (35/15) (too-many-locals)
app\auto_farm\rune_solver\vit_solver.py:147:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\auto_farm\rune_solver\vit_solver.py:117:16: C0415: Import outside toplevel (cv2) (import-outside-toplevel)
app\auto_farm\rune_solver\vit_solver.py:118:16: W0404: Reimport 'numpy' (imported line 8) (reimported)
app\auto_farm\rune_solver\vit_solver.py:118:16: C0415: Import outside toplevel (numpy) (import-outside-toplevel)
app\auto_farm\rune_solver\vit_solver.py:119:16: C0415: Import outside toplevel (PIL.ImageDraw, PIL.ImageFont) (import-outside-toplevel)
app\auto_farm\rune_solver\vit_solver.py:144:62: E1101: Module 'PIL.Image' has no 'NEAREST' member (no-member)
app\auto_farm\rune_solver\vit_solver.py:186:8: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
app\auto_farm\rune_solver\vit_solver.py:101:4: R0912: Too many branches (14/12) (too-many-branches)
app\auto_farm\rune_solver\vit_solver.py:101:4: R0915: Too many statements (55/50) (too-many-statements)
app\auto_farm\rune_solver\vit_solver.py:119:16: W0611: Unused ImageFont imported from PIL (unused-import)
app\auto_farm\rune_solver\vit_solver.py:31:0: R0903: Too few public methods (1/2) (too-few-public-methods)
app\auto_farm\rune_solver\vit_solver.py:5:0: W0611: Unused import os (unused-import)
************* Module app.tabs.auto_farm
app\tabs\auto_farm.py:315:0: C0301: Line too long (102/100) (line-too-long)
app\tabs\auto_farm.py:13:0: R0901: Too many ancestors (8/7) (too-many-ancestors)
app\tabs\auto_farm.py:13:0: R0902: Too many instance attributes (25/7) (too-many-instance-attributes)
app\tabs\auto_farm.py:73:4: R0915: Too many statements (62/50) (too-many-statements)
app\tabs\auto_farm.py:497:4: R0914: Too many local variables (16/15) (too-many-locals)
app\tabs\auto_farm.py:563:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\auto_farm.py:538:44: W0212: Access to a protected member _scan_for_rune of a client class (protected-access)
app\tabs\auto_farm.py:548:28: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
app\tabs\auto_farm.py:548:56: E1101: Module 'cv2' has no 'COLOR_BGR2RGB' member (no-member)
app\tabs\auto_farm.py:554:82: E1101: Module 'PIL.Image' has no 'LANCZOS' member (no-member)
app\tabs\auto_farm.py:566:12: W0107: Unnecessary pass statement (unnecessary-pass)
app\tabs\auto_farm.py:563:8: W0612: Unused variable 'e' (unused-variable)
app\tabs\auto_farm.py:570:35: W0613: Unused argument 'event' (unused-argument)
app\tabs\auto_farm.py:588:8: W0201: Attribute 'settings' defined outside __init__ (attribute-defined-outside-init)
app\tabs\auto_farm.py:3:0: W0611: Unused import time (unused-import)
app\tabs\auto_farm.py:5:0: W0611: Unused messagebox imported from tkinter (unused-import)
************* Module app.tabs.auto_farm_firmware
app\tabs\auto_farm_firmware.py:10:0: R0901: Too many ancestors (8/7) (too-many-ancestors)
app\tabs\auto_farm_firmware.py:10:0: R0902: Too many instance attributes (13/7) (too-many-instance-attributes)
app\tabs\auto_farm_firmware.py:13:4: R0915: Too many statements (71/50) (too-many-statements)
app\tabs\auto_farm_firmware.py:238:8: C0415: Import outside toplevel (tkinter.filedialog) (import-outside-toplevel)
app\tabs\auto_farm_firmware.py:272:8: W0612: Unused variable 'is_simulation' (unused-variable)
app\tabs\auto_farm_firmware.py:367:0: R0901: Too many ancestors (8/7) (too-many-ancestors)
app\tabs\auto_farm_firmware.py:370:52: W0613: Unused argument 'reload_callback' (unused-argument)
************* Module app.tabs.calibration
app\tabs\calibration.py:456:0: C0301: Line too long (101/100) (line-too-long)
app\tabs\calibration.py:8:0: R0901: Too many ancestors (8/7) (too-many-ancestors)
app\tabs\calibration.py:11:4: R0914: Too many local variables (30/15) (too-many-locals)
app\tabs\calibration.py:11:4: R0915: Too many statements (81/50) (too-many-statements)
app\tabs\calibration.py:364:4: R0914: Too many local variables (17/15) (too-many-locals)
app\tabs\calibration.py:386:8: W0621: Redefining name 'os' from outer scope (line 3) (redefined-outer-name)
app\tabs\calibration.py:381:16: R1713: Consider using str.join(sequence) for concatenating strings from an iterable (consider-using-join)
app\tabs\calibration.py:385:8: C0415: Import outside toplevel (json) (import-outside-toplevel)
app\tabs\calibration.py:386:8: W0404: Reimport 'os' (imported line 3) (reimported)
app\tabs\calibration.py:386:8: C0415: Import outside toplevel (os) (import-outside-toplevel)
app\tabs\calibration.py:399:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\calibration.py:410:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\calibration.py:427:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\calibration.py:442:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\calibration.py:364:4: R0912: Too many branches (16/12) (too-many-branches)
app\tabs\calibration.py:364:4: R0915: Too many statements (56/50) (too-many-statements)
app\tabs\calibration.py:399:8: W0612: Unused variable 'e' (unused-variable)
app\tabs\calibration.py:459:4: R0914: Too many local variables (18/15) (too-many-locals)
app\tabs\calibration.py:489:8: W0621: Redefining name 'os' from outer scope (line 3) (redefined-outer-name)
app\tabs\calibration.py:476:16: R1713: Consider using str.join(sequence) for concatenating strings from an iterable (consider-using-join)
app\tabs\calibration.py:488:8: C0415: Import outside toplevel (json) (import-outside-toplevel)
app\tabs\calibration.py:489:8: W0404: Reimport 'os' (imported line 3) (reimported)
app\tabs\calibration.py:489:8: C0415: Import outside toplevel (os) (import-outside-toplevel)
app\tabs\calibration.py:500:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\calibration.py:511:23: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\calibration.py:524:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\calibration.py:545:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\calibration.py:459:4: R0912: Too many branches (16/12) (too-many-branches)
app\tabs\calibration.py:459:4: R0915: Too many statements (56/50) (too-many-statements)
app\tabs\calibration.py:500:8: W0612: Unused variable 'e' (unused-variable)
************* Module app.tabs.dashboard
app\tabs\dashboard.py:123:0: C0301: Line too long (122/100) (line-too-long)
app\tabs\dashboard.py:15:0: R0901: Too many ancestors (8/7) (too-many-ancestors)
app\tabs\dashboard.py:15:0: R0902: Too many instance attributes (43/7) (too-many-instance-attributes)
app\tabs\dashboard.py:26:8: C0415: Import outside toplevel (sys) (import-outside-toplevel)
app\tabs\dashboard.py:18:4: R0915: Too many statements (52/50) (too-many-statements)
app\tabs\dashboard.py:112:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\dashboard.py:109:21: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
app\tabs\dashboard.py:114:16: W0107: Unnecessary pass statement (unnecessary-pass)
app\tabs\dashboard.py:112:12: W0612: Unused variable 'e' (unused-variable)
app\tabs\dashboard.py:141:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\dashboard.py:128:17: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
app\tabs\dashboard.py:712:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\dashboard.py:722:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\dashboard.py:724:16: W0107: Unnecessary pass statement (unnecessary-pass)
app\tabs\dashboard.py:722:12: W0612: Unused variable 'e' (unused-variable)
app\tabs\dashboard.py:712:8: W0612: Unused variable 'e' (unused-variable)
app\tabs\dashboard.py:860:4: R0914: Too many local variables (19/15) (too-many-locals)
app\tabs\dashboard.py:910:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\dashboard.py:891:24: R1723: Unnecessary "else" after "break", remove the "else" and de-indent the code inside it (no-else-break)
app\tabs\dashboard.py:15:0: R0904: Too many public methods (32/20) (too-many-public-methods)
************* Module app.tabs.pattern
app\tabs\pattern.py:385:0: C0301: Line too long (102/100) (line-too-long)
app\tabs\pattern.py:391:0: C0301: Line too long (105/100) (line-too-long)
app\tabs\pattern.py:398:0: C0301: Line too long (152/100) (line-too-long)
app\tabs\pattern.py:470:0: C0301: Line too long (101/100) (line-too-long)
app\tabs\pattern.py:11:0: R0901: Too many ancestors (8/7) (too-many-ancestors)
app\tabs\pattern.py:11:0: R0902: Too many instance attributes (12/7) (too-many-instance-attributes)
app\tabs\pattern.py:14:4: R0914: Too many local variables (16/15) (too-many-locals)
app\tabs\pattern.py:14:4: R0915: Too many statements (83/50) (too-many-statements)
app\tabs\pattern.py:280:24: W0613: Unused argument 'event' (unused-argument)
app\tabs\pattern.py:291:32: W0613: Unused argument 'event' (unused-argument)
app\tabs\pattern.py:379:4: R0914: Too many local variables (19/15) (too-many-locals)
app\tabs\pattern.py:405:16: R1713: Consider using str.join(sequence) for concatenating strings from an iterable (consider-using-join)
app\tabs\pattern.py:409:8: C0415: Import outside toplevel (json) (import-outside-toplevel)
app\tabs\pattern.py:410:8: C0415: Import outside toplevel (os) (import-outside-toplevel)
app\tabs\pattern.py:423:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\pattern.py:431:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\pattern.py:446:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\pattern.py:457:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\pattern.py:379:4: R0912: Too many branches (20/12) (too-many-branches)
app\tabs\pattern.py:379:4: R0915: Too many statements (63/50) (too-many-statements)
app\tabs\pattern.py:423:8: W0612: Unused variable 'e' (unused-variable)
app\tabs\pattern.py:474:0: R0901: Too many ancestors (8/7) (too-many-ancestors)
************* Module app.tabs.profiles
app\tabs\profiles.py:156:0: C0301: Line too long (105/100) (line-too-long)
app\tabs\profiles.py:10:0: R0901: Too many ancestors (8/7) (too-many-ancestors)
app\tabs\profiles.py:10:0: R0902: Too many instance attributes (11/7) (too-many-instance-attributes)
app\tabs\profiles.py:13:4: R0914: Too many local variables (26/15) (too-many-locals)
app\tabs\profiles.py:13:4: R0915: Too many statements (122/50) (too-many-statements)
app\tabs\profiles.py:407:8: C0415: Import outside toplevel (time) (import-outside-toplevel)
app\tabs\profiles.py:457:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\profiles.py:482:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\profiles.py:495:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\profiles.py:517:16: R1713: Consider using str.join(sequence) for concatenating strings from an iterable (consider-using-join)
app\tabs\profiles.py:526:16: R1713: Consider using str.join(sequence) for concatenating strings from an iterable (consider-using-join)
app\tabs\profiles.py:596:11: W0212: Access to a protected member _pending_config_data of a client class (protected-access)
app\tabs\profiles.py:597:23: W0212: Access to a protected member _pending_config_data of a client class (protected-access)
app\tabs\profiles.py:598:12: W0212: Access to a protected member _pending_config_data of a client class (protected-access)
app\tabs\profiles.py:617:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\profiles.py:601:16: C0415: Import outside toplevel (app.connection.SerialConnectionManager) (import-outside-toplevel)
app\tabs\profiles.py:653:8: W0107: Unnecessary pass statement (unnecessary-pass)
app\tabs\profiles.py:657:8: W0107: Unnecessary pass statement (unnecessary-pass)
************* Module app.tabs.recorder
app\tabs\recorder.py:359:0: C0301: Line too long (142/100) (line-too-long)
app\tabs\recorder.py:395:0: C0301: Line too long (166/100) (line-too-long)
app\tabs\recorder.py:400:0: C0301: Line too long (159/100) (line-too-long)
app\tabs\recorder.py:497:0: C0301: Line too long (113/100) (line-too-long)
app\tabs\recorder.py:604:0: C0301: Line too long (117/100) (line-too-long)
app\tabs\recorder.py:791:0: C0301: Line too long (110/100) (line-too-long)
app\tabs\recorder.py:800:0: C0301: Line too long (105/100) (line-too-long)
app\tabs\recorder.py:807:0: C0301: Line too long (152/100) (line-too-long)
app\tabs\recorder.py:878:0: C0301: Line too long (105/100) (line-too-long)
app\tabs\recorder.py:949:0: C0301: Line too long (126/100) (line-too-long)
app\tabs\recorder.py:1:0: C0302: Too many lines in module (1095/1000) (too-many-lines)
app\tabs\recorder.py:18:0: R0901: Too many ancestors (8/7) (too-many-ancestors)
app\tabs\recorder.py:18:0: R0902: Too many instance attributes (31/7) (too-many-instance-attributes)
app\tabs\recorder.py:21:4: R0915: Too many statements (120/50) (too-many-statements)
app\tabs\recorder.py:366:8: W0603: Using the global statement (global-statement)
app\tabs\recorder.py:375:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\recorder.py:371:12: C0415: Import outside toplevel (keyboard) (import-outside-toplevel)
app\tabs\recorder.py:371:12: W0611: Unused import keyboard (unused-import)
app\tabs\recorder.py:375:8: W0612: Unused variable 'e' (unused-variable)
app\tabs\recorder.py:422:23: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\recorder.py:419:20: C0415: Import outside toplevel (keyboard) (import-outside-toplevel)
app\tabs\recorder.py:441:23: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\recorder.py:438:20: C0415: Import outside toplevel (keyboard) (import-outside-toplevel)
app\tabs\recorder.py:443:20: W0107: Unnecessary pass statement (unnecessary-pass)
app\tabs\recorder.py:441:16: W0612: Unused variable 'e' (unused-variable)
app\tabs\recorder.py:463:29: W0613: Unused argument 'event' (unused-argument)
app\tabs\recorder.py:474:28: W0613: Unused argument 'event' (unused-argument)
app\tabs\recorder.py:525:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\recorder.py:518:16: C0415: Import outside toplevel (keyboard) (import-outside-toplevel)
app\tabs\recorder.py:527:16: W0107: Unnecessary pass statement (unnecessary-pass)
app\tabs\recorder.py:525:12: W0612: Unused variable 'e' (unused-variable)
app\tabs\recorder.py:592:4: R0914: Too many local variables (18/15) (too-many-locals)
app\tabs\recorder.py:636:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\recorder.py:629:16: C0415: Import outside toplevel (keyboard) (import-outside-toplevel)
app\tabs\recorder.py:638:16: W0107: Unnecessary pass statement (unnecessary-pass)
app\tabs\recorder.py:592:4: R0912: Too many branches (20/12) (too-many-branches)
app\tabs\recorder.py:592:4: R0915: Too many statements (58/50) (too-many-statements)
app\tabs\recorder.py:636:12: W0612: Unused variable 'e' (unused-variable)
app\tabs\recorder.py:703:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\recorder.py:705:16: W0107: Unnecessary pass statement (unnecessary-pass)
app\tabs\recorder.py:703:12: W0612: Unused variable 'e' (unused-variable)
app\tabs\recorder.py:722:28: W0613: Unused argument 'event' (unused-argument)
app\tabs\recorder.py:734:30: W0613: Unused argument 'event' (unused-argument)
app\tabs\recorder.py:781:4: R0914: Too many local variables (19/15) (too-many-locals)
app\tabs\recorder.py:818:12: W0621: Redefining name 'json' from outer scope (line 3) (redefined-outer-name)
app\tabs\recorder.py:814:20: R1713: Consider using str.join(sequence) for concatenating strings from an iterable (consider-using-join)
app\tabs\recorder.py:818:12: W0404: Reimport 'json' (imported line 3) (reimported)
app\tabs\recorder.py:818:12: C0415: Import outside toplevel (json) (import-outside-toplevel)
app\tabs\recorder.py:819:12: C0415: Import outside toplevel (os) (import-outside-toplevel)
app\tabs\recorder.py:832:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\recorder.py:840:23: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\recorder.py:855:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\recorder.py:866:23: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\recorder.py:781:4: R0912: Too many branches (20/12) (too-many-branches)
app\tabs\recorder.py:781:4: R0915: Too many statements (64/50) (too-many-statements)
app\tabs\recorder.py:832:12: W0612: Unused variable 'e' (unused-variable)
app\tabs\recorder.py:962:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\recorder.py:881:4: R0915: Too many statements (53/50) (too-many-statements)
app\tabs\recorder.py:692:8: W0201: Attribute '_reload_timer' defined outside __init__ (attribute-defined-outside-init)
app\tabs\recorder.py:696:8: W0201: Attribute '_reload_timer' defined outside __init__ (attribute-defined-outside-init)
app\tabs\recorder.py:18:0: R0904: Too many public methods (22/20) (too-many-public-methods)
app\tabs\recorder.py:13:0: C0411: standard import "importlib.util" should be placed before first party import "app.models.Action"  (wrong-import-order)
************* Module app.tabs.robot_settings
app\tabs\robot_settings.py:608:0: C0301: Line too long (107/100) (line-too-long)
app\tabs\robot_settings.py:649:0: C0301: Line too long (104/100) (line-too-long)
app\tabs\robot_settings.py:681:0: C0301: Line too long (121/100) (line-too-long)
app\tabs\robot_settings.py:1:0: C0302: Too many lines in module (1051/1000) (too-many-lines)
app\tabs\robot_settings.py:12:0: R0901: Too many ancestors (8/7) (too-many-ancestors)
app\tabs\robot_settings.py:12:0: R0902: Too many instance attributes (37/7) (too-many-instance-attributes)
app\tabs\robot_settings.py:95:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\robot_settings.py:97:12: W0107: Unnecessary pass statement (unnecessary-pass)
app\tabs\robot_settings.py:15:4: R0915: Too many statements (54/50) (too-many-statements)
app\tabs\robot_settings.py:95:8: W0612: Unused variable 'e' (unused-variable)
app\tabs\robot_settings.py:107:0: W0613: Unused argument 'args' (unused-argument)
app\tabs\robot_settings.py:129:0: W0613: Unused argument 'args' (unused-argument)
app\tabs\robot_settings.py:153:0: W0613: Unused argument 'args' (unused-argument)
app\tabs\robot_settings.py:178:0: W0613: Unused argument 'args' (unused-argument)
app\tabs\robot_settings.py:199:0: W0613: Unused argument 'args' (unused-argument)
app\tabs\robot_settings.py:220:0: W0613: Unused argument 'args' (unused-argument)
app\tabs\robot_settings.py:602:4: R0914: Too many local variables (16/15) (too-many-locals)
app\tabs\robot_settings.py:616:16: R1713: Consider using str.join(sequence) for concatenating strings from an iterable (consider-using-join)
app\tabs\robot_settings.py:620:8: C0415: Import outside toplevel (json) (import-outside-toplevel)
app\tabs\robot_settings.py:621:8: C0415: Import outside toplevel (os) (import-outside-toplevel)
app\tabs\robot_settings.py:634:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\robot_settings.py:642:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\robot_settings.py:658:15: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\robot_settings.py:669:19: W0718: Catching too general exception Exception (broad-exception-caught)
app\tabs\robot_settings.py:602:4: R0912: Too many branches (16/12) (too-many-branches)
app\tabs\robot_settings.py:602:4: R0915: Too many statements (57/50) (too-many-statements)
app\tabs\robot_settings.py:634:8: W0612: Unused variable 'e' (unused-variable)
app\tabs\robot_settings.py:685:4: R0914: Too many local variables (17/15) (too-many-locals)
app\tabs\robot_settings.py:685:4: R0915: Too many statements (60/50) (too-many-statements)
app\tabs\robot_settings.py:965:21: W1309: Using an f-string that does not have any interpolated variables (f-string-without-interpolation)
app\tabs\robot_settings.py:12:0: R0904: Too many public methods (22/20) (too-many-public-methods)
app\tabs\robot_settings.py:994:0: R0901: Too many ancestors (8/7) (too-many-ancestors)
************* Module app.tabs.simulation
app\tabs\simulation.py:21:0: C0301: Line too long (105/100) (line-too-long)
app\tabs\simulation.py:640:0: C0301: Line too long (110/100) (line-too-long)
app\tabs\simulation.py:8:0: R0901: Too many ancestors (8/7) (too-many-ancestors)
app\tabs\simulation.py:8:0: R0902: Too many instance attributes (18/7) (too-many-instance-attributes)
app\tabs\simulation.py:11:4: R0914: Too many local variables (18/15) (too-many-locals)
app\tabs\simulation.py:311:42: W0108: Lambda may not be necessary (unnecessary-lambda)
app\tabs\simulation.py:312:44: W0108: Lambda may not be necessary (unnecessary-lambda)
app\tabs\simulation.py:11:4: R0915: Too many statements (76/50) (too-many-statements)
app\tabs\simulation.py:189:12: W0612: Unused variable 'label' (unused-variable)
app\tabs\simulation.py:189:19: W0612: Unused variable 'unit_x' (unused-variable)
app\tabs\simulation.py:189:27: W0612: Unused variable 'unit_y' (unused-variable)
app\tabs\simulation.py:189:35: W0612: Unused variable 'unit_w' (unused-variable)
app\tabs\simulation.py:189:43: W0612: Unused variable 'unit_h' (unused-variable)
app\tabs\simulation.py:387:4: R0914: Too many local variables (33/15) (too-many-locals)
app\tabs\simulation.py:542:8: C0415: Import outside toplevel (time) (import-outside-toplevel)
app\tabs\simulation.py:559:4: R0915: Too many statements (53/50) (too-many-statements)
************* Module app.tabs.tester
app\tabs\tester.py:26:0: C0301: Line too long (174/100) (line-too-long)
app\tabs\tester.py:124:0: C0301: Line too long (105/100) (line-too-long)
app\tabs\tester.py:7:0: R0901: Too many ancestors (8/7) (too-many-ancestors)
app\tabs\tester.py:7:0: R0902: Too many instance attributes (10/7) (too-many-instance-attributes)
app\tabs\tester.py:283:12: W0612: Unused variable 'label' (unused-variable)
app\tabs\tester.py:283:19: W0612: Unused variable 'unit_x' (unused-variable)
app\tabs\tester.py:283:27: W0612: Unused variable 'unit_y' (unused-variable)
app\tabs\tester.py:283:35: W0612: Unused variable 'unit_w' (unused-variable)
app\tabs\tester.py:283:43: W0612: Unused variable 'unit_h' (unused-variable)
app\tabs\tester.py:288:4: R0914: Too many local variables (30/15) (too-many-locals)
app\tabs\tester.py:455:12: C0206: Consider iterating with .items() (consider-using-dict-items)
************* Module app.tabs.validator
app\tabs\validator.py:23:0: C0301: Line too long (104/100) (line-too-long)
app\tabs\validator.py:28:0: C0301: Line too long (137/100) (line-too-long)
app\tabs\validator.py:33:0: C0301: Line too long (182/100) (line-too-long)
app\tabs\validator.py:38:0: C0301: Line too long (119/100) (line-too-long)
app\tabs\validator.py:51:0: C0301: Line too long (210/100) (line-too-long)
app\tabs\validator.py:61:0: C0301: Line too long (126/100) (line-too-long)
app\tabs\validator.py:65:0: C0301: Line too long (110/100) (line-too-long)
app\tabs\validator.py:73:0: C0301: Line too long (148/100) (line-too-long)
app\tabs\validator.py:81:0: C0301: Line too long (152/100) (line-too-long)
app\tabs\validator.py:85:0: C0301: Line too long (151/100) (line-too-long)
app\tabs\validator.py:95:0: C0301: Line too long (174/100) (line-too-long)
app\tabs\validator.py:106:0: C0301: Line too long (103/100) (line-too-long)
app\tabs\validator.py:117:0: C0301: Line too long (104/100) (line-too-long)
app\tabs\validator.py:121:0: C0301: Line too long (120/100) (line-too-long)
app\tabs\validator.py:324:0: C0301: Line too long (125/100) (line-too-long)
app\tabs\validator.py:55:16: W1309: Using an f-string that does not have any interpolated variables (f-string-without-interpolation)
app\tabs\validator.py:9:0: R0912: Too many branches (25/12) (too-many-branches)
app\tabs\validator.py:9:0: R0915: Too many statements (53/50) (too-many-statements)
app\tabs\validator.py:127:0: R0901: Too many ancestors (8/7) (too-many-ancestors)
app\tabs\validator.py:130:4: R0915: Too many statements (51/50) (too-many-statements)
app\tabs\validator.py:290:8: C0415: Import outside toplevel (tkinter.messagebox) (import-outside-toplevel)
************* Module dist.lg_audio_helper_app._internal.cv2.config-3
dist\lg_audio_helper_app\_internal\cv2\config-3.py:1:0: C0103: Module name "config-3" doesn't conform to snake_case naming style (invalid-name)
dist\lg_audio_helper_app\_internal\cv2\config-3.py:3:4: E0602: Undefined variable 'LOADER_DIR' (undefined-variable)
dist\lg_audio_helper_app\_internal\cv2\config-3.py:4:4: E0601: Using variable 'PYTHON_EXTENSIONS_PATHS' before assignment (used-before-assignment)
dist\lg_audio_helper_app\_internal\cv2\config-3.py:12:0: W0702: No exception type(s) specified (bare-except)
dist\lg_audio_helper_app\_internal\cv2\config-3.py:16:3: E0602: Undefined variable 'sys' (undefined-variable)
dist\lg_audio_helper_app\_internal\cv2\config-3.py:17:4: E0602: Undefined variable 'os' (undefined-variable)
dist\lg_audio_helper_app\_internal\cv2\config-3.py:17:48: E0602: Undefined variable 'os' (undefined-variable)
dist\lg_audio_helper_app\_internal\cv2\config-3.py:18:8: E0602: Undefined variable 'os' (undefined-variable)
dist\lg_audio_helper_app\_internal\cv2\config-3.py:18:24: E0602: Undefined variable 'os' (undefined-variable)
dist\lg_audio_helper_app\_internal\cv2\config-3.py:22:3: E0602: Undefined variable 'sys' (undefined-variable)
dist\lg_audio_helper_app\_internal\cv2\config-3.py:23:4: E0602: Undefined variable 'os' (undefined-variable)
dist\lg_audio_helper_app\_internal\cv2\config-3.py:23:35: E0602: Undefined variable 'os' (undefined-variable)
dist\lg_audio_helper_app\_internal\cv2\config-3.py:24:8: E0602: Undefined variable 'os' (undefined-variable)
dist\lg_audio_helper_app\_internal\cv2\config-3.py:24:24: E0602: Undefined variable 'os' (undefined-variable)
************* Module dist.lg_audio_helper_app._internal.cv2.config
dist\lg_audio_helper_app\_internal\cv2\config.py:5:30: E0602: Undefined variable 'LOADER_DIR' (undefined-variable)
dist\lg_audio_helper_app\_internal\cv2\config.py:6:4: E0601: Using variable 'BINARIES_PATHS' before assignment (used-before-assignment)
************* Module dist.lg_audio_helper_app._internal.cv2.load_config_py3
dist\lg_audio_helper_app\_internal\cv2\load_config_py3.py:9:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
dist\lg_audio_helper_app\_internal\cv2\load_config_py3.py:11:12: W0122: Use of exec (exec-used)
************* Module dist.lg_audio_helper_app._internal.cv2.version
dist\lg_audio_helper_app\_internal\cv2\version.py:2:0: C0103: Constant name "opencv_version" doesn't conform to UPPER_CASE naming style (invalid-name)
dist\lg_audio_helper_app\_internal\cv2\version.py:3:0: C0103: Constant name "contrib" doesn't conform to UPPER_CASE naming style (invalid-name)
dist\lg_audio_helper_app\_internal\cv2\version.py:4:0: C0103: Constant name "headless" doesn't conform to UPPER_CASE naming style (invalid-name)
dist\lg_audio_helper_app\_internal\cv2\version.py:5:0: C0103: Constant name "rolling" doesn't conform to UPPER_CASE naming style (invalid-name)
dist\lg_audio_helper_app\_internal\cv2\version.py:6:0: C0103: Constant name "ci_build" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module dist.lg_audio_helper_app._internal.cv2.__init__
dist\lg_audio_helper_app\_internal\cv2\__init__.py:80:0: C0301: Line too long (127/100) (line-too-long)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:88:0: C0301: Line too long (114/100) (line-too-long)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:114:0: C0301: Line too long (121/100) (line-too-long)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:122:0: C0301: Line too long (111/100) (line-too-long)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:152:0: C0301: Line too long (120/100) (line-too-long)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:169:0: C0301: Line too long (128/100) (line-too-long)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:19:1: W0511: TODO (fixme)
************* Module dist.lg_audio_helper_app._internal.cv2
dist\lg_audio_helper_app\_internal\cv2\__init__.py:25:18: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:26:25: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:45:35: C0321: More than one statement on a single line (multiple-statements)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:45:41: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:66:4: C0103: Variable name "__INIT_FILE_PATH" doesn't conform to snake_case naming style (invalid-name)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:71:0: R0914: Too many local variables (21/15) (too-many-locals)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:73:4: W0621: Redefining name 'sys' from outer scope (line 6) (redefined-outer-name)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:73:4: W0404: Reimport 'sys' (imported line 6) (reimported)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:73:4: C0415: Import outside toplevel (sys) (import-outside-toplevel)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:75:4: C0415: Import outside toplevel (copy) (import-outside-toplevel)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:83:4: C0103: Variable name "DEBUG" doesn't conform to snake_case naming style (invalid-name)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:85:8: C0103: Variable name "DEBUG" doesn't conform to snake_case naming style (invalid-name)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:87:4: C0415: Import outside toplevel (platform) (import-outside-toplevel)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:88:14: C0321: More than one statement on a single line (multiple-statements)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:88:20: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:90:4: C0103: Variable name "LOADER_DIR" doesn't conform to snake_case naming style (invalid-name)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:92:4: C0103: Variable name "PYTHON_EXTENSIONS_PATHS" doesn't conform to snake_case naming style (invalid-name)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:93:4: C0103: Variable name "BINARIES_PATHS" doesn't conform to snake_case naming style (invalid-name)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:99:8: C0415: Import outside toplevel (load_config_py2.exec_file_wrapper) (import-outside-toplevel)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:101:8: C0415: Import outside toplevel (load_config_py3.exec_file_wrapper) (import-outside-toplevel)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:108:26: C0321: More than one statement on a single line (multiple-statements)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:108:32: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:110:22: C0321: More than one statement on a single line (multiple-statements)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:110:28: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:114:30: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:118:8: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:119:8: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:122:14: C0321: More than one statement on a single line (multiple-statements)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:122:20: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:123:14: C0321: More than one statement on a single line (multiple-statements)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:123:20: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:125:4: C0103: Variable name "applySysPathWorkaround" doesn't conform to snake_case naming style (invalid-name)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:127:8: C0103: Variable name "applySysPathWorkaround" doesn't conform to snake_case naming style (invalid-name)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:133:8: W0702: No exception type(s) specified (bare-except)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:130:12: C0103: Variable name "BASE_DIR" doesn't conform to snake_case naming style (invalid-name)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:132:16: C0103: Variable name "applySysPathWorkaround" doesn't conform to snake_case naming style (invalid-name)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:134:22: C0321: More than one statement on a single line (multiple-statements)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:135:12: W0107: Unnecessary pass statement (unnecessary-pass)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:145:23: W0718: Catching too general exception Exception (broad-exception-caught)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:146:30: C0321: More than one statement on a single line (multiple-statements)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:147:20: W0107: Unnecessary pass statement (unnecessary-pass)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:149:18: C0321: More than one statement on a single line (multiple-statements)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:149:24: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:154:14: C0321: More than one statement on a single line (multiple-statements)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:173:11: W0718: Catching too general exception Exception (broad-exception-caught)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:178:14: C0321: More than one statement on a single line (multiple-statements)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:182:22: C0321: More than one statement on a single line (multiple-statements)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:184:14: C0321: More than one statement on a single line (multiple-statements)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:71:0: R0912: Too many branches (30/12) (too-many-branches)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:71:0: R0915: Too many statements (87/50) (too-many-statements)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:92:4: W0641: Possibly unused variable 'PYTHON_EXTENSIONS_PATHS' (possibly-unused-variable)
dist\lg_audio_helper_app\_internal\cv2\__init__.py:93:4: W0641: Possibly unused variable 'BINARIES_PATHS' (possibly-unused-variable)
************* Module dist.lg_audio_helper_app._internal.cv2.gapi.__init__
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:331:0: W0311: Bad indentation. Found 19 spaces, expected 16 (bad-indentation)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:347:0: C0301: Line too long (108/100) (line-too-long)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:348:0: C0301: Line too long (104/100) (line-too-long)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:356:0: C0301: Line too long (108/100) (line-too-long)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:357:0: C0301: Line too long (105/100) (line-too-long)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:361:0: C0301: Line too long (106/100) (line-too-long)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:377:0: C0301: Line too long (119/100) (line-too-long)
************* Module dist.lg_audio_helper_app._internal.cv2.gapi
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:20:11: E1101: Module 'cv2' has no 'gapi_GNetPackage' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:26:20: E1101: Module 'cv2' has no 'GCompileArg' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:30:0: C0103: Function name "GIn" doesn't conform to snake_case naming style (invalid-name)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:36:0: C0103: Function name "GOut" doesn't conform to snake_case naming style (invalid-name)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:60:15: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:64:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:66:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:66:31: E1101: Module 'cv2.gapi' has no 'CV_BOOL' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:62:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:70:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:72:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:72:31: E1101: Module 'cv2.gapi' has no 'CV_INT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:68:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:76:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:78:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:78:31: E1101: Module 'cv2.gapi' has no 'CV_INT64' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:74:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:82:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:84:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:84:31: E1101: Module 'cv2.gapi' has no 'CV_UINT64' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:80:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:88:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:90:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:90:31: E1101: Module 'cv2.gapi' has no 'CV_DOUBLE' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:86:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:94:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:96:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:96:31: E1101: Module 'cv2.gapi' has no 'CV_FLOAT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:92:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:100:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:102:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:102:31: E1101: Module 'cv2.gapi' has no 'CV_STRING' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:98:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:106:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:108:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:108:31: E1101: Module 'cv2.gapi' has no 'CV_POINT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:104:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:112:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:114:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:114:31: E1101: Module 'cv2.gapi' has no 'CV_POINT2F' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:110:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:118:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:120:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:120:31: E1101: Module 'cv2.gapi' has no 'CV_POINT3F' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:116:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:124:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:126:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:126:31: E1101: Module 'cv2.gapi' has no 'CV_SIZE' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:122:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:130:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:132:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:132:31: E1101: Module 'cv2.gapi' has no 'CV_RECT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:128:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:136:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:138:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:138:31: E1101: Module 'cv2.gapi' has no 'CV_DRAW_PRIM' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:134:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:142:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:144:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:144:31: E1101: Module 'cv2.gapi' has no 'CV_ANY' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:140:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:54:0: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:153:15: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:157:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:159:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:159:30: E1101: Module 'cv2.gapi' has no 'CV_BOOL' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:155:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:163:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:165:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:165:30: E1101: Module 'cv2.gapi' has no 'CV_INT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:161:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:169:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:171:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:171:30: E1101: Module 'cv2.gapi' has no 'CV_INT64' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:167:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:175:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:177:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:177:30: E1101: Module 'cv2.gapi' has no 'CV_UINT64' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:173:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:181:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:183:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:183:30: E1101: Module 'cv2.gapi' has no 'CV_DOUBLE' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:179:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:187:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:189:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:189:30: E1101: Module 'cv2.gapi' has no 'CV_FLOAT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:185:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:193:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:195:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:195:30: E1101: Module 'cv2.gapi' has no 'CV_STRING' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:191:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:199:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:201:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:201:30: E1101: Module 'cv2.gapi' has no 'CV_POINT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:197:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:205:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:207:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:207:30: E1101: Module 'cv2.gapi' has no 'CV_POINT2F' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:203:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:211:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:213:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:213:30: E1101: Module 'cv2.gapi' has no 'CV_POINT3F' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:209:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:217:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:219:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:219:30: E1101: Module 'cv2.gapi' has no 'CV_SIZE' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:215:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:223:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:225:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:225:30: E1101: Module 'cv2.gapi' has no 'CV_RECT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:221:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:229:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:231:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:231:30: E1101: Module 'cv2.gapi' has no 'CV_SCALAR' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:227:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:235:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:237:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:237:30: E1101: Module 'cv2.gapi' has no 'CV_MAT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:233:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:241:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:243:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:243:30: E1101: Module 'cv2.gapi' has no 'CV_GMAT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:239:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:247:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:249:19: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:249:29: E1101: Module 'cv2.gapi' has no 'CV_DRAW_PRIM' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:245:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:253:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:255:19: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:255:29: E1101: Module 'cv2.gapi' has no 'CV_ANY' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:251:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:147:0: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:263:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:263:31: E1101: Module 'cv2.gapi' has no 'CV_BOOL' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:264:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:264:31: E1101: Module 'cv2.gapi' has no 'CV_INT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:265:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:265:31: E1101: Module 'cv2.gapi' has no 'CV_INT64' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:266:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:266:31: E1101: Module 'cv2.gapi' has no 'CV_UINT64' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:267:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:267:31: E1101: Module 'cv2.gapi' has no 'CV_DOUBLE' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:268:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:268:31: E1101: Module 'cv2.gapi' has no 'CV_FLOAT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:269:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:269:31: E1101: Module 'cv2.gapi' has no 'CV_STRING' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:270:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:270:31: E1101: Module 'cv2.gapi' has no 'CV_POINT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:271:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:271:31: E1101: Module 'cv2.gapi' has no 'CV_POINT2F' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:272:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:272:31: E1101: Module 'cv2.gapi' has no 'CV_POINT3F' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:273:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:273:31: E1101: Module 'cv2.gapi' has no 'CV_SIZE' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:274:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:274:31: E1101: Module 'cv2.gapi' has no 'CV_RECT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:275:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:275:31: E1101: Module 'cv2.gapi' has no 'CV_SCALAR' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:276:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:276:31: E1101: Module 'cv2.gapi' has no 'CV_MAT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:277:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:277:31: E1101: Module 'cv2.gapi' has no 'CV_GMAT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:278:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:278:31: E1101: Module 'cv2.gapi' has no 'CV_DRAW_PRIM' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:279:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:279:31: E1101: Module 'cv2.gapi' has no 'CV_ANY' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:282:19: W0109: Duplicate key 'cv.GOpaque.Size' in dictionary (duplicate-key)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:282:19: W0109: Duplicate key 'cv.GOpaque.Rect' in dictionary (duplicate-key)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:283:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:283:32: E1101: Module 'cv2.gapi' has no 'CV_SIZE' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:284:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:284:32: E1101: Module 'cv2.gapi' has no 'CV_RECT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:285:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:285:32: E1101: Module 'cv2.gapi' has no 'CV_BOOL' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:286:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:286:32: E1101: Module 'cv2.gapi' has no 'CV_INT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:287:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:287:32: E1101: Module 'cv2.gapi' has no 'CV_INT64' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:288:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:288:32: E1101: Module 'cv2.gapi' has no 'CV_UINT64' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:289:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:289:32: E1101: Module 'cv2.gapi' has no 'CV_DOUBLE' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:290:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:290:32: E1101: Module 'cv2.gapi' has no 'CV_FLOAT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:291:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:291:32: E1101: Module 'cv2.gapi' has no 'CV_STRING' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:292:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:292:32: E1101: Module 'cv2.gapi' has no 'CV_POINT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:293:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:293:32: E1101: Module 'cv2.gapi' has no 'CV_POINT2F' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:294:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:294:32: E1101: Module 'cv2.gapi' has no 'CV_POINT3F' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:295:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:295:32: E1101: Module 'cv2.gapi' has no 'CV_SIZE' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:296:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:296:32: E1101: Module 'cv2.gapi' has no 'CV_RECT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:297:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:297:32: E1101: Module 'cv2.gapi' has no 'CV_DRAW_PRIM' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:298:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:298:32: E1101: Module 'cv2.gapi' has no 'CV_ANY' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:302:8: E1101: Module 'cv2.gapi' has no 'CV_BOOL' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:303:8: E1101: Module 'cv2.gapi' has no 'CV_INT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:304:8: E1101: Module 'cv2.gapi' has no 'CV_INT64' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:305:8: E1101: Module 'cv2.gapi' has no 'CV_UINT64' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:306:8: E1101: Module 'cv2.gapi' has no 'CV_DOUBLE' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:307:8: E1101: Module 'cv2.gapi' has no 'CV_FLOAT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:308:8: E1101: Module 'cv2.gapi' has no 'CV_STRING' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:309:8: E1101: Module 'cv2.gapi' has no 'CV_POINT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:310:8: E1101: Module 'cv2.gapi' has no 'CV_POINT2F' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:311:8: E1101: Module 'cv2.gapi' has no 'CV_POINT3F' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:312:8: E1101: Module 'cv2.gapi' has no 'CV_SIZE' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:313:8: E1101: Module 'cv2.gapi' has no 'CV_RECT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:314:8: E1101: Module 'cv2.gapi' has no 'CV_SCALAR' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:315:8: E1101: Module 'cv2.gapi' has no 'CV_MAT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:316:8: E1101: Module 'cv2.gapi' has no 'CV_GMAT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:317:8: E1101: Module 'cv2.gapi' has no 'CV_DRAW_PRIM' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:324:12: W0719: Raising too general exception: Exception (broad-exception-raised)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:324:28: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:327:12: W0719: Raising too general exception: Exception (broad-exception-raised)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:327:28: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:330:25: E1101: Module 'cv2' has no 'GMat' member; maybe 'Mat'? (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:330:34: E1101: Module 'cv2' has no 'GScalar' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:331:19: W0719: Raising too general exception: Exception (broad-exception-raised)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:331:35: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:364:12: W0621: Redefining name 'op' from outer scope (line 259) (redefined-outer-name)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:337:16: W0719: Raising too general exception: Exception (broad-exception-raised)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:337:32: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:342:20: R1720: Unnecessary "elif" after "raise", remove the leading "el" from "elif" (no-else-raise)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:342:41: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:343:24: W0719: Raising too general exception: Exception (broad-exception-raised)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:343:40: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:344:57: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:347:24: W0719: Raising too general exception: Exception (broad-exception-raised)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:347:40: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:351:20: R1720: Unnecessary "elif" after "raise", remove the leading "el" from "elif" (no-else-raise)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:351:41: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:352:24: W0719: Raising too general exception: Exception (broad-exception-raised)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:352:40: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:353:57: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:356:24: W0719: Raising too general exception: Exception (broad-exception-raised)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:356:40: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:360:23: C0123: Use isinstance() rather than type() for a typecheck. (unidiomatic-typecheck)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:361:24: W0719: Raising too general exception: Exception (broad-exception-raised)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:361:40: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:364:17: W0212: Access to a protected member __op of a client class (protected-access)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:364:17: E1101: Module 'cv2.gapi' has no '__op' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:368:31: E1101: Module 'cv2' has no 'GMat' member; maybe 'Mat'? (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:370:33: E1101: Module 'cv2' has no 'GScalar' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:377:20: W0719: Raising too general exception: Exception (broad-exception-raised)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:377:36: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:334:8: R0912: Too many branches (15/12) (too-many-branches)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:403:32: E1101: Module 'cv2' has no 'gapi_wip_gst_GStreamerPipeline' member (no-member)
************* Module dist.lg_audio_helper_app._internal.cv2.mat_wrapper.__init__
dist\lg_audio_helper_app\_internal\cv2\mat_wrapper\__init__.py:21:0: C0301: Line too long (106/100) (line-too-long)
************* Module dist.lg_audio_helper_app._internal.cv2.mat_wrapper
dist\lg_audio_helper_app\_internal\cv2\mat_wrapper\__init__.py:18:4: W0105: String statement has no effect (pointless-string-statement)
dist\lg_audio_helper_app\_internal\cv2\mat_wrapper\__init__.py:29:4: W0231: __init__ method from base class 'ndarray' is not called (super-init-not-called)
dist\lg_audio_helper_app\_internal\cv2\mat_wrapper\__init__.py:29:4: W0231: __init__ method from base class 'ndarray' is not called (super-init-not-called)
dist\lg_audio_helper_app\_internal\cv2\mat_wrapper\__init__.py:33:28: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\lg_audio_helper_app\_internal\cv2\mat_wrapper\__init__.py:44:0: W0212: Access to a protected member _registerMatType of a client class (protected-access)
dist\lg_audio_helper_app\_internal\cv2\mat_wrapper\__init__.py:44:0: E1101: Module 'cv2' has no '_registerMatType' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\mat_wrapper\__init__.py:6:0: C0411: standard import "typing.TYPE_CHECKING" should be placed before third party imports "numpy", "cv2" (wrong-import-order)
************* Module dist.lg_audio_helper_app._internal.cv2.typing.__init__
dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:154:0: C0301: Line too long (104/100) (line-too-long)
dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:157:0: C0301: Line too long (193/100) (line-too-long)
************* Module dist.lg_audio_helper_app._internal.cv2.typing
dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:89:4: C0103: Class name "TermCriteria_Type" doesn't conform to PascalCase naming style (invalid-name)
dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:148:18: E1101: Module 'cv2' has no 'Feature2D' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:149:22: E1101: Module 'cv2' has no 'Feature2D' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:150:19: E1101: Module 'cv2' has no 'Feature2D' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:151:34: E1101: Module 'cv2' has no 'GMat' member; maybe 'Mat'? (no-member)
dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:151:44: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:151:58: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:154:41: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:154:55: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:156:25: E1101: Module 'cv2' has no 'GMat' member; maybe 'Mat'? (no-member)
dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:156:43: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:156:57: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:166:26: E1101: Module 'cv2' has no 'GMat' member; maybe 'Mat'? (no-member)
dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:166:44: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:166:58: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:172:0: C0103: Class name "map_string_and_string" doesn't conform to PascalCase naming style (invalid-name)
dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:173:0: C0103: Class name "map_string_and_int" doesn't conform to PascalCase naming style (invalid-name)
dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:174:0: C0103: Class name "map_string_and_vector_size_t" doesn't conform to PascalCase naming style (invalid-name)
dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:175:0: C0103: Class name "map_string_and_vector_float" doesn't conform to PascalCase naming style (invalid-name)
dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:176:0: C0103: Class name "map_int_and_double" doesn't conform to PascalCase naming style (invalid-name)
dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:64:0: C0411: standard import "typing" should be placed before third party imports "cv2.mat_wrapper", "numpy", "cv2.dnn", "cv2" (wrong-import-order)
dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:62:0: C0412: Imports from package cv2 are not grouped (ungrouped-imports)
************* Module dist.lg_audio_helper_app._internal.cv2.utils
dist\lg_audio_helper_app\_internal\cv2\utils\__init__.py:11:0: C0103: Function name "testOverwriteNativeMethod" doesn't conform to snake_case naming style (invalid-name)
dist\lg_audio_helper_app\_internal\cv2\utils\__init__.py:15:8: W0212: Access to a protected member _native of a client class (protected-access)
dist\lg_audio_helper_app\_internal\cv2\utils\__init__.py:15:8: E1101: Module 'cv2.utils' has no '_native' member (no-member)
************* Module dist.NanoKeyboardControllerLiteApp._internal.cv2.config-3
dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:1:0: C0103: Module name "config-3" doesn't conform to snake_case naming style (invalid-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:3:4: E0602: Undefined variable 'LOADER_DIR' (undefined-variable)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:4:4: E0601: Using variable 'PYTHON_EXTENSIONS_PATHS' before assignment (used-before-assignment)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:12:0: W0702: No exception type(s) specified (bare-except)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:16:3: E0602: Undefined variable 'sys' (undefined-variable)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:17:4: E0602: Undefined variable 'os' (undefined-variable)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:17:48: E0602: Undefined variable 'os' (undefined-variable)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:18:8: E0602: Undefined variable 'os' (undefined-variable)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:18:24: E0602: Undefined variable 'os' (undefined-variable)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:22:3: E0602: Undefined variable 'sys' (undefined-variable)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:23:4: E0602: Undefined variable 'os' (undefined-variable)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:23:35: E0602: Undefined variable 'os' (undefined-variable)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:24:8: E0602: Undefined variable 'os' (undefined-variable)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:24:24: E0602: Undefined variable 'os' (undefined-variable)
************* Module dist.NanoKeyboardControllerLiteApp._internal.cv2.config
dist\NanoKeyboardControllerLiteApp\_internal\cv2\config.py:5:30: E0602: Undefined variable 'LOADER_DIR' (undefined-variable)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\config.py:6:4: E0601: Using variable 'BINARIES_PATHS' before assignment (used-before-assignment)
************* Module dist.NanoKeyboardControllerLiteApp._internal.cv2.load_config_py3
dist\NanoKeyboardControllerLiteApp\_internal\cv2\load_config_py3.py:9:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\load_config_py3.py:11:12: W0122: Use of exec (exec-used)
************* Module dist.NanoKeyboardControllerLiteApp._internal.cv2.version
dist\NanoKeyboardControllerLiteApp\_internal\cv2\version.py:2:0: C0103: Constant name "opencv_version" doesn't conform to UPPER_CASE naming style (invalid-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\version.py:3:0: C0103: Constant name "contrib" doesn't conform to UPPER_CASE naming style (invalid-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\version.py:4:0: C0103: Constant name "headless" doesn't conform to UPPER_CASE naming style (invalid-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\version.py:5:0: C0103: Constant name "rolling" doesn't conform to UPPER_CASE naming style (invalid-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\version.py:6:0: C0103: Constant name "ci_build" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module dist.NanoKeyboardControllerLiteApp._internal.cv2.__init__
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:80:0: C0301: Line too long (127/100) (line-too-long)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:88:0: C0301: Line too long (114/100) (line-too-long)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:114:0: C0301: Line too long (121/100) (line-too-long)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:122:0: C0301: Line too long (111/100) (line-too-long)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:152:0: C0301: Line too long (120/100) (line-too-long)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:169:0: C0301: Line too long (128/100) (line-too-long)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:19:1: W0511: TODO (fixme)
************* Module dist.NanoKeyboardControllerLiteApp._internal.cv2
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:25:18: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:26:25: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:45:35: C0321: More than one statement on a single line (multiple-statements)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:45:41: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:66:4: C0103: Variable name "__INIT_FILE_PATH" doesn't conform to snake_case naming style (invalid-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:71:0: R0914: Too many local variables (21/15) (too-many-locals)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:73:4: W0621: Redefining name 'sys' from outer scope (line 6) (redefined-outer-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:73:4: W0404: Reimport 'sys' (imported line 6) (reimported)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:73:4: C0415: Import outside toplevel (sys) (import-outside-toplevel)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:75:4: C0415: Import outside toplevel (copy) (import-outside-toplevel)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:83:4: C0103: Variable name "DEBUG" doesn't conform to snake_case naming style (invalid-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:85:8: C0103: Variable name "DEBUG" doesn't conform to snake_case naming style (invalid-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:87:4: C0415: Import outside toplevel (platform) (import-outside-toplevel)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:88:14: C0321: More than one statement on a single line (multiple-statements)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:88:20: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:90:4: C0103: Variable name "LOADER_DIR" doesn't conform to snake_case naming style (invalid-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:92:4: C0103: Variable name "PYTHON_EXTENSIONS_PATHS" doesn't conform to snake_case naming style (invalid-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:93:4: C0103: Variable name "BINARIES_PATHS" doesn't conform to snake_case naming style (invalid-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:99:8: C0415: Import outside toplevel (load_config_py2.exec_file_wrapper) (import-outside-toplevel)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:101:8: C0415: Import outside toplevel (load_config_py3.exec_file_wrapper) (import-outside-toplevel)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:108:26: C0321: More than one statement on a single line (multiple-statements)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:108:32: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:110:22: C0321: More than one statement on a single line (multiple-statements)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:110:28: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:114:30: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:118:8: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:119:8: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:122:14: C0321: More than one statement on a single line (multiple-statements)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:122:20: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:123:14: C0321: More than one statement on a single line (multiple-statements)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:123:20: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:125:4: C0103: Variable name "applySysPathWorkaround" doesn't conform to snake_case naming style (invalid-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:127:8: C0103: Variable name "applySysPathWorkaround" doesn't conform to snake_case naming style (invalid-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:133:8: W0702: No exception type(s) specified (bare-except)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:130:12: C0103: Variable name "BASE_DIR" doesn't conform to snake_case naming style (invalid-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:132:16: C0103: Variable name "applySysPathWorkaround" doesn't conform to snake_case naming style (invalid-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:134:22: C0321: More than one statement on a single line (multiple-statements)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:135:12: W0107: Unnecessary pass statement (unnecessary-pass)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:145:23: W0718: Catching too general exception Exception (broad-exception-caught)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:146:30: C0321: More than one statement on a single line (multiple-statements)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:147:20: W0107: Unnecessary pass statement (unnecessary-pass)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:149:18: C0321: More than one statement on a single line (multiple-statements)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:149:24: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:154:14: C0321: More than one statement on a single line (multiple-statements)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:173:11: W0718: Catching too general exception Exception (broad-exception-caught)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:178:14: C0321: More than one statement on a single line (multiple-statements)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:182:22: C0321: More than one statement on a single line (multiple-statements)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:184:14: C0321: More than one statement on a single line (multiple-statements)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:71:0: R0912: Too many branches (30/12) (too-many-branches)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:71:0: R0915: Too many statements (87/50) (too-many-statements)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:92:4: W0641: Possibly unused variable 'PYTHON_EXTENSIONS_PATHS' (possibly-unused-variable)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:93:4: W0641: Possibly unused variable 'BINARIES_PATHS' (possibly-unused-variable)
************* Module dist.NanoKeyboardControllerLiteApp._internal.cv2.gapi.__init__
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:331:0: W0311: Bad indentation. Found 19 spaces, expected 16 (bad-indentation)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:347:0: C0301: Line too long (108/100) (line-too-long)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:348:0: C0301: Line too long (104/100) (line-too-long)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:356:0: C0301: Line too long (108/100) (line-too-long)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:357:0: C0301: Line too long (105/100) (line-too-long)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:361:0: C0301: Line too long (106/100) (line-too-long)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:377:0: C0301: Line too long (119/100) (line-too-long)
************* Module dist.NanoKeyboardControllerLiteApp._internal.cv2.gapi
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:20:11: E1101: Module 'cv2' has no 'gapi_GNetPackage' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:26:20: E1101: Module 'cv2' has no 'GCompileArg' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:30:0: C0103: Function name "GIn" doesn't conform to snake_case naming style (invalid-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:36:0: C0103: Function name "GOut" doesn't conform to snake_case naming style (invalid-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:60:15: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:64:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:66:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:66:31: E1101: Module 'cv2.gapi' has no 'CV_BOOL' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:62:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:70:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:72:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:72:31: E1101: Module 'cv2.gapi' has no 'CV_INT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:68:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:76:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:78:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:78:31: E1101: Module 'cv2.gapi' has no 'CV_INT64' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:74:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:82:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:84:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:84:31: E1101: Module 'cv2.gapi' has no 'CV_UINT64' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:80:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:88:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:90:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:90:31: E1101: Module 'cv2.gapi' has no 'CV_DOUBLE' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:86:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:94:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:96:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:96:31: E1101: Module 'cv2.gapi' has no 'CV_FLOAT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:92:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:100:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:102:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:102:31: E1101: Module 'cv2.gapi' has no 'CV_STRING' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:98:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:106:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:108:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:108:31: E1101: Module 'cv2.gapi' has no 'CV_POINT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:104:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:112:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:114:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:114:31: E1101: Module 'cv2.gapi' has no 'CV_POINT2F' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:110:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:118:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:120:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:120:31: E1101: Module 'cv2.gapi' has no 'CV_POINT3F' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:116:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:124:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:126:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:126:31: E1101: Module 'cv2.gapi' has no 'CV_SIZE' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:122:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:130:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:132:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:132:31: E1101: Module 'cv2.gapi' has no 'CV_RECT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:128:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:136:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:138:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:138:31: E1101: Module 'cv2.gapi' has no 'CV_DRAW_PRIM' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:134:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:142:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:144:19: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:144:31: E1101: Module 'cv2.gapi' has no 'CV_ANY' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:140:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:54:0: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:153:15: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:157:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:159:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:159:30: E1101: Module 'cv2.gapi' has no 'CV_BOOL' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:155:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:163:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:165:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:165:30: E1101: Module 'cv2.gapi' has no 'CV_INT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:161:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:169:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:171:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:171:30: E1101: Module 'cv2.gapi' has no 'CV_INT64' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:167:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:175:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:177:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:177:30: E1101: Module 'cv2.gapi' has no 'CV_UINT64' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:173:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:181:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:183:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:183:30: E1101: Module 'cv2.gapi' has no 'CV_DOUBLE' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:179:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:187:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:189:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:189:30: E1101: Module 'cv2.gapi' has no 'CV_FLOAT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:185:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:193:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:195:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:195:30: E1101: Module 'cv2.gapi' has no 'CV_STRING' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:191:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:199:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:201:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:201:30: E1101: Module 'cv2.gapi' has no 'CV_POINT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:197:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:205:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:207:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:207:30: E1101: Module 'cv2.gapi' has no 'CV_POINT2F' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:203:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:211:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:213:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:213:30: E1101: Module 'cv2.gapi' has no 'CV_POINT3F' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:209:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:217:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:219:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:219:30: E1101: Module 'cv2.gapi' has no 'CV_SIZE' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:215:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:223:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:225:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:225:30: E1101: Module 'cv2.gapi' has no 'CV_RECT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:221:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:229:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:231:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:231:30: E1101: Module 'cv2.gapi' has no 'CV_SCALAR' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:227:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:235:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:237:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:237:30: E1101: Module 'cv2.gapi' has no 'CV_MAT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:233:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:241:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:243:19: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:243:30: E1101: Module 'cv2.gapi' has no 'CV_GMAT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:239:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:247:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:249:19: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:249:29: E1101: Module 'cv2.gapi' has no 'CV_DRAW_PRIM' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:245:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:253:8: C0202: Class method __new__ should have 'cls' as first argument (bad-classmethod-argument)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:255:19: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:255:29: E1101: Module 'cv2.gapi' has no 'CV_ANY' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:251:4: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:147:0: R0903: Too few public methods (1/2) (too-few-public-methods)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:263:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:263:31: E1101: Module 'cv2.gapi' has no 'CV_BOOL' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:264:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:264:31: E1101: Module 'cv2.gapi' has no 'CV_INT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:265:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:265:31: E1101: Module 'cv2.gapi' has no 'CV_INT64' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:266:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:266:31: E1101: Module 'cv2.gapi' has no 'CV_UINT64' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:267:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:267:31: E1101: Module 'cv2.gapi' has no 'CV_DOUBLE' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:268:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:268:31: E1101: Module 'cv2.gapi' has no 'CV_FLOAT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:269:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:269:31: E1101: Module 'cv2.gapi' has no 'CV_STRING' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:270:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:270:31: E1101: Module 'cv2.gapi' has no 'CV_POINT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:271:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:271:31: E1101: Module 'cv2.gapi' has no 'CV_POINT2F' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:272:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:272:31: E1101: Module 'cv2.gapi' has no 'CV_POINT3F' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:273:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:273:31: E1101: Module 'cv2.gapi' has no 'CV_SIZE' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:274:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:274:31: E1101: Module 'cv2.gapi' has no 'CV_RECT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:275:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:275:31: E1101: Module 'cv2.gapi' has no 'CV_SCALAR' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:276:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:276:31: E1101: Module 'cv2.gapi' has no 'CV_MAT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:277:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:277:31: E1101: Module 'cv2.gapi' has no 'CV_GMAT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:278:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:278:31: E1101: Module 'cv2.gapi' has no 'CV_DRAW_PRIM' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:279:12: E1101: Module 'cv2' has no 'GArray' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:279:31: E1101: Module 'cv2.gapi' has no 'CV_ANY' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:282:19: W0109: Duplicate key 'cv.GOpaque.Size' in dictionary (duplicate-key)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:282:19: W0109: Duplicate key 'cv.GOpaque.Rect' in dictionary (duplicate-key)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:283:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:283:32: E1101: Module 'cv2.gapi' has no 'CV_SIZE' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:284:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:284:32: E1101: Module 'cv2.gapi' has no 'CV_RECT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:285:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:285:32: E1101: Module 'cv2.gapi' has no 'CV_BOOL' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:286:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:286:32: E1101: Module 'cv2.gapi' has no 'CV_INT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:287:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:287:32: E1101: Module 'cv2.gapi' has no 'CV_INT64' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:288:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:288:32: E1101: Module 'cv2.gapi' has no 'CV_UINT64' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:289:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:289:32: E1101: Module 'cv2.gapi' has no 'CV_DOUBLE' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:290:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:290:32: E1101: Module 'cv2.gapi' has no 'CV_FLOAT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:291:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:291:32: E1101: Module 'cv2.gapi' has no 'CV_STRING' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:292:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:292:32: E1101: Module 'cv2.gapi' has no 'CV_POINT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:293:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:293:32: E1101: Module 'cv2.gapi' has no 'CV_POINT2F' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:294:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:294:32: E1101: Module 'cv2.gapi' has no 'CV_POINT3F' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:295:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:295:32: E1101: Module 'cv2.gapi' has no 'CV_SIZE' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:296:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:296:32: E1101: Module 'cv2.gapi' has no 'CV_RECT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:297:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:297:32: E1101: Module 'cv2.gapi' has no 'CV_DRAW_PRIM' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:298:12: E1101: Module 'cv2' has no 'GOpaque' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:298:32: E1101: Module 'cv2.gapi' has no 'CV_ANY' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:302:8: E1101: Module 'cv2.gapi' has no 'CV_BOOL' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:303:8: E1101: Module 'cv2.gapi' has no 'CV_INT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:304:8: E1101: Module 'cv2.gapi' has no 'CV_INT64' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:305:8: E1101: Module 'cv2.gapi' has no 'CV_UINT64' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:306:8: E1101: Module 'cv2.gapi' has no 'CV_DOUBLE' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:307:8: E1101: Module 'cv2.gapi' has no 'CV_FLOAT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:308:8: E1101: Module 'cv2.gapi' has no 'CV_STRING' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:309:8: E1101: Module 'cv2.gapi' has no 'CV_POINT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:310:8: E1101: Module 'cv2.gapi' has no 'CV_POINT2F' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:311:8: E1101: Module 'cv2.gapi' has no 'CV_POINT3F' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:312:8: E1101: Module 'cv2.gapi' has no 'CV_SIZE' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:313:8: E1101: Module 'cv2.gapi' has no 'CV_RECT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:314:8: E1101: Module 'cv2.gapi' has no 'CV_SCALAR' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:315:8: E1101: Module 'cv2.gapi' has no 'CV_MAT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:316:8: E1101: Module 'cv2.gapi' has no 'CV_GMAT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:317:8: E1101: Module 'cv2.gapi' has no 'CV_DRAW_PRIM' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:324:12: W0719: Raising too general exception: Exception (broad-exception-raised)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:324:28: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:327:12: W0719: Raising too general exception: Exception (broad-exception-raised)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:327:28: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:330:25: E1101: Module 'cv2' has no 'GMat' member; maybe 'Mat'? (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:330:34: E1101: Module 'cv2' has no 'GScalar' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:331:19: W0719: Raising too general exception: Exception (broad-exception-raised)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:331:35: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:364:12: W0621: Redefining name 'op' from outer scope (line 259) (redefined-outer-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:337:16: W0719: Raising too general exception: Exception (broad-exception-raised)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:337:32: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:342:20: R1720: Unnecessary "elif" after "raise", remove the leading "el" from "elif" (no-else-raise)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:342:41: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:343:24: W0719: Raising too general exception: Exception (broad-exception-raised)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:343:40: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:344:57: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:347:24: W0719: Raising too general exception: Exception (broad-exception-raised)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:347:40: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:351:20: R1720: Unnecessary "elif" after "raise", remove the leading "el" from "elif" (no-else-raise)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:351:41: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:352:24: W0719: Raising too general exception: Exception (broad-exception-raised)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:352:40: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:353:57: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:356:24: W0719: Raising too general exception: Exception (broad-exception-raised)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:356:40: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:360:23: C0123: Use isinstance() rather than type() for a typecheck. (unidiomatic-typecheck)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:361:24: W0719: Raising too general exception: Exception (broad-exception-raised)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:361:40: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:364:17: W0212: Access to a protected member __op of a client class (protected-access)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:364:17: E1101: Module 'cv2.gapi' has no '__op' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:368:31: E1101: Module 'cv2' has no 'GMat' member; maybe 'Mat'? (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:370:33: E1101: Module 'cv2' has no 'GScalar' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:377:20: W0719: Raising too general exception: Exception (broad-exception-raised)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:377:36: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:334:8: R0912: Too many branches (15/12) (too-many-branches)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:403:32: E1101: Module 'cv2' has no 'gapi_wip_gst_GStreamerPipeline' member (no-member)
************* Module dist.NanoKeyboardControllerLiteApp._internal.cv2.mat_wrapper.__init__
dist\NanoKeyboardControllerLiteApp\_internal\cv2\mat_wrapper\__init__.py:21:0: C0301: Line too long (106/100) (line-too-long)
************* Module dist.NanoKeyboardControllerLiteApp._internal.cv2.mat_wrapper
dist\NanoKeyboardControllerLiteApp\_internal\cv2\mat_wrapper\__init__.py:18:4: W0105: String statement has no effect (pointless-string-statement)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\mat_wrapper\__init__.py:29:4: W0231: __init__ method from base class 'ndarray' is not called (super-init-not-called)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\mat_wrapper\__init__.py:29:4: W0231: __init__ method from base class 'ndarray' is not called (super-init-not-called)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\mat_wrapper\__init__.py:33:28: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\mat_wrapper\__init__.py:44:0: W0212: Access to a protected member _registerMatType of a client class (protected-access)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\mat_wrapper\__init__.py:44:0: E1101: Module 'cv2' has no '_registerMatType' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\mat_wrapper\__init__.py:6:0: C0411: standard import "typing.TYPE_CHECKING" should be placed before third party imports "numpy", "cv2" (wrong-import-order)
************* Module dist.NanoKeyboardControllerLiteApp._internal.cv2.typing.__init__
dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:154:0: C0301: Line too long (104/100) (line-too-long)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:157:0: C0301: Line too long (193/100) (line-too-long)
************* Module dist.NanoKeyboardControllerLiteApp._internal.cv2.typing
dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:89:4: C0103: Class name "TermCriteria_Type" doesn't conform to PascalCase naming style (invalid-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:148:18: E1101: Module 'cv2' has no 'Feature2D' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:149:22: E1101: Module 'cv2' has no 'Feature2D' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:150:19: E1101: Module 'cv2' has no 'Feature2D' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:151:34: E1101: Module 'cv2' has no 'GMat' member; maybe 'Mat'? (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:151:44: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:151:58: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:154:41: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:154:55: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:156:25: E1101: Module 'cv2' has no 'GMat' member; maybe 'Mat'? (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:156:43: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:156:57: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:166:26: E1101: Module 'cv2' has no 'GMat' member; maybe 'Mat'? (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:166:44: E1101: Module 'cv2' has no 'GOpaqueT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:166:58: E1101: Module 'cv2' has no 'GArrayT' member (no-member)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:172:0: C0103: Class name "map_string_and_string" doesn't conform to PascalCase naming style (invalid-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:173:0: C0103: Class name "map_string_and_int" doesn't conform to PascalCase naming style (invalid-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:174:0: C0103: Class name "map_string_and_vector_size_t" doesn't conform to PascalCase naming style (invalid-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:175:0: C0103: Class name "map_string_and_vector_float" doesn't conform to PascalCase naming style (invalid-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:176:0: C0103: Class name "map_int_and_double" doesn't conform to PascalCase naming style (invalid-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:64:0: C0411: standard import "typing" should be placed before third party imports "cv2.mat_wrapper", "numpy", "cv2.dnn", "cv2" (wrong-import-order)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:62:0: C0412: Imports from package cv2 are not grouped (ungrouped-imports)
************* Module dist.NanoKeyboardControllerLiteApp._internal.cv2.utils
dist\NanoKeyboardControllerLiteApp\_internal\cv2\utils\__init__.py:11:0: C0103: Function name "testOverwriteNativeMethod" doesn't conform to snake_case naming style (invalid-name)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\utils\__init__.py:15:8: W0212: Access to a protected member _native of a client class (protected-access)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\utils\__init__.py:15:8: E1101: Module 'cv2.utils' has no '_native' member (no-member)
************* Module scratch.analyze_panel_pixels
scratch\analyze_panel_pixels.py:7:0: R0914: Too many local variables (18/15) (too-many-locals)
scratch\analyze_panel_pixels.py:9:10: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\analyze_panel_pixels.py:18:10: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
scratch\analyze_panel_pixels.py:18:28: E1101: Module 'cv2' has no 'COLOR_BGR2HSV' member (no-member)
scratch\analyze_panel_pixels.py:22:11: E1101: Module 'cv2' has no 'inRange' member (no-member)
scratch\analyze_panel_pixels.py:25:18: E1101: Module 'cv2' has no 'findContours' member (no-member)
scratch\analyze_panel_pixels.py:25:41: E1101: Module 'cv2' has no 'RETR_EXTERNAL' member (no-member)
scratch\analyze_panel_pixels.py:25:60: E1101: Module 'cv2' has no 'CHAIN_APPROX_SIMPLE' member (no-member)
scratch\analyze_panel_pixels.py:34:15: E1101: Module 'cv2' has no 'contourArea' member (no-member)
scratch\analyze_panel_pixels.py:36:33: E1101: Module 'cv2' has no 'boundingRect' member (no-member)
scratch\analyze_panel_pixels.py:42:16: E1101: Module 'cv2' has no 'imwrite' member (no-member)
scratch\analyze_panel_pixels.py:29:7: W0612: Unused variable 'w' (unused-variable)
************* Module scratch.analyze_resizing
scratch\analyze_resizing.py:14:0: C0413: Import "from app.auto_farm.rune_solver.panel_detect import arrow_boxes_for" should be placed at the top of the module (wrong-import-position)
scratch\analyze_resizing.py:15:0: C0413: Import "from app.auto_farm.rune_solver.vit_solver import ViTSolver" should be placed at the top of the module (wrong-import-position)
scratch\analyze_resizing.py:18:0: R0914: Too many local variables (19/15) (too-many-locals)
scratch\analyze_resizing.py:25:12: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\analyze_resizing.py:42:18: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
scratch\analyze_resizing.py:42:44: E1101: Module 'cv2' has no 'COLOR_BGR2RGB' member (no-member)
scratch\analyze_resizing.py:53:45: E1101: Module 'PIL.Image' has no 'LANCZOS' member (no-member)
scratch\analyze_resizing.py:46:4: W0612: Unused variable 'solver' (unused-variable)
scratch\analyze_resizing.py:3:0: W0611: Unused import os (unused-import)
scratch\analyze_resizing.py:8:0: W0611: Unused numpy imported as np (unused-import)
************* Module scratch.check_actual_right_endcap
scratch\check_actual_right_endcap.py:9:0: C0301: Line too long (115/100) (line-too-long)
scratch\check_actual_right_endcap.py:15:0: C0301: Line too long (113/100) (line-too-long)
scratch\check_actual_right_endcap.py:45:0: C0301: Line too long (122/100) (line-too-long)
scratch\check_actual_right_endcap.py:7:0: R0914: Too many local variables (17/15) (too-many-locals)
scratch\check_actual_right_endcap.py:10:10: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\check_actual_right_endcap.py:16:14: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\check_actual_right_endcap.py:25:10: E1101: Module 'cv2' has no 'matchTemplate' member (no-member)
scratch\check_actual_right_endcap.py:25:40: E1101: Module 'cv2' has no 'TM_CCOEFF_NORMED' member (no-member)
scratch\check_actual_right_endcap.py:34:29: E1101: Module 'cv2' has no 'minMaxLoc' member (no-member)
scratch\check_actual_right_endcap.py:44:4: E1101: Module 'cv2' has no 'imwrite' member (no-member)
scratch\check_actual_right_endcap.py:4:0: W0611: Unused numpy imported as np (unused-import)
************* Module scratch.check_interpolated_crops
scratch\check_interpolated_crops.py:8:0: C0301: Line too long (115/100) (line-too-long)
scratch\check_interpolated_crops.py:16:0: C0301: Line too long (135/100) (line-too-long)
scratch\check_interpolated_crops.py:33:0: C0301: Line too long (133/100) (line-too-long)
scratch\check_interpolated_crops.py:9:10: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\check_interpolated_crops.py:34:8: E1101: Module 'cv2' has no 'imwrite' member (no-member)
************* Module scratch.check_spec_error
scratch\check_spec_error.py:39:0: W0613: Unused argument 'args' (unused-argument)
scratch\check_spec_error.py:36:0: R0903: Too few public methods (0/2) (too-few-public-methods)
scratch\check_spec_error.py:106:7: W0718: Catching too general exception Exception (broad-exception-caught)
************* Module scratch.check_template_layout
scratch\check_template_layout.py:9:14: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\check_template_layout.py:19:4: C0103: Variable name "_TPL_BOX" doesn't conform to snake_case naming style (invalid-name)
scratch\check_template_layout.py:20:4: E1101: Module 'cv2' has no 'rectangle' member (no-member)
scratch\check_template_layout.py:23:4: E1101: Module 'cv2' has no 'rectangle' member (no-member)
scratch\check_template_layout.py:25:4: E1101: Module 'cv2' has no 'imwrite' member (no-member)
scratch\check_template_layout.py:4:0: W0611: Unused numpy imported as np (unused-import)
************* Module scratch.compare_pixels
scratch\compare_pixels.py:10:10: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\compare_pixels.py:12:10: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\compare_pixels.py:19:4: E1101: Module 'cv2' has no 'imwrite' member (no-member)
scratch\compare_pixels.py:26:4: E1101: Module 'cv2' has no 'imwrite' member (no-member)
scratch\compare_pixels.py:33:10: E1101: Module 'cv2' has no 'matchTemplate' member (no-member)
scratch\compare_pixels.py:33:43: E1101: Module 'cv2' has no 'TM_CCOEFF_NORMED' member (no-member)
scratch\compare_pixels.py:4:0: W0611: Unused numpy imported as np (unused-import)
************* Module scratch.crop_possible_arrows
scratch\crop_possible_arrows.py:9:10: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\crop_possible_arrows.py:39:8: E1101: Module 'cv2' has no 'circle' member (no-member)
scratch\crop_possible_arrows.py:42:8: E1101: Module 'cv2' has no 'imwrite' member (no-member)
scratch\crop_possible_arrows.py:23:8: W0612: Unused variable 'idx' (unused-variable)
scratch\crop_possible_arrows.py:4:0: W0611: Unused numpy imported as np (unused-import)
************* Module scratch.debug_build
scratch\debug_build.py:22:0: C0301: Line too long (143/100) (line-too-long)
scratch\debug_build.py:33:0: C0413: Import "import PyInstaller.__main__" should be placed at the top of the module (wrong-import-position)
scratch\debug_build.py:3:0: W0611: Unused import sys (unused-import)
************* Module scratch.debug_panel_detail
scratch\debug_panel_detail.py:12:0: C0413: Import "from app.auto_farm.rune_solver.panel_detect import detect_panel_origin, detect_right_endcap" should be placed at the top of the module (wrong-import-position)
scratch\debug_panel_detail.py:16:0: R0914: Too many local variables (39/15) (too-many-locals)
scratch\debug_panel_detail.py:18:10: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\debug_panel_detail.py:19:14: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\debug_panel_detail.py:21:4: C0103: Variable name "_TPL_BOX" doesn't conform to snake_case naming style (invalid-name)
scratch\debug_panel_detail.py:29:8: C0103: Variable name "L" doesn't conform to snake_case naming style (invalid-name)
scratch\debug_panel_detail.py:32:8: C0103: Variable name "L" doesn't conform to snake_case naming style (invalid-name)
scratch\debug_panel_detail.py:41:8: C0103: Variable name "R" doesn't conform to snake_case naming style (invalid-name)
scratch\debug_panel_detail.py:43:8: C0103: Variable name "R" doesn't conform to snake_case naming style (invalid-name)
scratch\debug_panel_detail.py:48:10: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
scratch\debug_panel_detail.py:48:28: E1101: Module 'cv2' has no 'COLOR_BGR2HSV' member (no-member)
scratch\debug_panel_detail.py:51:11: E1101: Module 'cv2' has no 'inRange' member (no-member)
scratch\debug_panel_detail.py:53:18: E1101: Module 'cv2' has no 'findContours' member (no-member)
scratch\debug_panel_detail.py:53:41: E1101: Module 'cv2' has no 'RETR_EXTERNAL' member (no-member)
scratch\debug_panel_detail.py:53:60: E1101: Module 'cv2' has no 'CHAIN_APPROX_SIMPLE' member (no-member)
scratch\debug_panel_detail.py:60:15: E1101: Module 'cv2' has no 'contourArea' member (no-member)
scratch\debug_panel_detail.py:62:25: E1101: Module 'cv2' has no 'boundingRect' member (no-member)
scratch\debug_panel_detail.py:16:0: R0912: Too many branches (17/12) (too-many-branches)
scratch\debug_panel_detail.py:16:0: R0915: Too many statements (61/50) (too-many-statements)
scratch\debug_panel_detail.py:7:0: W0611: Unused Image imported from PIL (unused-import)
************* Module scratch.detect_arrow_centers_by_color
scratch\detect_arrow_centers_by_color.py:9:0: C0301: Line too long (115/100) (line-too-long)
scratch\detect_arrow_centers_by_color.py:30:0: C0301: Line too long (107/100) (line-too-long)
scratch\detect_arrow_centers_by_color.py:59:0: C0301: Line too long (119/100) (line-too-long)
scratch\detect_arrow_centers_by_color.py:7:0: R0914: Too many local variables (20/15) (too-many-locals)
scratch\detect_arrow_centers_by_color.py:10:10: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\detect_arrow_centers_by_color.py:16:10: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
scratch\detect_arrow_centers_by_color.py:16:28: E1101: Module 'cv2' has no 'COLOR_BGR2HSV' member (no-member)
scratch\detect_arrow_centers_by_color.py:26:11: E1101: Module 'cv2' has no 'inRange' member (no-member)
scratch\detect_arrow_centers_by_color.py:29:4: E1101: Module 'cv2' has no 'imwrite' member (no-member)
scratch\detect_arrow_centers_by_color.py:35:18: E1101: Module 'cv2' has no 'findContours' member (no-member)
scratch\detect_arrow_centers_by_color.py:35:41: E1101: Module 'cv2' has no 'RETR_EXTERNAL' member (no-member)
scratch\detect_arrow_centers_by_color.py:35:60: E1101: Module 'cv2' has no 'CHAIN_APPROX_SIMPLE' member (no-member)
scratch\detect_arrow_centers_by_color.py:39:15: E1101: Module 'cv2' has no 'contourArea' member (no-member)
scratch\detect_arrow_centers_by_color.py:42:25: E1101: Module 'cv2' has no 'boundingRect' member (no-member)
scratch\detect_arrow_centers_by_color.py:58:8: E1101: Module 'cv2' has no 'imwrite' member (no-member)
************* Module scratch.find_arrows_fullframe
scratch\find_arrows_fullframe.py:7:0: R0914: Too many local variables (19/15) (too-many-locals)
scratch\find_arrows_fullframe.py:10:10: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\find_arrows_fullframe.py:18:10: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
scratch\find_arrows_fullframe.py:18:28: E1101: Module 'cv2' has no 'COLOR_BGR2HSV' member (no-member)
scratch\find_arrows_fullframe.py:21:11: E1101: Module 'cv2' has no 'inRange' member (no-member)
scratch\find_arrows_fullframe.py:23:18: E1101: Module 'cv2' has no 'findContours' member (no-member)
scratch\find_arrows_fullframe.py:23:41: E1101: Module 'cv2' has no 'RETR_EXTERNAL' member (no-member)
scratch\find_arrows_fullframe.py:23:60: E1101: Module 'cv2' has no 'CHAIN_APPROX_SIMPLE' member (no-member)
scratch\find_arrows_fullframe.py:27:15: E1101: Module 'cv2' has no 'contourArea' member (no-member)
scratch\find_arrows_fullframe.py:29:25: E1101: Module 'cv2' has no 'boundingRect' member (no-member)
************* Module scratch.find_panel_scale
scratch\find_panel_scale.py:9:12: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\find_panel_scale.py:10:14: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\find_panel_scale.py:30:24: E1101: Module 'cv2' has no 'resize' member (no-member)
scratch\find_panel_scale.py:30:72: E1101: Module 'cv2' has no 'INTER_LANCZOS4' member (no-member)
scratch\find_panel_scale.py:31:14: E1101: Module 'cv2' has no 'matchTemplate' member (no-member)
scratch\find_panel_scale.py:31:52: E1101: Module 'cv2' has no 'TM_CCOEFF_NORMED' member (no-member)
scratch\find_panel_scale.py:32:33: E1101: Module 'cv2' has no 'minMaxLoc' member (no-member)
************* Module scratch.find_perfect_scale
scratch\find_perfect_scale.py:7:0: R0914: Too many local variables (19/15) (too-many-locals)
scratch\find_perfect_scale.py:10:14: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\find_perfect_scale.py:18:14: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\find_perfect_scale.py:19:4: C0103: Variable name "_TPL_BOX" doesn't conform to snake_case naming style (invalid-name)
scratch\find_perfect_scale.py:38:22: E1101: Module 'cv2' has no 'resize' member (no-member)
scratch\find_perfect_scale.py:38:72: E1101: Module 'cv2' has no 'INTER_LANCZOS4' member (no-member)
scratch\find_perfect_scale.py:39:18: E1101: Module 'cv2' has no 'matchTemplate' member (no-member)
scratch\find_perfect_scale.py:39:52: E1101: Module 'cv2' has no 'TM_CCOEFF_NORMED' member (no-member)
scratch\find_perfect_scale.py:40:37: E1101: Module 'cv2' has no 'minMaxLoc' member (no-member)
scratch\find_perfect_scale.py:60:18: E1101: Module 'cv2' has no 'resize' member (no-member)
scratch\find_perfect_scale.py:60:68: E1101: Module 'cv2' has no 'INTER_LANCZOS4' member (no-member)
scratch\find_perfect_scale.py:61:14: E1101: Module 'cv2' has no 'matchTemplate' member (no-member)
scratch\find_perfect_scale.py:61:48: E1101: Module 'cv2' has no 'TM_CCOEFF_NORMED' member (no-member)
scratch\find_perfect_scale.py:62:33: E1101: Module 'cv2' has no 'minMaxLoc' member (no-member)
************* Module scratch.find_right_matches
scratch\find_right_matches.py:9:10: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\find_right_matches.py:14:14: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\find_right_matches.py:17:10: E1101: Module 'cv2' has no 'matchTemplate' member (no-member)
scratch\find_right_matches.py:17:40: E1101: Module 'cv2' has no 'TM_CCOEFF_NORMED' member (no-member)
************* Module scratch.inspect_matches
scratch\inspect_matches.py:9:10: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\inspect_matches.py:14:14: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\inspect_matches.py:28:4: E1101: Module 'cv2' has no 'imwrite' member (no-member)
scratch\inspect_matches.py:29:4: E1101: Module 'cv2' has no 'imwrite' member (no-member)
scratch\inspect_matches.py:30:4: E1101: Module 'cv2' has no 'imwrite' member (no-member)
scratch\inspect_matches.py:31:4: E1101: Module 'cv2' has no 'imwrite' member (no-member)
scratch\inspect_matches.py:4:0: W0611: Unused numpy imported as np (unused-import)
************* Module scratch.overlay_detected_centers
scratch\overlay_detected_centers.py:9:0: C0301: Line too long (115/100) (line-too-long)
scratch\overlay_detected_centers.py:37:0: C0301: Line too long (122/100) (line-too-long)
scratch\overlay_detected_centers.py:10:10: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\overlay_detected_centers.py:26:8: E1101: Module 'cv2' has no 'circle' member (no-member)
scratch\overlay_detected_centers.py:27:8: E1101: Module 'cv2' has no 'putText' member (no-member)
scratch\overlay_detected_centers.py:31:12: E1101: Module 'cv2' has no 'FONT_HERSHEY_SIMPLEX' member (no-member)
scratch\overlay_detected_centers.py:38:4: E1101: Module 'cv2' has no 'imwrite' member (no-member)
scratch\overlay_detected_centers.py:4:0: W0611: Unused numpy imported as np (unused-import)
************* Module scratch.test_colorkey_theme
scratch\test_colorkey_theme.py:10:0: R0902: Too many instance attributes (9/7) (too-many-instance-attributes)
scratch\test_colorkey_theme.py:101:8: C0415: Import outside toplevel (os) (import-outside-toplevel)
scratch\test_colorkey_theme.py:7:0: W0611: Unused Image imported from PIL (unused-import)
************* Module scratch.test_colorkey_transparency
scratch\test_colorkey_transparency.py:68:8: C0415: Import outside toplevel (os) (import-outside-toplevel)
scratch\test_colorkey_transparency.py:4:0: W0611: Unused ttk imported from tkinter (unused-import)
scratch\test_colorkey_transparency.py:7:0: W0611: Unused Image imported from PIL (unused-import)
************* Module scratch.test_color_vit
scratch\test_color_vit.py:13:0: C0301: Line too long (115/100) (line-too-long)
scratch\test_color_vit.py:49:0: C0301: Line too long (163/100) (line-too-long)
scratch\test_color_vit.py:11:0: R0914: Too many local variables (26/15) (too-many-locals)
scratch\test_color_vit.py:30:22: W0212: Access to a protected member _crop_with_offset of a client class (protected-access)
scratch\test_color_vit.py:31:25: W0212: Access to a protected member _preprocess of a client class (protected-access)
scratch\test_color_vit.py:3:0: W0611: Unused import cv2 (unused-import)
************* Module scratch.test_crops_with_vit
scratch\test_crops_with_vit.py:12:0: C0413: Import "from app.auto_farm.rune_solver.crop import DIRECTIONS" should be placed at the top of the module (wrong-import-position)
scratch\test_crops_with_vit.py:13:0: C0413: Import "from app.auto_farm.rune_solver.vit_solver import ViTSolver" should be placed at the top of the module (wrong-import-position)
scratch\test_crops_with_vit.py:47:14: W0212: Access to a protected member _preprocess of a client class (protected-access)
scratch\test_crops_with_vit.py:5:0: W0611: Unused import cv2 (unused-import)
************* Module scratch.test_full_pipeline_fix
scratch\test_full_pipeline_fix.py:11:0: C0413: Import "from app.auto_farm.rune_solver.crop import DIRECTIONS" should be placed at the top of the module (wrong-import-position)
scratch\test_full_pipeline_fix.py:12:0: C0413: Import "from app.auto_farm.rune_solver.vit_solver import ViTSolver" should be placed at the top of the module (wrong-import-position)
scratch\test_full_pipeline_fix.py:24:41: E1101: Module 'PIL.Image' has no 'LANCZOS' member (no-member)
scratch\test_full_pipeline_fix.py:36:0: R0914: Too many local variables (19/15) (too-many-locals)
scratch\test_full_pipeline_fix.py:38:10: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
scratch\test_full_pipeline_fix.py:38:32: E1101: Module 'cv2' has no 'COLOR_BGR2HSV' member (no-member)
scratch\test_full_pipeline_fix.py:41:11: E1101: Module 'cv2' has no 'inRange' member (no-member)
scratch\test_full_pipeline_fix.py:43:18: E1101: Module 'cv2' has no 'findContours' member (no-member)
scratch\test_full_pipeline_fix.py:43:41: E1101: Module 'cv2' has no 'RETR_EXTERNAL' member (no-member)
scratch\test_full_pipeline_fix.py:43:60: E1101: Module 'cv2' has no 'CHAIN_APPROX_SIMPLE' member (no-member)
scratch\test_full_pipeline_fix.py:47:15: E1101: Module 'cv2' has no 'contourArea' member (no-member)
scratch\test_full_pipeline_fix.py:49:25: E1101: Module 'cv2' has no 'boundingRect' member (no-member)
scratch\test_full_pipeline_fix.py:74:0: R0914: Too many local variables (16/15) (too-many-locals)
scratch\test_full_pipeline_fix.py:76:4: C0415: Import outside toplevel (itertools) (import-outside-toplevel)
scratch\test_full_pipeline_fix.py:74:35: W0613: Unused argument 'img_h' (unused-argument)
scratch\test_full_pipeline_fix.py:74:42: W0613: Unused argument 'img_w' (unused-argument)
scratch\test_full_pipeline_fix.py:104:0: R0914: Too many local variables (30/15) (too-many-locals)
scratch\test_full_pipeline_fix.py:106:18: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\test_full_pipeline_fix.py:113:18: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
scratch\test_full_pipeline_fix.py:113:44: E1101: Module 'cv2' has no 'COLOR_BGR2RGB' member (no-member)
scratch\test_full_pipeline_fix.py:119:18: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
scratch\test_full_pipeline_fix.py:119:50: E1101: Module 'cv2' has no 'COLOR_RGB2BGR' member (no-member)
scratch\test_full_pipeline_fix.py:132:14: W1309: Using an f-string that does not have any interpolated variables (f-string-without-interpolation)
scratch\test_full_pipeline_fix.py:143:8: C0415: Import outside toplevel (app.auto_farm.rune_solver.panel_detect.arrow_boxes_for) (import-outside-toplevel)
scratch\test_full_pipeline_fix.py:159:16: W0212: Access to a protected member _crop_with_offset of a client class (protected-access)
scratch\test_full_pipeline_fix.py:160:25: W0212: Access to a protected member _preprocess of a client class (protected-access)
scratch\test_full_pipeline_fix.py:169:4: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
************* Module scratch.test_internal_libs
scratch\test_internal_libs.py:11:0: C0413: Import "import cv2" should be placed at the top of the module (wrong-import-position)
scratch\test_internal_libs.py:13:0: C0413: Import "import numpy as np" should be placed at the top of the module (wrong-import-position)
scratch\test_internal_libs.py:14:0: C0413: Import "import onnxruntime as ort" should be placed at the top of the module (wrong-import-position)
scratch\test_internal_libs.py:15:0: C0413: Import "from PIL import Image" should be placed at the top of the module (wrong-import-position)
scratch\test_internal_libs.py:24:0: C0413: Import "from app.auto_farm.rune_solver.vit_solver import ViTSolver" should be placed at the top of the module (wrong-import-position)
scratch\test_internal_libs.py:27:0: C0103: Constant name "img_path" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module scratch.test_interpolation_vit
scratch\test_interpolation_vit.py:12:0: C0301: Line too long (115/100) (line-too-long)
scratch\test_interpolation_vit.py:17:0: C0301: Line too long (113/100) (line-too-long)
scratch\test_interpolation_vit.py:63:0: C0301: Line too long (110/100) (line-too-long)
scratch\test_interpolation_vit.py:10:0: R0914: Too many local variables (55/15) (too-many-locals)
scratch\test_interpolation_vit.py:14:13: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\test_interpolation_vit.py:18:14: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\test_interpolation_vit.py:23:12: E1101: Module 'cv2' has no 'matchTemplate' member (no-member)
scratch\test_interpolation_vit.py:23:45: E1101: Module 'cv2' has no 'TM_CCOEFF_NORMED' member (no-member)
scratch\test_interpolation_vit.py:44:12: E1101: Module 'cv2' has no 'matchTemplate' member (no-member)
scratch\test_interpolation_vit.py:44:45: E1101: Module 'cv2' has no 'TM_CCOEFF_NORMED' member (no-member)
scratch\test_interpolation_vit.py:63:58: E0601: Using variable 'rx_score' before assignment (used-before-assignment)
scratch\test_interpolation_vit.py:67:4: C0103: Variable name "L" doesn't conform to snake_case naming style (invalid-name)
scratch\test_interpolation_vit.py:68:4: C0103: Variable name "R" doesn't conform to snake_case naming style (invalid-name)
scratch\test_interpolation_vit.py:69:4: C0103: Variable name "W_panel" doesn't conform to snake_case naming style (invalid-name)
scratch\test_interpolation_vit.py:92:22: W0212: Access to a protected member _crop_with_offset of a client class (protected-access)
scratch\test_interpolation_vit.py:93:25: W0212: Access to a protected member _preprocess of a client class (protected-access)
scratch\test_interpolation_vit.py:107:4: C0415: Import outside toplevel (app.auto_farm.rune_solver.crop.DIRECTIONS) (import-outside-toplevel)
scratch\test_interpolation_vit.py:10:0: R0915: Too many statements (61/50) (too-many-statements)
************* Module scratch.test_main_app_screenshot
scratch\test_main_app_screenshot.py:23:0: C0301: Line too long (103/100) (line-too-long)
scratch\test_main_app_screenshot.py:9:0: C0413: Import "import time" should be placed at the top of the module (wrong-import-position)
scratch\test_main_app_screenshot.py:10:0: C0413: Import "import tkinter as tk" should be placed at the top of the module (wrong-import-position)
scratch\test_main_app_screenshot.py:12:0: C0413: Import "from PIL import ImageGrab" should be placed at the top of the module (wrong-import-position)
scratch\test_main_app_screenshot.py:14:0: C0413: Import "from app.main import ModernApp" should be placed at the top of the module (wrong-import-position)
scratch\test_main_app_screenshot.py:9:0: W0611: Unused import time (unused-import)
scratch\test_main_app_screenshot.py:10:0: W0611: Unused tkinter imported as tk (unused-import)
************* Module scratch.test_opacity
scratch\test_opacity.py:4:0: W0611: Unused ttk imported from tkinter (unused-import)
************* Module scratch.test_opacity_notebook
scratch\test_opacity_notebook.py:11:0: R0902: Too many instance attributes (8/7) (too-many-instance-attributes)
scratch\test_opacity_notebook.py:89:8: C0415: Import outside toplevel (os) (import-outside-toplevel)
scratch\test_opacity_notebook.py:3:0: W0611: Unused import time (unused-import)
scratch\test_opacity_notebook.py:8:0: W0611: Unused Image imported from PIL (unused-import)
************* Module scratch.test_opacity_screenshot
scratch\test_opacity_screenshot.py:68:8: C0415: Import outside toplevel (os) (import-outside-toplevel)
scratch\test_opacity_screenshot.py:3:0: W0611: Unused import time (unused-import)
scratch\test_opacity_screenshot.py:5:0: W0611: Unused ttk imported from tkinter (unused-import)
scratch\test_opacity_screenshot.py:8:0: W0611: Unused Image imported from PIL (unused-import)
scratch\test_opacity_screenshot.py:8:0: W0611: Unused ImageDraw imported from PIL (unused-import)
************* Module scratch.test_proportional_fix
scratch\test_proportional_fix.py:11:0: C0413: Import "from app.auto_farm.rune_solver.crop import DIRECTIONS" should be placed at the top of the module (wrong-import-position)
scratch\test_proportional_fix.py:12:0: C0413: Import "from app.auto_farm.rune_solver.panel_detect import arrow_boxes_for" should be placed at the top of the module (wrong-import-position)
scratch\test_proportional_fix.py:13:0: C0413: Import "from app.auto_farm.rune_solver.vit_solver import ViTSolver" should be placed at the top of the module (wrong-import-position)
scratch\test_proportional_fix.py:22:41: E1101: Module 'PIL.Image' has no 'LANCZOS' member (no-member)
scratch\test_proportional_fix.py:37:0: R0914: Too many local variables (28/15) (too-many-locals)
scratch\test_proportional_fix.py:40:18: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\test_proportional_fix.py:47:18: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
scratch\test_proportional_fix.py:47:44: E1101: Module 'cv2' has no 'COLOR_BGR2RGB' member (no-member)
scratch\test_proportional_fix.py:52:45: E1101: Module 'PIL.Image' has no 'LANCZOS' member (no-member)
scratch\test_proportional_fix.py:65:16: W0212: Access to a protected member _crop_with_offset of a client class (protected-access)
scratch\test_proportional_fix.py:66:29: W0212: Access to a protected member _preprocess of a client class (protected-access)
scratch\test_proportional_fix.py:75:4: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
scratch\test_proportional_fix.py:92:16: W0212: Access to a protected member _crop_with_offset of a client class (protected-access)
scratch\test_proportional_fix.py:93:29: W0212: Access to a protected member _preprocess of a client class (protected-access)
scratch\test_proportional_fix.py:101:4: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
************* Module scratch.test_proportional_resize
scratch\test_proportional_resize.py:12:0: C0413: Import "from app.auto_farm.rune_solver.panel_detect import detect_panel_origin, detect_right_endcap" should be placed at the top of the module (wrong-import-position)
scratch\test_proportional_resize.py:16:0: R0914: Too many local variables (67/15) (too-many-locals)
scratch\test_proportional_resize.py:18:14: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\test_proportional_resize.py:29:10: E1101: Module 'cv2' has no 'resize' member (no-member)
scratch\test_proportional_resize.py:29:60: E1101: Module 'cv2' has no 'INTER_LANCZOS4' member (no-member)
scratch\test_proportional_resize.py:33:14: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\test_proportional_resize.py:34:4: C0103: Variable name "_TPL_BOX" doesn't conform to snake_case naming style (invalid-name)
scratch\test_proportional_resize.py:42:4: C0103: Variable name "L" doesn't conform to snake_case naming style (invalid-name)
scratch\test_proportional_resize.py:50:4: C0103: Variable name "R" doesn't conform to snake_case naming style (invalid-name)
scratch\test_proportional_resize.py:54:10: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
scratch\test_proportional_resize.py:54:28: E1101: Module 'cv2' has no 'COLOR_BGR2HSV' member (no-member)
scratch\test_proportional_resize.py:57:11: E1101: Module 'cv2' has no 'inRange' member (no-member)
scratch\test_proportional_resize.py:59:18: E1101: Module 'cv2' has no 'findContours' member (no-member)
scratch\test_proportional_resize.py:59:41: E1101: Module 'cv2' has no 'RETR_EXTERNAL' member (no-member)
scratch\test_proportional_resize.py:59:60: E1101: Module 'cv2' has no 'CHAIN_APPROX_SIMPLE' member (no-member)
scratch\test_proportional_resize.py:66:15: E1101: Module 'cv2' has no 'contourArea' member (no-member)
scratch\test_proportional_resize.py:68:25: E1101: Module 'cv2' has no 'boundingRect' member (no-member)
scratch\test_proportional_resize.py:107:4: C0103: Variable name "ARROW_HALF_W" doesn't conform to snake_case naming style (invalid-name)
scratch\test_proportional_resize.py:108:4: C0103: Variable name "ARROW_HALF_H" doesn't conform to snake_case naming style (invalid-name)
scratch\test_proportional_resize.py:123:4: C0415: Import outside toplevel (app.auto_farm.rune_solver.crop.DIRECTIONS) (import-outside-toplevel)
scratch\test_proportional_resize.py:124:4: C0415: Import outside toplevel (app.auto_farm.rune_solver.vit_solver.ViTSolver) (import-outside-toplevel)
scratch\test_proportional_resize.py:127:30: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
scratch\test_proportional_resize.py:127:48: E1101: Module 'cv2' has no 'COLOR_BGR2RGB' member (no-member)
scratch\test_proportional_resize.py:133:27: W0212: Access to a protected member _crop_with_offset of a client class (protected-access)
scratch\test_proportional_resize.py:134:25: W0212: Access to a protected member _preprocess of a client class (protected-access)
scratch\test_proportional_resize.py:16:0: R0912: Too many branches (19/12) (too-many-branches)
scratch\test_proportional_resize.py:16:0: R0915: Too many statements (88/50) (too-many-statements)
************* Module scratch.test_prop_scaling
scratch\test_prop_scaling.py:34:0: C0301: Line too long (108/100) (line-too-long)
scratch\test_prop_scaling.py:60:0: C0301: Line too long (141/100) (line-too-long)
scratch\test_prop_scaling.py:9:14: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\test_prop_scaling.py:14:14: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\test_prop_scaling.py:48:18: E1101: Module 'cv2' has no 'resize' member (no-member)
scratch\test_prop_scaling.py:48:68: E1101: Module 'cv2' has no 'INTER_LANCZOS4' member (no-member)
scratch\test_prop_scaling.py:51:16: E1101: Module 'cv2' has no 'matchTemplate' member (no-member)
scratch\test_prop_scaling.py:51:50: E1101: Module 'cv2' has no 'TM_CCOEFF_NORMED' member (no-member)
scratch\test_prop_scaling.py:52:37: E1101: Module 'cv2' has no 'minMaxLoc' member (no-member)
scratch\test_prop_scaling.py:55:16: E1101: Module 'cv2' has no 'matchTemplate' member (no-member)
scratch\test_prop_scaling.py:55:50: E1101: Module 'cv2' has no 'TM_CCOEFF_NORMED' member (no-member)
scratch\test_prop_scaling.py:56:37: E1101: Module 'cv2' has no 'minMaxLoc' member (no-member)
scratch\test_prop_scaling.py:4:0: W0611: Unused numpy imported as np (unused-import)
************* Module scratch.test_robust_color_detect
scratch\test_robust_color_detect.py:7:0: R0914: Too many local variables (34/15) (too-many-locals)
scratch\test_robust_color_detect.py:9:14: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\test_robust_color_detect.py:16:10: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
scratch\test_robust_color_detect.py:16:32: E1101: Module 'cv2' has no 'COLOR_BGR2HSV' member (no-member)
scratch\test_robust_color_detect.py:19:11: E1101: Module 'cv2' has no 'inRange' member (no-member)
scratch\test_robust_color_detect.py:21:18: E1101: Module 'cv2' has no 'findContours' member (no-member)
scratch\test_robust_color_detect.py:21:41: E1101: Module 'cv2' has no 'RETR_EXTERNAL' member (no-member)
scratch\test_robust_color_detect.py:21:60: E1101: Module 'cv2' has no 'CHAIN_APPROX_SIMPLE' member (no-member)
scratch\test_robust_color_detect.py:25:15: E1101: Module 'cv2' has no 'contourArea' member (no-member)
scratch\test_robust_color_detect.py:27:25: E1101: Module 'cv2' has no 'boundingRect' member (no-member)
scratch\test_robust_color_detect.py:43:4: R1702: Too many nested blocks (7/5) (too-many-nested-blocks)
scratch\test_robust_color_detect.py:7:0: R0912: Too many branches (17/12) (too-many-branches)
************* Module scratch.test_robust_solver
scratch\test_robust_solver.py:13:0: C0301: Line too long (115/100) (line-too-long)
scratch\test_robust_solver.py:18:0: C0301: Line too long (113/100) (line-too-long)
scratch\test_robust_solver.py:113:0: C0301: Line too long (113/100) (line-too-long)
scratch\test_robust_solver.py:11:0: R0914: Too many local variables (68/15) (too-many-locals)
scratch\test_robust_solver.py:15:13: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\test_robust_solver.py:19:14: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\test_robust_solver.py:24:12: E1101: Module 'cv2' has no 'matchTemplate' member (no-member)
scratch\test_robust_solver.py:24:45: E1101: Module 'cv2' has no 'TM_CCOEFF_NORMED' member (no-member)
scratch\test_robust_solver.py:40:4: C0103: Variable name "L" doesn't conform to snake_case naming style (invalid-name)
scratch\test_robust_solver.py:44:12: E1101: Module 'cv2' has no 'matchTemplate' member (no-member)
scratch\test_robust_solver.py:44:45: E1101: Module 'cv2' has no 'TM_CCOEFF_NORMED' member (no-member)
scratch\test_robust_solver.py:61:4: C0103: Variable name "R" doesn't conform to snake_case naming style (invalid-name)
scratch\test_robust_solver.py:65:10: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
scratch\test_robust_solver.py:65:31: E1101: Module 'cv2' has no 'COLOR_BGR2HSV' member (no-member)
scratch\test_robust_solver.py:68:11: E1101: Module 'cv2' has no 'inRange' member (no-member)
scratch\test_robust_solver.py:70:18: E1101: Module 'cv2' has no 'findContours' member (no-member)
scratch\test_robust_solver.py:70:41: E1101: Module 'cv2' has no 'RETR_EXTERNAL' member (no-member)
scratch\test_robust_solver.py:70:60: E1101: Module 'cv2' has no 'CHAIN_APPROX_SIMPLE' member (no-member)
scratch\test_robust_solver.py:76:15: E1101: Module 'cv2' has no 'contourArea' member (no-member)
scratch\test_robust_solver.py:78:25: E1101: Module 'cv2' has no 'boundingRect' member (no-member)
scratch\test_robust_solver.py:115:8: C0103: Variable name "W_panel" doesn't conform to snake_case naming style (invalid-name)
scratch\test_robust_solver.py:127:22: W0212: Access to a protected member _crop_with_offset of a client class (protected-access)
scratch\test_robust_solver.py:128:25: W0212: Access to a protected member _preprocess of a client class (protected-access)
scratch\test_robust_solver.py:11:0: R0912: Too many branches (20/12) (too-many-branches)
scratch\test_robust_solver.py:11:0: R0915: Too many statements (88/50) (too-many-statements)
************* Module scratch.test_sidebar_transparency
scratch\test_sidebar_transparency.py:8:0: C0413: Import "import time" should be placed at the top of the module (wrong-import-position)
scratch\test_sidebar_transparency.py:9:0: C0413: Import "import tkinter as tk" should be placed at the top of the module (wrong-import-position)
scratch\test_sidebar_transparency.py:11:0: C0413: Import "import pywinstyles" should be placed at the top of the module (wrong-import-position)
scratch\test_sidebar_transparency.py:12:0: C0413: Import "from PIL import ImageGrab" should be placed at the top of the module (wrong-import-position)
scratch\test_sidebar_transparency.py:14:0: C0413: Import "from app.main import ModernApp" should be placed at the top of the module (wrong-import-position)
scratch\test_sidebar_transparency.py:30:23: W0718: Catching too general exception Exception (broad-exception-caught)
scratch\test_sidebar_transparency.py:8:0: W0611: Unused import time (unused-import)
************* Module scratch.test_vit_filtering
scratch\test_vit_filtering.py:12:0: C0413: Import "from app.auto_farm.rune_solver.crop import DIRECTIONS" should be placed at the top of the module (wrong-import-position)
scratch\test_vit_filtering.py:13:0: C0413: Import "from app.auto_farm.rune_solver.vit_solver import ViTSolver" should be placed at the top of the module (wrong-import-position)
scratch\test_vit_filtering.py:16:0: R0914: Too many local variables (38/15) (too-many-locals)
scratch\test_vit_filtering.py:19:14: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\test_vit_filtering.py:27:10: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
scratch\test_vit_filtering.py:27:32: E1101: Module 'cv2' has no 'COLOR_BGR2HSV' member (no-member)
scratch\test_vit_filtering.py:30:11: E1101: Module 'cv2' has no 'inRange' member (no-member)
scratch\test_vit_filtering.py:32:18: E1101: Module 'cv2' has no 'findContours' member (no-member)
scratch\test_vit_filtering.py:32:41: E1101: Module 'cv2' has no 'RETR_EXTERNAL' member (no-member)
scratch\test_vit_filtering.py:32:60: E1101: Module 'cv2' has no 'CHAIN_APPROX_SIMPLE' member (no-member)
scratch\test_vit_filtering.py:36:15: E1101: Module 'cv2' has no 'contourArea' member (no-member)
scratch\test_vit_filtering.py:38:25: E1101: Module 'cv2' has no 'boundingRect' member (no-member)
scratch\test_vit_filtering.py:51:34: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
scratch\test_vit_filtering.py:51:56: E1101: Module 'cv2' has no 'COLOR_BGR2RGB' member (no-member)
scratch\test_vit_filtering.py:69:14: W0212: Access to a protected member _preprocess of a client class (protected-access)
scratch\test_vit_filtering.py:16:0: R0912: Too many branches (13/12) (too-many-branches)
scratch\test_vit_filtering.py:16:0: R0915: Too many statements (54/50) (too-many-statements)
scratch\test_vit_filtering.py:59:28: W0612: Unused variable 'bbox' (unused-variable)
************* Module scratch.test_vit_filtering_fixed
scratch\test_vit_filtering_fixed.py:12:0: C0413: Import "from app.auto_farm.rune_solver.crop import DIRECTIONS" should be placed at the top of the module (wrong-import-position)
scratch\test_vit_filtering_fixed.py:13:0: C0413: Import "from app.auto_farm.rune_solver.vit_solver import ViTSolver" should be placed at the top of the module (wrong-import-position)
scratch\test_vit_filtering_fixed.py:16:0: R0914: Too many local variables (48/15) (too-many-locals)
scratch\test_vit_filtering_fixed.py:18:14: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\test_vit_filtering_fixed.py:26:10: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
scratch\test_vit_filtering_fixed.py:26:32: E1101: Module 'cv2' has no 'COLOR_BGR2HSV' member (no-member)
scratch\test_vit_filtering_fixed.py:29:11: E1101: Module 'cv2' has no 'inRange' member (no-member)
scratch\test_vit_filtering_fixed.py:31:18: E1101: Module 'cv2' has no 'findContours' member (no-member)
scratch\test_vit_filtering_fixed.py:31:41: E1101: Module 'cv2' has no 'RETR_EXTERNAL' member (no-member)
scratch\test_vit_filtering_fixed.py:31:60: E1101: Module 'cv2' has no 'CHAIN_APPROX_SIMPLE' member (no-member)
scratch\test_vit_filtering_fixed.py:35:15: E1101: Module 'cv2' has no 'contourArea' member (no-member)
scratch\test_vit_filtering_fixed.py:37:25: E1101: Module 'cv2' has no 'boundingRect' member (no-member)
scratch\test_vit_filtering_fixed.py:61:22: E1101: Module 'cv2' has no 'resize' member (no-member)
scratch\test_vit_filtering_fixed.py:61:72: E1101: Module 'cv2' has no 'INTER_LANCZOS4' member (no-member)
scratch\test_vit_filtering_fixed.py:62:34: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
scratch\test_vit_filtering_fixed.py:62:64: E1101: Module 'cv2' has no 'COLOR_BGR2RGB' member (no-member)
scratch\test_vit_filtering_fixed.py:83:14: W0212: Access to a protected member _preprocess of a client class (protected-access)
scratch\test_vit_filtering_fixed.py:16:0: R0912: Too many branches (14/12) (too-many-branches)
scratch\test_vit_filtering_fixed.py:16:0: R0915: Too many statements (63/50) (too-many-statements)
scratch\test_vit_filtering_fixed.py:67:28: W0612: Unused variable 'bbox' (unused-variable)
************* Module scratch.test_widget_opacity
scratch\test_widget_opacity.py:57:8: C0415: Import outside toplevel (os) (import-outside-toplevel)
scratch\test_widget_opacity.py:4:0: W0611: Unused ttk imported from tkinter (unused-import)
scratch\test_widget_opacity.py:7:0: W0611: Unused Image imported from PIL (unused-import)
************* Module scratch.try_delete_files
scratch\try_delete_files.py:8:0: C0301: Line too long (128/100) (line-too-long)
scratch\try_delete_files.py:18:15: W0718: Catching too general exception Exception (broad-exception-caught)
************* Module scratch.visualize_crop
scratch\visualize_crop.py:7:0: R0914: Too many local variables (31/15) (too-many-locals)
scratch\visualize_crop.py:10:10: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\visualize_crop.py:29:4: E1101: Module 'cv2' has no 'rectangle' member (no-member)
scratch\visualize_crop.py:33:10: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
scratch\visualize_crop.py:33:32: E1101: Module 'cv2' has no 'COLOR_BGR2HSV' member (no-member)
scratch\visualize_crop.py:36:11: E1101: Module 'cv2' has no 'inRange' member (no-member)
scratch\visualize_crop.py:38:18: E1101: Module 'cv2' has no 'findContours' member (no-member)
scratch\visualize_crop.py:38:41: E1101: Module 'cv2' has no 'RETR_EXTERNAL' member (no-member)
scratch\visualize_crop.py:38:60: E1101: Module 'cv2' has no 'CHAIN_APPROX_SIMPLE' member (no-member)
scratch\visualize_crop.py:42:15: E1101: Module 'cv2' has no 'contourArea' member (no-member)
scratch\visualize_crop.py:44:33: E1101: Module 'cv2' has no 'boundingRect' member (no-member)
scratch\visualize_crop.py:52:10: W1309: Using an f-string that does not have any interpolated variables (f-string-without-interpolation)
scratch\visualize_crop.py:56:8: E1101: Module 'cv2' has no 'circle' member (no-member)
scratch\visualize_crop.py:57:8: E1101: Module 'cv2' has no 'putText' member (no-member)
scratch\visualize_crop.py:58:51: E1101: Module 'cv2' has no 'FONT_HERSHEY_SIMPLEX' member (no-member)
scratch\visualize_crop.py:61:4: E1101: Module 'cv2' has no 'imwrite' member (no-member)
scratch\visualize_crop.py:62:4: E1101: Module 'cv2' has no 'imwrite' member (no-member)
************* Module scratch.visualize_matches
scratch\visualize_matches.py:7:0: R0914: Too many local variables (16/15) (too-many-locals)
scratch\visualize_matches.py:9:10: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\visualize_matches.py:14:14: E1101: Module 'cv2' has no 'imread' member (no-member)
scratch\visualize_matches.py:20:10: E1101: Module 'cv2' has no 'matchTemplate' member (no-member)
scratch\visualize_matches.py:20:40: E1101: Module 'cv2' has no 'TM_CCOEFF_NORMED' member (no-member)
scratch\visualize_matches.py:47:8: E1101: Module 'cv2' has no 'rectangle' member (no-member)
scratch\visualize_matches.py:48:8: E1101: Module 'cv2' has no 'putText' member (no-member)
scratch\visualize_matches.py:52:12: E1101: Module 'cv2' has no 'FONT_HERSHEY_SIMPLEX' member (no-member)
scratch\visualize_matches.py:62:4: E1101: Module 'cv2' has no 'imwrite' member (no-member)
scratch\visualize_matches.py:1:0: R0801: Similar lines in 2 files
==dist.NanoKeyboardControllerLiteApp._internal.cv2.gapi.__init__:[1:403]
==dist.lg_audio_helper_app._internal.cv2.gapi.__init__:[1:403]
__all__ = ['op', 'kernel']

import sys
import cv2 as cv

# NB: Register function in specific module
def register(mname):
    """TODO: add documentation"""
    def parameterized(func):
        """TODO: add documentation"""
        sys.modules[mname].__dict__[func.__name__] = func
        return func
    return parameterized


@register('cv2.gapi')
def networks(*args):
    """TODO: add documentation"""
    return cv.gapi_GNetPackage(list(map(cv.detail.strip, args)))


@register('cv2.gapi')
def compile_args(*args):
    """TODO: add documentation"""
    return list(map(cv.GCompileArg, args))


@register('cv2')
def GIn(*args):
    """TODO: add documentation"""
    return [*args]


@register('cv2')
def GOut(*args):
    """TODO: add documentation"""
    return [*args]


@register('cv2')
def gin(*args):
    """TODO: add documentation"""
    return [*args]


@register('cv2.gapi')
def descr_of(*args):
    """TODO: add documentation"""
    return [*args]


@register('cv2')
class GOpaque():
    """TODO: add documentation"""
    # NB: Inheritance from c++ class cause segfault.
    # So just aggregate cv.GOpaqueT instead of inheritance
    def __new__(cls, argtype):
        """TODO: add documentation"""
        return cv.GOpaqueT(argtype)

    class Bool():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GOpaqueT(cv.gapi.CV_BOOL)

    class Int():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GOpaqueT(cv.gapi.CV_INT)

    class Int64():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GOpaqueT(cv.gapi.CV_INT64)

    class UInt64():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GOpaqueT(cv.gapi.CV_UINT64)

    class Double():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GOpaqueT(cv.gapi.CV_DOUBLE)

    class Float():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GOpaqueT(cv.gapi.CV_FLOAT)

    class String():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GOpaqueT(cv.gapi.CV_STRING)

    class Point():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GOpaqueT(cv.gapi.CV_POINT)

    class Point2f():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GOpaqueT(cv.gapi.CV_POINT2F)

    class Point3f():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GOpaqueT(cv.gapi.CV_POINT3F)

    class Size():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GOpaqueT(cv.gapi.CV_SIZE)

    class Rect():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GOpaqueT(cv.gapi.CV_RECT)

    class Prim():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GOpaqueT(cv.gapi.CV_DRAW_PRIM)

    class Any():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GOpaqueT(cv.gapi.CV_ANY)

@register('cv2')
class GArray():
    """TODO: add documentation"""
    # NB: Inheritance from c++ class cause segfault.
    # So just aggregate cv.GArrayT instead of inheritance
    def __new__(cls, argtype):
        """TODO: add documentation"""
        return cv.GArrayT(argtype)

    class Bool():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GArrayT(cv.gapi.CV_BOOL)

    class Int():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GArrayT(cv.gapi.CV_INT)

    class Int64():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GArrayT(cv.gapi.CV_INT64)

    class UInt64():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GArrayT(cv.gapi.CV_UINT64)

    class Double():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GArrayT(cv.gapi.CV_DOUBLE)

    class Float():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GArrayT(cv.gapi.CV_FLOAT)

    class String():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GArrayT(cv.gapi.CV_STRING)

    class Point():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GArrayT(cv.gapi.CV_POINT)

    class Point2f():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GArrayT(cv.gapi.CV_POINT2F)

    class Point3f():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GArrayT(cv.gapi.CV_POINT3F)

    class Size():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GArrayT(cv.gapi.CV_SIZE)

    class Rect():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GArrayT(cv.gapi.CV_RECT)

    class Scalar():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GArrayT(cv.gapi.CV_SCALAR)

    class Mat():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GArrayT(cv.gapi.CV_MAT)

    class GMat():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GArrayT(cv.gapi.CV_GMAT)

    class Prim():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GArray(cv.gapi.CV_DRAW_PRIM)

    class Any():
        """TODO: add documentation"""
        def __new__(self):
            """TODO: add documentation"""
            return cv.GArray(cv.gapi.CV_ANY)


# NB: Top lvl decorator takes arguments
def op(op_id, in_types, out_types):
    """TODO: add documentation"""

    garray_types= {
            cv.GArray.Bool:    cv.gapi.CV_BOOL,
            cv.GArray.Int:     cv.gapi.CV_INT,
            cv.GArray.Int64:   cv.gapi.CV_INT64,
            cv.GArray.UInt64:  cv.gapi.CV_UINT64,
            cv.GArray.Double:  cv.gapi.CV_DOUBLE,
            cv.GArray.Float:   cv.gapi.CV_FLOAT,
            cv.GArray.String:  cv.gapi.CV_STRING,
            cv.GArray.Point:   cv.gapi.CV_POINT,
            cv.GArray.Point2f: cv.gapi.CV_POINT2F,
            cv.GArray.Point3f: cv.gapi.CV_POINT3F,
            cv.GArray.Size:    cv.gapi.CV_SIZE,
            cv.GArray.Rect:    cv.gapi.CV_RECT,
            cv.GArray.Scalar:  cv.gapi.CV_SCALAR,
            cv.GArray.Mat:     cv.gapi.CV_MAT,
            cv.GArray.GMat:    cv.gapi.CV_GMAT,
            cv.GArray.Prim:    cv.gapi.CV_DRAW_PRIM,
            cv.GArray.Any:     cv.gapi.CV_ANY
    }

    gopaque_types= {
            cv.GOpaque.Size:    cv.gapi.CV_SIZE,
            cv.GOpaque.Rect:    cv.gapi.CV_RECT,
            cv.GOpaque.Bool:    cv.gapi.CV_BOOL,
            cv.GOpaque.Int:     cv.gapi.CV_INT,
            cv.GOpaque.Int64:   cv.gapi.CV_INT64,
            cv.GOpaque.UInt64:  cv.gapi.CV_UINT64,
            cv.GOpaque.Double:  cv.gapi.CV_DOUBLE,
            cv.GOpaque.Float:   cv.gapi.CV_FLOAT,
            cv.GOpaque.String:  cv.gapi.CV_STRING,
            cv.GOpaque.Point:   cv.gapi.CV_POINT,
            cv.GOpaque.Point2f: cv.gapi.CV_POINT2F,
            cv.GOpaque.Point3f: cv.gapi.CV_POINT3F,
            cv.GOpaque.Size:    cv.gapi.CV_SIZE,
            cv.GOpaque.Rect:    cv.gapi.CV_RECT,
            cv.GOpaque.Prim:    cv.gapi.CV_DRAW_PRIM,
            cv.GOpaque.Any:     cv.gapi.CV_ANY
    }

    type2str = {
        cv.gapi.CV_BOOL:      'cv.gapi.CV_BOOL' ,
        cv.gapi.CV_INT:       'cv.gapi.CV_INT' ,
        cv.gapi.CV_INT64:     'cv.gapi.CV_INT64' ,
        cv.gapi.CV_UINT64:    'cv.gapi.CV_UINT64' ,
        cv.gapi.CV_DOUBLE:    'cv.gapi.CV_DOUBLE' ,
        cv.gapi.CV_FLOAT:     'cv.gapi.CV_FLOAT' ,
        cv.gapi.CV_STRING:    'cv.gapi.CV_STRING' ,
        cv.gapi.CV_POINT:     'cv.gapi.CV_POINT' ,
        cv.gapi.CV_POINT2F:   'cv.gapi.CV_POINT2F' ,
        cv.gapi.CV_POINT3F:   'cv.gapi.CV_POINT3F' ,
        cv.gapi.CV_SIZE:      'cv.gapi.CV_SIZE',
        cv.gapi.CV_RECT:      'cv.gapi.CV_RECT',
        cv.gapi.CV_SCALAR:    'cv.gapi.CV_SCALAR',
        cv.gapi.CV_MAT:       'cv.gapi.CV_MAT',
        cv.gapi.CV_GMAT:      'cv.gapi.CV_GMAT',
        cv.gapi.CV_DRAW_PRIM: 'cv.gapi.CV_DRAW_PRIM'
    }

    # NB: Second lvl decorator takes class to decorate
    def op_with_params(cls):
        """TODO: add documentation"""
        if not in_types:
            raise Exception('{} operation should have at least one input!'.format(cls.__name__))

        if not out_types:
            raise Exception('{} operation should have at least one output!'.format(cls.__name__))

        for i, t in enumerate(out_types):
            if t not in [cv.GMat, cv.GScalar, *garray_types, *gopaque_types]:
                   raise Exception('{} unsupported output type: {} in position: {}'
                           .format(cls.__name__, t.__name__, i))

        def on(*args):
            """TODO: add documentation"""
            if len(in_types) != len(args):
                raise Exception('Invalid number of input elements!\nExpected: {}, Actual: {}'
                        .format(len(in_types), len(args)))

            for i, (t, a) in enumerate(zip(in_types, args)):
                if t in garray_types:
                    if not isinstance(a, cv.GArrayT):
                        raise Exception("{} invalid type for argument {}.\nExpected: {}, Actual: {}"
                                .format(cls.__name__, i, cv.GArrayT.__name__, type(a).__name__))

                    elif a.type() != garray_types[t]:
                        raise Exception("{} invalid GArrayT type for argument {}.\nExpected: {}, Actual: {}"
                                .format(cls.__name__, i, type2str[garray_types[t]], type2str[a.type()]))

                elif t in gopaque_types:
                    if not isinstance(a, cv.GOpaqueT):
                        raise Exception("{} invalid type for argument {}.\nExpected: {}, Actual: {}"
                                .format(cls.__name__, i, cv.GOpaqueT.__name__, type(a).__name__))

                    elif a.type() != gopaque_types[t]:
                        raise Exception("{} invalid GOpaque type for argument {}.\nExpected: {}, Actual: {}"
                                .format(cls.__name__, i, type2str[gopaque_types[t]], type2str[a.type()]))

                else:
                    if t != type(a):
                        raise Exception('{} invalid input type for argument {}.\nExpected: {}, Actual: {}'
                                .format(cls.__name__, i, t.__name__, type(a).__name__))

            op = cv.gapi.__op(op_id, cls.outMeta, *args)

            out_protos = []
            for i, out_type in enumerate(out_types):
                if out_type == cv.GMat:
                    out_protos.append(op.getGMat())
                elif out_type == cv.GScalar:
                    out_protos.append(op.getGScalar())
                elif out_type in gopaque_types:
                    out_protos.append(op.getGOpaque(gopaque_types[out_type]))
                elif out_type in garray_types:
                    out_protos.append(op.getGArray(garray_types[out_type]))
                else:
                    raise Exception("""In {}: G-API operation can't produce the output with type: {} in position: {}"""
                            .format(cls.__name__, out_type.__name__, i))

            return tuple(out_protos) if len(out_protos) != 1 else out_protos[0]

        # NB: Extend operation class
        cls.id = op_id
        cls.on = staticmethod(on)
        return cls

    return op_with_params


def kernel(op_cls):
    """TODO: add documentation"""
    # NB: Second lvl decorator takes class to decorate
    def kernel_with_params(cls):
        """TODO: add documentation"""
        # NB: Add new members to kernel class
        cls.id      = op_cls.id
        cls.outMeta = op_cls.outMeta
        return cls

    return kernel_with_params


cv.gapi.wip.GStreamerPipeline = cv.gapi_wip_gst_GStreamerPipeline (duplicate-code)
Traceback (most recent call last):
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python311\Lib\site-packages\pylint\reporters\base_reporter.py", line 46, in writeln
    print(string, file=self.out)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python311\Lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeEncodeError: 'charmap' codec can't encode character '\u25b2' in position 4830: character maps to <undefined>

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python311\Lib\site-packages\pylint\__main__.py", line 10, in <module>
    pylint.run_pylint()
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python311\Lib\site-packages\pylint\__init__.py", line 34, in run_pylint
    PylintRun(argv or sys.argv[1:])
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python311\Lib\site-packages\pylint\lint\run.py", line 239, in __init__
    linter.check(args)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python311\Lib\site-packages\pylint\lint\pylinter.py", line 720, in check
    with self._astroid_module_checker() as check_astroid_module:
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python311\Lib\contextlib.py", line 144, in __exit__
    next(self.gen)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python311\Lib\site-packages\pylint\lint\pylinter.py", line 996, in _astroid_module_checker
    checker.close()
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python311\Lib\site-packages\pylint\checkers\symilar.py", line 857, in close
    self.add_message("R0801", args=(len(couples), "\n".join(msg)))
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python311\Lib\site-packages\pylint\checkers\base_checker.py", line 153, in add_message
    self.linter.add_message(
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python311\Lib\site-packages\pylint\lint\pylinter.py", line 1310, in add_message
    self._add_one_message(
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python311\Lib\site-packages\pylint\lint\pylinter.py", line 1268, in _add_one_message
    self.reporter.handle_message(
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python311\Lib\site-packages\pylint\reporters\text.py", line 161, in handle_message
    self.write_message(msg)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python311\Lib\site-packages\pylint\reporters\text.py", line 154, in write_message
    self.writeln(self._fixed_template.format(**self_dict))
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python311\Lib\site-packages\pylint\reporters\base_reporter.py", line 48, in writeln
    print(self.reencode_output_after_unicode_error(string), file=self.out)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python311\Lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeEncodeError: 'charmap' codec can't encode character '\u25b2' in position 4830: character maps to <undefined>


## Style Issues (flake8)

.\app\auto_farm\capture.py:6:1: E402 module level import not at top of file
.\app\auto_farm\capture.py:7:1: E402 module level import not at top of file
.\app\auto_farm\capture.py:8:1: E402 module level import not at top of file
.\app\auto_farm\capture.py:10:1: E402 module level import not at top of file
.\app\auto_farm\capture.py:11:1: E402 module level import not at top of file
.\app\auto_farm\capture.py:12:1: E402 module level import not at top of file
.\app\auto_farm\capture.py:13:1: E402 module level import not at top of file
.\app\auto_farm\capture.py:17:1: F401 'app.auto_farm.utils.multi_match' imported but unused
.\app\auto_farm\capture.py:17:1: E402 module level import not at top of file
.\app\auto_farm\capture.py:23:1: F841 local variable 'e' is assigned to but never used
.\app\auto_farm\capture.py:29:80: E501 line too long (87 > 79 characters)
.\app\auto_farm\capture.py:30:80: E501 line too long (87 > 79 characters)
.\app\auto_farm\capture.py:31:80: E501 line too long (84 > 79 characters)
.\app\auto_farm\capture.py:121:80: E501 line too long (107 > 79 characters)
.\app\auto_farm\capture.py:137:80: E501 line too long (93 > 79 characters)
.\app\auto_farm\capture.py:146:80: E501 line too long (105 > 79 characters)
.\app\auto_farm\capture.py:149:80: E501 line too long (82 > 79 characters)
.\app\auto_farm\capture.py:151:9: F841 local variable 'e' is assigned to but never used
.\app\auto_farm\capture.py:155:80: E501 line too long (86 > 79 characters)
.\app\auto_farm\capture.py:156:80: E501 line too long (86 > 79 characters)
.\app\auto_farm\capture.py:157:13: F841 local variable 'e' is assigned to but never used
.\app\auto_farm\capture.py:171:80: E501 line too long (84 > 79 characters)
.\app\auto_farm\capture.py:181:17: F841 local variable 'e' is assigned to but never used
.\app\auto_farm\capture.py:197:17: F841 local variable 'e' is assigned to but never used
.\app\auto_farm\capture.py:211:80: E501 line too long (121 > 79 characters)
.\app\auto_farm\capture.py:212:80: E501 line too long (114 > 79 characters)
.\app\auto_farm\capture.py:221:80: E501 line too long (81 > 79 characters)
.\app\auto_farm\capture.py:222:80: E501 line too long (94 > 79 characters)
.\app\auto_farm\capture.py:223:80: E501 line too long (101 > 79 characters)
.\app\auto_farm\capture.py:249:80: E501 line too long (97 > 79 characters)
.\app\auto_farm\capture.py:251:80: E501 line too long (104 > 79 characters)
.\app\auto_farm\capture.py:266:80: E501 line too long (91 > 79 characters)
.\app\auto_farm\capture.py:268:80: E501 line too long (112 > 79 characters)
.\app\auto_farm\capture.py:273:80: E501 line too long (99 > 79 characters)
.\app\auto_farm\capture.py:287:80: E501 line too long (85 > 79 characters)
.\app\auto_farm\capture.py:296:80: E501 line too long (88 > 79 characters)
.\app\auto_farm\capture.py:316:80: E501 line too long (91 > 79 characters)
.\app\auto_farm\capture.py:322:80: E501 line too long (113 > 79 characters)
.\app\auto_farm\capture.py:323:58: E203 whitespace before ':'
.\app\auto_farm\capture.py:323:79: E203 whitespace before ':'
.\app\auto_farm\capture.py:323:80: E501 line too long (97 > 79 characters)
.\app\auto_farm\capture.py:326:80: E501 line too long (111 > 79 characters)
.\app\auto_farm\capture.py:333:80: E501 line too long (83 > 79 characters)
.\app\auto_farm\capture.py:335:80: E501 line too long (81 > 79 characters)
.\app\auto_farm\capture.py:338:80: E501 line too long (94 > 79 characters)
.\app\auto_farm\capture.py:339:80: E501 line too long (94 > 79 characters)
.\app\auto_farm\capture.py:341:80: E501 line too long (86 > 79 characters)
.\app\auto_farm\capture.py:344:80: E501 line too long (80 > 79 characters)
.\app\auto_farm\controller.py:37:80: E501 line too long (82 > 79 characters)
.\app\auto_farm\controller.py:38:80: E501 line too long (82 > 79 characters)
.\app\auto_farm\controller.py:47:80: E501 line too long (122 > 79 characters)
.\app\auto_farm\controller.py:48:9: F401 'glob' imported but unused
.\app\auto_farm\controller.py:61:80: E501 line too long (106 > 79 characters)
.\app\auto_farm\controller.py:67:80: E501 line too long (103 > 79 characters)
.\app\auto_farm\controller.py:121:13: F841 local variable 'e' is assigned to but never used
.\app\auto_farm\controller.py:135:80: E501 line too long (87 > 79 characters)
.\app\auto_farm\controller.py:137:80: E501 line too long (96 > 79 characters)
.\app\auto_farm\controller.py:148:80: E501 line too long (84 > 79 characters)
.\app\auto_farm\controller.py:155:80: E501 line too long (81 > 79 characters)
.\app\auto_farm\controller.py:157:80: E501 line too long (95 > 79 characters)
.\app\auto_farm\controller.py:160:80: E501 line too long (89 > 79 characters)
.\app\auto_farm\controller.py:163:80: E501 line too long (90 > 79 characters)
.\app\auto_farm\controller.py:166:21: F841 local variable 'e' is assigned to but never used
.\app\auto_farm\controller.py:174:80: E501 line too long (86 > 79 characters)
.\app\auto_farm\controller.py:202:80: E501 line too long (124 > 79 characters)
.\app\auto_farm\controller.py:214:80: E501 line too long (124 > 79 characters)
.\app\auto_farm\controller.py:230:80: E501 line too long (117 > 79 characters)
.\app\auto_farm\controller.py:252:80: E501 line too long (96 > 79 characters)
.\app\auto_farm\controller.py:262:80: E501 line too long (88 > 79 characters)
.\app\auto_farm\controller.py:277:80: E501 line too long (84 > 79 characters)
.\app\auto_farm\controller.py:283:80: E501 line too long (86 > 79 characters)
.\app\auto_farm\controller.py:308:17: F841 local variable 'e' is assigned to but never used
.\app\auto_farm\controller.py:312:80: E501 line too long (99 > 79 characters)
.\app\auto_farm\controller.py:316:80: E501 line too long (110 > 79 characters)
.\app\auto_farm\controller.py:332:80: E501 line too long (94 > 79 characters)
.\app\auto_farm\controller.py:337:80: E501 line too long (110 > 79 characters)
.\app\auto_farm\controller.py:353:80: E501 line too long (94 > 79 characters)
.\app\auto_farm\controller.py:390:80: E501 line too long (82 > 79 characters)
.\app\auto_farm\controller.py:399:80: E501 line too long (97 > 79 characters)
.\app\auto_farm\controller.py:413:9: F841 local variable 'e' is assigned to but never used
.\app\auto_farm\controller.py:418:80: E501 line too long (81 > 79 characters)
.\app\auto_farm\controller.py:424:43: E203 whitespace before ':'
.\app\auto_farm\controller.py:426:80: E501 line too long (99 > 79 characters)
.\app\auto_farm\controller.py:436:80: E501 line too long (88 > 79 characters)
.\app\auto_farm\controller.py:452:80: E501 line too long (93 > 79 characters)
.\app\auto_farm\controller.py:464:80: E501 line too long (118 > 79 characters)
.\app\auto_farm\controller.py:487:80: E501 line too long (84 > 79 characters)
.\app\auto_farm\controller.py:493:80: E501 line too long (90 > 79 characters)
.\app\auto_farm\controller.py:495:80: E501 line too long (84 > 79 characters)
.\app\auto_farm\controller.py:499:80: E501 line too long (83 > 79 characters)
.\app\auto_farm\controller.py:505:80: E501 line too long (89 > 79 characters)
.\app\auto_farm\controller.py:506:80: E501 line too long (89 > 79 characters)
.\app\auto_farm\controller.py:514:80: E501 line too long (89 > 79 characters)
.\app\auto_farm\controller.py:515:80: E501 line too long (89 > 79 characters)
.\app\auto_farm\controller.py:528:80: E501 line too long (85 > 79 characters)
.\app\auto_farm\controller.py:532:80: E501 line too long (205 > 79 characters)
.\app\auto_farm\controller.py:546:80: E501 line too long (107 > 79 characters)
.\app\auto_farm\controller.py:554:80: E501 line too long (118 > 79 characters)
.\app\auto_farm\controller.py:571:80: E501 line too long (90 > 79 characters)
.\app\auto_farm\controller.py:574:80: E501 line too long (85 > 79 characters)
.\app\auto_farm\controller.py:586:80: E501 line too long (131 > 79 characters)
.\app\auto_farm\controller.py:591:80: E501 line too long (99 > 79 characters)
.\app\auto_farm\controller.py:592:80: E501 line too long (100 > 79 characters)
.\app\auto_farm\controller.py:595:80: E501 line too long (120 > 79 characters)
.\app\auto_farm\controller.py:600:80: E501 line too long (95 > 79 characters)
.\app\auto_farm\controller.py:609:80: E501 line too long (81 > 79 characters)
.\app\auto_farm\controller.py:610:43: E203 whitespace before ':'
.\app\auto_farm\controller.py:610:64: E203 whitespace before ':'
.\app\auto_farm\controller.py:614:80: E501 line too long (81 > 79 characters)
.\app\auto_farm\controller.py:615:80: E501 line too long (90 > 79 characters)
.\app\auto_farm\controller.py:619:80: E501 line too long (93 > 79 characters)
.\app\auto_farm\controller.py:621:80: E501 line too long (90 > 79 characters)
.\app\auto_farm\controller.py:628:80: E501 line too long (86 > 79 characters)
.\app\auto_farm\controller.py:632:80: E501 line too long (81 > 79 characters)
.\app\auto_farm\controller.py:638:80: E501 line too long (91 > 79 characters)
.\app\auto_farm\controller.py:639:13: F841 local variable 'app' is assigned to but never used
.\app\auto_farm\controller.py:641:80: E501 line too long (99 > 79 characters)
.\app\auto_farm\controller.py:642:80: E501 line too long (96 > 79 characters)
.\app\auto_farm\controller.py:643:80: E501 line too long (110 > 79 characters)
.\app\auto_farm\controller.py:648:80: E501 line too long (89 > 79 characters)
.\app\auto_farm\controller.py:654:80: E501 line too long (89 > 79 characters)
.\app\auto_farm\controller.py:659:80: E501 line too long (90 > 79 characters)
.\app\auto_farm\controller.py:663:80: E501 line too long (98 > 79 characters)
.\app\auto_farm\controller.py:673:80: E501 line too long (87 > 79 characters)
.\app\auto_farm\controller.py:676:80: E501 line too long (91 > 79 characters)
.\app\auto_farm\controller.py:687:80: E501 line too long (90 > 79 characters)
.\app\auto_farm\controller.py:695:80: E501 line too long (87 > 79 characters)
.\app\auto_farm\controller.py:701:80: E501 line too long (93 > 79 characters)
.\app\auto_farm\controller.py:710:80: E501 line too long (96 > 79 characters)
.\app\auto_farm\controller.py:713:80: E501 line too long (132 > 79 characters)
.\app\auto_farm\controller.py:718:80: E501 line too long (92 > 79 characters)
.\app\auto_farm\controller.py:726:80: E501 line too long (86 > 79 characters)
.\app\auto_farm\controller.py:736:80: E501 line too long (94 > 79 characters)
.\app\auto_farm\controller.py:739:80: E501 line too long (131 > 79 characters)
.\app\auto_farm\controller.py:744:80: E501 line too long (92 > 79 characters)
.\app\auto_farm\controller.py:764:80: E501 line too long (89 > 79 characters)
.\app\auto_farm\controller.py:767:80: E501 line too long (89 > 79 characters)
.\app\auto_farm\controller.py:769:80: E501 line too long (106 > 79 characters)
.\app\auto_farm\controller.py:773:80: E501 line too long (93 > 79 characters)
.\app\auto_farm\controller.py:775:80: E501 line too long (115 > 79 characters)
.\app\auto_farm\controller.py:784:80: E501 line too long (97 > 79 characters)
.\app\auto_farm\controller.py:788:80: E501 line too long (89 > 79 characters)
.\app\auto_farm\controller.py:792:80: E501 line too long (95 > 79 characters)
.\app\auto_farm\controller.py:816:80: E501 line too long (89 > 79 characters)
.\app\auto_farm\controller.py:820:80: E501 line too long (87 > 79 characters)
.\app\auto_farm\controller.py:824:80: E501 line too long (91 > 79 characters)
.\app\auto_farm\controller.py:832:80: E501 line too long (100 > 79 characters)
.\app\auto_farm\controller.py:842:80: E501 line too long (96 > 79 characters)
.\app\auto_farm\controller.py:848:80: E501 line too long (88 > 79 characters)
.\app\auto_farm\controller.py:849:80: E501 line too long (89 > 79 characters)
.\app\auto_farm\controller.py:853:80: E501 line too long (104 > 79 characters)
.\app\auto_farm\controller.py:857:80: E501 line too long (100 > 79 characters)
.\app\auto_farm\controller.py:862:80: E501 line too long (110 > 79 characters)
.\app\auto_farm\controller.py:870:80: E501 line too long (121 > 79 characters)
.\app\auto_farm\controller.py:878:80: E501 line too long (105 > 79 characters)
.\app\auto_farm\controller.py:883:80: E501 line too long (86 > 79 characters)
.\app\auto_farm\controller.py:886:80: E501 line too long (109 > 79 characters)
.\app\auto_farm\controller.py:891:80: E501 line too long (82 > 79 characters)
.\app\auto_farm\controller.py:896:80: E501 line too long (93 > 79 characters)
.\app\auto_farm\controller.py:901:80: E501 line too long (86 > 79 characters)
.\app\auto_farm\controller.py:905:80: E501 line too long (88 > 79 characters)
.\app\auto_farm\controller.py:907:80: E501 line too long (87 > 79 characters)
.\app\auto_farm\controller.py:909:80: E501 line too long (96 > 79 characters)
.\app\auto_farm\controller.py:910:80: E501 line too long (87 > 79 characters)
.\app\auto_farm\controller.py:915:80: E501 line too long (104 > 79 characters)
.\app\auto_farm\controller.py:917:80: E501 line too long (84 > 79 characters)
.\app\auto_farm\controller.py:921:80: E501 line too long (93 > 79 characters)
.\app\auto_farm\controller.py:925:80: E501 line too long (84 > 79 characters)
.\app\auto_farm\controller.py:931:80: E501 line too long (126 > 79 characters)
.\app\auto_farm\controller.py:939:80: E501 line too long (121 > 79 characters)
.\app\auto_farm\controller.py:947:80: E501 line too long (105 > 79 characters)
.\app\auto_farm\controller.py:965:13: F841 local variable 'e' is assigned to but never used
.\app\auto_farm\controller.py:970:80: E501 line too long (92 > 79 characters)
.\app\auto_farm\controller.py:984:80: E501 line too long (147 > 79 characters)
.\app\auto_farm\controller.py:994:80: E501 line too long (83 > 79 characters)
.\app\auto_farm\controller.py:1027:80: E501 line too long (99 > 79 characters)
.\app\auto_farm\controller.py:1031:80: E501 line too long (86 > 79 characters)
.\app\auto_farm\controller.py:1034:80: E501 line too long (85 > 79 characters)
.\app\auto_farm\controller.py:1063:80: E501 line too long (80 > 79 characters)
.\app\auto_farm\controller.py:1069:80: E501 line too long (91 > 79 characters)
.\app\auto_farm\controller.py:1095:80: E501 line too long (89 > 79 characters)
.\app\auto_farm\controller.py:1110:80: E501 line too long (115 > 79 characters)
.\app\auto_farm\rune_solver\data_vit.py:24:80: E501 line too long (85 > 79 characters)
.\app\auto_farm\rune_solver\hybrid_solver.py:35:80: E501 line too long (86 > 79 characters)
.\app\auto_farm\rune_solver\hybrid_solver.py:54:9: F401 'torch' imported but unused
.\app\auto_farm\rune_solver\hybrid_solver.py:57:80: E501 line too long (90 > 79 characters)
.\app\auto_farm\rune_solver\hybrid_solver.py:59:9: E741 ambiguous variable name 'l'
.\app\auto_farm\rune_solver\hybrid_solver.py:82:80: E501 line too long (100 > 79 characters)
.\app\auto_farm\rune_solver\hybrid_solver.py:92:80: E501 line too long (104 > 79 characters)
.\app\auto_farm\rune_solver\hybrid_solver.py:102:80: E501 line too long (99 > 79 characters)
.\app\auto_farm\rune_solver\hybrid_solver.py:107:80: E501 line too long (90 > 79 characters)
.\app\auto_farm\rune_solver\hybrid_solver.py:109:80: E501 line too long (81 > 79 characters)
.\app\auto_farm\rune_solver\hybrid_solver.py:112:80: E501 line too long (81 > 79 characters)
.\app\auto_farm\rune_solver\hybrid_solver.py:115:80: E501 line too long (84 > 79 characters)
.\app\auto_farm\rune_solver\hybrid_solver.py:118:80: E501 line too long (110 > 79 characters)
.\app\auto_farm\rune_solver\hybrid_solver.py:124:80: E501 line too long (108 > 79 characters)
.\app\auto_farm\rune_solver\hybrid_solver.py:127:80: E501 line too long (90 > 79 characters)
.\app\auto_farm\rune_solver\model_vit.py:3:80: E501 line too long (87 > 79 characters)
.\app\auto_farm\rune_solver\panel_detect.py:22:80: E501 line too long (87 > 79 characters)
.\app\auto_farm\rune_solver\panel_detect.py:32:80: E501 line too long (86 > 79 characters)
.\app\auto_farm\rune_solver\panel_detect.py:39:80: E501 line too long (97 > 79 characters)
.\app\auto_farm\rune_solver\panel_detect.py:40:80: E501 line too long (100 > 79 characters)
.\app\auto_farm\rune_solver\panel_detect.py:56:80: E501 line too long (87 > 79 characters)
.\app\auto_farm\rune_solver\panel_detect.py:73:80: E501 line too long (104 > 79 characters)
.\app\auto_farm\rune_solver\panel_detect.py:99:80: E501 line too long (87 > 79 characters)
.\app\auto_farm\rune_solver\panel_detect.py:107:80: E501 line too long (83 > 79 characters)
.\app\auto_farm\rune_solver\panel_detect.py:109:32: E203 whitespace before ':'
.\app\auto_farm\rune_solver\panel_detect.py:109:59: E203 whitespace before ':'
.\app\auto_farm\rune_solver\panel_detect.py:115:80: E501 line too long (81 > 79 characters)
.\app\auto_farm\rune_solver\panel_detect.py:123:80: E501 line too long (81 > 79 characters)
.\app\auto_farm\rune_solver\panel_detect.py:143:80: E501 line too long (85 > 79 characters)
.\app\auto_farm\rune_solver\panel_detect.py:147:80: E501 line too long (84 > 79 characters)
.\app\auto_farm\rune_solver\panel_detect.py:151:80: E501 line too long (82 > 79 characters)
.\app\auto_farm\rune_solver\panel_detect.py:217:80: E501 line too long (100 > 79 characters)
.\app\auto_farm\rune_solver\panel_detect.py:220:80: E501 line too long (93 > 79 characters)
.\app\auto_farm\rune_solver\panel_detect.py:224:80: E501 line too long (92 > 79 characters)
.\app\auto_farm\rune_solver\panel_detect.py:229:71: E741 ambiguous variable name 'l'
.\app\auto_farm\rune_solver\panel_detect.py:229:80: E501 line too long (90 > 79 characters)
.\app\auto_farm\rune_solver\roboflow_client.py:41:80: E501 line too long (80 > 79 characters)
.\app\auto_farm\rune_solver\roboflow_client.py:43:80: E501 line too long (92 > 79 characters)
.\app\auto_farm\rune_solver\roboflow_client.py:82:80: E501 line too long (82 > 79 characters)
.\app\auto_farm\rune_solver\roboflow_client.py:90:80: E501 line too long (110 > 79 characters)
.\app\auto_farm\rune_solver\roboflow_client.py:93:80: E501 line too long (82 > 79 characters)
.\app\auto_farm\rune_solver\roboflow_client.py:102:80: E501 line too long (89 > 79 characters)
.\app\auto_farm\rune_solver\roboflow_client.py:103:21: F841 local variable 'e' is assigned to but never used
.\app\auto_farm\rune_solver\roboflow_client.py:109:80: E501 line too long (87 > 79 characters)
.\app\auto_farm\rune_solver\roboflow_client.py:113:80: E501 line too long (126 > 79 characters)
.\app\auto_farm\rune_solver\roboflow_client.py:116:80: E501 line too long (86 > 79 characters)
.\app\auto_farm\rune_solver\roboflow_client.py:130:80: E501 line too long (97 > 79 characters)
.\app\auto_farm\rune_solver\roboflow_client.py:137:80: E501 line too long (100 > 79 characters)
.\app\auto_farm\rune_solver\roboflow_client.py:139:25: F841 local variable 'e' is assigned to but never used
.\app\auto_farm\rune_solver\roboflow_client.py:144:80: E501 line too long (91 > 79 characters)
.\app\auto_farm\rune_solver\roboflow_client.py:147:80: E501 line too long (82 > 79 characters)
.\app\auto_farm\rune_solver\roboflow_client.py:149:80: E501 line too long (103 > 79 characters)
.\app\auto_farm\rune_solver\roboflow_client.py:154:80: E501 line too long (97 > 79 characters)
.\app\auto_farm\rune_solver\roboflow_client.py:155:80: E501 line too long (102 > 79 characters)
.\app\auto_farm\rune_solver\roboflow_client.py:157:80: E501 line too long (104 > 79 characters)
.\app\auto_farm\rune_solver\roboflow_client.py:162:80: E501 line too long (87 > 79 characters)
.\app\auto_farm\rune_solver\solver.py:30:80: E501 line too long (89 > 79 characters)
.\app\auto_farm\rune_solver\solver.py:45:80: E501 line too long (98 > 79 characters)
.\app\auto_farm\rune_solver\solver.py:46:80: E501 line too long (90 > 79 characters)
.\app\auto_farm\rune_solver\solver.py:72:80: E501 line too long (119 > 79 characters)
.\app\auto_farm\rune_solver\solver.py:76:80: E501 line too long (85 > 79 characters)
.\app\auto_farm\rune_solver\solver.py:98:80: E501 line too long (85 > 79 characters)
.\app\auto_farm\rune_solver\solver.py:103:80: E501 line too long (84 > 79 characters)
.\app\auto_farm\rune_solver\vit_solver.py:1:80: E501 line too long (88 > 79 characters)
.\app\auto_farm\rune_solver\vit_solver.py:5:1: F401 'os' imported but unused
.\app\auto_farm\rune_solver\vit_solver.py:27:80: E501 line too long (83 > 79 characters)
.\app\auto_farm\rune_solver\vit_solver.py:28:80: E501 line too long (82 > 79 characters)
.\app\auto_farm\rune_solver\vit_solver.py:47:80: E501 line too long (95 > 79 characters)
.\app\auto_farm\rune_solver\vit_solver.py:56:80: E501 line too long (82 > 79 characters)
.\app\auto_farm\rune_solver\vit_solver.py:70:80: E501 line too long (83 > 79 characters)
.\app\auto_farm\rune_solver\vit_solver.py:81:80: E501 line too long (84 > 79 characters)
.\app\auto_farm\rune_solver\vit_solver.py:102:80: E501 line too long (85 > 79 characters)
.\app\auto_farm\rune_solver\vit_solver.py:117:17: F401 'cv2 as _cv2' imported but unused
.\app\auto_farm\rune_solver\vit_solver.py:118:17: F401 'numpy as _np' imported but unused
.\app\auto_farm\rune_solver\vit_solver.py:119:17: F401 'PIL.ImageFont' imported but unused
.\app\auto_farm\rune_solver\vit_solver.py:136:80: E501 line too long (91 > 79 characters)
.\app\auto_farm\rune_solver\vit_solver.py:152:80: E501 line too long (133 > 79 characters)
.\app\auto_farm\rune_solver\vit_solver.py:171:80: E501 line too long (81 > 79 characters)
.\app\auto_farm\rune_solver\vit_solver.py:188:80: E501 line too long (94 > 79 characters)
.\app\auto_farm\rune_solver\vit_solver.py:190:80: E501 line too long (103 > 79 characters)
.\app\auto_farm\utils.py:19:80: E501 line too long (82 > 79 characters)
.\app\auto_farm\utils.py:33:80: E501 line too long (84 > 79 characters)
.\app\auto_farm\utils.py:67:5: F841 local variable 'e' is assigned to but never used
.\app\auto_farm\utils.py:77:80: E501 line too long (81 > 79 characters)
.\app\auto_farm\vkeys.py:1:80: E501 line too long (104 > 79 characters)
.\app\auto_farm\vkeys.py:28:80: E501 line too long (85 > 79 characters)
.\app\auto_farm\vkeys.py:36:1: E302 expected 2 blank lines, found 1
.\app\auto_farm\vkeys.py:66:1: E305 expected 2 blank lines after class or function definition, found 1
.\app\auto_farm\vkeys.py:112:80: E501 line too long (85 > 79 characters)
.\app\auto_farm\vkeys.py:120:80: E501 line too long (95 > 79 characters)
.\app\auto_farm\vkeys.py:128:80: E501 line too long (90 > 79 characters)
.\app\auto_farm\vkeys.py:138:80: E501 line too long (85 > 79 characters)
.\app\auto_farm\vkeys.py:157:80: E501 line too long (91 > 79 characters)
.\app\auto_farm\vkeys.py:177:80: E501 line too long (85 > 79 characters)
.\app\auto_farm\vkeys.py:181:80: E501 line too long (81 > 79 characters)
.\app\auto_farm\vkeys.py:200:80: E501 line too long (85 > 79 characters)
.\app\auto_farm\vkeys.py:204:80: E501 line too long (127 > 79 characters)
.\app\auto_farm\vkeys.py:210:80: E501 line too long (93 > 79 characters)
.\app\connection.py:9:80: E501 line too long (88 > 79 characters)
.\app\connection.py:71:80: E501 line too long (93 > 79 characters)
.\app\connection.py:76:80: E501 line too long (86 > 79 characters)
.\app\connection.py:89:80: E501 line too long (88 > 79 characters)
.\app\connection.py:112:13: F841 local variable 'e' is assigned to but never used
.\app\connection.py:151:80: E501 line too long (80 > 79 characters)
.\app\connection.py:153:80: E501 line too long (101 > 79 characters)
.\app\connection.py:155:35: E203 whitespace before ':'
.\app\connection.py:169:80: E501 line too long (88 > 79 characters)
.\app\connection.py:225:80: E501 line too long (96 > 79 characters)
.\app\connection.py:228:80: E501 line too long (94 > 79 characters)
.\app\connection.py:231:80: E501 line too long (83 > 79 characters)
.\app\connection.py:235:80: E501 line too long (91 > 79 characters)
.\app\connection.py:252:80: E501 line too long (97 > 79 characters)
.\app\connection.py:271:80: E501 line too long (84 > 79 characters)
.\app\connection.py:282:59: E203 whitespace before ':'
.\app\connection.py:286:65: E203 whitespace before ':'
.\app\connection.py:286:80: E501 line too long (80 > 79 characters)
.\app\connection.py:288:65: E203 whitespace before ':'
.\app\connection.py:288:80: E501 line too long (80 > 79 characters)
.\app\connection.py:290:65: E203 whitespace before ':'
.\app\connection.py:290:80: E501 line too long (80 > 79 characters)
.\app\connection.py:292:65: E203 whitespace before ':'
.\app\connection.py:292:80: E501 line too long (80 > 79 characters)
.\app\connection.py:294:68: E203 whitespace before ':'
.\app\connection.py:294:80: E501 line too long (83 > 79 characters)
.\app\connection.py:311:54: E203 whitespace before ':'
.\app\connection.py:313:54: E203 whitespace before ':'
.\app\connection.py:315:80: E501 line too long (94 > 79 characters)
.\app\connection.py:324:80: E501 line too long (95 > 79 characters)
.\app\connection.py:333:80: E501 line too long (86 > 79 characters)
.\app\connection.py:339:80: E501 line too long (87 > 79 characters)
.\app\connection.py:339:85: E203 whitespace before ':'
.\app\connection.py:344:80: E501 line too long (81 > 79 characters)
.\app\connection.py:346:80: E501 line too long (96 > 79 characters)
.\app\connection.py:367:80: E501 line too long (96 > 79 characters)
.\app\connection.py:371:80: E501 line too long (102 > 79 characters)
.\app\connection.py:377:80: E501 line too long (83 > 79 characters)
.\app\connection.py:387:80: E501 line too long (91 > 79 characters)
.\app\connection.py:389:80: E501 line too long (107 > 79 characters)
.\app\connection.py:392:80: E501 line too long (91 > 79 characters)
.\app\connection.py:394:80: E501 line too long (96 > 79 characters)
.\app\connection.py:399:80: E501 line too long (96 > 79 characters)
.\app\connection.py:402:80: E501 line too long (80 > 79 characters)
.\app\connection.py:410:80: E501 line too long (85 > 79 characters)
.\app\connection.py:414:80: E501 line too long (86 > 79 characters)
.\app\connection.py:415:80: E501 line too long (81 > 79 characters)
.\app\connection.py:416:80: E501 line too long (83 > 79 characters)
.\app\connection.py:419:80: E501 line too long (80 > 79 characters)
.\app\connection.py:427:80: E501 line too long (82 > 79 characters)
.\app\connection.py:465:80: E501 line too long (99 > 79 characters)
.\app\connection.py:472:80: E501 line too long (88 > 79 characters)
.\app\connection.py:493:80: E501 line too long (86 > 79 characters)
.\app\driver_manager.py:13:80: E501 line too long (86 > 79 characters)
.\app\driver_manager.py:15:80: E501 line too long (86 > 79 characters)
.\app\driver_manager.py:23:80: E501 line too long (87 > 79 characters)
.\app\driver_manager.py:28:80: E501 line too long (83 > 79 characters)
.\app\driver_manager.py:32:80: E501 line too long (81 > 79 characters)
.\app\driver_manager.py:85:5: F841 local variable 'e' is assigned to but never used
.\app\driver_manager.py:94:80: E501 line too long (82 > 79 characters)
.\app\driver_manager.py:95:80: E501 line too long (96 > 79 characters)
.\app\driver_manager.py:107:80: E501 line too long (85 > 79 characters)
.\app\driver_manager.py:127:80: E501 line too long (84 > 79 characters)
.\app\driver_manager.py:143:80: E501 line too long (83 > 79 characters)
.\app\driver_manager.py:146:80: E501 line too long (93 > 79 characters)
.\app\driver_manager.py:164:80: E501 line too long (84 > 79 characters)
.\app\driver_manager.py:165:80: E501 line too long (96 > 79 characters)
.\app\driver_manager.py:167:80: E501 line too long (92 > 79 characters)
.\app\driver_manager.py:172:80: E501 line too long (91 > 79 characters)
.\app\driver_manager.py:176:80: E501 line too long (96 > 79 characters)
.\app\main.py:7:1: F841 local variable 'e' is assigned to but never used
.\app\main.py:11:5: F841 local variable 'e' is assigned to but never used
.\app\main.py:48:80: E501 line too long (84 > 79 characters)
.\app\main.py:71:80: E501 line too long (80 > 79 characters)
.\app\main.py:79:80: E501 line too long (86 > 79 characters)
.\app\main.py:107:80: E501 line too long (97 > 79 characters)
.\app\main.py:109:80: E501 line too long (108 > 79 characters)
.\app\main.py:122:80: E501 line too long (97 > 79 characters)
.\app\main.py:125:80: E501 line too long (92 > 79 characters)
.\app\main.py:159:80: E501 line too long (86 > 79 characters)
.\app\main.py:161:80: E501 line too long (82 > 79 characters)
.\app\main.py:164:80: E501 line too long (100 > 79 characters)
.\app\main.py:180:80: E501 line too long (92 > 79 characters)
.\app\main.py:196:80: E501 line too long (88 > 79 characters)
.\app\main.py:197:80: E501 line too long (88 > 79 characters)
.\app\main.py:226:80: E501 line too long (87 > 79 characters)
.\app\main.py:229:80: E501 line too long (93 > 79 characters)
.\app\main.py:244:80: E501 line too long (95 > 79 characters)
.\app\main.py:253:80: E501 line too long (85 > 79 characters)
.\app\main.py:281:80: E501 line too long (89 > 79 characters)
.\app\main.py:338:80: E501 line too long (94 > 79 characters)
.\app\main.py:340:80: E501 line too long (100 > 79 characters)
.\app\main.py:347:80: E501 line too long (89 > 79 characters)
.\app\main.py:353:80: E501 line too long (89 > 79 characters)
.\app\main.py:357:80: E501 line too long (81 > 79 characters)
.\app\main.py:391:80: E501 line too long (101 > 79 characters)
.\app\main.py:396:80: E501 line too long (89 > 79 characters)
.\app\main.py:397:80: E501 line too long (81 > 79 characters)
.\app\main.py:399:80: E501 line too long (81 > 79 characters)
.\app\main.py:456:80: E501 line too long (98 > 79 characters)
.\app\main.py:461:80: E501 line too long (88 > 79 characters)
.\app\main.py:468:80: E501 line too long (88 > 79 characters)
.\app\main.py:471:80: E501 line too long (88 > 79 characters)
.\app\main.py:478:80: E501 line too long (88 > 79 characters)
.\app\models.py:53:80: E501 line too long (83 > 79 characters)
.\app\models.py:102:80: E501 line too long (83 > 79 characters)
.\app\tabs\auto_farm.py:3:1: F401 'time' imported but unused
.\app\tabs\auto_farm.py:5:1: F401 'tkinter.messagebox' imported but unused
.\app\tabs\auto_farm.py:22:80: E501 line too long (83 > 79 characters)
.\app\tabs\auto_farm.py:23:80: E501 line too long (92 > 79 characters)
.\app\tabs\auto_farm.py:45:80: E501 line too long (97 > 79 characters)
.\app\tabs\auto_farm.py:48:80: E501 line too long (81 > 79 characters)
.\app\tabs\auto_farm.py:51:80: E501 line too long (99 > 79 characters)
.\app\tabs\auto_farm.py:79:80: E501 line too long (82 > 79 characters)
.\app\tabs\auto_farm.py:83:80: E501 line too long (100 > 79 characters)
.\app\tabs\auto_farm.py:146:80: E501 line too long (100 > 79 characters)
.\app\tabs\auto_farm.py:191:80: E501 line too long (89 > 79 characters)
.\app\tabs\auto_farm.py:198:80: E501 line too long (89 > 79 characters)
.\app\tabs\auto_farm.py:203:80: E501 line too long (100 > 79 characters)
.\app\tabs\auto_farm.py:206:80: E501 line too long (85 > 79 characters)
.\app\tabs\auto_farm.py:213:80: E501 line too long (100 > 79 characters)
.\app\tabs\auto_farm.py:237:80: E501 line too long (86 > 79 characters)
.\app\tabs\auto_farm.py:249:80: E501 line too long (91 > 79 characters)
.\app\tabs\auto_farm.py:257:80: E501 line too long (89 > 79 characters)
.\app\tabs\auto_farm.py:268:80: E501 line too long (96 > 79 characters)
.\app\tabs\auto_farm.py:277:80: E501 line too long (95 > 79 characters)
.\app\tabs\auto_farm.py:295:80: E501 line too long (83 > 79 characters)
.\app\tabs\auto_farm.py:296:80: E501 line too long (83 > 79 characters)
.\app\tabs\auto_farm.py:299:80: E501 line too long (80 > 79 characters)
.\app\tabs\auto_farm.py:313:80: E501 line too long (94 > 79 characters)
.\app\tabs\auto_farm.py:314:80: E501 line too long (96 > 79 characters)
.\app\tabs\auto_farm.py:315:80: E501 line too long (102 > 79 characters)
.\app\tabs\auto_farm.py:332:80: E501 line too long (81 > 79 characters)
.\app\tabs\auto_farm.py:355:80: E501 line too long (95 > 79 characters)
.\app\tabs\auto_farm.py:387:80: E501 line too long (87 > 79 characters)
.\app\tabs\auto_farm.py:388:80: E501 line too long (87 > 79 characters)
.\app\tabs\auto_farm.py:411:80: E501 line too long (91 > 79 characters)
.\app\tabs\auto_farm.py:414:80: E501 line too long (91 > 79 characters)
.\app\tabs\auto_farm.py:417:80: E501 line too long (91 > 79 characters)
.\app\tabs\auto_farm.py:436:80: E501 line too long (81 > 79 characters)
.\app\tabs\auto_farm.py:458:80: E501 line too long (93 > 79 characters)
.\app\tabs\auto_farm.py:463:80: E501 line too long (93 > 79 characters)
.\app\tabs\auto_farm.py:470:80: E501 line too long (94 > 79 characters)
.\app\tabs\auto_farm.py:473:80: E501 line too long (80 > 79 characters)
.\app\tabs\auto_farm.py:489:80: E501 line too long (94 > 79 characters)
.\app\tabs\auto_farm.py:495:80: E501 line too long (81 > 79 characters)
.\app\tabs\auto_farm.py:498:80: E501 line too long (81 > 79 characters)
.\app\tabs\auto_farm.py:500:80: E501 line too long (84 > 79 characters)
.\app\tabs\auto_farm.py:507:80: E501 line too long (81 > 79 characters)
.\app\tabs\auto_farm.py:513:80: E501 line too long (90 > 79 characters)
.\app\tabs\auto_farm.py:517:80: E501 line too long (85 > 79 characters)
.\app\tabs\auto_farm.py:534:80: E501 line too long (86 > 79 characters)
.\app\tabs\auto_farm.py:538:80: E501 line too long (100 > 79 characters)
.\app\tabs\auto_farm.py:541:80: E501 line too long (90 > 79 characters)
.\app\tabs\auto_farm.py:554:80: E501 line too long (96 > 79 characters)
.\app\tabs\auto_farm.py:561:80: E501 line too long (91 > 79 characters)
.\app\tabs\auto_farm.py:563:9: F841 local variable 'e' is assigned to but never used
.\app\tabs\auto_farm.py:591:80: E501 line too long (91 > 79 characters)
.\app\tabs\auto_farm.py:595:80: E501 line too long (94 > 79 characters)
.\app\tabs\auto_farm.py:599:80: E501 line too long (89 > 79 characters)
.\app\tabs\auto_farm_firmware.py:24:80: E501 line too long (91 > 79 characters)
.\app\tabs\auto_farm_firmware.py:30:80: E501 line too long (89 > 79 characters)
.\app\tabs\auto_farm_firmware.py:33:80: E501 line too long (87 > 79 characters)
.\app\tabs\auto_farm_firmware.py:45:80: E501 line too long (91 > 79 characters)
.\app\tabs\auto_farm_firmware.py:48:80: E501 line too long (96 > 79 characters)
.\app\tabs\auto_farm_firmware.py:53:80: E501 line too long (81 > 79 characters)
.\app\tabs\auto_farm_firmware.py:57:80: E501 line too long (99 > 79 characters)
.\app\tabs\auto_farm_firmware.py:103:80: E501 line too long (80 > 79 characters)
.\app\tabs\auto_farm_firmware.py:108:80: E501 line too long (94 > 79 characters)
.\app\tabs\auto_farm_firmware.py:112:80: E501 line too long (84 > 79 characters)
.\app\tabs\auto_farm_firmware.py:135:80: E501 line too long (98 > 79 characters)
.\app\tabs\auto_farm_firmware.py:138:80: E501 line too long (98 > 79 characters)
.\app\tabs\auto_farm_firmware.py:141:80: E501 line too long (98 > 79 characters)
.\app\tabs\auto_farm_firmware.py:203:80: E501 line too long (95 > 79 characters)
.\app\tabs\auto_farm_firmware.py:220:80: E501 line too long (95 > 79 characters)
.\app\tabs\auto_farm_firmware.py:228:80: E501 line too long (85 > 79 characters)
.\app\tabs\auto_farm_firmware.py:233:80: E501 line too long (86 > 79 characters)
.\app\tabs\auto_farm_firmware.py:258:80: E501 line too long (87 > 79 characters)
.\app\tabs\auto_farm_firmware.py:259:80: E501 line too long (85 > 79 characters)
.\app\tabs\auto_farm_firmware.py:263:80: E501 line too long (84 > 79 characters)
.\app\tabs\auto_farm_firmware.py:267:80: E501 line too long (100 > 79 characters)
.\app\tabs\auto_farm_firmware.py:272:9: F841 local variable 'is_simulation' is assigned to but never used
.\app\tabs\auto_farm_firmware.py:285:80: E501 line too long (80 > 79 characters)
.\app\tabs\auto_farm_firmware.py:288:80: E501 line too long (95 > 79 characters)
.\app\tabs\auto_farm_firmware.py:300:80: E501 line too long (84 > 79 characters)
.\app\tabs\auto_farm_firmware.py:336:80: E501 line too long (83 > 79 characters)
.\app\tabs\auto_farm_firmware.py:338:80: E501 line too long (91 > 79 characters)
.\app\tabs\auto_farm_firmware.py:357:80: E501 line too long (94 > 79 characters)
.\app\tabs\calibration.py:21:80: E501 line too long (88 > 79 characters)
.\app\tabs\calibration.py:22:80: E501 line too long (85 > 79 characters)
.\app\tabs\calibration.py:27:80: E501 line too long (96 > 79 characters)
.\app\tabs\calibration.py:30:80: E501 line too long (95 > 79 characters)
.\app\tabs\calibration.py:33:80: E501 line too long (81 > 79 characters)
.\app\tabs\calibration.py:75:80: E501 line too long (99 > 79 characters)
.\app\tabs\calibration.py:76:80: E501 line too long (99 > 79 characters)
.\app\tabs\calibration.py:127:80: E501 line too long (94 > 79 characters)
.\app\tabs\calibration.py:129:80: E501 line too long (81 > 79 characters)
.\app\tabs\calibration.py:135:80: E501 line too long (100 > 79 characters)
.\app\tabs\calibration.py:138:80: E501 line too long (93 > 79 characters)
.\app\tabs\calibration.py:157:80: E501 line too long (87 > 79 characters)
.\app\tabs\calibration.py:160:80: E501 line too long (89 > 79 characters)
.\app\tabs\calibration.py:191:80: E501 line too long (100 > 79 characters)
.\app\tabs\calibration.py:193:80: E501 line too long (88 > 79 characters)
.\app\tabs\calibration.py:211:80: E501 line too long (88 > 79 characters)
.\app\tabs\calibration.py:212:80: E501 line too long (88 > 79 characters)
.\app\tabs\calibration.py:233:80: E501 line too long (99 > 79 characters)
.\app\tabs\calibration.py:252:80: E501 line too long (90 > 79 characters)
.\app\tabs\calibration.py:255:80: E501 line too long (92 > 79 characters)
.\app\tabs\calibration.py:287:80: E501 line too long (89 > 79 characters)
.\app\tabs\calibration.py:290:80: E501 line too long (91 > 79 characters)
.\app\tabs\calibration.py:304:80: E501 line too long (81 > 79 characters)
.\app\tabs\calibration.py:308:80: E501 line too long (94 > 79 characters)
.\app\tabs\calibration.py:309:80: E501 line too long (94 > 79 characters)
.\app\tabs\calibration.py:318:80: E501 line too long (86 > 79 characters)
.\app\tabs\calibration.py:332:80: E501 line too long (84 > 79 characters)
.\app\tabs\calibration.py:337:80: E501 line too long (87 > 79 characters)
.\app\tabs\calibration.py:338:80: E501 line too long (82 > 79 characters)
.\app\tabs\calibration.py:339:80: E501 line too long (82 > 79 characters)
.\app\tabs\calibration.py:358:80: E501 line too long (100 > 79 characters)
.\app\tabs\calibration.py:369:80: E501 line too long (94 > 79 characters)
.\app\tabs\calibration.py:370:80: E501 line too long (97 > 79 characters)
.\app\tabs\calibration.py:373:80: E501 line too long (93 > 79 characters)
.\app\tabs\calibration.py:378:80: E501 line too long (95 > 79 characters)
.\app\tabs\calibration.py:399:9: F841 local variable 'e' is assigned to but never used
.\app\tabs\calibration.py:410:13: F841 local variable 'e' is assigned to but never used
.\app\tabs\calibration.py:429:80: E501 line too long (100 > 79 characters)
.\app\tabs\calibration.py:439:80: E501 line too long (87 > 79 characters)
.\app\tabs\calibration.py:444:80: E501 line too long (92 > 79 characters)
.\app\tabs\calibration.py:447:80: E501 line too long (99 > 79 characters)
.\app\tabs\calibration.py:450:80: E501 line too long (88 > 79 characters)
.\app\tabs\calibration.py:456:80: E501 line too long (101 > 79 characters)
.\app\tabs\calibration.py:464:80: E501 line too long (94 > 79 characters)
.\app\tabs\calibration.py:465:80: E501 line too long (97 > 79 characters)
.\app\tabs\calibration.py:468:80: E501 line too long (93 > 79 characters)
.\app\tabs\calibration.py:473:80: E501 line too long (95 > 79 characters)
.\app\tabs\calibration.py:500:9: F841 local variable 'e' is assigned to but never used
.\app\tabs\calibration.py:511:17: F841 local variable 'e' is assigned to but never used
.\app\tabs\calibration.py:526:80: E501 line too long (100 > 79 characters)
.\app\tabs\calibration.py:535:80: E501 line too long (80 > 79 characters)
.\app\tabs\calibration.py:544:80: E501 line too long (85 > 79 characters)
.\app\tabs\dashboard.py:46:80: E501 line too long (91 > 79 characters)
.\app\tabs\dashboard.py:53:80: E501 line too long (83 > 79 characters)
.\app\tabs\dashboard.py:58:80: E501 line too long (98 > 79 characters)
.\app\tabs\dashboard.py:59:80: E501 line too long (95 > 79 characters)
.\app\tabs\dashboard.py:63:80: E501 line too long (96 > 79 characters)
.\app\tabs\dashboard.py:65:80: E501 line too long (99 > 79 characters)
.\app\tabs\dashboard.py:97:80: E501 line too long (86 > 79 characters)
.\app\tabs\dashboard.py:112:13: F841 local variable 'e' is assigned to but never used
.\app\tabs\dashboard.py:123:80: E501 line too long (122 > 79 characters)
.\app\tabs\dashboard.py:153:80: E501 line too long (88 > 79 characters)
.\app\tabs\dashboard.py:162:80: E501 line too long (100 > 79 characters)
.\app\tabs\dashboard.py:163:80: E501 line too long (97 > 79 characters)
.\app\tabs\dashboard.py:194:80: E501 line too long (88 > 79 characters)
.\app\tabs\dashboard.py:210:80: E501 line too long (82 > 79 characters)
.\app\tabs\dashboard.py:214:80: E501 line too long (89 > 79 characters)
.\app\tabs\dashboard.py:240:80: E501 line too long (88 > 79 characters)
.\app\tabs\dashboard.py:246:80: E501 line too long (83 > 79 characters)
.\app\tabs\dashboard.py:248:80: E501 line too long (91 > 79 characters)
.\app\tabs\dashboard.py:252:80: E501 line too long (87 > 79 characters)
.\app\tabs\dashboard.py:262:80: E501 line too long (91 > 79 characters)
.\app\tabs\dashboard.py:264:80: E501 line too long (89 > 79 characters)
.\app\tabs\dashboard.py:316:80: E501 line too long (82 > 79 characters)
.\app\tabs\dashboard.py:321:80: E501 line too long (83 > 79 characters)
.\app\tabs\dashboard.py:327:80: E501 line too long (99 > 79 characters)
.\app\tabs\dashboard.py:329:80: E501 line too long (99 > 79 characters)
.\app\tabs\dashboard.py:411:80: E501 line too long (100 > 79 characters)
.\app\tabs\dashboard.py:425:80: E501 line too long (86 > 79 characters)
.\app\tabs\dashboard.py:437:80: E501 line too long (87 > 79 characters)
.\app\tabs\dashboard.py:465:80: E501 line too long (86 > 79 characters)
.\app\tabs\dashboard.py:491:80: E501 line too long (92 > 79 characters)
.\app\tabs\dashboard.py:494:80: E501 line too long (92 > 79 characters)
.\app\tabs\dashboard.py:497:80: E501 line too long (92 > 79 characters)
.\app\tabs\dashboard.py:564:80: E501 line too long (93 > 79 characters)
.\app\tabs\dashboard.py:598:80: E501 line too long (81 > 79 characters)
.\app\tabs\dashboard.py:605:80: E501 line too long (81 > 79 characters)
.\app\tabs\dashboard.py:644:80: E501 line too long (80 > 79 characters)
.\app\tabs\dashboard.py:693:80: E501 line too long (89 > 79 characters)
.\app\tabs\dashboard.py:702:80: E501 line too long (98 > 79 characters)
.\app\tabs\dashboard.py:712:9: F841 local variable 'e' is assigned to but never used
.\app\tabs\dashboard.py:722:13: F841 local variable 'e' is assigned to but never used
.\app\tabs\dashboard.py:734:80: E501 line too long (99 > 79 characters)
.\app\tabs\dashboard.py:737:80: E501 line too long (83 > 79 characters)
.\app\tabs\dashboard.py:742:80: E501 line too long (84 > 79 characters)
.\app\tabs\dashboard.py:751:80: E501 line too long (92 > 79 characters)
.\app\tabs\dashboard.py:763:80: E501 line too long (86 > 79 characters)
.\app\tabs\dashboard.py:771:80: E501 line too long (82 > 79 characters)
.\app\tabs\dashboard.py:773:80: E501 line too long (98 > 79 characters)
.\app\tabs\dashboard.py:788:80: E501 line too long (82 > 79 characters)
.\app\tabs\dashboard.py:812:80: E501 line too long (89 > 79 characters)
.\app\tabs\dashboard.py:820:80: E501 line too long (86 > 79 characters)
.\app\tabs\dashboard.py:841:80: E501 line too long (83 > 79 characters)
.\app\tabs\dashboard.py:872:80: E501 line too long (88 > 79 characters)
.\app\tabs\dashboard.py:877:80: E501 line too long (86 > 79 characters)
.\app\tabs\dashboard.py:885:80: E501 line too long (94 > 79 characters)
.\app\tabs\dashboard.py:892:80: E501 line too long (81 > 79 characters)
.\app\tabs\dashboard.py:901:80: E501 line too long (85 > 79 characters)
.\app\tabs\dashboard.py:907:80: E501 line too long (94 > 79 characters)
.\app\tabs\dashboard.py:924:80: E501 line too long (82 > 79 characters)
.\app\tabs\dashboard.py:928:80: E501 line too long (88 > 79 characters)
.\app\tabs\dashboard.py:934:80: E501 line too long (80 > 79 characters)
.\app\tabs\pattern.py:25:80: E501 line too long (86 > 79 characters)
.\app\tabs\pattern.py:56:80: E501 line too long (83 > 79 characters)
.\app\tabs\pattern.py:71:80: E501 line too long (88 > 79 characters)
.\app\tabs\pattern.py:76:80: E501 line too long (89 > 79 characters)
.\app\tabs\pattern.py:107:80: E501 line too long (95 > 79 characters)
.\app\tabs\pattern.py:122:80: E501 line too long (95 > 79 characters)
.\app\tabs\pattern.py:165:80: E501 line too long (82 > 79 characters)
.\app\tabs\pattern.py:166:80: E501 line too long (82 > 79 characters)
.\app\tabs\pattern.py:181:80: E501 line too long (80 > 79 characters)
.\app\tabs\pattern.py:182:80: E501 line too long (88 > 79 characters)
.\app\tabs\pattern.py:183:80: E501 line too long (90 > 79 characters)
.\app\tabs\pattern.py:205:80: E501 line too long (86 > 79 characters)
.\app\tabs\pattern.py:206:80: E501 line too long (88 > 79 characters)
.\app\tabs\pattern.py:222:80: E501 line too long (90 > 79 characters)
.\app\tabs\pattern.py:223:80: E501 line too long (92 > 79 characters)
.\app\tabs\pattern.py:249:80: E501 line too long (92 > 79 characters)
.\app\tabs\pattern.py:257:80: E501 line too long (89 > 79 characters)
.\app\tabs\pattern.py:261:80: E501 line too long (98 > 79 characters)
.\app\tabs\pattern.py:276:80: E501 line too long (97 > 79 characters)
.\app\tabs\pattern.py:306:80: E501 line too long (99 > 79 characters)
.\app\tabs\pattern.py:328:80: E501 line too long (82 > 79 characters)
.\app\tabs\pattern.py:344:80: E501 line too long (97 > 79 characters)
.\app\tabs\pattern.py:385:80: E501 line too long (102 > 79 characters)
.\app\tabs\pattern.py:388:80: E501 line too long (96 > 79 characters)
.\app\tabs\pattern.py:391:80: E501 line too long (105 > 79 characters)
.\app\tabs\pattern.py:394:80: E501 line too long (83 > 79 characters)
.\app\tabs\pattern.py:398:80: E501 line too long (152 > 79 characters)
.\app\tabs\pattern.py:401:80: E501 line too long (85 > 79 characters)
.\app\tabs\pattern.py:403:80: E501 line too long (92 > 79 characters)
.\app\tabs\pattern.py:414:80: E501 line too long (91 > 79 characters)
.\app\tabs\pattern.py:423:9: F841 local variable 'e' is assigned to but never used
.\app\tabs\pattern.py:431:13: F841 local variable 'e' is assigned to but never used
.\app\tabs\pattern.py:438:80: E501 line too long (89 > 79 characters)
.\app\tabs\pattern.py:440:80: E501 line too long (80 > 79 characters)
.\app\tabs\pattern.py:448:80: E501 line too long (95 > 79 characters)
.\app\tabs\pattern.py:456:80: E501 line too long (99 > 79 characters)
.\app\tabs\pattern.py:459:80: E501 line too long (92 > 79 characters)
.\app\tabs\pattern.py:462:80: E501 line too long (92 > 79 characters)
.\app\tabs\pattern.py:464:80: E501 line too long (82 > 79 characters)
.\app\tabs\pattern.py:470:80: E501 line too long (101 > 79 characters)
.\app\tabs\profiles.py:13:80: E501 line too long (80 > 79 characters)
.\app\tabs\profiles.py:27:80: E501 line too long (85 > 79 characters)
.\app\tabs\profiles.py:53:80: E501 line too long (100 > 79 characters)
.\app\tabs\profiles.py:56:80: E501 line too long (100 > 79 characters)
.\app\tabs\profiles.py:59:80: E501 line too long (100 > 79 characters)
.\app\tabs\profiles.py:91:80: E501 line too long (82 > 79 characters)
.\app\tabs\profiles.py:94:80: E501 line too long (84 > 79 characters)
.\app\tabs\profiles.py:112:80: E501 line too long (95 > 79 characters)
.\app\tabs\profiles.py:113:80: E501 line too long (97 > 79 characters)
.\app\tabs\profiles.py:139:80: E501 line too long (93 > 79 characters)
.\app\tabs\profiles.py:141:80: E501 line too long (95 > 79 characters)
.\app\tabs\profiles.py:143:80: E501 line too long (82 > 79 characters)
.\app\tabs\profiles.py:148:80: E501 line too long (87 > 79 characters)
.\app\tabs\profiles.py:156:80: E501 line too long (105 > 79 characters)
.\app\tabs\profiles.py:194:80: E501 line too long (87 > 79 characters)
.\app\tabs\profiles.py:195:80: E501 line too long (87 > 79 characters)
.\app\tabs\profiles.py:211:80: E501 line too long (87 > 79 characters)
.\app\tabs\profiles.py:212:80: E501 line too long (87 > 79 characters)
.\app\tabs\profiles.py:243:80: E501 line too long (99 > 79 characters)
.\app\tabs\profiles.py:244:80: E501 line too long (99 > 79 characters)
.\app\tabs\profiles.py:282:80: E501 line too long (83 > 79 characters)
.\app\tabs\profiles.py:283:80: E501 line too long (83 > 79 characters)
.\app\tabs\profiles.py:316:80: E501 line too long (99 > 79 characters)
.\app\tabs\profiles.py:319:80: E501 line too long (99 > 79 characters)
.\app\tabs\profiles.py:322:80: E501 line too long (99 > 79 characters)
.\app\tabs\profiles.py:353:80: E501 line too long (95 > 79 characters)
.\app\tabs\profiles.py:354:80: E501 line too long (97 > 79 characters)
.\app\tabs\profiles.py:381:80: E501 line too long (97 > 79 characters)
.\app\tabs\profiles.py:394:80: E501 line too long (83 > 79 characters)
.\app\tabs\profiles.py:396:80: E501 line too long (80 > 79 characters)
.\app\tabs\profiles.py:420:80: E501 line too long (87 > 79 characters)
.\app\tabs\profiles.py:427:80: E501 line too long (81 > 79 characters)
.\app\tabs\profiles.py:435:80: E501 line too long (87 > 79 characters)
.\app\tabs\profiles.py:460:80: E501 line too long (80 > 79 characters)
.\app\tabs\profiles.py:465:80: E501 line too long (98 > 79 characters)
.\app\tabs\profiles.py:480:80: E501 line too long (89 > 79 characters)
.\app\tabs\profiles.py:493:80: E501 line too long (92 > 79 characters)
.\app\tabs\profiles.py:498:80: E501 line too long (90 > 79 characters)
.\app\tabs\profiles.py:506:80: E501 line too long (90 > 79 characters)
.\app\tabs\profiles.py:508:80: E501 line too long (87 > 79 characters)
.\app\tabs\profiles.py:515:80: E501 line too long (92 > 79 characters)
.\app\tabs\profiles.py:518:80: E501 line too long (88 > 79 characters)
.\app\tabs\profiles.py:519:80: E501 line too long (93 > 79 characters)
.\app\tabs\profiles.py:528:80: E501 line too long (88 > 79 characters)
.\app\tabs\profiles.py:529:80: E501 line too long (80 > 79 characters)
.\app\tabs\profiles.py:539:80: E501 line too long (85 > 79 characters)
.\app\tabs\profiles.py:545:80: E501 line too long (86 > 79 characters)
.\app\tabs\profiles.py:547:80: E501 line too long (81 > 79 characters)
.\app\tabs\profiles.py:549:80: E501 line too long (86 > 79 characters)
.\app\tabs\profiles.py:555:80: E501 line too long (85 > 79 characters)
.\app\tabs\profiles.py:560:80: E501 line too long (91 > 79 characters)
.\app\tabs\profiles.py:562:80: E501 line too long (89 > 79 characters)
.\app\tabs\profiles.py:581:80: E501 line too long (80 > 79 characters)
.\app\tabs\profiles.py:603:80: E501 line too long (80 > 79 characters)
.\app\tabs\profiles.py:605:80: E501 line too long (80 > 79 characters)
.\app\tabs\profiles.py:610:80: E501 line too long (87 > 79 characters)
.\app\tabs\profiles.py:616:80: E501 line too long (97 > 79 characters)
.\app\tabs\profiles.py:623:80: E501 line too long (90 > 79 characters)
.\app\tabs\profiles.py:629:80: E501 line too long (89 > 79 characters)
.\app\tabs\profiles.py:632:80: E501 line too long (80 > 79 characters)
.\app\tabs\recorder.py:35:80: E501 line too long (82 > 79 characters)
.\app\tabs\recorder.py:51:80: E501 line too long (84 > 79 characters)
.\app\tabs\recorder.py:106:80: E501 line too long (81 > 79 characters)
.\app\tabs\recorder.py:120:80: E501 line too long (90 > 79 characters)
.\app\tabs\recorder.py:121:80: E501 line too long (80 > 79 characters)
.\app\tabs\recorder.py:145:80: E501 line too long (87 > 79 characters)
.\app\tabs\recorder.py:164:80: E501 line too long (97 > 79 characters)
.\app\tabs\recorder.py:165:80: E501 line too long (99 > 79 characters)
.\app\tabs\recorder.py:184:80: E501 line too long (89 > 79 characters)
.\app\tabs\recorder.py:189:80: E501 line too long (81 > 79 characters)
.\app\tabs\recorder.py:214:80: E501 line too long (82 > 79 characters)
.\app\tabs\recorder.py:228:80: E501 line too long (87 > 79 characters)
.\app\tabs\recorder.py:233:80: E501 line too long (93 > 79 characters)
.\app\tabs\recorder.py:240:80: E501 line too long (98 > 79 characters)
.\app\tabs\recorder.py:257:80: E501 line too long (99 > 79 characters)
.\app\tabs\recorder.py:268:80: E501 line too long (99 > 79 characters)
.\app\tabs\recorder.py:276:80: E501 line too long (89 > 79 characters)
.\app\tabs\recorder.py:310:80: E501 line too long (84 > 79 characters)
.\app\tabs\recorder.py:313:80: E501 line too long (86 > 79 characters)
.\app\tabs\recorder.py:329:80: E501 line too long (96 > 79 characters)
.\app\tabs\recorder.py:331:80: E501 line too long (91 > 79 characters)
.\app\tabs\recorder.py:334:80: E501 line too long (92 > 79 characters)
.\app\tabs\recorder.py:336:80: E501 line too long (98 > 79 characters)
.\app\tabs\recorder.py:341:80: E501 line too long (89 > 79 characters)
.\app\tabs\recorder.py:344:80: E501 line too long (81 > 79 characters)
.\app\tabs\recorder.py:345:80: E501 line too long (94 > 79 characters)
.\app\tabs\recorder.py:356:80: E501 line too long (88 > 79 characters)
.\app\tabs\recorder.py:359:80: E501 line too long (142 > 79 characters)
.\app\tabs\recorder.py:362:80: E501 line too long (86 > 79 characters)
.\app\tabs\recorder.py:370:80: E501 line too long (87 > 79 characters)
.\app\tabs\recorder.py:375:9: F841 local variable 'e' is assigned to but never used
.\app\tabs\recorder.py:395:80: E501 line too long (166 > 79 characters)
.\app\tabs\recorder.py:400:80: E501 line too long (159 > 79 characters)
.\app\tabs\recorder.py:416:80: E501 line too long (87 > 79 characters)
.\app\tabs\recorder.py:425:80: E501 line too long (98 > 79 characters)
.\app\tabs\recorder.py:429:80: E501 line too long (96 > 79 characters)
.\app\tabs\recorder.py:441:17: F841 local variable 'e' is assigned to but never used
.\app\tabs\recorder.py:456:80: E501 line too long (85 > 79 characters)
.\app\tabs\recorder.py:460:80: E501 line too long (82 > 79 characters)
.\app\tabs\recorder.py:469:80: E501 line too long (92 > 79 characters)
.\app\tabs\recorder.py:472:80: E501 line too long (93 > 79 characters)
.\app\tabs\recorder.py:480:80: E501 line too long (82 > 79 characters)
.\app\tabs\recorder.py:497:80: E501 line too long (113 > 79 characters)
.\app\tabs\recorder.py:525:13: F841 local variable 'e' is assigned to but never used
.\app\tabs\recorder.py:536:80: E501 line too long (81 > 79 characters)
.\app\tabs\recorder.py:604:80: E501 line too long (117 > 79 characters)
.\app\tabs\recorder.py:614:80: E501 line too long (98 > 79 characters)
.\app\tabs\recorder.py:636:13: F841 local variable 'e' is assigned to but never used
.\app\tabs\recorder.py:648:80: E501 line too long (85 > 79 characters)
.\app\tabs\recorder.py:703:13: F841 local variable 'e' is assigned to but never used
.\app\tabs\recorder.py:719:80: E501 line too long (97 > 79 characters)
.\app\tabs\recorder.py:750:80: E501 line too long (99 > 79 characters)
.\app\tabs\recorder.py:774:80: E501 line too long (95 > 79 characters)
.\app\tabs\recorder.py:785:80: E501 line too long (97 > 79 characters)
.\app\tabs\recorder.py:791:80: E501 line too long (110 > 79 characters)
.\app\tabs\recorder.py:797:80: E501 line too long (96 > 79 characters)
.\app\tabs\recorder.py:800:80: E501 line too long (105 > 79 characters)
.\app\tabs\recorder.py:803:80: E501 line too long (83 > 79 characters)
.\app\tabs\recorder.py:807:80: E501 line too long (152 > 79 characters)
.\app\tabs\recorder.py:810:80: E501 line too long (85 > 79 characters)
.\app\tabs\recorder.py:812:80: E501 line too long (96 > 79 characters)
.\app\tabs\recorder.py:823:80: E501 line too long (95 > 79 characters)
.\app\tabs\recorder.py:832:13: F841 local variable 'e' is assigned to but never used
.\app\tabs\recorder.py:840:17: F841 local variable 'e' is assigned to but never used
.\app\tabs\recorder.py:847:80: E501 line too long (93 > 79 characters)
.\app\tabs\recorder.py:849:80: E501 line too long (84 > 79 characters)
.\app\tabs\recorder.py:857:80: E501 line too long (99 > 79 characters)
.\app\tabs\recorder.py:865:80: E501 line too long (97 > 79 characters)
.\app\tabs\recorder.py:868:80: E501 line too long (96 > 79 characters)
.\app\tabs\recorder.py:871:80: E501 line too long (90 > 79 characters)
.\app\tabs\recorder.py:878:80: E501 line too long (105 > 79 characters)
.\app\tabs\recorder.py:909:80: E501 line too long (92 > 79 characters)
.\app\tabs\recorder.py:914:80: E501 line too long (84 > 79 characters)
.\app\tabs\recorder.py:916:80: E501 line too long (86 > 79 characters)
.\app\tabs\recorder.py:938:80: E501 line too long (80 > 79 characters)
.\app\tabs\recorder.py:944:80: E501 line too long (90 > 79 characters)
.\app\tabs\recorder.py:949:80: E501 line too long (126 > 79 characters)
.\app\tabs\recorder.py:961:80: E501 line too long (97 > 79 characters)
.\app\tabs\recorder.py:966:80: E501 line too long (86 > 79 characters)
.\app\tabs\recorder.py:1024:80: E501 line too long (100 > 79 characters)
.\app\tabs\recorder.py:1027:80: E501 line too long (98 > 79 characters)
.\app\tabs\recorder.py:1033:80: E501 line too long (100 > 79 characters)
.\app\tabs\recorder.py:1036:80: E501 line too long (98 > 79 characters)
.\app\tabs\recorder.py:1042:80: E501 line too long (94 > 79 characters)
.\app\tabs\recorder.py:1058:80: E501 line too long (92 > 79 characters)
.\app\tabs\recorder.py:1060:80: E501 line too long (99 > 79 characters)
.\app\tabs\recorder.py:1062:80: E501 line too long (99 > 79 characters)
.\app\tabs\robot_settings.py:25:80: E501 line too long (88 > 79 characters)
.\app\tabs\robot_settings.py:28:80: E501 line too long (84 > 79 characters)
.\app\tabs\robot_settings.py:31:80: E501 line too long (82 > 79 characters)
.\app\tabs\robot_settings.py:41:80: E501 line too long (86 > 79 characters)
.\app\tabs\robot_settings.py:48:80: E501 line too long (83 > 79 characters)
.\app\tabs\robot_settings.py:52:80: E501 line too long (98 > 79 characters)
.\app\tabs\robot_settings.py:53:80: E501 line too long (95 > 79 characters)
.\app\tabs\robot_settings.py:57:80: E501 line too long (96 > 79 characters)
.\app\tabs\robot_settings.py:59:80: E501 line too long (99 > 79 characters)
.\app\tabs\robot_settings.py:87:80: E501 line too long (95 > 79 characters)
.\app\tabs\robot_settings.py:95:9: F841 local variable 'e' is assigned to but never used
.\app\tabs\robot_settings.py:125:80: E501 line too long (96 > 79 characters)
.\app\tabs\robot_settings.py:244:80: E501 line too long (91 > 79 characters)
.\app\tabs\robot_settings.py:248:80: E501 line too long (85 > 79 characters)
.\app\tabs\robot_settings.py:283:80: E501 line too long (81 > 79 characters)
.\app\tabs\robot_settings.py:308:80: E501 line too long (98 > 79 characters)
.\app\tabs\robot_settings.py:334:80: E501 line too long (90 > 79 characters)
.\app\tabs\robot_settings.py:340:80: E501 line too long (92 > 79 characters)
.\app\tabs\robot_settings.py:350:80: E501 line too long (93 > 79 characters)
.\app\tabs\robot_settings.py:370:80: E501 line too long (81 > 79 characters)
.\app\tabs\robot_settings.py:409:80: E501 line too long (98 > 79 characters)
.\app\tabs\robot_settings.py:440:80: E501 line too long (98 > 79 characters)
.\app\tabs\robot_settings.py:456:80: E501 line too long (92 > 79 characters)
.\app\tabs\robot_settings.py:458:80: E501 line too long (96 > 79 characters)
.\app\tabs\robot_settings.py:467:80: E501 line too long (92 > 79 characters)
.\app\tabs\robot_settings.py:472:80: E501 line too long (93 > 79 characters)
.\app\tabs\robot_settings.py:496:80: E501 line too long (97 > 79 characters)
.\app\tabs\robot_settings.py:501:80: E501 line too long (93 > 79 characters)
.\app\tabs\robot_settings.py:525:80: E501 line too long (97 > 79 characters)
.\app\tabs\robot_settings.py:530:80: E501 line too long (99 > 79 characters)
.\app\tabs\robot_settings.py:549:80: E501 line too long (82 > 79 characters)
.\app\tabs\robot_settings.py:551:80: E501 line too long (81 > 79 characters)
.\app\tabs\robot_settings.py:608:80: E501 line too long (107 > 79 characters)
.\app\tabs\robot_settings.py:612:80: E501 line too long (85 > 79 characters)
.\app\tabs\robot_settings.py:614:80: E501 line too long (100 > 79 characters)
.\app\tabs\robot_settings.py:634:9: F841 local variable 'e' is assigned to but never used
.\app\tabs\robot_settings.py:642:13: F841 local variable 'e' is assigned to but never used
.\app\tabs\robot_settings.py:649:80: E501 line too long (104 > 79 characters)
.\app\tabs\robot_settings.py:651:80: E501 line too long (80 > 79 characters)
.\app\tabs\robot_settings.py:652:80: E501 line too long (83 > 79 characters)
.\app\tabs\robot_settings.py:660:80: E501 line too long (97 > 79 characters)
.\app\tabs\robot_settings.py:668:80: E501 line too long (92 > 79 characters)
.\app\tabs\robot_settings.py:671:80: E501 line too long (92 > 79 characters)
.\app\tabs\robot_settings.py:674:80: E501 line too long (87 > 79 characters)
.\app\tabs\robot_settings.py:681:80: E501 line too long (121 > 79 characters)
.\app\tabs\robot_settings.py:687:80: E501 line too long (88 > 79 characters)
.\app\tabs\robot_settings.py:760:80: E501 line too long (80 > 79 characters)
.\app\tabs\robot_settings.py:841:80: E501 line too long (97 > 79 characters)
.\app\tabs\robot_settings.py:844:80: E501 line too long (97 > 79 characters)
.\app\tabs\robot_settings.py:847:80: E501 line too long (97 > 79 characters)
.\app\tabs\robot_settings.py:876:80: E501 line too long (93 > 79 characters)
.\app\tabs\robot_settings.py:902:80: E501 line too long (89 > 79 characters)
.\app\tabs\robot_settings.py:906:80: E501 line too long (90 > 79 characters)
.\app\tabs\robot_settings.py:911:80: E501 line too long (94 > 79 characters)
.\app\tabs\robot_settings.py:914:80: E501 line too long (85 > 79 characters)
.\app\tabs\robot_settings.py:919:80: E501 line too long (81 > 79 characters)
.\app\tabs\robot_settings.py:921:80: E501 line too long (94 > 79 characters)
.\app\tabs\robot_settings.py:928:80: E501 line too long (86 > 79 characters)
.\app\tabs\robot_settings.py:932:80: E501 line too long (98 > 79 characters)
.\app\tabs\robot_settings.py:937:80: E501 line too long (96 > 79 characters)
.\app\tabs\robot_settings.py:941:80: E501 line too long (97 > 79 characters)
.\app\tabs\robot_settings.py:955:80: E501 line too long (85 > 79 characters)
.\app\tabs\robot_settings.py:960:80: E501 line too long (80 > 79 characters)
.\app\tabs\robot_settings.py:962:80: E501 line too long (84 > 79 characters)
.\app\tabs\robot_settings.py:965:22: F541 f-string is missing placeholders
.\app\tabs\robot_settings.py:967:80: E501 line too long (93 > 79 characters)
.\app\tabs\simulation.py:21:80: E501 line too long (105 > 79 characters)
.\app\tabs\simulation.py:22:80: E501 line too long (93 > 79 characters)
.\app\tabs\simulation.py:189:80: E501 line too long (82 > 79 characters)
.\app\tabs\simulation.py:197:80: E501 line too long (84 > 79 characters)
.\app\tabs\simulation.py:203:80: E501 line too long (82 > 79 characters)
.\app\tabs\simulation.py:244:80: E501 line too long (95 > 79 characters)
.\app\tabs\simulation.py:304:80: E501 line too long (84 > 79 characters)
.\app\tabs\simulation.py:309:80: E501 line too long (96 > 79 characters)
.\app\tabs\simulation.py:341:80: E501 line too long (99 > 79 characters)
.\app\tabs\simulation.py:344:80: E501 line too long (99 > 79 characters)
.\app\tabs\simulation.py:347:80: E501 line too long (99 > 79 characters)
.\app\tabs\simulation.py:351:80: E501 line too long (99 > 79 characters)
.\app\tabs\simulation.py:374:80: E501 line too long (95 > 79 characters)
.\app\tabs\simulation.py:420:80: E501 line too long (82 > 79 characters)
.\app\tabs\simulation.py:425:80: E501 line too long (89 > 79 characters)
.\app\tabs\simulation.py:478:80: E501 line too long (83 > 79 characters)
.\app\tabs\simulation.py:502:80: E501 line too long (87 > 79 characters)
.\app\tabs\simulation.py:514:80: E501 line too long (81 > 79 characters)
.\app\tabs\simulation.py:518:80: E501 line too long (97 > 79 characters)
.\app\tabs\simulation.py:532:80: E501 line too long (94 > 79 characters)
.\app\tabs\simulation.py:575:80: E501 line too long (86 > 79 characters)
.\app\tabs\simulation.py:590:80: E501 line too long (80 > 79 characters)
.\app\tabs\simulation.py:608:80: E501 line too long (93 > 79 characters)
.\app\tabs\simulation.py:621:80: E501 line too long (95 > 79 characters)
.\app\tabs\simulation.py:624:80: E501 line too long (83 > 79 characters)
.\app\tabs\simulation.py:631:80: E501 line too long (80 > 79 characters)
.\app\tabs\simulation.py:636:80: E501 line too long (93 > 79 characters)
.\app\tabs\simulation.py:640:80: E501 line too long (110 > 79 characters)
.\app\tabs\tester.py:19:80: E501 line too long (99 > 79 characters)
.\app\tabs\tester.py:26:80: E501 line too long (174 > 79 characters)
.\app\tabs\tester.py:90:80: E501 line too long (100 > 79 characters)
.\app\tabs\tester.py:93:80: E501 line too long (100 > 79 characters)
.\app\tabs\tester.py:106:80: E501 line too long (88 > 79 characters)
.\app\tabs\tester.py:115:80: E501 line too long (89 > 79 characters)
.\app\tabs\tester.py:124:80: E501 line too long (105 > 79 characters)
.\app\tabs\tester.py:125:80: E501 line too long (93 > 79 characters)
.\app\tabs\tester.py:283:80: E501 line too long (82 > 79 characters)
.\app\tabs\tester.py:301:80: E501 line too long (82 > 79 characters)
.\app\tabs\tester.py:328:80: E501 line too long (82 > 79 characters)
.\app\tabs\tester.py:345:80: E501 line too long (84 > 79 characters)
.\app\tabs\tester.py:403:80: E501 line too long (87 > 79 characters)
.\app\tabs\tester.py:427:80: E501 line too long (81 > 79 characters)
.\app\tabs\tester.py:436:80: E501 line too long (87 > 79 characters)
.\app\tabs\tester.py:443:80: E501 line too long (93 > 79 characters)
.\app\tabs\tester.py:446:80: E501 line too long (90 > 79 characters)
.\app\tabs\tester.py:450:80: E501 line too long (97 > 79 characters)
.\app\tabs\tester.py:452:80: E501 line too long (98 > 79 characters)
.\app\tabs\tester.py:462:80: E501 line too long (91 > 79 characters)
.\app\tabs\validator.py:21:80: E501 line too long (90 > 79 characters)
.\app\tabs\validator.py:23:80: E501 line too long (104 > 79 characters)
.\app\tabs\validator.py:28:80: E501 line too long (137 > 79 characters)
.\app\tabs\validator.py:33:80: E501 line too long (182 > 79 characters)
.\app\tabs\validator.py:38:80: E501 line too long (119 > 79 characters)
.\app\tabs\validator.py:44:80: E501 line too long (98 > 79 characters)
.\app\tabs\validator.py:47:80: E501 line too long (97 > 79 characters)
.\app\tabs\validator.py:48:80: E501 line too long (87 > 79 characters)
.\app\tabs\validator.py:51:80: E501 line too long (210 > 79 characters)
.\app\tabs\validator.py:55:17: F541 f-string is missing placeholders
.\app\tabs\validator.py:55:80: E501 line too long (94 > 79 characters)
.\app\tabs\validator.py:61:80: E501 line too long (126 > 79 characters)
.\app\tabs\validator.py:65:80: E501 line too long (110 > 79 characters)
.\app\tabs\validator.py:73:80: E501 line too long (148 > 79 characters)
.\app\tabs\validator.py:77:80: E501 line too long (81 > 79 characters)
.\app\tabs\validator.py:81:80: E501 line too long (152 > 79 characters)
.\app\tabs\validator.py:85:80: E501 line too long (151 > 79 characters)
.\app\tabs\validator.py:95:80: E501 line too long (174 > 79 characters)
.\app\tabs\validator.py:100:80: E501 line too long (90 > 79 characters)
.\app\tabs\validator.py:106:80: E501 line too long (103 > 79 characters)
.\app\tabs\validator.py:109:80: E501 line too long (87 > 79 characters)
.\app\tabs\validator.py:114:80: E501 line too long (81 > 79 characters)
.\app\tabs\validator.py:117:80: E501 line too long (104 > 79 characters)
.\app\tabs\validator.py:121:80: E501 line too long (120 > 79 characters)
.\app\tabs\validator.py:139:80: E501 line too long (93 > 79 characters)
.\app\tabs\validator.py:142:80: E501 line too long (80 > 79 characters)
.\app\tabs\validator.py:157:80: E501 line too long (88 > 79 characters)
.\app\tabs\validator.py:158:80: E501 line too long (91 > 79 characters)
.\app\tabs\validator.py:159:80: E501 line too long (91 > 79 characters)
.\app\tabs\validator.py:163:80: E501 line too long (80 > 79 characters)
.\app\tabs\validator.py:190:80: E501 line too long (92 > 79 characters)
.\app\tabs\validator.py:193:80: E501 line too long (92 > 79 characters)
.\app\tabs\validator.py:196:80: E501 line too long (92 > 79 characters)
.\app\tabs\validator.py:227:80: E501 line too long (93 > 79 characters)
.\app\tabs\validator.py:228:80: E501 line too long (95 > 79 characters)
.\app\tabs\validator.py:245:80: E501 line too long (95 > 79 characters)
.\app\tabs\validator.py:246:80: E501 line too long (97 > 79 characters)
.\app\tabs\validator.py:272:80: E501 line too long (97 > 79 characters)
.\app\tabs\validator.py:282:80: E501 line too long (90 > 79 characters)
.\app\tabs\validator.py:292:80: E501 line too long (90 > 79 characters)
.\app\tabs\validator.py:302:80: E501 line too long (83 > 79 characters)
.\app\tabs\validator.py:320:80: E501 line too long (88 > 79 characters)
.\app\tabs\validator.py:324:80: E501 line too long (125 > 79 characters)
.\app\tabs\validator.py:330:80: E501 line too long (86 > 79 characters)
.\apply_fixes.py:3:1: F401 'os' imported but unused
.\apply_fixes.py:15:80: E501 line too long (82 > 79 characters)
.\apply_fixes.py:31:80: E501 line too long (87 > 79 characters)
.\apply_fixes.py:56:80: E501 line too long (90 > 79 characters)
.\apply_fixes.py:60:80: E501 line too long (80 > 79 characters)
.\apply_fixes.py:71:80: E501 line too long (84 > 79 characters)
.\apply_fixes.py:94:80: E501 line too long (90 > 79 characters)
.\apply_fixes.py:107:80: E501 line too long (80 > 79 characters)
.\apply_fixes.py:143:80: E501 line too long (155 > 79 characters)
.\apply_fixes.py:146:80: E501 line too long (88 > 79 characters)
.\apply_fixes.py:148:80: E501 line too long (80 > 79 characters)
.\apply_fixes.py:152:80: E501 line too long (95 > 79 characters)
.\audit_report.py:11:1: F401 'difflib' imported but unused
.\audit_report.py:12:1: F401 'os' imported but unused
.\audit_report.py:23:80: E501 line too long (82 > 79 characters)
.\audit_report.py:29:80: E501 line too long (82 > 79 characters)
.\audit_report.py:56:9: F841 local variable 'e' is assigned to but never used
.\audit_report.py:65:80: E501 line too long (80 > 79 characters)
.\audit_report.py:101:9: F841 local variable 'e' is assigned to but never used
.\audit_report.py:107:80: E501 line too long (80 > 79 characters)
.\check_image.py:4:1: F401 'PIL.Image' imported but unused
.\check_image.py:9:80: E501 line too long (143 > 79 characters)
.\convert_vit_to_onnx.py:6:1: F401 'numpy as np' imported but unused
.\convert_vit_to_onnx.py:16:5: F841 local variable 'e' is assigned to but never used
.\convert_vit_to_onnx.py:29:80: E501 line too long (84 > 79 characters)
.\convert_vit_to_onnx.py:36:80: E501 line too long (83 > 79 characters)
.\debug_minimap_capture.py:3:80: E501 line too long (85 > 79 characters)
.\debug_minimap_capture.py:11:1: E402 module level import not at top of file
.\debug_minimap_capture.py:15:1: F401 'time' imported but unused
.\debug_minimap_capture.py:15:1: E402 module level import not at top of file
.\debug_minimap_capture.py:16:1: E402 module level import not at top of file
.\debug_minimap_capture.py:18:1: E402 module level import not at top of file
.\debug_minimap_capture.py:19:1: E402 module level import not at top of file
.\debug_minimap_capture.py:20:1: E402 module level import not at top of file
.\debug_minimap_capture.py:21:1: E402 module level import not at top of file
.\debug_minimap_capture.py:32:5: E722 do not use bare 'except'
.\debug_minimap_capture.py:34:1: E722 do not use bare 'except'
.\debug_minimap_capture.py:44:80: E501 line too long (90 > 79 characters)
.\debug_minimap_capture.py:65:80: E501 line too long (89 > 79 characters)
.\debug_minimap_capture.py:77:80: E501 line too long (121 > 79 characters)
.\debug_minimap_capture.py:93:11: F541 f-string is missing placeholders
.\debug_minimap_capture.py:97:24: E203 whitespace before ':'
.\debug_minimap_capture.py:97:41: E203 whitespace before ':'
.\debug_minimap_capture.py:99:11: F541 f-string is missing placeholders
.\debug_minimap_capture.py:99:80: E501 line too long (84 > 79 characters)
.\debug_minimap_capture.py:102:5: F401 'app.auto_farm.utils.multi_match' imported but unused
.\debug_minimap_capture.py:104:80: E501 line too long (87 > 79 characters)
.\debug_minimap_capture.py:105:80: E501 line too long (87 > 79 characters)
.\debug_minimap_capture.py:106:80: E501 line too long (84 > 79 characters)
.\debug_minimap_capture.py:118:80: E501 line too long (87 > 79 characters)
.\debug_minimap_capture.py:129:80: E501 line too long (90 > 79 characters)
.\debug_minimap_capture.py:133:80: E501 line too long (85 > 79 characters)
.\debug_minimap_capture.py:139:80: E501 line too long (91 > 79 characters)
.\debug_minimap_capture.py:146:19: F541 f-string is missing placeholders
.\debug_minimap_capture.py:149:37: E203 whitespace before ':'
.\debug_minimap_capture.py:149:58: E203 whitespace before ':'
.\debug_minimap_capture.py:151:19: F541 f-string is missing placeholders
.\debug_minimap_capture.py:155:80: E501 line too long (97 > 79 characters)
.\debug_minimap_capture.py:157:80: E501 line too long (93 > 79 characters)
.\debug_minimap_capture.py:162:80: E501 line too long (80 > 79 characters)
.\debug_minimap_capture.py:163:80: E501 line too long (80 > 79 characters)
.\debug_minimap_capture.py:169:80: E501 line too long (87 > 79 characters)
.\debug_minimap_capture.py:172:19: F541 f-string is missing placeholders
.\debug_minimap_capture.py:174:80: E501 line too long (84 > 79 characters)
.\debug_minimap_capture.py:175:15: F541 f-string is missing placeholders
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:12:5: F401 'numpy.core.multiarray' imported but unused
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:45:34: E701 multiple statements on one line (colon)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:45:80: E501 line too long (86 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:80:80: E501 line too long (127 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:88:13: E701 multiple statements on one line (colon)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:88:80: E501 line too long (114 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:108:25: E701 multiple statements on one line (colon)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:108:80: E501 line too long (90 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:110:21: E701 multiple statements on one line (colon)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:114:80: E501 line too long (121 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:122:13: E701 multiple statements on one line (colon)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:122:80: E501 line too long (111 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:123:13: E701 multiple statements on one line (colon)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:123:80: E501 line too long (93 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:131:80: E501 line too long (84 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:133:9: E722 do not use bare 'except'
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:134:21: E701 multiple statements on one line (colon)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:134:80: E501 line too long (98 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:141:80: E501 line too long (90 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:146:29: E701 multiple statements on one line (colon)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:146:70: E225 missing whitespace around operator
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:148:80: E501 line too long (98 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:149:17: E701 multiple statements on one line (colon)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:149:80: E501 line too long (81 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:152:80: E501 line too long (120 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:154:13: E701 multiple statements on one line (colon)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:163:80: E501 line too long (96 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:164:80: E501 line too long (86 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:169:80: E501 line too long (128 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:178:13: E701 multiple statements on one line (colon)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:182:21: E701 multiple statements on one line (colon)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py:184:13: E701 multiple statements on one line (colon)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:3:5: F821 undefined name 'LOADER_DIR'
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:4:5: F821 undefined name 'PYTHON_EXTENSIONS_PATHS'
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:12:1: E722 do not use bare 'except'
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:16:4: F821 undefined name 'sys'
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:17:5: F821 undefined name 'os'
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:17:49: F821 undefined name 'os'
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:18:9: F821 undefined name 'os'
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:18:25: F821 undefined name 'os'
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:22:4: F821 undefined name 'sys'
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:23:5: F821 undefined name 'os'
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:23:36: F821 undefined name 'os'
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:24:9: F821 undefined name 'os'
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\config-3.py:24:25: F821 undefined name 'os'
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\config.py:5:31: F821 undefined name 'LOADER_DIR'
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\config.py:6:5: F821 undefined name 'BINARIES_PATHS'
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:8:1: E302 expected 2 blank lines, found 1
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:146:1: E302 expected 2 blank lines, found 1
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:262:17: E225 missing whitespace around operator
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:282:18: E225 missing whitespace around operator
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:302:48: E203 whitespace before ','
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:303:47: E203 whitespace before ','
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:304:49: E203 whitespace before ','
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:305:50: E203 whitespace before ','
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:306:50: E203 whitespace before ','
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:307:49: E203 whitespace before ','
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:308:50: E203 whitespace before ','
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:309:49: E203 whitespace before ','
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:310:51: E203 whitespace before ','
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:311:51: E203 whitespace before ','
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:324:80: E501 line too long (96 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:327:80: E501 line too long (97 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:331:20: E111 indentation is not a multiple of 4
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:331:20: E117 over-indented
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:331:80: E501 line too long (83 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:332:28: E128 continuation line under-indented for visual indent
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:337:80: E501 line too long (93 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:338:25: E128 continuation line under-indented for visual indent
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:343:80: E501 line too long (100 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:344:33: E128 continuation line under-indented for visual indent
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:344:80: E501 line too long (96 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:347:80: E501 line too long (108 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:348:33: E128 continuation line under-indented for visual indent
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:348:80: E501 line too long (104 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:352:80: E501 line too long (100 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:353:33: E128 continuation line under-indented for visual indent
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:353:80: E501 line too long (97 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:356:80: E501 line too long (108 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:357:33: E128 continuation line under-indented for visual indent
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:357:80: E501 line too long (105 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:361:80: E501 line too long (106 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:362:33: E128 continuation line under-indented for visual indent
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:362:80: E501 line too long (87 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:377:80: E501 line too long (119 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:378:29: E128 continuation line under-indented for visual indent
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:396:15: E221 multiple spaces before operator
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\mat_wrapper\__init__.py:14:80: E501 line too long (80 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\mat_wrapper\__init__.py:16:1: E302 expected 2 blank lines, found 1
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\mat_wrapper\__init__.py:21:80: E501 line too long (106 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\mat_wrapper\__init__.py:31:80: E501 line too long (94 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\misc\__init__.py:2:1: F401 '.version.get_ocv_version' imported but unused
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:154:80: E501 line too long (104 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:157:80: E501 line too long (193 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:167:80: E501 line too long (96 > 79 characters)
.\dist\NanoKeyboardControllerLiteApp\_internal\cv2\typing\__init__.py:168:80: E501 line too long (97 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:12:5: F401 'numpy.core.multiarray' imported but unused
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:45:34: E701 multiple statements on one line (colon)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:45:80: E501 line too long (86 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:80:80: E501 line too long (127 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:88:13: E701 multiple statements on one line (colon)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:88:80: E501 line too long (114 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:108:25: E701 multiple statements on one line (colon)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:108:80: E501 line too long (90 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:110:21: E701 multiple statements on one line (colon)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:114:80: E501 line too long (121 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:122:13: E701 multiple statements on one line (colon)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:122:80: E501 line too long (111 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:123:13: E701 multiple statements on one line (colon)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:123:80: E501 line too long (93 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:131:80: E501 line too long (84 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:133:9: E722 do not use bare 'except'
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:134:21: E701 multiple statements on one line (colon)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:134:80: E501 line too long (98 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:141:80: E501 line too long (90 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:146:29: E701 multiple statements on one line (colon)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:146:70: E225 missing whitespace around operator
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:148:80: E501 line too long (98 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:149:17: E701 multiple statements on one line (colon)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:149:80: E501 line too long (81 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:152:80: E501 line too long (120 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:154:13: E701 multiple statements on one line (colon)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:163:80: E501 line too long (96 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:164:80: E501 line too long (86 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:169:80: E501 line too long (128 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:178:13: E701 multiple statements on one line (colon)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:182:21: E701 multiple statements on one line (colon)
.\dist\lg_audio_helper_app\_internal\cv2\__init__.py:184:13: E701 multiple statements on one line (colon)
.\dist\lg_audio_helper_app\_internal\cv2\config-3.py:3:5: F821 undefined name 'LOADER_DIR'
.\dist\lg_audio_helper_app\_internal\cv2\config-3.py:4:5: F821 undefined name 'PYTHON_EXTENSIONS_PATHS'
.\dist\lg_audio_helper_app\_internal\cv2\config-3.py:12:1: E722 do not use bare 'except'
.\dist\lg_audio_helper_app\_internal\cv2\config-3.py:16:4: F821 undefined name 'sys'
.\dist\lg_audio_helper_app\_internal\cv2\config-3.py:17:5: F821 undefined name 'os'
.\dist\lg_audio_helper_app\_internal\cv2\config-3.py:17:49: F821 undefined name 'os'
.\dist\lg_audio_helper_app\_internal\cv2\config-3.py:18:9: F821 undefined name 'os'
.\dist\lg_audio_helper_app\_internal\cv2\config-3.py:18:25: F821 undefined name 'os'
.\dist\lg_audio_helper_app\_internal\cv2\config-3.py:22:4: F821 undefined name 'sys'
.\dist\lg_audio_helper_app\_internal\cv2\config-3.py:23:5: F821 undefined name 'os'
.\dist\lg_audio_helper_app\_internal\cv2\config-3.py:23:36: F821 undefined name 'os'
.\dist\lg_audio_helper_app\_internal\cv2\config-3.py:24:9: F821 undefined name 'os'
.\dist\lg_audio_helper_app\_internal\cv2\config-3.py:24:25: F821 undefined name 'os'
.\dist\lg_audio_helper_app\_internal\cv2\config.py:5:31: F821 undefined name 'LOADER_DIR'
.\dist\lg_audio_helper_app\_internal\cv2\config.py:6:5: F821 undefined name 'BINARIES_PATHS'
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:8:1: E302 expected 2 blank lines, found 1
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:146:1: E302 expected 2 blank lines, found 1
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:262:17: E225 missing whitespace around operator
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:282:18: E225 missing whitespace around operator
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:302:48: E203 whitespace before ','
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:303:47: E203 whitespace before ','
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:304:49: E203 whitespace before ','
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:305:50: E203 whitespace before ','
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:306:50: E203 whitespace before ','
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:307:49: E203 whitespace before ','
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:308:50: E203 whitespace before ','
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:309:49: E203 whitespace before ','
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:310:51: E203 whitespace before ','
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:311:51: E203 whitespace before ','
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:324:80: E501 line too long (96 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:327:80: E501 line too long (97 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:331:20: E111 indentation is not a multiple of 4
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:331:20: E117 over-indented
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:331:80: E501 line too long (83 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:332:28: E128 continuation line under-indented for visual indent
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:337:80: E501 line too long (93 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:338:25: E128 continuation line under-indented for visual indent
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:343:80: E501 line too long (100 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:344:33: E128 continuation line under-indented for visual indent
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:344:80: E501 line too long (96 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:347:80: E501 line too long (108 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:348:33: E128 continuation line under-indented for visual indent
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:348:80: E501 line too long (104 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:352:80: E501 line too long (100 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:353:33: E128 continuation line under-indented for visual indent
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:353:80: E501 line too long (97 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:356:80: E501 line too long (108 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:357:33: E128 continuation line under-indented for visual indent
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:357:80: E501 line too long (105 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:361:80: E501 line too long (106 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:362:33: E128 continuation line under-indented for visual indent
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:362:80: E501 line too long (87 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:377:80: E501 line too long (119 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:378:29: E128 continuation line under-indented for visual indent
.\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:396:15: E221 multiple spaces before operator
.\dist\lg_audio_helper_app\_internal\cv2\mat_wrapper\__init__.py:14:80: E501 line too long (80 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\mat_wrapper\__init__.py:16:1: E302 expected 2 blank lines, found 1
.\dist\lg_audio_helper_app\_internal\cv2\mat_wrapper\__init__.py:21:80: E501 line too long (106 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\mat_wrapper\__init__.py:31:80: E501 line too long (94 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\misc\__init__.py:2:1: F401 '.version.get_ocv_version' imported but unused
.\dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:154:80: E501 line too long (104 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:157:80: E501 line too long (193 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:167:80: E501 line too long (96 > 79 characters)
.\dist\lg_audio_helper_app\_internal\cv2\typing\__init__.py:168:80: E501 line too long (97 > 79 characters)
.\generate_wiring_pdf.py:9:1: F401 'reportlab.lib.enums.TA_LEFT' imported but unused
.\generate_wiring_pdf.py:18:80: E501 line too long (83 > 79 characters)
.\generate_wiring_pdf.py:42:80: E501 line too long (84 > 79 characters)
.\generate_wiring_pdf.py:56:80: E501 line too long (98 > 79 characters)
.\generate_wiring_pdf.py:58:80: E501 line too long (100 > 79 characters)
.\generate_wiring_pdf.py:61:80: E501 line too long (99 > 79 characters)
.\generate_wiring_pdf.py:63:80: E501 line too long (97 > 79 characters)
.\generate_wiring_pdf.py:64:80: E501 line too long (84 > 79 characters)
.\generate_wiring_pdf.py:65:80: E501 line too long (96 > 79 characters)
.\generate_wiring_pdf.py:70:80: E501 line too long (93 > 79 characters)
.\generate_wiring_pdf.py:85:80: E501 line too long (87 > 79 characters)
.\generate_wiring_pdf.py:135:80: E501 line too long (87 > 79 characters)
.\generate_wiring_pdf.py:141:80: E501 line too long (90 > 79 characters)
.\generate_wiring_pdf.py:218:9: F841 local variable 'left_comp_right' is assigned to but never used
.\generate_wiring_pdf.py:224:80: E501 line too long (98 > 79 characters)
.\generate_wiring_pdf.py:257:80: E501 line too long (93 > 79 characters)
.\generate_wiring_pdf.py:310:80: E501 line too long (93 > 79 characters)
.\generate_wiring_pdf.py:320:80: E501 line too long (98 > 79 characters)
.\generate_wiring_pdf.py:348:80: E501 line too long (94 > 79 characters)
.\generate_wiring_pdf.py:374:80: E501 line too long (85 > 79 characters)
.\generate_wiring_pdf.py:381:80: E501 line too long (96 > 79 characters)
.\generate_wiring_pdf.py:410:80: E501 line too long (90 > 79 characters)
.\generate_wiring_pdf.py:412:80: E501 line too long (88 > 79 characters)
.\generate_wiring_pdf.py:423:80: E501 line too long (95 > 79 characters)
.\generate_wiring_pdf.py:451:80: E501 line too long (97 > 79 characters)
.\generate_wiring_pdf.py:461:80: E501 line too long (93 > 79 characters)
.\generate_wiring_pdf.py:496:80: E501 line too long (91 > 79 characters)
.\generate_wiring_pdf.py:525:80: E501 line too long (83 > 79 characters)
.\generate_wiring_pdf.py:526:80: E501 line too long (93 > 79 characters)
.\generate_wiring_pdf.py:559:80: E501 line too long (99 > 79 characters)
.\generate_wiring_pdf.py:563:80: E501 line too long (92 > 79 characters)
.\generate_wiring_pdf.py:579:80: E501 line too long (94 > 79 characters)
.\generate_wiring_pdf.py:580:80: E501 line too long (89 > 79 characters)
.\generate_wiring_pdf.py:581:80: E501 line too long (91 > 79 characters)
.\generate_wiring_pdf.py:602:13: F841 local variable 'mid_x' is assigned to but never used
.\generate_wiring_pdf.py:609:80: E501 line too long (80 > 79 characters)
.\generate_wiring_pdf.py:615:80: E501 line too long (80 > 79 characters)
.\generate_wiring_pdf.py:624:80: E501 line too long (81 > 79 characters)
.\generate_wiring_pdf.py:652:80: E501 line too long (87 > 79 characters)
.\generate_wiring_pdf.py:653:80: E501 line too long (98 > 79 characters)
.\generate_wiring_pdf.py:662:80: E501 line too long (88 > 79 characters)
.\generate_wiring_pdf.py:675:80: E501 line too long (81 > 79 characters)
.\generate_wiring_pdf.py:694:80: E501 line too long (88 > 79 characters)
.\generate_wiring_pdf.py:700:80: E501 line too long (83 > 79 characters)
.\generate_wiring_pdf.py:703:80: E501 line too long (82 > 79 characters)
.\generate_wiring_pdf.py:709:80: E501 line too long (98 > 79 characters)
.\generate_wiring_pdf.py:768:80: E501 line too long (95 > 79 characters)
.\generate_wiring_pdf.py:780:80: E501 line too long (95 > 79 characters)
.\generate_wiring_pdf.py:781:80: E501 line too long (97 > 79 characters)
.\generate_wiring_pdf.py:782:80: E501 line too long (89 > 79 characters)
.\generate_wiring_pdf.py:783:80: E501 line too long (91 > 79 characters)
.\generate_wiring_pdf.py:784:80: E501 line too long (95 > 79 characters)
.\generate_wiring_pdf.py:785:80: E501 line too long (86 > 79 characters)
.\generate_wiring_pdf.py:786:80: E501 line too long (86 > 79 characters)
.\generate_wiring_pdf.py:788:80: E501 line too long (87 > 79 characters)
.\generate_wiring_pdf.py:797:80: E501 line too long (97 > 79 characters)
.\generate_wiring_pdf.py:808:80: E501 line too long (102 > 79 characters)
.\generate_wiring_pdf.py:816:80: E501 line too long (82 > 79 characters)
.\generate_wiring_pdf.py:817:80: E501 line too long (89 > 79 characters)
.\generate_wiring_pdf.py:818:80: E501 line too long (90 > 79 characters)
.\generate_wiring_pdf.py:819:80: E501 line too long (87 > 79 characters)
.\generate_wiring_pdf.py:820:80: E501 line too long (89 > 79 characters)
.\generate_wiring_pdf.py:821:80: E501 line too long (90 > 79 characters)
.\generate_wiring_pdf.py:822:80: E501 line too long (86 > 79 characters)
.\generate_wiring_pdf.py:831:80: E501 line too long (82 > 79 characters)
.\generate_wiring_pdf.py:832:80: E501 line too long (88 > 79 characters)
.\generate_wiring_pdf.py:839:80: E501 line too long (82 > 79 characters)
.\generate_wiring_pdf.py:842:80: E501 line too long (89 > 79 characters)
.\generate_wiring_pdf.py:843:80: E501 line too long (91 > 79 characters)
.\generate_wiring_pdf.py:851:80: E501 line too long (85 > 79 characters)
.\generate_wiring_pdf.py:852:80: E501 line too long (85 > 79 characters)
.\generate_wiring_pdf.py:853:80: E501 line too long (91 > 79 characters)
.\generate_wiring_pdf.py:869:80: E501 line too long (106 > 79 characters)
.\generate_wiring_pdf.py:880:80: E501 line too long (97 > 79 characters)
.\generate_wiring_pdf.py:888:80: E501 line too long (98 > 79 characters)
.\generate_wiring_pdf.py:893:80: E501 line too long (80 > 79 characters)
.\generate_wiring_pdf.py:928:80: E501 line too long (80 > 79 characters)
.\generate_wiring_pdf.py:938:80: E501 line too long (81 > 79 characters)
.\generate_wiring_pdf.py:953:80: E501 line too long (91 > 79 characters)
.\generate_wiring_pdf.py:954:80: E501 line too long (99 > 79 characters)
.\generate_wiring_pdf.py:955:80: E501 line too long (95 > 79 characters)
.\generate_wiring_pdf.py:956:80: E501 line too long (86 > 79 characters)
.\generate_wiring_pdf.py:958:80: E501 line too long (98 > 79 characters)
.\generate_wiring_pdf.py:960:80: E501 line too long (84 > 79 characters)
.\generate_wiring_pdf.py:970:80: E501 line too long (80 > 79 characters)
.\generate_wiring_pdf.py:976:80: E501 line too long (84 > 79 characters)
.\generate_wiring_pdf.py:981:80: E501 line too long (82 > 79 characters)
.\generate_wiring_pdf.py:982:80: E501 line too long (86 > 79 characters)
.\generate_wiring_pdf.py:987:80: E501 line too long (91 > 79 characters)
.\generate_wiring_pdf.py:988:80: E501 line too long (89 > 79 characters)
.\generate_wiring_pdf.py:996:80: E501 line too long (95 > 79 characters)
.\generate_wiring_pdf.py:1021:80: E501 line too long (104 > 79 characters)
.\lazy_imports.py:3:80: E501 line too long (81 > 79 characters)
.\list_matching_windows.py:41:80: E501 line too long (96 > 79 characters)
.\list_matching_windows.py:51:80: E501 line too long (83 > 79 characters)
.\scratch\analyze_panel_pixels.py:16:80: E501 line too long (85 > 79 characters)
.\scratch\analyze_panel_pixels.py:25:80: E501 line too long (84 > 79 characters)
.\scratch\analyze_panel_pixels.py:39:80: E501 line too long (87 > 79 characters)
.\scratch\analyze_panel_pixels.py:41:29: E203 whitespace before ':'
.\scratch\analyze_panel_pixels.py:41:44: E203 whitespace before ':'
.\scratch\analyze_resizing.py:3:1: F401 'os' imported but unused
.\scratch\analyze_resizing.py:8:1: F401 'numpy as np' imported but unused
.\scratch\analyze_resizing.py:12:80: E501 line too long (88 > 79 characters)
.\scratch\analyze_resizing.py:14:1: E402 module level import not at top of file
.\scratch\analyze_resizing.py:15:1: E402 module level import not at top of file
.\scratch\analyze_resizing.py:46:5: F841 local variable 'solver' is assigned to but never used
.\scratch\analyze_resizing.py:63:80: E501 line too long (81 > 79 characters)
.\scratch\check_actual_right_endcap.py:4:1: F401 'numpy as np' imported but unused
.\scratch\check_actual_right_endcap.py:9:80: E501 line too long (115 > 79 characters)
.\scratch\check_actual_right_endcap.py:15:80: E501 line too long (113 > 79 characters)
.\scratch\check_actual_right_endcap.py:43:22: E203 whitespace before ':'
.\scratch\check_actual_right_endcap.py:43:44: E203 whitespace before ':'
.\scratch\check_actual_right_endcap.py:45:80: E501 line too long (122 > 79 characters)
.\scratch\check_dist.py:8:80: E501 line too long (87 > 79 characters)
.\scratch\check_interpolated_crops.py:8:80: E501 line too long (115 > 79 characters)
.\scratch\check_interpolated_crops.py:16:80: E501 line too long (135 > 79 characters)
.\scratch\check_interpolated_crops.py:28:9: E741 ambiguous variable name 'l'
.\scratch\check_interpolated_crops.py:33:80: E501 line too long (133 > 79 characters)
.\scratch\check_interpolated_crops.py:35:80: E501 line too long (86 > 79 characters)
.\scratch\check_spec_error.py:45:80: E501 line too long (96 > 79 characters)
.\scratch\check_template_layout.py:4:1: F401 'numpy as np' imported but unused
.\scratch\check_template_layout.py:20:80: E501 line too long (94 > 79 characters)
.\scratch\compare_pixels.py:4:1: F401 'numpy as np' imported but unused
.\scratch\compare_pixels.py:21:80: E501 line too long (88 > 79 characters)
.\scratch\compare_pixels.py:32:80: E501 line too long (87 > 79 characters)
.\scratch\crop_possible_arrows.py:4:1: F401 'numpy as np' imported but unused
.\scratch\debug_build.py:3:1: F401 'sys' imported but unused
.\scratch\debug_build.py:22:80: E501 line too long (143 > 79 characters)
.\scratch\debug_build.py:33:1: E402 module level import not at top of file
.\scratch\debug_panel_detail.py:7:1: F401 'PIL.Image' imported but unused
.\scratch\debug_panel_detail.py:10:80: E501 line too long (88 > 79 characters)
.\scratch\debug_panel_detail.py:12:1: E402 module level import not at top of file
.\scratch\debug_panel_detail.py:22:32: E203 whitespace before ':'
.\scratch\debug_panel_detail.py:22:59: E203 whitespace before ':'
.\scratch\debug_panel_detail.py:53:80: E501 line too long (84 > 79 characters)
.\scratch\debug_panel_detail.py:67:80: E501 line too long (82 > 79 characters)
.\scratch\debug_panel_detail.py:73:80: E501 line too long (90 > 79 characters)
.\scratch\debug_panel_detail.py:94:80: E501 line too long (87 > 79 characters)
.\scratch\debug_panel_detail.py:96:80: E501 line too long (89 > 79 characters)
.\scratch\detect_arrow_centers_by_color.py:9:80: E501 line too long (115 > 79 characters)
.\scratch\detect_arrow_centers_by_color.py:30:80: E501 line too long (107 > 79 characters)
.\scratch\detect_arrow_centers_by_color.py:35:80: E501 line too long (84 > 79 characters)
.\scratch\detect_arrow_centers_by_color.py:55:80: E501 line too long (80 > 79 characters)
.\scratch\detect_arrow_centers_by_color.py:57:27: E203 whitespace before ':'
.\scratch\detect_arrow_centers_by_color.py:57:56: E203 whitespace before ':'
.\scratch\detect_arrow_centers_by_color.py:59:80: E501 line too long (119 > 79 characters)
.\scratch\find_arrows_fullframe.py:23:80: E501 line too long (84 > 79 characters)
.\scratch\find_panel_scale.py:12:80: E501 line too long (87 > 79 characters)
.\scratch\find_panel_scale.py:17:80: E501 line too long (87 > 79 characters)
.\scratch\find_panel_scale.py:19:80: E501 line too long (84 > 79 characters)
.\scratch\find_panel_scale.py:30:80: E501 line too long (91 > 79 characters)
.\scratch\find_panel_scale.py:34:80: E501 line too long (99 > 79 characters)
.\scratch\find_perfect_scale.py:20:32: E203 whitespace before ':'
.\scratch\find_perfect_scale.py:20:59: E203 whitespace before ':'
.\scratch\find_perfect_scale.py:38:80: E501 line too long (91 > 79 characters)
.\scratch\find_perfect_scale.py:49:80: E501 line too long (84 > 79 characters)
.\scratch\find_perfect_scale.py:60:80: E501 line too long (87 > 79 characters)
.\scratch\find_perfect_scale.py:67:80: E501 line too long (93 > 79 characters)
.\scratch\inspect_matches.py:4:1: F401 'numpy as np' imported but unused
.\scratch\inspect_matches.py:25:21: E203 whitespace before ':'
.\scratch\inspect_matches.py:25:35: E203 whitespace before ':'
.\scratch\inspect_matches.py:26:21: E203 whitespace before ':'
.\scratch\inspect_matches.py:26:35: E203 whitespace before ':'
.\scratch\overlay_detected_centers.py:4:1: F401 'numpy as np' imported but unused
.\scratch\overlay_detected_centers.py:9:80: E501 line too long (115 > 79 characters)
.\scratch\overlay_detected_centers.py:37:80: E501 line too long (122 > 79 characters)
.\scratch\test_color_vit.py:3:1: F401 'cv2' imported but unused
.\scratch\test_color_vit.py:13:80: E501 line too long (115 > 79 characters)
.\scratch\test_color_vit.py:49:80: E501 line too long (163 > 79 characters)
.\scratch\test_colorkey_theme.py:7:1: F401 'PIL.Image' imported but unused
.\scratch\test_colorkey_theme.py:27:80: E501 line too long (84 > 79 characters)
.\scratch\test_colorkey_theme.py:28:80: E501 line too long (80 > 79 characters)
.\scratch\test_colorkey_theme.py:30:80: E501 line too long (86 > 79 characters)
.\scratch\test_colorkey_theme.py:40:80: E501 line too long (93 > 79 characters)
.\scratch\test_colorkey_theme.py:52:80: E501 line too long (98 > 79 characters)
.\scratch\test_colorkey_theme.py:69:80: E501 line too long (97 > 79 characters)
.\scratch\test_colorkey_theme.py:74:80: E501 line too long (81 > 79 characters)
.\scratch\test_colorkey_theme.py:77:80: E501 line too long (100 > 79 characters)
.\scratch\test_colorkey_theme.py:82:80: E501 line too long (90 > 79 characters)
.\scratch\test_colorkey_theme.py:104:80: E501 line too long (96 > 79 characters)
.\scratch\test_colorkey_transparency.py:4:1: F401 'tkinter.ttk' imported but unused
.\scratch\test_colorkey_transparency.py:7:1: F401 'PIL.Image' imported but unused
.\scratch\test_colorkey_transparency.py:46:80: E501 line too long (84 > 79 characters)
.\scratch\test_colorkey_transparency.py:50:80: E501 line too long (85 > 79 characters)
.\scratch\test_colorkey_transparency.py:71:80: E501 line too long (96 > 79 characters)
.\scratch\test_crops_with_vit.py:5:1: F401 'cv2' imported but unused
.\scratch\test_crops_with_vit.py:10:80: E501 line too long (88 > 79 characters)
.\scratch\test_crops_with_vit.py:12:1: E402 module level import not at top of file
.\scratch\test_crops_with_vit.py:13:1: E402 module level import not at top of file
.\scratch\test_crops_with_vit.py:27:80: E501 line too long (95 > 79 characters)
.\scratch\test_crops_with_vit.py:28:80: E501 line too long (83 > 79 characters)
.\scratch\test_crops_with_vit.py:32:80: E501 line too long (86 > 79 characters)
.\scratch\test_crops_with_vit.py:35:80: E501 line too long (81 > 79 characters)
.\scratch\test_crops_with_vit.py:37:80: E501 line too long (80 > 79 characters)
.\scratch\test_crops_with_vit.py:58:80: E501 line too long (87 > 79 characters)
.\scratch\test_crops_with_vit.py:59:80: E501 line too long (96 > 79 characters)
.\scratch\test_full_pipeline_fix.py:9:80: E501 line too long (88 > 79 characters)
.\scratch\test_full_pipeline_fix.py:11:1: E402 module level import not at top of file
.\scratch\test_full_pipeline_fix.py:12:1: E402 module level import not at top of file
.\scratch\test_full_pipeline_fix.py:19:80: E501 line too long (84 > 79 characters)
.\scratch\test_full_pipeline_fix.py:20:80: E501 line too long (83 > 79 characters)
.\scratch\test_full_pipeline_fix.py:43:80: E501 line too long (84 > 79 characters)
.\scratch\test_full_pipeline_fix.py:75:80: E501 line too long (81 > 79 characters)
.\scratch\test_full_pipeline_fix.py:132:15: F541 f-string is missing placeholders
.\scratch\test_full_pipeline_fix.py:138:80: E501 line too long (100 > 79 characters)
.\scratch\test_full_pipeline_fix.py:149:67: E741 ambiguous variable name 'l'
.\scratch\test_full_pipeline_fix.py:149:80: E501 line too long (86 > 79 characters)
.\scratch\test_full_pipeline_fix.py:170:80: E501 line too long (89 > 79 characters)
.\scratch\test_internal_libs.py:11:1: E402 module level import not at top of file
.\scratch\test_internal_libs.py:13:1: E402 module level import not at top of file
.\scratch\test_internal_libs.py:14:1: E402 module level import not at top of file
.\scratch\test_internal_libs.py:15:1: E402 module level import not at top of file
.\scratch\test_internal_libs.py:24:1: E402 module level import not at top of file
.\scratch\test_interpolation_vit.py:12:80: E501 line too long (115 > 79 characters)
.\scratch\test_interpolation_vit.py:17:80: E501 line too long (113 > 79 characters)
.\scratch\test_interpolation_vit.py:63:80: E501 line too long (110 > 79 characters)
.\scratch\test_interpolation_vit.py:70:80: E501 line too long (81 > 79 characters)
.\scratch\test_interpolation_vit.py:83:80: E501 line too long (93 > 79 characters)
.\scratch\test_interpolation_vit.py:87:80: E501 line too long (89 > 79 characters)
.\scratch\test_main_app_screenshot.py:9:1: F401 'time' imported but unused
.\scratch\test_main_app_screenshot.py:9:1: E402 module level import not at top of file
.\scratch\test_main_app_screenshot.py:10:1: F401 'tkinter as tk' imported but unused
.\scratch\test_main_app_screenshot.py:10:1: E402 module level import not at top of file
.\scratch\test_main_app_screenshot.py:12:1: E402 module level import not at top of file
.\scratch\test_main_app_screenshot.py:14:1: E402 module level import not at top of file
.\scratch\test_main_app_screenshot.py:23:80: E501 line too long (103 > 79 characters)
.\scratch\test_main_app_screenshot.py:45:80: E501 line too long (96 > 79 characters)
.\scratch\test_opacity.py:4:1: F401 'tkinter.ttk' imported but unused
.\scratch\test_opacity.py:23:80: E501 line too long (98 > 79 characters)
.\scratch\test_opacity.py:40:80: E501 line too long (81 > 79 characters)
.\scratch\test_opacity_notebook.py:3:1: F401 'time' imported but unused
.\scratch\test_opacity_notebook.py:8:1: F401 'PIL.Image' imported but unused
.\scratch\test_opacity_notebook.py:26:80: E501 line too long (86 > 79 characters)
.\scratch\test_opacity_notebook.py:33:80: E501 line too long (88 > 79 characters)
.\scratch\test_opacity_notebook.py:34:80: E501 line too long (93 > 79 characters)
.\scratch\test_opacity_notebook.py:39:80: E501 line too long (98 > 79 characters)
.\scratch\test_opacity_notebook.py:62:80: E501 line too long (80 > 79 characters)
.\scratch\test_opacity_notebook.py:65:80: E501 line too long (99 > 79 characters)
.\scratch\test_opacity_notebook.py:70:80: E501 line too long (90 > 79 characters)
.\scratch\test_opacity_notebook.py:92:80: E501 line too long (96 > 79 characters)
.\scratch\test_opacity_screenshot.py:3:1: F401 'time' imported but unused
.\scratch\test_opacity_screenshot.py:5:1: F401 'tkinter.ttk' imported but unused
.\scratch\test_opacity_screenshot.py:8:1: F401 'PIL.Image' imported but unused
.\scratch\test_opacity_screenshot.py:8:1: F401 'PIL.ImageDraw' imported but unused
.\scratch\test_opacity_screenshot.py:25:80: E501 line too long (98 > 79 characters)
.\scratch\test_opacity_screenshot.py:27:80: E501 line too long (100 > 79 characters)
.\scratch\test_opacity_screenshot.py:46:80: E501 line too long (100 > 79 characters)
.\scratch\test_opacity_screenshot.py:71:80: E501 line too long (96 > 79 characters)
.\scratch\test_prop_scaling.py:4:1: F401 'numpy as np' imported but unused
.\scratch\test_prop_scaling.py:21:80: E501 line too long (94 > 79 characters)
.\scratch\test_prop_scaling.py:28:80: E501 line too long (92 > 79 characters)
.\scratch\test_prop_scaling.py:30:80: E501 line too long (91 > 79 characters)
.\scratch\test_prop_scaling.py:31:80: E501 line too long (96 > 79 characters)
.\scratch\test_prop_scaling.py:33:80: E501 line too long (95 > 79 characters)
.\scratch\test_prop_scaling.py:34:80: E501 line too long (108 > 79 characters)
.\scratch\test_prop_scaling.py:36:80: E501 line too long (92 > 79 characters)
.\scratch\test_prop_scaling.py:38:80: E501 line too long (98 > 79 characters)
.\scratch\test_prop_scaling.py:41:80: E501 line too long (98 > 79 characters)
.\scratch\test_prop_scaling.py:48:80: E501 line too long (87 > 79 characters)
.\scratch\test_prop_scaling.py:60:80: E501 line too long (141 > 79 characters)
.\scratch\test_proportional_fix.py:9:80: E501 line too long (88 > 79 characters)
.\scratch\test_proportional_fix.py:11:1: E402 module level import not at top of file
.\scratch\test_proportional_fix.py:12:1: E402 module level import not at top of file
.\scratch\test_proportional_fix.py:13:1: E402 module level import not at top of file
.\scratch\test_proportional_fix.py:16:80: E501 line too long (99 > 79 characters)
.\scratch\test_proportional_fix.py:17:80: E501 line too long (83 > 79 characters)
.\scratch\test_proportional_fix.py:71:80: E501 line too long (87 > 79 characters)
.\scratch\test_proportional_fix.py:72:80: E501 line too long (80 > 79 characters)
.\scratch\test_proportional_fix.py:76:80: E501 line too long (93 > 79 characters)
.\scratch\test_proportional_fix.py:97:80: E501 line too long (87 > 79 characters)
.\scratch\test_proportional_fix.py:98:80: E501 line too long (80 > 79 characters)
.\scratch\test_proportional_fix.py:102:80: E501 line too long (93 > 79 characters)
.\scratch\test_proportional_resize.py:10:80: E501 line too long (88 > 79 characters)
.\scratch\test_proportional_resize.py:12:1: E402 module level import not at top of file
.\scratch\test_proportional_resize.py:35:32: E203 whitespace before ':'
.\scratch\test_proportional_resize.py:35:59: E203 whitespace before ':'
.\scratch\test_proportional_resize.py:59:80: E501 line too long (84 > 79 characters)
.\scratch\test_proportional_resize.py:73:80: E501 line too long (82 > 79 characters)
.\scratch\test_proportional_resize.py:98:80: E501 line too long (87 > 79 characters)
.\scratch\test_proportional_resize.py:100:80: E501 line too long (89 > 79 characters)
.\scratch\test_proportional_resize.py:113:80: E501 line too long (92 > 79 characters)
.\scratch\test_proportional_resize.py:119:80: E501 line too long (92 > 79 characters)
.\scratch\test_robust_color_detect.py:21:80: E501 line too long (84 > 79 characters)
.\scratch\test_robust_color_detect.py:29:80: E501 line too long (81 > 79 characters)
.\scratch\test_robust_color_detect.py:47:25: E741 ambiguous variable name 'l'
.\scratch\test_robust_color_detect.py:48:80: E501 line too long (92 > 79 characters)
.\scratch\test_robust_color_detect.py:53:80: E501 line too long (80 > 79 characters)
.\scratch\test_robust_color_detect.py:73:80: E501 line too long (87 > 79 characters)
.\scratch\test_robust_solver.py:13:80: E501 line too long (115 > 79 characters)
.\scratch\test_robust_solver.py:18:80: E501 line too long (113 > 79 characters)
.\scratch\test_robust_solver.py:70:80: E501 line too long (84 > 79 characters)
.\scratch\test_robust_solver.py:113:80: E501 line too long (113 > 79 characters)
.\scratch\test_sidebar_transparency.py:8:1: F401 'time' imported but unused
.\scratch\test_sidebar_transparency.py:8:1: E402 module level import not at top of file
.\scratch\test_sidebar_transparency.py:9:1: E402 module level import not at top of file
.\scratch\test_sidebar_transparency.py:11:1: E402 module level import not at top of file
.\scratch\test_sidebar_transparency.py:12:1: E402 module level import not at top of file
.\scratch\test_sidebar_transparency.py:14:1: E402 module level import not at top of file
.\scratch\test_sidebar_transparency.py:24:80: E501 line too long (81 > 79 characters)
.\scratch\test_sidebar_transparency.py:26:80: E501 line too long (85 > 79 characters)
.\scratch\test_sidebar_transparency.py:46:80: E501 line too long (96 > 79 characters)
.\scratch\test_sidebar_transparency.py:48:80: E501 line too long (81 > 79 characters)
.\scratch\test_vit_filtering.py:10:80: E501 line too long (88 > 79 characters)
.\scratch\test_vit_filtering.py:12:1: E402 module level import not at top of file
.\scratch\test_vit_filtering.py:13:1: E402 module level import not at top of file
.\scratch\test_vit_filtering.py:28:80: E501 line too long (86 > 79 characters)
.\scratch\test_vit_filtering.py:32:80: E501 line too long (84 > 79 characters)
.\scratch\test_vit_filtering.py:61:9: E741 ambiguous variable name 'l'
.\scratch\test_vit_filtering.py:82:80: E501 line too long (82 > 79 characters)
.\scratch\test_vit_filtering.py:107:80: E501 line too long (84 > 79 characters)
.\scratch\test_vit_filtering_fixed.py:10:80: E501 line too long (88 > 79 characters)
.\scratch\test_vit_filtering_fixed.py:12:1: E402 module level import not at top of file
.\scratch\test_vit_filtering_fixed.py:13:1: E402 module level import not at top of file
.\scratch\test_vit_filtering_fixed.py:31:80: E501 line too long (84 > 79 characters)
.\scratch\test_vit_filtering_fixed.py:48:80: E501 line too long (90 > 79 characters)
.\scratch\test_vit_filtering_fixed.py:54:80: E501 line too long (81 > 79 characters)
.\scratch\test_vit_filtering_fixed.py:55:80: E501 line too long (87 > 79 characters)
.\scratch\test_vit_filtering_fixed.py:61:80: E501 line too long (91 > 79 characters)
.\scratch\test_vit_filtering_fixed.py:62:80: E501 line too long (83 > 79 characters)
.\scratch\test_vit_filtering_fixed.py:71:80: E501 line too long (94 > 79 characters)
.\scratch\test_vit_filtering_fixed.py:75:9: E741 ambiguous variable name 'l'
.\scratch\test_vit_filtering_fixed.py:97:80: E501 line too long (98 > 79 characters)
.\scratch\test_vit_filtering_fixed.py:122:80: E501 line too long (84 > 79 characters)
.\scratch\test_widget_opacity.py:4:1: F401 'tkinter.ttk' imported but unused
.\scratch\test_widget_opacity.py:7:1: F401 'PIL.Image' imported but unused
.\scratch\test_widget_opacity.py:30:80: E501 line too long (92 > 79 characters)
.\scratch\test_widget_opacity.py:35:80: E501 line too long (93 > 79 characters)
.\scratch\test_widget_opacity.py:60:80: E501 line too long (96 > 79 characters)
.\scratch\try_delete_files.py:8:80: E501 line too long (128 > 79 characters)
.\scratch\visualize_crop.py:31:80: E501 line too long (84 > 79 characters)
.\scratch\visualize_crop.py:38:80: E501 line too long (84 > 79 characters)
.\scratch\visualize_crop.py:52:11: F541 f-string is missing placeholders
.\scratch\visualize_crop.py:58:80: E501 line too long (96 > 79 characters)
.\scratch\visualize_matches.py:17:80: E501 line too long (86 > 79 characters)
.\setup_wallpaper.py:12:80: E501 line too long (83 > 79 characters)
.\test_coordinates.py:29:80: E501 line too long (84 > 79 characters)
.\test_lie_detection.py:6:1: F401 'numpy as np' imported but unused
.\test_lie_detection.py:46:80: E501 line too long (83 > 79 characters)
.\test_lie_detection.py:58:80: E501 line too long (136 > 79 characters)
.\test_lie_detection.py:62:80: E501 line too long (97 > 79 characters)
.\test_lie_detection.py:70:80: E501 line too long (81 > 79 characters)
.\test_lie_detection.py:72:80: E501 line too long (86 > 79 characters)
.\test_lie_detection.py:75:80: E501 line too long (147 > 79 characters)
.\test_lie_detection.py:81:80: E501 line too long (101 > 79 characters)
.\test_roboflow.py:10:80: E501 line too long (83 > 79 characters)
.\test_roboflow.py:12:1: E402 module level import not at top of file
.\test_roboflow.py:21:80: E501 line too long (132 > 79 characters)
.\test_roboflow.py:25:80: E501 line too long (144 > 79 characters)
.\test_wide_search.py:7:1: F401 'PIL.Image' imported but unused
.\test_wide_search.py:20:30: E203 whitespace before ':'
.\test_wide_search.py:20:57: E203 whitespace before ':'
.\test_wide_search.py:46:80: E501 line too long (81 > 79 characters)


## Unused Code (vulture)

app\auto_farm\controller.py:35: unused variable 'RUNE_TEMPLATE' (60% confidence)
app\auto_farm\controller.py:90: unused attribute 'last_lie_check_time' (60% confidence)
app\auto_farm\rune_solver\model_vit.py:36: unused attribute 'requires_grad' (60% confidence)
app\auto_farm\rune_solver\model_vit.py:51: unused method 'forward' (60% confidence)
app\auto_farm\rune_solver\panel_detect.py:23: unused variable 'ARROW_CENTERS_REL' (60% confidence)
app\auto_farm\rune_solver\vit_solver.py:117: unused import '_cv2' (90% confidence)
app\auto_farm\rune_solver\vit_solver.py:118: unused import '_np' (90% confidence)
app\auto_farm\rune_solver\vit_solver.py:119: unused import 'ImageFont' (90% confidence)
app\driver_manager.py:156: unused variable 'dirs' (60% confidence)
app\main.py:485: unused method 'on_connection_state_changed' (60% confidence)
app\tabs\auto_farm_firmware.py:272: unused variable 'is_simulation' (60% confidence)
app\tabs\auto_farm_firmware.py:370: unused variable 'reload_callback' (100% confidence)
app\tabs\dashboard.py:44: unused attribute '_last_chips' (60% confidence)
app\tabs\dashboard.py:590: unused method 'check_status' (60% confidence)
app\tabs\dashboard.py:731: unused attribute '_last_chips' (60% confidence)
app\tabs\profiles.py:647: unused method 'load_profile' (60% confidence)
app\tabs\profiles.py:651: unused method 'toggle_json_preview' (60% confidence)
app\tabs\profiles.py:655: unused method 'hide_json_preview' (60% confidence)
audit_report.py:11: unused import 'difflib' (90% confidence)
dist\lg_audio_helper_app\_internal\cv2\data\__init__.py:4: unused variable 'haarcascades' (60% confidence)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:17: unused function 'networks' (60% confidence)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:23: unused function 'compile_args' (60% confidence)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:29: unused function 'GIn' (60% confidence)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:35: unused function 'GOut' (60% confidence)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:41: unused function 'gin' (60% confidence)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:47: unused function 'descr_of' (60% confidence)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:58: unused function '__new__' (60% confidence)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:151: unused function '__new__' (60% confidence)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py:403: unused attribute 'GStreamerPipeline' (60% confidence)
dist\lg_audio_helper_app\_internal\cv2\mat_wrapper\__init__.py:24: unused function '__new__' (60% confidence)
dist\lg_audio_helper_app\_internal\cv2\mat_wrapper\__init__.py:42: unused attribute '__module__' (60% confidence)
dist\lg_audio_helper_app\_internal\cv2\misc\version.py:5: unused function 'get_ocv_version' (60% confidence)
dist\lg_audio_helper_app\_internal\cv2\version.py:2: unused variable 'opencv_version' (60% confidence)
dist\lg_audio_helper_app\_internal\cv2\version.py:3: unused variable 'contrib' (60% confidence)
dist\lg_audio_helper_app\_internal\cv2\version.py:5: unused variable 'rolling' (60% confidence)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\data\__init__.py:4: unused variable 'haarcascades' (60% confidence)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:17: unused function 'networks' (60% confidence)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:23: unused function 'compile_args' (60% confidence)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:29: unused function 'GIn' (60% confidence)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:35: unused function 'GOut' (60% confidence)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:41: unused function 'gin' (60% confidence)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:47: unused function 'descr_of' (60% confidence)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:58: unused function '__new__' (60% confidence)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:151: unused function '__new__' (60% confidence)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py:403: unused attribute 'GStreamerPipeline' (60% confidence)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\mat_wrapper\__init__.py:24: unused function '__new__' (60% confidence)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\mat_wrapper\__init__.py:42: unused attribute '__module__' (60% confidence)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\misc\version.py:5: unused function 'get_ocv_version' (60% confidence)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\version.py:2: unused variable 'opencv_version' (60% confidence)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\version.py:3: unused variable 'contrib' (60% confidence)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\version.py:5: unused variable 'rolling' (60% confidence)
generate_wiring_pdf.py:9: unused import 'TA_LEFT' (90% confidence)
generate_wiring_pdf.py:34: unused variable 'C_WHITE' (60% confidence)
generate_wiring_pdf.py:35: unused variable 'C_BROWN' (60% confidence)
generate_wiring_pdf.py:36: unused variable 'C_PINK' (60% confidence)
generate_wiring_pdf.py:58: unused variable 'H2' (60% confidence)
generate_wiring_pdf.py:64: unused variable 'MONO' (60% confidence)
generate_wiring_pdf.py:116: unused method 'wrap' (60% confidence)
generate_wiring_pdf.py:116: unused variable 'aH' (100% confidence)
generate_wiring_pdf.py:116: unused variable 'aW' (100% confidence)
generate_wiring_pdf.py:195: unused function 'label_pin' (60% confidence)
generate_wiring_pdf.py:218: unused variable 'left_comp_right' (60% confidence)
generate_wiring_pdf.py:273: unused variable 'label_text' (60% confidence)
generate_wiring_pdf.py:293: unused variable 'label_text' (60% confidence)
generate_wiring_pdf.py:481: unused variable 'spin' (60% confidence)
generate_wiring_pdf.py:520: unused variable 'spin' (60% confidence)
generate_wiring_pdf.py:526: unused variable 'mid_x' (60% confidence)
generate_wiring_pdf.py:544: unused variable 'spin' (60% confidence)
generate_wiring_pdf.py:602: unused variable 'mid_x' (60% confidence)
scratch\check_spec_error.py:36: unused class 'MockAnalysis' (60% confidence)


## Cyclomatic Complexity (radon)

apply_fixes.py
    F 49:0 add_placeholder_docstrings - C (20)
    F 103:0 replace_generic_excepts - B (7)
    F 131:0 analyze_complexity - A (5)
    F 13:0 run_cmd - A (2)
    F 124:0 process_files - A (2)
    F 22:0 install_dev_deps - A (1)
    F 28:0 format_code - A (1)
audit_report.py
    F 47:0 duplicate_code_report - C (13)
    F 84:0 anti_cheat_checks - B (6)
    F 21:0 run_tool - A (1)
    F 27:0 pylint_report - A (1)
    F 32:0 flake8_report - A (1)
    F 37:0 vulture_report - A (1)
    F 42:0 radon_report - A (1)
    F 110:0 main - A (1)
check_image.py
    F 7:0 main - A (2)
convert_vit_to_onnx.py
    F 21:0 main - A (2)
debug_minimap_capture.py
    F 38:0 find_game_window - A (5)
    F 52:0 get_client_rect - A (1)
generate_wiring_pdf.py
    M 120:4 ClearWiringDiagram.draw - B (10)
    C 104:0 ClearWiringDiagram - A (5)
    F 737:0 build_pdf - A (2)
    F 40:0 S - A (1)
    F 68:0 HR - A (1)
    F 73:0 make_table - A (1)
    M 110:4 ClearWiringDiagram.__init__ - A (1)
    M 116:4 ClearWiringDiagram.wrap - A (1)
lazy_imports.py
    F 11:0 lazy_import - A (2)
setup_wallpaper.py
    F 9:0 setup_wallpaper - A (5)
test_coordinates.py
    F 15:0 main - A (1)
test_lie_detection.py
    F 11:0 test_lie_detection - B (10)
test_onnx_solver.py
    F 10:0 main - A (2)
test_roboflow.py
    F 15:0 main - A (5)
test_wide_search.py
    F 12:0 main - B (7)
app\connection.py
    M 167:4 SerialConnectionManager.upload_profile - C (15)
    M 318:4 SerialConnectionManager._read_listener - C (14)
    M 260:4 SerialConnectionManager.parse_config_hex - B (7)
    C 19:0 SerialConnectionManager - B (6)
    M 139:4 SerialConnectionManager.send_command_chunked - A (5)
    M 354:4 SerialConnectionManager._simulated_listener - A (5)
    M 50:4 SerialConnectionManager.get_available_ports - A (4)
    M 59:4 SerialConnectionManager.connect - A (4)
    M 105:4 SerialConnectionManager.disconnect - A (4)
    M 119:4 SerialConnectionManager.send_command - A (4)
    M 242:4 SerialConnectionManager.request_config_read - A (3)
    M 38:4 SerialConnectionManager.log - A (2)
    M 45:4 SerialConnectionManager.update_status - A (2)
    M 366:4 SerialConnectionManager.flash_firmware - A (2)
    M 22:4 SerialConnectionManager.__init__ - A (1)
app\driver_manager.py
    F 11:0 detect_connected_chips - C (11)
    F 99:0 download_and_install_driver - A (3)
app\main.py
    M 447:4 ModernApp.connection_status_handler - C (16)
    M 141:4 ModernApp.__init__ - C (11)
    M 81:4 WallpaperManager.trigger_draw - B (10)
    C 138:0 ModernApp - B (6)
    M 404:4 ModernApp.show_page - A (5)
    C 40:0 WallpaperManager - A (4)
    M 54:4 WallpaperManager.load_image - A (4)
    M 434:4 ModernApp.reload_all_tabs - A (4)
    M 75:4 WallpaperManager.on_widget_resize - A (2)
    M 424:4 ModernApp.on_nav_enter - A (2)
    M 429:4 ModernApp.on_nav_leave - A (2)
    M 43:4 WallpaperManager.__init__ - A (1)
    M 68:4 WallpaperManager.register - A (1)
    M 443:4 ModernApp.connection_logger - A (1)
    M 485:4 ModernApp.on_connection_state_changed - A (1)
app\models.py
    M 129:4 RobotProfile.load_from_dict - A (5)
    C 77:0 RobotProfile - A (3)
    M 112:4 RobotProfile.to_dict - A (3)
    C 6:0 ServoConfig - A (2)
    C 36:0 Action - A (2)
    M 53:4 Action.__init__ - A (2)
    M 9:4 ServoConfig.__init__ - A (1)
    M 16:4 ServoConfig.to_dict - A (1)
    M 26:4 ServoConfig.from_dict - A (1)
    M 59:4 Action.to_dict - A (1)
    M 68:4 Action.from_dict - A (1)
    M 80:4 RobotProfile.__init__ - A (1)
    M 146:4 RobotProfile.to_json - A (1)
    M 150:4 RobotProfile.load_from_json - A (1)
app\auto_farm\capture.py
    M 144:4 Capture._main - E (33)
    C 37:0 Capture - B (8)
    M 82:4 Capture._find_game_window - B (7)
    M 56:4 Capture.fps - A (3)
    M 65:4 Capture.start - A (2)
    M 74:4 Capture.stop - A (2)
    M 120:4 Capture._update_window_rect - A (2)
    M 40:4 Capture.__init__ - A (1)
app\auto_farm\controller.py
    M 662:4 AutoFarmController._solve_rune_process - F (43)
    M 469:4 AutoFarmController._monitor_loop - E (35)
    M 969:4 AutoFarmController._navigate_to - C (18)
    M 276:4 AutoFarmController._release_all_keys - C (12)
    C 73:0 AutoFarmController - B (9)
    M 134:4 AutoFarmController._focus_game_window - B (9)
    M 229:4 AutoFarmController._press_key - B (9)
    M 176:4 AutoFarmController._get_servo_index_for_key - B (8)
    M 315:4 AutoFarmController._key_down - B (6)
    M 336:4 AutoFarmController._key_up - B (6)
    M 376:4 AutoFarmController.play_alert - B (6)
    M 417:4 AutoFarmController._check_buff_active - B (6)
    M 256:4 AutoFarmController._send_puzzle_sequence - A (4)
    M 440:4 AutoFarmController._scan_for_rune - A (4)
    M 104:4 AutoFarmController.load_settings - A (3)
    M 196:4 AutoFarmController._hardware_key_down - A (3)
    M 208:4 AutoFarmController._hardware_key_up - A (3)
    M 76:4 AutoFarmController.__init__ - A (2)
    M 126:4 AutoFarmController.save_settings - A (2)
    M 220:4 AutoFarmController._hardware_press_key - A (2)
    M 357:4 AutoFarmController.start - A (2)
    M 367:4 AutoFarmController.stop - A (2)
    M 408:4 AutoFarmController.stop_alert - A (2)
app\auto_farm\utils.py
    F 54:0 match_score - B (6)
    F 32:0 multi_match - A (4)
    F 11:0 resolve_path - A (2)
    F 18:0 load_image - A (2)
    F 72:0 filter_color - A (2)
    F 27:0 distance - A (1)
app\auto_farm\vkeys.py
    F 156:0 key_down - B (8)
    F 180:0 key_up - B (7)
    F 119:4 _win32_send_input - A (5)
    F 203:0 press - A (5)
    F 36:0 _ensure_pynput - A (4)
    F 151:4 _win32_send_input - A (1)
    C 77:4 KeyboardInput - A (1)
    C 88:4 MouseInput - A (1)
    C 100:4 HardwareInput - A (1)
    C 109:4 InputUnion - A (1)
    C 114:4 Input - A (1)
app\auto_farm\rune_solver\data_vit.py
    F 13:0 build_transforms - A (2)
app\auto_farm\rune_solver\hybrid_solver.py
    M 70:4 HybridSolver.solve - C (20)
    C 19:0 HybridSolver - B (7)
    M 22:4 HybridSolver.__init__ - A (3)
    M 44:4 HybridSolver._get_transforms - A (2)
    M 52:4 HybridSolver._crop_box - A (1)
app\auto_farm\rune_solver\model_vit.py
    C 16:0 ArrowViT - A (3)
    M 19:4 ArrowViT.__init__ - A (3)
    M 44:4 ArrowViT.train - A (2)
    M 51:4 ArrowViT.forward - A (2)
app\auto_farm\rune_solver\panel_detect.py
    F 99:0 arrow_boxes_for - E (37)
    F 70:0 detect_right_endcap - B (6)
    F 39:0 detect_panel_origin - A (4)
app\auto_farm\rune_solver\roboflow_client.py
    M 65:4 RoboflowClient.infer - C (18)
    C 22:0 RoboflowClient - C (11)
    M 25:4 RoboflowClient.__init__ - C (11)
    M 57:4 RoboflowClient._encode - A (2)
app\auto_farm\rune_solver\solver.py
    C 27:0 RuneSolver - B (10)
    M 76:4 RuneSolver.solve - B (10)
    M 30:4 RuneSolver.__init__ - B (8)
app\auto_farm\rune_solver\vit_solver.py
    M 101:4 ViTSolver.solve - C (16)
    C 31:0 ViTSolver - A (5)
    M 78:4 ViTSolver._proportional_resize_center_crop - A (3)
    M 34:4 ViTSolver.__init__ - A (2)
    M 55:4 ViTSolver._crop_with_offset - A (1)
    M 65:4 ViTSolver._preprocess - A (1)
app\tabs\auto_farm.py
    M 497:4 AutoFarmTab.update_gui_loop - C (12)
    C 13:0 AutoFarmTab - A (3)
    M 16:4 AutoFarmTab.__init__ - A (2)
    M 575:4 AutoFarmTab.update_blink_dropdown_state - A (2)
    M 73:4 AutoFarmTab.create_left_card - A (1)
    M 326:4 AutoFarmTab.create_right_card - A (1)
    M 438:4 AutoFarmTab.get_display_jump_mode - A (1)
    M 447:4 AutoFarmTab.get_raw_jump_mode - A (1)
    M 456:4 AutoFarmTab.get_display_input_mode - A (1)
    M 461:4 AutoFarmTab.get_raw_input_mode - A (1)
    M 466:4 AutoFarmTab.save_settings_from_gui - A (1)
    M 482:4 AutoFarmTab.mute_siren - A (1)
    M 491:4 AutoFarmTab.trigger_recalibration - A (1)
    M 570:4 AutoFarmTab.on_jump_mode_changed - A (1)
    M 585:4 AutoFarmTab.reload_from_profile - A (1)
app\tabs\auto_farm_firmware.py
    M 330:4 FirmwareFlasherFrame.log_fw_message - C (14)
    M 256:4 FirmwareFlasherFrame.start_firmware_flash - B (10)
    M 218:4 FirmwareFlasherFrame.refresh_hex_files - B (7)
    C 10:0 FirmwareFlasherFrame - B (6)
    M 236:4 FirmwareFlasherFrame.browse_custom_hex - A (4)
    M 402:4 AutoFarmFirmwareTab.reload_from_profile - A (3)
    C 367:0 AutoFarmFirmwareTab - A (2)
    M 397:4 AutoFarmFirmwareTab.reload_table - A (2)
    M 13:4 FirmwareFlasherFrame.__init__ - A (1)
    M 353:4 FirmwareFlasherFrame.clear_fw_log - A (1)
    M 360:4 FirmwareFlasherFrame.copy_fw_log - A (1)
    M 370:4 AutoFarmFirmwareTab.__init__ - A (1)
    M 386:4 AutoFarmFirmwareTab.on_profile_updated - A (1)
    M 391:4 AutoFarmFirmwareTab.on_profile_updated - A (1)
app\tabs\calibration.py
    M 364:4 CalibrationTab.save_profile - D (24)
    M 459:4 CalibrationTab.save_profile_as - D (24)
    C 8:0 CalibrationTab - B (9)
    M 549:4 CalibrationTab.reload_from_profile - A (3)
    M 11:4 CalibrationTab.__init__ - A (2)
    M 343:4 CalibrationTab.update_profile_servo_angle - A (2)
    M 350:4 CalibrationTab.test_angle - A (1)
    M 355:4 CalibrationTab.run_test_sequence - A (1)
app\tabs\dashboard.py
    M 607:4 DashboardTab.log_message - C (15)
    M 638:4 DashboardTab.update_status_label - C (14)
    M 860:4 DashboardTab.query_rpc_balance - B (10)
    M 729:4 DashboardTab.update_hw_status_ui - B (8)
    M 117:4 DashboardTab.save_wallet_address - B (6)
    M 803:4 DashboardTab.toggle_connect - A (5)
    M 830:4 DashboardTab.update_timer_loop - A (5)
    M 941:4 DashboardTab.rpc_polling_loop - A (5)
    C 15:0 DashboardTab - A (4)
    M 691:4 DashboardTab.update_duration - A (4)
    M 707:4 DashboardTab.poll_usb_hardware - A (4)
    M 919:4 DashboardTab.refresh_balance_labels - A (4)
    M 105:4 DashboardTab.load_wallet_address - A (3)
    M 675:4 DashboardTab.update_log_loop - A (3)
    M 756:4 DashboardTab.check_connection_readiness - A (3)
    M 18:4 DashboardTab.__init__ - A (2)
    M 450:4 DashboardTab.update_ui_state_visibility - A (2)
    M 776:4 DashboardTab.trigger_driver_install - A (2)
    M 795:4 DashboardTab.refresh_ports - A (2)
    M 100:4 DashboardTab.destroy - A (1)
    M 145:4 DashboardTab.delete_wallet_address - A (1)
    M 151:4 DashboardTab.create_serial_card - A (1)
    M 238:4 DashboardTab.create_control_card - A (1)
    M 319:4 DashboardTab.create_wallet_card - A (1)
    M 463:4 DashboardTab.create_log_card - A (1)
    M 577:4 DashboardTab.start_pattern - A (1)
    M 581:4 DashboardTab.stop_pattern - A (1)
    M 585:4 DashboardTab.estop - A (1)
    M 590:4 DashboardTab.check_status - A (1)
    M 594:4 DashboardTab.clear_log - A (1)
    M 601:4 DashboardTab.copy_log - A (1)
    M 683:4 DashboardTab.reload_table - A (1)
    M 687:4 DashboardTab.reload_from_profile - A (1)
    M 826:4 DashboardTab.trigger_rpc_fetch - A (1)
app\tabs\pattern.py
    M 379:4 PatternEditorFrame.save_profile - D (25)
    M 516:4 PatternBuilderTab.reload_from_profile - B (7)
    C 11:0 PatternEditorFrame - A (5)
    M 246:4 PatternEditorFrame.update_duration_estimation - A (4)
    M 321:4 PatternEditorFrame.delete_action - A (4)
    C 474:0 PatternBuilderTab - A (4)
    M 507:4 PatternBuilderTab.reload_table - A (4)
    M 266:4 PatternEditorFrame.reload_table - A (3)
    M 291:4 PatternEditorFrame.on_fields_changed - A (3)
    M 349:4 PatternEditorFrame.move_up - A (3)
    M 364:4 PatternEditorFrame.move_down - A (3)
    M 280:4 PatternEditorFrame.on_select - A (2)
    M 337:4 PatternEditorFrame.duplicate_action - A (2)
    M 14:4 PatternEditorFrame.__init__ - A (1)
    M 312:4 PatternEditorFrame.add_action - A (1)
    M 477:4 PatternBuilderTab.__init__ - A (1)
    M 495:4 PatternBuilderTab.on_profile_updated - A (1)
    M 500:4 PatternBuilderTab.on_profile_updated - A (1)
app\tabs\profiles.py
    M 503:4 ProfileManagerTab.upload_config - B (9)
    M 557:4 ProfileManagerTab.read_config - A (5)
    M 594:4 ProfileManagerTab._poll_config_response - A (4)
    C 10:0 ProfileManagerTab - A (3)
    M 440:4 ProfileManagerTab.export_json - A (3)
    M 462:4 ProfileManagerTab.import_json - A (3)
    M 487:4 ProfileManagerTab.apply_json_preview - A (2)
    M 13:4 ProfileManagerTab.__init__ - A (1)
    M 405:4 ProfileManagerTab.log_activity - A (1)
    M 416:4 ProfileManagerTab.clear_log - A (1)
    M 426:4 ProfileManagerTab.reload_from_profile - A (1)
    M 431:4 ProfileManagerTab.copy_json - A (1)
    M 643:4 ProfileManagerTab.save_profile - A (1)
    M 647:4 ProfileManagerTab.load_profile - A (1)
    M 651:4 ProfileManagerTab.toggle_json_preview - A (1)
    M 655:4 ProfileManagerTab.hide_json_preview - A (1)
app\tabs\recorder.py
    M 781:4 RecorderTab.save_to_profile - D (26)
    M 592:4 RecorderTab.on_global_key_event - D (22)
    M 485:4 RecorderTab.on_key_press - C (16)
    M 544:4 RecorderTab.on_key_release - B (10)
    M 997:4 RecorderTab.draw_hud - B (9)
    M 403:4 RecorderTab.toggle_recording - B (8)
    C 18:0 RecorderTab - B (6)
    M 322:4 RecorderTab.update_global_mode_ui_state - A (3)
    M 463:4 RecorderTab.on_focus_click - A (3)
    M 474:4 RecorderTab.on_focus_lost - A (3)
    M 694:4 RecorderTab._do_reload_table - A (3)
    M 707:4 RecorderTab.reload_table - A (3)
    M 734:4 RecorderTab.on_field_edited - A (3)
    M 755:4 RecorderTab.delete_selected_row - A (3)
    M 769:4 RecorderTab.clear_recording - A (3)
    M 364:4 RecorderTab.run_keyboard_install_thread - A (2)
    M 382:4 RecorderTab.finish_keyboard_installation - A (2)
    M 452:4 RecorderTab.update_rec_ui_button_style - A (2)
    M 688:4 RecorderTab.schedule_reload_table - A (2)
    M 722:4 RecorderTab.on_row_select - A (2)
    M 881:4 RecorderTab.open_json_editor - A (2)
    M 21:4 RecorderTab.__init__ - A (1)
    M 347:4 RecorderTab.on_toggle_global_checkbox - A (1)
    M 351:4 RecorderTab.start_keyboard_installation - A (1)
    M 1091:4 RecorderTab.reload_from_profile - A (1)
app\tabs\robot_settings.py
    M 602:4 TimingSettingsFrame.save_blink_config - D (21)
    M 1036:4 RobotSettingsTab.reload_from_profile - B (7)
    M 107:4 TimingSettingsFrame.on_loop_count_write - A (5)
    M 129:4 TimingSettingsFrame.on_random_min_write - A (5)
    M 153:4 TimingSettingsFrame.on_random_max_write - A (5)
    M 444:4 TimingSettingsFrame.on_toggle_random_enabled - A (5)
    M 898:4 TimingSettingsFrame.run_loop_simulation - A (5)
    M 934:4 TimingSettingsFrame.run_random_simulation - A (5)
    C 12:0 TimingSettingsFrame - A (4)
    M 178:4 TimingSettingsFrame.on_blink_init_write - A (4)
    M 199:4 TimingSettingsFrame.on_blink_hold_write - A (4)
    M 220:4 TimingSettingsFrame.on_blink_release_write - A (4)
    M 957:4 TimingSettingsFrame.run_test_blink - A (4)
    C 994:0 RobotSettingsTab - A (4)
    M 1027:4 RobotSettingsTab.reload_table - A (4)
    M 15:4 TimingSettingsFrame.__init__ - A (2)
    M 99:4 TimingSettingsFrame.on_scale_scroll - A (2)
    M 326:4 TimingSettingsFrame.on_mode_change - A (2)
    M 242:4 TimingSettingsFrame.create_loop_card - A (1)
    M 343:4 TimingSettingsFrame.on_autostart_change - A (1)
    M 348:4 TimingSettingsFrame.create_random_delay_card - A (1)
    M 460:4 TimingSettingsFrame.on_toggle_random_skip - A (1)
    M 465:4 TimingSettingsFrame.create_blink_timing_card - A (1)
    M 593:4 TimingSettingsFrame.update_blink_flow_label - A (1)
    M 685:4 TimingSettingsFrame.create_testing_card - A (1)
    M 889:4 TimingSettingsFrame.log_sim - A (1)
    M 975:4 TimingSettingsFrame.reload_from_profile - A (1)
    M 997:4 RobotSettingsTab.__init__ - A (1)
    M 1015:4 RobotSettingsTab.on_profile_updated - A (1)
    M 1020:4 RobotSettingsTab.on_profile_updated - A (1)
app\tabs\simulation.py
    M 387:4 SimulationTab.draw_arena - C (13)
    M 480:4 SimulationTab.on_key_release - B (10)
    M 540:4 SimulationTab.trace_log - B (10)
    M 459:4 SimulationTab.on_key_press - B (9)
    C 8:0 SimulationTab - B (7)
    M 559:4 SimulationTab.run_next_step - B (7)
    M 11:4 SimulationTab.__init__ - A (4)
    M 504:4 SimulationTab.toggle_simulation - A (2)
    M 511:4 SimulationTab.start_simulation - A (2)
    M 526:4 SimulationTab.stop_simulation - A (2)
app\tabs\tester.py
    M 405:4 KeyboardTesterTab.on_key_release - C (12)
    C 7:0 KeyboardTesterTab - B (10)
    M 288:4 KeyboardTesterTab.draw_keys - B (10)
    M 376:4 KeyboardTesterTab.on_key_press - B (10)
    M 10:4 KeyboardTesterTab.__init__ - B (8)
    M 438:4 KeyboardTesterTab.toggle_tester_state - B (6)
app\tabs\validator.py
    F 9:0 validate_profile - D (28)
    M 294:4 ValidatorTab.run_validation - B (7)
    C 127:0 ValidatorTab - A (3)
    M 130:4 ValidatorTab.__init__ - A (1)
    M 278:4 ValidatorTab.clear_log - A (1)
    M 285:4 ValidatorTab.copy_log - A (1)
dist\lg_audio_helper_app\_internal\cv2\load_config_py3.py
    F 7:4 exec_file_wrapper - A (1)
dist\lg_audio_helper_app\_internal\cv2\__init__.py
    F 71:0 bootstrap - D (30)
    F 23:0 __load_extra_py_code_for_module - B (7)
    F 50:0 __collect_extra_submodules - A (3)
dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py
    C 54:0 GOpaque - A (2)
    C 147:0 GArray - A (2)
    F 8:0 register - A (1)
    F 18:0 networks - A (1)
    F 24:0 compile_args - A (1)
    F 30:0 GIn - A (1)
    F 36:0 GOut - A (1)
    F 42:0 gin - A (1)
    F 48:0 descr_of - A (1)
    F 259:0 op - A (1)
    F 390:0 kernel - A (1)
    M 58:4 GOpaque.__new__ - A (1)
    M 151:4 GArray.__new__ - A (1)
dist\lg_audio_helper_app\_internal\cv2\mat_wrapper\__init__.py
    C 16:0 Mat - A (3)
    M 29:4 Mat.__init__ - A (2)
    M 35:4 Mat.__array_finalize__ - A (2)
    M 24:4 Mat.__new__ - A (1)
dist\lg_audio_helper_app\_internal\cv2\misc\version.py
    F 5:0 get_ocv_version - A (1)
dist\lg_audio_helper_app\_internal\cv2\utils\__init__.py
    F 11:0 testOverwriteNativeMethod - A (1)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\load_config_py3.py
    F 7:4 exec_file_wrapper - A (1)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py
    F 71:0 bootstrap - D (30)
    F 23:0 __load_extra_py_code_for_module - B (7)
    F 50:0 __collect_extra_submodules - A (3)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py
    C 54:0 GOpaque - A (2)
    C 147:0 GArray - A (2)
    F 8:0 register - A (1)
    F 18:0 networks - A (1)
    F 24:0 compile_args - A (1)
    F 30:0 GIn - A (1)
    F 36:0 GOut - A (1)
    F 42:0 gin - A (1)
    F 48:0 descr_of - A (1)
    F 259:0 op - A (1)
    F 390:0 kernel - A (1)
    M 58:4 GOpaque.__new__ - A (1)
    M 151:4 GArray.__new__ - A (1)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\mat_wrapper\__init__.py
    C 16:0 Mat - A (3)
    M 29:4 Mat.__init__ - A (2)
    M 35:4 Mat.__array_finalize__ - A (2)
    M 24:4 Mat.__new__ - A (1)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\misc\version.py
    F 5:0 get_ocv_version - A (1)
dist\NanoKeyboardControllerLiteApp\_internal\cv2\utils\__init__.py
    F 11:0 testOverwriteNativeMethod - A (1)
scratch\analyze_panel_pixels.py
    F 7:0 main - A (5)
scratch\analyze_resizing.py
    F 18:0 main - A (2)
scratch\check_actual_right_endcap.py
    F 7:0 main - A (3)
scratch\check_dist.py
    F 6:0 main - B (7)
scratch\check_interpolated_crops.py
    F 6:0 main - A (3)
scratch\check_spec_error.py
    C 36:0 MockAnalysis - A (2)
    M 39:4 MockAnalysis.__init__ - A (1)
scratch\check_template_layout.py
    F 7:0 main - A (2)
scratch\compare_pixels.py
    F 7:0 main - A (1)
scratch\crop_possible_arrows.py
    F 7:0 main - A (3)
scratch\debug_build.py
    F 9:0 custom_collect - B (8)
scratch\debug_panel_detail.py
    F 16:0 main - C (20)
scratch\detect_arrow_centers_by_color.py
    F 7:0 main - B (6)
scratch\find_arrows_fullframe.py
    F 7:0 main - B (7)
scratch\find_panel_scale.py
    F 7:0 main - A (5)
scratch\find_perfect_scale.py
    F 7:0 main - C (11)
scratch\find_right_matches.py
    F 7:0 main - B (8)
scratch\inspect_matches.py
    F 7:0 main - A (2)
scratch\overlay_detected_centers.py
    F 7:0 main - A (3)
scratch\test_colorkey_theme.py
    C 10:0 TestApp - A (2)
    M 13:4 TestApp.__init__ - A (1)
    M 91:4 TestApp.take_screenshot - A (1)
scratch\test_colorkey_transparency.py
    C 10:0 TestApp - A (2)
    M 13:4 TestApp.__init__ - A (1)
    M 58:4 TestApp.take_screenshot - A (1)
scratch\test_color_vit.py
    F 11:0 main - B (6)
scratch\test_crops_with_vit.py
    F 16:0 main - A (2)
scratch\test_full_pipeline_fix.py
    F 74:0 find_best_4_arrows - C (13)
    F 104:0 main - C (12)
    F 36:0 detect_arrows_by_color - B (9)
    F 19:0 proportional_resize_center_crop - A (3)
scratch\test_interpolation_vit.py
    F 10:0 main - C (13)
scratch\test_main_app_screenshot.py
    C 17:0 AutomatedScreenshotApp - A (2)
    M 20:4 AutomatedScreenshotApp.__init__ - A (1)
    M 26:4 AutomatedScreenshotApp.navigate_and_screenshot - A (1)
    M 35:4 AutomatedScreenshotApp.capture - A (1)
scratch\test_opacity.py
    C 9:0 TestApp - A (2)
    M 12:4 TestApp.__init__ - A (1)
scratch\test_opacity_notebook.py
    C 11:0 TestApp - A (2)
    M 14:4 TestApp.__init__ - A (1)
    M 79:4 TestApp.take_screenshot - A (1)
scratch\test_opacity_screenshot.py
    C 11:0 TestApp - A (2)
    M 14:4 TestApp.__init__ - A (1)
    M 56:4 TestApp.take_screenshot - A (1)
scratch\test_proportional_fix.py
    F 37:0 main - C (12)
    F 16:0 proportional_resize_center_crop - A (3)
scratch\test_proportional_resize.py
    F 16:0 main - D (24)
scratch\test_prop_scaling.py
    F 7:0 main - A (3)
scratch\test_robust_color_detect.py
    F 7:0 main - D (22)
scratch\test_robust_solver.py
    F 11:0 main - D (21)
scratch\test_sidebar_transparency.py
    M 20:4 AutomatedSidebarTest.__init__ - A (5)
    C 17:0 AutomatedSidebarTest - A (4)
    M 35:4 AutomatedSidebarTest.capture - A (1)
scratch\test_vit_filtering.py
    F 16:0 main - C (13)
scratch\test_vit_filtering_fixed.py
    F 16:0 main - C (14)
scratch\test_widget_opacity.py
    C 10:0 TestApp - A (2)
    M 13:4 TestApp.__init__ - A (1)
    M 47:4 TestApp.take_screenshot - A (1)
scratch\try_delete_files.py
    F 6:0 main - A (4)
scratch\visualize_crop.py
    F 7:0 main - B (6)
scratch\visualize_matches.py
    F 7:0 main - B (8)

443 blocks (classes, functions, methods) analyzed.
Average complexity: A (4.625282167042889)


## Duplicate Code Detection

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\connection.py :: send_command
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\connection.py :: send_command_chunked

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\main.py :: __init__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\main.py :: load_image

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\auto_farm.py :: __init__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\auto_farm_firmware.py :: __init__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\calibration.py :: __init__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\pattern.py :: __init__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\pattern.py :: __init__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\recorder.py :: __init__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\robot_settings.py :: __init__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\robot_settings.py :: __init__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\simulation.py :: __init__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\tester.py :: __init__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\validator.py :: __init__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\auto_farm_firmware.py :: on_profile_updated
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\pattern.py :: on_profile_updated
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\robot_settings.py :: on_profile_updated

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\calibration.py :: save_profile
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\calibration.py :: save_profile_as

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\dashboard.py :: reload_table
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\dashboard.py :: reload_from_profile

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\profiles.py :: log_activity
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\simulation.py :: trace_log

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\profiles.py :: toggle_json_preview
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\profiles.py :: hide_json_preview

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\recorder.py :: on_key_press
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\recorder.py :: on_key_release

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\recorder.py :: on_row_select
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\recorder.py :: on_field_edited

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\tester.py :: on_key_press
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\tester.py :: on_key_release

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\load_config_py3.py :: exec_file_wrapper
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\load_config_py3.py :: exec_file_wrapper

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\__init__.py :: __load_extra_py_code_for_module
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py :: __load_extra_py_code_for_module

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\__init__.py :: __collect_extra_submodules
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py :: __collect_extra_submodules

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\__init__.py :: modules_filter
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py :: modules_filter

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\__init__.py :: bootstrap
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py :: bootstrap

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\__init__.py :: load_first_config
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\__init__.py :: load_first_config

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: register
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: register

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: parameterized
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: parameterized

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: networks
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: networks

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: compile_args
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: compile_args

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: GIn
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: GOut
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: gin
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: descr_of
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: GIn
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: GOut
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: gin
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: descr_of

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: op
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: op

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: op_with_params
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: op_with_params

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: on
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: on

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: kernel
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: kernel

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\gapi\__init__.py :: kernel_with_params
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\gapi\__init__.py :: kernel_with_params

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\mat_wrapper\__init__.py :: __new__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\mat_wrapper\__init__.py :: __new__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\mat_wrapper\__init__.py :: __init__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\mat_wrapper\__init__.py :: __init__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\mat_wrapper\__init__.py :: __array_finalize__
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\mat_wrapper\__init__.py :: __array_finalize__

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\misc\version.py :: get_ocv_version
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\misc\version.py :: get_ocv_version

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\lg_audio_helper_app\_internal\cv2\utils\__init__.py :: testOverwriteNativeMethod
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\dist\NanoKeyboardControllerLiteApp\_internal\cv2\utils\__init__.py :: testOverwriteNativeMethod

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\scratch\analyze_panel_pixels.py :: main
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\scratch\crop_possible_arrows.py :: main

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\scratch\check_actual_right_endcap.py :: main
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\scratch\check_interpolated_crops.py :: main
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\scratch\detect_arrow_centers_by_color.py :: main
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\scratch\overlay_detected_centers.py :: main

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\scratch\find_arrows_fullframe.py :: main
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\scratch\visualize_crop.py :: main

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\scratch\find_right_matches.py :: main
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\scratch\inspect_matches.py :: main
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\scratch\visualize_matches.py :: main

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\scratch\test_colorkey_theme.py :: take_screenshot
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\scratch\test_colorkey_transparency.py :: take_screenshot
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\scratch\test_opacity_notebook.py :: take_screenshot
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\scratch\test_widget_opacity.py :: take_screenshot

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\scratch\test_interpolation_vit.py :: main
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\scratch\test_robust_solver.py :: main

Duplicate functions detected:
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\scratch\test_proportional_resize.py :: main
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\scratch\test_prop_scaling.py :: main
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\scratch\test_robust_color_detect.py :: main
- C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\scratch\test_vit_filtering_fixed.py :: main



## Anti‑Cheat Safety Assessment

C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\audit_report.py: imports or uses `pyautogui`
C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\audit_report.py: imports or uses `pynput`
C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\audit_report.py: imports or uses `ctypes`
C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\audit_report.py: imports or uses `win32api`
C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\audit_report.py: imports or uses `win32gui`
C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\audit_report.py: imports or uses `win32con`
C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\audit_report.py: imports or uses `keyboard`
C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\audit_report.py: imports or uses `mouse`
C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\audit_report.py: imports or uses `pydirectinput`
C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\debug_minimap_capture.py: imports or uses `ctypes`
C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\debug_minimap_capture.py: imports or uses `win32gui`
C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\main.py: imports or uses `ctypes`
C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\auto_farm\capture.py: imports or uses `ctypes`
C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\auto_farm\capture.py: imports or uses `win32gui`
C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\auto_farm\controller.py: imports or uses `pynput`
C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\auto_farm\controller.py: imports or uses `win32api`
C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\auto_farm\controller.py: imports or uses `win32gui`
C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\auto_farm\controller.py: imports or uses `win32con`
C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\auto_farm\vkeys.py: imports or uses `pynput`
C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\auto_farm\vkeys.py: imports or uses `ctypes`
C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\auto_farm\vkeys.py: imports or uses `keyboard`
C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\auto_farm\vkeys.py: imports or uses `mouse`
C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\auto_farm.py: imports or uses `pynput`
C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\recorder.py: imports or uses `keyboard`
C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\simulation.py: imports or uses `keyboard`
C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie\app\tabs\tester.py: imports or uses `keyboard`