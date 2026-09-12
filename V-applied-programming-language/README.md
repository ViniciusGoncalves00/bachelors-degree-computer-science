#### Applied Programming Language

Assignments, exercises, and other materials related to the Applied Programming Language course.

# Breakout Game

A simple Breakout / Arkanoid-style game built with Python and PyGame.

# Installation

## 1. Clone the repository

```bash
git clone <repository-url>
cd breakout-game
```

---

## 2. Create virtual environment

```bash
uv venv
```

---

## 3. Activate environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## 4. Install dependencies

```bash
uv sync
```

---

# Running the Game

```bash
uv run python main.py
```

---

# Build Executable (.exe)

Install PyInstaller:

```bash
uv add --dev pyinstaller
```

Build:

```bash
uv run pyinstaller --onefile --noconsole --clean -n breakout main.py
```

Executable output:

```text
dist/breakout.exe
```

---
