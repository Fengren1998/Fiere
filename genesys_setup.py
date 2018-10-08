from cx_Freeze import setup, Executable
import os
import os.path
import sys


base = None

executables = [Executable("genesysUI.py", base=base)]

packages = ['tkinter', 'random', 'PIL']
excludes = []

options = {
    'build_exe': {
        'packages': packages,
        'excludes': excludes,
    },
}

setup(
    name = "Genesys",
    options = options,
    version = "1",
    description = 'RPG Companion',
    executables = executables
)
