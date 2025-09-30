#!/bin/bash
# Setup script for MuseScore to LilyPond converter

echo "🎵 Setting up MuseScore to LilyPond converter environment..."

# Check if we're already in a virtual environment
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "✅ Virtual environment already active: $VIRTUAL_ENV"
else
    echo "📦 Creating and activating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    echo "✅ Virtual environment activated"
fi

# Install Python dependencies (if any)
if [ -f requirements.txt ]; then
    echo "📋 Installing Python dependencies..."
    pip install -r requirements.txt
fi

# Check system dependencies
echo "🔍 Checking system dependencies..."

# Check for MuseScore
if command -v musescore3 &> /dev/null || command -v musescore &> /dev/null || command -v mscore &> /dev/null; then
    echo "✅ MuseScore found"
else
    echo "❌ MuseScore not found. Please install it:"
    echo "   Ubuntu/Debian: sudo apt install musescore3"
    echo "   macOS: brew install musescore"
    echo "   Windows: Download from https://musescore.org/"
fi

# Check for LilyPond
if command -v musicxml2ly &> /dev/null; then
    echo "✅ LilyPond (musicxml2ly) found"
else
    echo "❌ LilyPond not found. Please install it:"
    echo "   Ubuntu/Debian: sudo apt install lilypond"
    echo "   macOS: brew install lilypond"
    echo "   Windows: Download from https://lilypond.org/"
fi

# Make scripts executable
chmod +x convert_musescore_to_lilypond.py
chmod +x batch_convert.py

echo ""
echo "🎉 Setup complete!"
echo ""
echo "To use the converter:"
echo "  1. Activate virtual environment: source venv/bin/activate"
echo "  2. Test single file: python convert_musescore_to_lilypond.py 1.mscx"
echo "  3. Batch convert all: python batch_convert.py"
echo ""
echo "📚 See README.md for more information"