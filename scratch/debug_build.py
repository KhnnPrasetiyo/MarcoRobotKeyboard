"""TODO: module documentation"""

import sys

import PyInstaller.building.api
from PyInstaller.building.api import COLLECT


def custom_collect(*args, **kwargs):
    """TODO: add documentation"""
    print("\n==================================================")
    print("INTERCEPTED COLLECT CALL")
    print("==================================================")
    for idx, arg in enumerate(args):
        print(f"Arg {idx} type: {type(arg)}")
        if isinstance(arg, list):
            print(f"  Length: {len(arg)}")
            bad_count = 0
            for item_idx, item in enumerate(arg):
                if not isinstance(item, tuple) or len(item) != 3:
                    print(
                        f"  [BAD ITEM] at index {item_idx}: {item} (type={type(item)}, len={len(item) if hasattr(item, '__len__') else 'N/A'})"
                    )
                    bad_count += 1
            if bad_count == 0:
                print("  All items in this list are valid 3-tuples.")
    print("==================================================\n")
    return COLLECT(*args, **kwargs)


PyInstaller.building.api.COLLECT = custom_collect

import PyInstaller.__main__

PyInstaller.__main__.run(["--noconfirm", "NanoKeyboardControllerLite.spec"])
