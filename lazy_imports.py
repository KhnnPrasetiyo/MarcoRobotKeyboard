# lazy_imports.py
"""Utility module providing a lazy import helper.
It allows importing heavy or suspicious modules only when they are actually used,
thereby reducing their presence in the process import table at startup.
"""

import importlib
import sys


def lazy_import(module_name: str):
    """Return the imported module, loading it on first call.
    Subsequent calls will return the cached module from sys.modules.
    """
    if module_name in sys.modules:
        return sys.modules[module_name]
    return importlib.import_module(module_name)
