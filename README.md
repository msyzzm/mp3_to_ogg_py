# mp3-to-ogg-py

A conversion tool for export mp3 files as ogg, and vice versa

English | [简体中文](README_CN.md)

## Installation

### Quick Start (Recommended)

**Windows users:**
1. Double-click `install.bat` (automatically installs all dependencies and tools)
2. Use `audio-converter` command from anywhere

**Other systems:**
```bash
# 1. Navigate to the project directory
cd mp3-to-ogg-py

# 2. Install dependencies
pip install -r requirements.txt

# 3. Install CLI tool
pip install -e .
```

### Detailed Installation Methods

#### Method 1: One-click install (Windows)
Double-click `install.bat` or run in command line:
```bash
install.bat
```
This script will automatically:
- ✅ Install all Python dependencies
- ✅ Install the CLI tool
- ✅ Remind you to install FFmpeg

#### Method 2: Manual installation
```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Install as CLI tool (development mode)
pip install -e .

# Or install normally
pip install .
```

#### Method 3: Install dependencies only, run script directly
If you don't want to install the CLI tool and just want to run the script:

**Windows:**
```bash
# Double-click or run
install_dependencies.bat
```

**Other systems:**
```bash
# Install dependencies
pip install -r requirements.txt

# Run script directly
python3 mp3_to_ogg.py
```

## Usage
Then this will show up:
```
===============
Audio converter
===============
[1] Mp3 to Ogg
[2] Ogg to Mp3
[3] Exit
===============
Select an option -> 
```

### Option 1: Convert mp3 files to ogg
You can specify either a directory path (converts all MP3 files) or a single file path:

**Convert all MP3 files in a directory:**
```
Select an option -> 1
Write the path where the mp3 files are for export them as ogg
MP3 Path -> /home/klairm/Music/
```
or on Windows:
```
MP3 Path -> D:/Music/
```

**Convert a single MP3 file:**
```
Select an option -> 1
Write the path where the mp3 files are for export them as ogg
MP3 Path -> D:/Music/song.mp3
```

This will convert the file(s) to .ogg format in the `export/` subdirectory.

### Option 2: Convert ogg files to mp3
Same as option 1 but for ogg files - supports both directory and single file paths.

### Option 3: Exit
Exits the program.

## Features

✅ **Bidirectional conversion** - Supports MP3 ↔ OGG conversion
✅ **Batch processing** - Convert all files in a directory at once
✅ **Single file conversion** - Convert individual files
✅ **Smart skip** - Automatically skips already converted files
✅ **Cross-platform** - Works on Windows, Linux, and macOS
✅ **Progress indicator** - Shows progress animation during conversion
✅ **CLI tool** - Can be called from anywhere after installation

## Requirements
- Python 3.6+
- pydub
- progress
- ffmpeg (required by pydub for audio conversion)

### Installing FFmpeg

**Windows:**
1. Download from [FFmpeg official website](https://ffmpeg.org/download.html)
2. Extract and add to system PATH

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install ffmpeg
```

## Uninstall

Using uninstall script (Windows):
```bash
uninstall.bat
```

Or manually:
```bash
pip uninstall audio-converter-cli
```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details



