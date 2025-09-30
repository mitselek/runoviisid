# MuseScore to LilyPond Converter

This repository contains scripts to convert MuseScore files (`.mscz` and `.mscx`) to LilyPond format (`.ly`).

## ✅ Supported Formats

- **`.mscz`** - MuseScore compressed format (fully supported ✅)
- **`.mscx`** - MuseScore uncompressed XML format (fully supported ✅)
- **Output**: `.ly` - LilyPond notation files

## Quick Setup

Run the setup script to automatically configure everything:

```bash
./setup.sh
```

## Manual Prerequisites

If you prefer manual setup, you need to install:

1. **Python 3.6+** with venv support
2. **MuseScore** (with command-line support)

   - Ubuntu/Debian: `sudo apt install musescore3`
   - macOS: `brew install musescore`
   - Windows: Download from [musescore.org](https://musescore.org/)

3. **LilyPond** (includes `musicxml2ly`)

   - Ubuntu/Debian: `sudo apt install lilypond`
   - macOS: `brew install lilypond`
   - Windows: Download from [lilypond.org](https://lilypond.org/)

4. **Virtual Environment Setup**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Usage

### Check Dependencies

```bash
# Activate virtual environment first
source venv/bin/activate

# Check if everything is installed
python convert_musescore_to_lilypond.py --check-deps
```

### Convert Single File

```bash
# Convert .mscz file to same directory
python convert_musescore_to_lilypond.py song.mscz

# Convert .mscx file to specific output directory
python convert_musescore_to_lilypond.py song.mscx output_folder/

# Works with both compressed (.mscz) and uncompressed (.mscx) formats
```

### Batch Convert Directory

```bash
# Convert all files in current directory
python convert_musescore_to_lilypond.py --batch . lilypond_output/

# Convert all files recursively
python convert_musescore_to_lilypond.py --batch --recursive . lilypond_output/
```

### Simple Batch Convert (for this workspace)

```bash
# Convert all .mscz and .mscx files in the workspace
python batch_convert.py
```

This will:

- Convert all MuseScore files in the root directory
- Convert all MuseScore files in the `files/` directory
- Save all LilyPond files to `lilypond_output/` directory

## How It Works

The conversion process involves two steps:

1. **MuseScore → MusicXML**: Uses MuseScore's command-line export feature
2. **MusicXML → LilyPond**: Uses LilyPond's built-in `musicxml2ly` converter

## File Structure After Conversion

```text
runoviisid/
├── 1.mscz                          # Original MuseScore files
├── 2.mscz
├── files/
│   ├── 0001-r.mscx
│   └── ...
├── lilypond_output/                # Generated LilyPond files
│   ├── 1.ly
│   ├── 2.ly
│   └── files/
│       ├── 0001-r.ly
│       └── ...
├── convert_musescore_to_lilypond.py
├── batch_convert.py
└── README.md
```

## Features

- ✅ Batch conversion of multiple files
- ✅ Recursive directory scanning
- ✅ Automatic dependency checking
- ✅ Error handling and reporting
- ✅ Progress indicators
- ✅ Preserves directory structure
- ✅ Supports both `.mscz` and `.mscx` formats

## Troubleshooting

### "MuseScore not found"

- Make sure MuseScore is installed and accessible from command line
- Try running `mscore --version` or `musescore --version`

### "musicxml2ly not found"

- Make sure LilyPond is installed
- Try running `musicxml2ly --version`

### Conversion errors

- Check that the MuseScore file is not corrupted
- Ensure you have read permissions for input files
- Ensure you have write permissions for output directory

## Notes

- The conversion preserves most musical information, but some MuseScore-specific formatting may be lost
- LilyPond files may need manual adjustment for optimal engraving
- Large files may take some time to convert
- The script uses temporary files which are automatically cleaned up
