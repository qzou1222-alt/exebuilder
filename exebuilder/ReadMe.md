# exebuilder

Simple EXE builder for Python files.

## Install

```bash
pip install exebuilder
```

---

## Usage

### Build EXE

```python
from exebuilder import build

build("main.py")
```

creates:

```text
dist/main.exe
```

---

### Run as EXE

```python
from exebuilder import runasexe

runasexe("main.py")
```

Runs the Python file as a temporary EXE.

---

## CLI

```bash
python exebuilder my_file.py
```

creates:

```text
dist/main.exe
```

---

## Example

```python
from exebuilder import build, runasexe

build("game.py")

runasexe("tool.py")
```