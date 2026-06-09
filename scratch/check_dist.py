"""TODO: module documentation"""

import os


def main():
    """TODO: add documentation"""
    dist_dir = "c:/Users/Admin/Downloads/AutoFarmMaple/NanoKeyboardControllerLite/dist"
    if not os.path.exists(dist_dir):
        print(f"Dist dir {dist_dir} does not exist")
        return

    print(f"Contents of {dist_dir}:")
    for item in os.listdir(dist_dir):
        path = os.path.join(dist_dir, item)
        is_dir = os.path.isdir(path)
        print(f" - {item} ({'dir' if is_dir else 'file'})")
        if is_dir and item.startswith("NanoKeyboardControllerLite"):
            print(f"   Contents of {item}:")
            for sub in os.listdir(path):
                print(f"     - {sub}")


if __name__ == "__main__":
    main()
