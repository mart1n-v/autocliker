# Autoclicker

[![Latest Release](https://img.shields.io/github/v/release/mart1n-v/autocliker)](https://github.com/mart1n-v/autocliker/releases)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.13.2-blue.svg)](https://www.python.org/)
[![Issues](https://img.shields.io/github/issues/mart1n-v/autocliker)](https://github.com/mart1n-v/autocliker/issues)
[![Stars](https://img.shields.io/github/stars/mart1n-v/autocliker)](https://github.com/mart1n-v/autocliker/stargazers)

**Auto Key Presser** is a minimal Python tool with a GUI that repeatedly presses the **E** key at a custom interval. Great for games, testing, or any scenario where holding down a key just isn’t enough.

---

## Features

- **Presses the 'E' Key Automatically** – Because pressing it manually is so 2024.
- **Customizable Interval** – Set the delay between presses from 0.01 to 10 seconds.
- **Hotkey Toggle** – Hit **Ctrl+Shift+E** globally to start or stop without clicking the window.
- **Simple GUI** – Just a window with Start, Stop, Exit, and a box to set the interval.
- **Threaded Execution** – Keeps things running smoothly without freezing the interface.
- **Cross-Platform-ish** – Works on Windows and may work on Linux with the right permissions (note: `keyboard` library may need sudo).

---

## Installation

### Download the [latest release](https://github.com/mart1n-v/autocliker/releases)

### Or run the python file
```bash
git clone https://github.com/mart1n-v/autocliker.git
cd autocliker
pip install keyboard
python main.py
```