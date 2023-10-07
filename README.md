# BeheadBMP
A utility which replaces BMP images with the equivalent truncated DIB image in the Windows clipboard.

## Setup
Make sure Python 3.10+ is installed.<br>
Run the `setup.py` file. This should create your python virtual environment, `venv`, and a `run.bat` file.

Note: If the `run.bat` file is moved, run `setup.vbs` again.

## Running
Run the `run.vbs` file.

If you want BeheadBMP to run on startup, place a shortcut to `run.vbs` in your `%appdata%\Microsoft\Windows\Start Menu\Programs\Startup` folder.

## Usage
Behead a BMP image in the clipboard with the `Ctrl+Alt+X` keybind, or by pressing the tray icon/BeheadBMP option in it's context menu.
