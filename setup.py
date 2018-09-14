from cx_Freeze import setup, Executable
import os
import os.path
import sys


base = None

executables = [Executable("main.py", base=base)]

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

packages = ['numpy', 'numpy.core._methods', 'numpy.lib.format', 'tkinter']
excludes = ['IPython', 'OpenGL', 'asyncio', 'curses',
    'ipykernel', 'ipython_genutils',
    'jedi', 'jinja2', 'jsonschema', 'jupyter_client', 'jupyter_core',
    'lib2to3', 'markupsafe', 'matplotlib', 'notebook', 'pydoc_data', 'pyreadline',
    'pygame', 'pygments', 'pytz', 'requests', 'setuptools', 'testpath'
    'tkinter', 'tornado', 'traitlets', 'wcwidth', 'lxml', 'unittest'
    'distutils', 'multiprocessing', 'nose']

options = {
    'build_exe': {
        'include_files':[
                os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
                os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
        ],
        'packages': packages,
        'excludes': excludes,
    },
}

setup(
    name = "Fiere",
    options = options,
    version = "9.0.1",
    description = 'RPG Companion',
    executables = executables
)
