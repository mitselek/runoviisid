\version "2.24.3"

#(set-default-paper-size "a4")

number = "0025"
title = "Kuusalu"
subtitle = "Viljak-Vilberg (131)"
source = "Armas Launis – Eesti runoviisid (1930)"

melody = \relative c'' {
  \key g \major
  \time 4/4
  \autoBeamOff
  b8^\fermata a b4^\fermata b8 a b4^\fermata |
  b8 a b4 b8 a b4^\fermata \bar "|."
}

words = \lyricmode {
  Ku -- ku -- me ü -- le kol -- me kae -- vu.
}

\score {
  <<
    \new Staff \with { instrumentName = #number } { \melody }
    \addlyrics { \words }
  >>
  \layout {}
  \midi {}
}
