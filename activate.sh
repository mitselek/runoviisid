#!/bin/bash
# Quick activation script for the converter environment

if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "🔄 Virtual environment already active: $(basename $VIRTUAL_ENV)"
else
    echo "🚀 Activating virtual environment..."
    source venv/bin/activate
    echo "✅ Environment activated. You can now use the converter scripts!"
fi

echo ""
echo "📋 Available commands:"
echo "  python convert_musescore_to_lilypond.py --check-deps  # Check dependencies"
echo "  python convert_musescore_to_lilypond.py file.mscx     # Convert single file"
echo "  python batch_convert.py                               # Convert all files"
echo "  deactivate                                             # Exit virtual environment"