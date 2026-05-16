"""
Build EXE files from Python files. (v0.3.1)

Contents Updated!
=================

Fixed some module install bug.

Exebuilder
==========

CLI
---

exebuilder <file> [--quiet]
Build a Python file into an EXE using PyInstaller.

API
---

- build(file, prt=True)
  Build an EXE from a Python file.

- runasexe(file, prt=True)
  Build a temporary EXE and execute it immediately.

Utilities
---------

- is_pyfile(file)
  Check whether a file is a Python file.

- Warnings
  Built-in warning messages.
"""
from pathlib import Path as _P
__version__ = "0.3.1"
def is_pyfile(file:str|_P) -> bool:
    '''Return whether a file is a Python file.'''
    if isinstance(file,_P):
        file=file.name
    return file.endswith('.py')
class _Warnings:
    def __init__(self):
        self.warns:dict[int,str]=dict()
        self._private=False
    def __init_subclass__(cls):
        raise TypeError("[exebuilder._Warnings] cannot be subclass")
    def __setitem__(self, warnindex:int, warn:str):
        if not self._private:
            self.warns[warnindex]=warn
    def __getitem__(self, warnindex:int):
        return self.warns[warnindex]
Warnings=_Warnings()
'''Exebuilder's warnings. Use Warnings[index] to get it.'''
Warnings[1]="[exebuilder] only supports python file"
Warnings[2]="something wrong when [exebuilder] building"
def runasexe(pyfile: str | _P, prt:bool=True):
    """Build and run a temporary EXE from a Python file."""
    from tempfile import TemporaryDirectory
    import subprocess
    with TemporaryDirectory() as temp:
        temp = _P(temp)
        try:
            subprocess.run([
                "pyinstaller",
                "--onefile",
                "--distpath", str(temp),
                "--workpath", str(temp),
                "--specpath", str(temp),
                str(pyfile)
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
            )
        except subprocess.CalledProcessError:
            if prt:
                print(f"Running failed: {Warnings[2]}")
            return False
        exe = temp / f"{_P(pyfile).stem}.exe"
        subprocess.run([str(exe)])
    return True
def build(pyfile:str|_P, prt:bool=True) -> bool:
    '''Build an EXE from a python file. Prt controls whether messages are printed in the terminal.'''
    import subprocess
    import sys
    if isinstance(pyfile, _P):
        pyfile=str(pyfile)
    if not is_pyfile(pyfile):
        if prt:
            print(f"build failed: {Warnings[1]}")
        return False
    try:
        subprocess.run([
            sys.executable, "-m", "PyInstaller",
            "--onefile",
            pyfile,
        ],check=True,
        stdout=subprocess.DEVNULL if not prt else None)
    except subprocess.CalledProcessError:
        if prt:
            print(f"build failed: {Warnings[2]}")
        return False
    if prt:
        print("Building success")
    return True
Warnings._private=True