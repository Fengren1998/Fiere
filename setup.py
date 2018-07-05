from cx_Freeze import setup, Executable

base = None

executables = [Executable("main.py", base=base)]

'''
Important
1. xml
2. urllib
'''
'''excludes = ['IPython', 'OpenGL', 'asyncio', 'colorama', 'curses',
    'html', 'ipykernel', 'ipython_genutils',
    'jedi', 'jinja2', 'json', 'jsonschema', 'jupyter_client', 'jupyter_core',
    'lib2to3', 'logging', 'markupsafe', 'matplotlib', 'nose', 'notebook',
    'pygame', 'pygments', 'pytz', 'requests', 'setuptools', 'sqlite3', 'testpath',
    'tkinter', 'tornado', 'traitlets', 'wcwidth', 'lxml', 'zmq']'''
packages = ['numpy', 'numpy.core._methods', 'numpy.lib.format']
excludes = ['IPython', 'OpenGL', 'asyncio', 'curses',
    'ipykernel', 'ipython_genutils',
    'jedi', 'jinja2', 'jsonschema', 'jupyter_client', 'jupyter_core',
    'lib2to3', 'markupsafe', 'matplotlib', 'notebook', 'pydoc_data', 'pyreadline',
    'pygame', 'pygments', 'pytz', 'requests', 'setuptools', 'testpath'
    'tkinter', 'tornado', 'traitlets', 'wcwidth', 'lxml', 'unittest'
    'distutils', 'multiprocessing', 'nose']

options = {
    'build_exe': {
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
