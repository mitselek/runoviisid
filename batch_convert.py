#!/usr/bin/env python3
"""
Simple batch converter for the runoviisid workspace
Converts all .mscz and .mscx files to LilyPond format
"""

import os
from pathlib import Path
from convert_musescore_to_lilypond import MuseScoreToLilyPondConverter

def main():
    # Get the current directory (workspace root)
    workspace_root = Path.cwd()
    
    # Create output directory for LilyPond files
    output_dir = workspace_root / "lilypond_output"
    output_dir.mkdir(exist_ok=True)
    
    print(f"🎵 Converting MuseScore files in: {workspace_root}")
    print(f"📁 Output directory: {output_dir}")
    print()
    
    # Initialize converter
    converter = MuseScoreToLilyPondConverter()
    
    # Check dependencies
    if not converter.check_dependencies():
        print("\n❌ Please install required dependencies and try again.")
        return 1
    
    print()
    
    # Convert files in root directory
    print("Converting files in root directory...")
    success, message = converter.convert_directory(workspace_root, output_dir)
    
    # Convert files in the 'files' subdirectory
    files_dir = workspace_root / "files"
    if files_dir.exists():
        print(f"\nConverting files in '{files_dir.name}' directory...")
        files_output_dir = output_dir / "files"
        success2, message2 = converter.convert_directory(files_dir, files_output_dir)
    
    print(f"\n🎉 Batch conversion complete!")
    print(f"📂 Check the '{output_dir.name}' directory for your LilyPond files.")

if __name__ == "__main__":
    main()