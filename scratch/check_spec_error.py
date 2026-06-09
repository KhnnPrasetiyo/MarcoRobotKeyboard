"""TODO: module documentation"""

import glob
import os

# Copy the spec file logic to see what's causing the ValueError
datas = []
datas.append(("app/bin/avrdude.exe", "app/bin"))
datas.append(("app/bin/avrdude.conf", "app/bin"))

for hex_file in glob.glob("firmware/*.hex"):
    datas.append((hex_file, "firmware"))

for item in glob.glob("assets/*"):
    if os.path.isdir(item):
        if os.path.basename(item) == "models":
            for model_file in glob.glob("assets/models/*"):
                datas.append((model_file, "assets/models"))
        elif os.path.basename(item) == "alerts":
            for alert_file in glob.glob("assets/alerts/*"):
                datas.append((alert_file, "assets/alerts"))
    else:
        fname = os.path.basename(item)
        if fname.endswith("_old.png") or fname.endswith("_original.jpg"):
            continue
        datas.append((item, "assets"))

# Let's print the first few datas to check
print("First 5 datas:", datas[:5])
for d in datas:
    if len(d) != 2:
        print("Invalid data item (not 2-tuple):", d)


# Mock PyInstaller classes to trace Analysis
class MockAnalysis:
    """TODO: add documentation"""

    def __init__(self, *args, **kwargs):
        """TODO: add documentation"""
        self.datas = kwargs.get("datas", [])
        self.binaries = kwargs.get("binaries", [])


# Since we don't have the full PyInstaller Analysis class mock, let's run PyInstaller's Analysis
# by importing it and running it on our spec file.
try:
    from PyInstaller.building.build_main import Analysis

    print("Successfully imported PyInstaller Analysis.")

    a = Analysis(
        ["app/main.py"],
        pathex=[],
        binaries=[],
        datas=datas,
        excludes=[
            "torch",
            "torchvision",
            "timm",
            "sympy",
            "networkx",
            "mpmath",
            "fsspec",
            "safetensors",
            "huggingface_hub",
            "reportlab",
            "GitPython",
            "git",
            "sqlite3",
            "vtk",
            "trame",
            "trame_client",
            "trame_server",
            "trame_vuetify",
            "trame_common",
            "trame_components",
            "trame_vtk",
            "wslink",
            "cadquery",
            "ezdxf",
            "casadi",
            "nlopt",
            "matplotlib",
            "contourpy",
            "fonttools",
            "pytest",
            "win32ui",
            "Pythonwin",
        ],
    )

    print("Analysis finished.")
    print("Checking a.binaries elements...")
    bad_binaries = [x for x in a.binaries if len(x) != 3]
    print(f"Number of bad binaries: {len(bad_binaries)}")
    if bad_binaries:
        print("Bad binaries:", bad_binaries[:5])

    print("Checking a.datas elements...")
    bad_datas = [x for x in a.datas if len(x) != 3]
    print(f"Number of bad datas: {len(bad_datas)}")
    if bad_datas:
        print("Bad datas:", bad_datas[:5])

except Exception as e:
    print("Error during test:", e)
