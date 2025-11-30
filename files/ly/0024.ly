\version "2.24.3"

#(set-default-paper-size "a4")

number = "0024"
title = "Kuusalu"
subtitle = "Viljak-Vilberg (112)"
source = "Armas Launis – Eesti runoviisid (1930)"

melody = \relative c'' {
  \key g \major
  \time 4/4
  \autoBeamOff
  b8^\fermata a g4^\fermata b8 a g4^\fermata |
  b8 a g4 b8 a g4^\fermata \bar "|."
}

words = \lyricmode {
  Nei -- tsi -- ke -- ne noo -- ru -- ke -- ne,
  kui si -- na ta -- had mei -- le tul -- la...
}

\score {
  <<
    \new Staff \with { instrumentName = #number } { \melody }
    \addlyrics { \words }
  >>
  \layout {}
  \midi {}
}
