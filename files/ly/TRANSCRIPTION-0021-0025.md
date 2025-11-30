# Music Transcription Research - TODO

**Date**: November 30, 2025  
**Status**: Research and experimentation phase  
**Source**: Armas Launis – Eesti runoviisid (1930)

## Current Status

Music transcription from scanned historical sources remains an active research task. Initial attempts were made but require further refinement and validation against the source material.

## Work Done

### Methodology Development

- Created "Lilli Tuul" persona prompt for systematic music reading
- Established interval-based reading method to handle warped scans
- Developed conversion checklist for consistent transcription workflow
- Set up LilyPond build system with Makefile

### Experiments Conducted

- Tested OCR tools (Tesseract) - unsuitable for mixed staff/text
- Evaluated OMR software (Audiveris) - inaccurate for this engraving style
- Multiple iterations on melody 20 to refine reading methodology
- Template files created for melodies 21-25

## Challenges Identified

1. **Scan quality**: Book binding causes warped staff lines
2. **Visual ambiguity**: Distinguishing note durations, octaves, and bar lines from degraded prints
3. **Systematic errors**: Difficulty maintaining accuracy across multiple readings
4. **Verification**: Need reliable method to validate transcriptions against source

## TODO

- [ ] Validate all transcription attempts against original scans
- [ ] Develop better quality control process
- [ ] Consider alternative approaches (manual verification, expert consultation)
- [ ] Document proven successful techniques once established
- [ ] Scale to remaining ~2575 melodies only after validation

## Files & Artifacts

Located in: `/home/michelek/Documents/github/runoviisid/files/ly/`

- `.github/prompts/LilliTuul.prompt.md` - Reading methodology persona
- `Makefile` - Build system for LilyPond compilation
- `0020.ly` - Most refined attempt (melody 20)
- `0021.ly` through `0025.ly` - Experimental transcriptions (unvalidated)
- Various PDFs - Compiled output (accuracy not confirmed)

## Next Steps

1. Put music transcription on hold for now
2. Focus on other aspects of the digitization project
3. Return to transcription with fresh approach and/or external validation method
