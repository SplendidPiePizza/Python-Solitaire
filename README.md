# Python Solitaire
Solitaire In Python
## Prerequisites

1. **Python 3.x**: Python 3.6 or higher is recommended.
2. **tkinter**: Tkinter is the standard GUI library for Python and is usually included by default with Python installations.

# Compilation
# Option 1
### Windows

In order to make it binary exe you need *pyinstaller* installed, if pyinstaller in your machine then type this on your powershell or cmd
`pyinstaller --onefile --windowed main.py`

### MacOS

You Need PYinstaller and Same Procedure as windows just write this on your terminal
`pyinstaller --onefile --windowed --name=SolitaireApp main.py`

### Linux
You need pyinstaller then compile it
`pyinstaller --onefile main.py`
Then when its done make it executable
`chmod +x dist/main`
Execute it by typing this in terminal
`./dist/main`

## Option 2

Works for most operating systems
just type this `python main.py`
and it should run

# Troubleshooting

## Missing Libraries or Modules

If you encounter issues where certain libraries are not bundled with the executable (e.g., missing dependencies), you can try the following:
`pyinstaller --onefile --windowed --hidden-import=module_name main.py`

## Large Executable Size

If the generated executable is large, it’s because PyInstaller bundles all required libraries into the .exe or .app file. You can use compression tools or remove unnecessary files if needed.

for more troubleshooting or error just submit issue
