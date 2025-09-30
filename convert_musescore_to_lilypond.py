#!/usr/bin/env python3
"""
MuseScore to LilyPond Converter Script

This script converts MuseScore files (.mscz, .mscx) to LilyPond format (.ly)
using MuseScore's command-line export and LilyPond's musicxml2ly converter.

Usage:
    python convert_musescore_to_lilypond.py [input_file_or_directory] [output_directory]
    python convert_musescore_to_lilypond.py --batch [input_directory] [output_directory]

Requirements:
    - MuseScore installed with command-line access (mscore or musescore)
    - LilyPond installed with musicxml2ly
"""

import os
import sys
import subprocess
import argparse
import tempfile
from pathlib import Path
import shutil

class MuseScoreToLilyPondConverter:
    def __init__(self):
        self.musescore_cmd = self._find_musescore_executable()
        self.musicxml2ly_cmd = self._find_musicxml2ly_executable()
        
    def _find_musescore_executable(self):
        """Find the MuseScore executable"""
        possible_names = ['mscore', 'musescore', 'MuseScore', 'musescore3', 'musescore4']
        for name in possible_names:
            if shutil.which(name):
                return name
        return None
    
    def _find_musicxml2ly_executable(self):
        """Find the musicxml2ly executable"""
        if shutil.which('musicxml2ly'):
            return 'musicxml2ly'
        return None
    
    def check_dependencies(self):
        """Check if required dependencies are installed"""
        issues = []
        
        if not self.musescore_cmd:
            issues.append("MuseScore not found. Please install MuseScore and ensure it's in your PATH.")
            issues.append("  - Ubuntu/Debian: sudo apt install musescore3")
            issues.append("  - macOS: brew install musescore")
            issues.append("  - Windows: Download from https://musescore.org/")
        
        if not self.musicxml2ly_cmd:
            issues.append("musicxml2ly not found. Please install LilyPond.")
            issues.append("  - Ubuntu/Debian: sudo apt install lilypond")
            issues.append("  - macOS: brew install lilypond")
            issues.append("  - Windows: Download from https://lilypond.org/")
        
        if issues:
            print("❌ Missing dependencies:")
            for issue in issues:
                print(f"   {issue}")
            return False
        
        print("✅ All dependencies found:")
        print(f"   MuseScore: {self.musescore_cmd}")
        print(f"   musicxml2ly: {self.musicxml2ly_cmd}")
        return True
    
    def convert_to_musicxml(self, input_file, output_file):
        """Convert MuseScore file to MusicXML using MuseScore CLI"""
        try:
            cmd = [self.musescore_cmd, '-o', str(output_file), str(input_file)]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return True, None
        except subprocess.CalledProcessError as e:
            return False, f"MuseScore conversion failed: {e.stderr}"
        except Exception as e:
            return False, f"Error running MuseScore: {str(e)}"
    
    def convert_musicxml_to_lilypond(self, input_file, output_file):
        """Convert MusicXML to LilyPond using musicxml2ly"""
        try:
            cmd = [self.musicxml2ly_cmd, '--output', str(output_file), str(input_file)]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return True, None
        except subprocess.CalledProcessError as e:
            return False, f"musicxml2ly conversion failed: {e.stderr}"
        except Exception as e:
            return False, f"Error running musicxml2ly: {str(e)}"
    
    def convert_file(self, input_file, output_dir=None):
        """Convert a single MuseScore file to LilyPond"""
        input_path = Path(input_file)
        
        if not input_path.exists():
            return False, f"Input file not found: {input_file}"
        
        if input_path.suffix.lower() not in ['.mscz', '.mscx']:
            return False, f"Unsupported file format: {input_path.suffix}"
        
        # Determine output directory and filename
        if output_dir:
            output_dir = Path(output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
        else:
            output_dir = input_path.parent
        
        output_ly_file = output_dir / f"{input_path.stem}.ly"
        
        print(f"Converting: {input_path.name} -> {output_ly_file.name}")
        
        # Create temporary file for MusicXML
        with tempfile.NamedTemporaryFile(suffix='.musicxml', delete=False) as temp_xml:
            temp_xml_path = Path(temp_xml.name)
        
        try:
            # Step 1: Convert MuseScore to MusicXML
            success, error = self.convert_to_musicxml(input_path, temp_xml_path)
            if not success:
                return False, error
            
            # Step 2: Convert MusicXML to LilyPond
            success, error = self.convert_musicxml_to_lilypond(temp_xml_path, output_ly_file)
            if not success:
                return False, error
            
            print(f"✅ Successfully converted to: {output_ly_file}")
            return True, str(output_ly_file)
            
        finally:
            # Clean up temporary file
            if temp_xml_path.exists():
                temp_xml_path.unlink()
    
    def convert_directory(self, input_dir, output_dir=None, recursive=False):
        """Convert all MuseScore files in a directory"""
        input_path = Path(input_dir)
        
        if not input_path.is_dir():
            return False, f"Input directory not found: {input_dir}"
        
        # Find all MuseScore files
        patterns = ['*.mscz', '*.mscx']
        files = []
        
        for pattern in patterns:
            if recursive:
                files.extend(input_path.rglob(pattern))
            else:
                files.extend(input_path.glob(pattern))
        
        if not files:
            return False, f"No MuseScore files found in {input_dir}"
        
        print(f"Found {len(files)} MuseScore files to convert")
        
        successful = 0
        failed = 0
        
        for file_path in files:
            try:
                success, result = self.convert_file(file_path, output_dir)
                if success:
                    successful += 1
                else:
                    failed += 1
                    print(f"❌ Failed to convert {file_path.name}: {result}")
            except Exception as e:
                failed += 1
                print(f"❌ Error converting {file_path.name}: {str(e)}")
        
        print(f"\nConversion complete:")
        print(f"  ✅ Successful: {successful}")
        print(f"  ❌ Failed: {failed}")
        
        return True, f"Converted {successful}/{len(files)} files"

def main():
    parser = argparse.ArgumentParser(
        description="Convert MuseScore files to LilyPond format",
        epilog="Examples:\n"
               "  python %(prog)s song.mscz\n"
               "  python %(prog)s song.mscz output/\n"
               "  python %(prog)s --batch input_folder/ output_folder/\n"
               "  python %(prog)s --batch --recursive music/ lilypond_output/",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('input', nargs='?', help='Input file or directory')
    parser.add_argument('output', nargs='?', help='Output directory (optional)')
    parser.add_argument('--batch', '-b', action='store_true', 
                       help='Convert all files in input directory')
    parser.add_argument('--recursive', '-r', action='store_true',
                       help='Search recursively in subdirectories (with --batch)')
    parser.add_argument('--check-deps', action='store_true',
                       help='Check if required dependencies are installed')
    
    args = parser.parse_args()
    
    converter = MuseScoreToLilyPondConverter()
    
    # Check dependencies
    if args.check_deps:
        converter.check_dependencies()
        return 0
    
    if not args.input:
        parser.error("Input file or directory is required unless using --check-deps")
    
    if not converter.check_dependencies():
        return 1
    
    try:
        if args.batch:
            success, message = converter.convert_directory(
                args.input, args.output, args.recursive
            )
        else:
            success, message = converter.convert_file(args.input, args.output)
        
        if success:
            print(f"\n🎵 {message}")
            return 0
        else:
            print(f"\n❌ {message}")
            return 1
            
    except KeyboardInterrupt:
        print("\n⏹️  Conversion cancelled by user")
        return 1
    except Exception as e:
        print(f"\n💥 Unexpected error: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())