"""TODO: module documentation"""

import os


def main():
    """TODO: add documentation"""
    folder = "c:/Users/Admin/Downloads/AutoFarmMaple/NanoKeyboardControllerLite/dist/NanoKeyboardControllerLite/debug_rune_last"
    if not os.path.exists(folder):
        print("Folder does not exist")
        return

    for item in os.listdir(folder):
        path = os.path.join(folder, item)
        try:
            os.remove(path)
            print(f"Successfully deleted {item}")
        except Exception as e:
            print(f"Failed to delete {item}: {e}")


if __name__ == "__main__":
    main()
