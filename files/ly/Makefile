# Build all LilyPond scores in this directory

LILYPOND ?= lilypond
LY := $(wildcard *.ly)
PDFS := $(LY:.ly=.pdf)
MIDIS := $(LY:.ly=.midi)
FLAGS := -dno-point-and-click

.PHONY: all pdf midi clean

all: pdf

pdf: $(PDFS)

midi: $(MIDIS)
	@echo "MIDI generation complete (files with \\midi blocks will have output)."

%.pdf: %.ly
	$(LILYPOND) $(FLAGS) $<

%.midi: %.ly
	@# LilyPond writes MIDI only if a \\midi block exists; run and don't fail if absent
	@$(LILYPOND) $(FLAGS) $< >/dev/null 2>&1 || true
	@test -f $@ || { echo "No MIDI emitted by $< (no \\midi block)"; true; }

clean:
	rm -f $(PDFS) $(MIDIS) *.log *.tex *.ps *.eps *.count *.mid
