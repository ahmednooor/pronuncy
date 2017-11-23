import sys, os
from cx_Freeze import setup, Executable

os.environ["TCL_LIBRARY"] = "<path/to/your/python/>/tcl/tcl8.6"
os.environ["TK_LIBRARY"] = "<path/to/your/python/>/tcl/tk8.6"

base = None
include_files = [
    "./assets",
    "<path/to/your/python/>/DLLs/tcl86t.dll",
    "<path/to/your/python/>/DLLs/tk86t.dll"
]

if sys.platform == "win32":
    base = "Win32GUI"

setup(name = "pronuncy",
    version = "1.0",
    description = "English Pronunciation App",
    options = {
        "build_exe" : {
            "packages": ["pygame"],
            "include_files" : include_files
            }
    },
    executables = [Executable("pronuncy.py", base=base, targetName="pronuncy.exe", icon="./assets/media/favicon.ico")]
)
