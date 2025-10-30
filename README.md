# mp3-to-ogg-py
A conversion tool for export mp3 files as ogg, and vice versa

## Installation

### Method 1: Install as a command-line tool (Recommended)
```bash
# Navigate to the project directory
cd mp3-to-ogg-py

# Install in development mode (editable)
pip install -e .

# Or install normally
pip install .
```

After installation, you can use the `audio-converter` command from anywhere:
```bash
audio-converter
```

### Method 2: Run directly
```bash
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

## Requirements
- Python 3.6+
- pydub
- progress
- ffmpeg (required by pydub for audio conversion)

## Uninstall
```bash
pip uninstall audio-converter-cli
```



