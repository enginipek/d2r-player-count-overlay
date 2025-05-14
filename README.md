# Diablo II Players Overlay

A lightweight always-on-top overlay for Diablo II that displays the current `/players X` setting.
Supports input via typing or pasting the `/players X` command.

## Features

- Displays current `/players` setting (1–8)
- Detects both typed and pasted commands (e.g., `/players 5`)
- Always-on-top overlay window
- Sleek UI with auto-hide close button on mouse hover
- Minimal CPU and memory usage

## Usage

1. Run the script below or the compiled `.exe`.
```bash
python overlay.py
```
2. In Diablo II, either:
   - Type `/players X` and press `Enter`
   - Paste `/players X`, optionally edit the number, and press `Enter`
3. The overlay updates with the correct number

## Example

```
/players 8
```

## Dependencies

- `tkinter`
- `keyboard`
- `pyperclip`
- `pyinstaller` (optional for building EXE file)

Install them via:

```bash
pip install keyboard pyperclip
```

## Build EXE (Optional)

If you want to build an executable using `pyinstaller`:

```bash
pyinstaller --onefile --windowed players_overlay.py
```

## License

MIT
