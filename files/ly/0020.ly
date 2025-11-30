\version "2.24.0"

% Viis 20. Harju-Jaani. Viljak-Vilberg (10) [37].
% v7 — ground truth per user: 10x 1/8, last 1/4
% Notes: D F# E | D F# E | D D C | C D(1/4)

\header {
  title = "20. Harju-Jaani"
  composer = "Viljak-Vilberg (10) [37]"
}

\relative c' {
  \key g \major
  \time 3/8
  \autoBeamOff
  
  % Bar 1 (3x 1/8) — beam notes 2-3 (as in source)
  d8 fis[ e ] |
  % Bar 2 (3x 1/8) — beam notes 2-3 (as in source)
  d8 fis[ e ] |
  % Bar 3 (3x 1/8) — beam notes 2-3
  d8 d[ c ] |
  % Bar 4 (1/8 + 1/4)
  c8 d4 \bar "|."
}

\addlyrics {
  Läh- me kii- ke kat- su- mai- e.
}
