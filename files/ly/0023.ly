\version "2.24.3"

#(set-default-paper-size "a4")

number = "0023"
title = "Ridala"
subtitle = "Kreek-Mudda (11)"
source = "Armas Launis – Eesti runoviisid (1930)"

melody = \relative c'' {
  \key g \major
  \time 6/8
  \autoBeamOff
  g8[ a] b c8[ b] a |
  g8[ a] b c8[ b] a |
  g8[ a] b c8[ b] a |
  g4. r4 r8 \bar "|."
}

words = \lyricmode {
  A -- nu leks al -- la me -- re ää -- re
  sii -- di -- kek -- ki lo -- pu -- ta -- ma.
}

\score {
  <<
    \new Staff \with { instrumentName = #number } { \melody }
    \addlyrics { \words }
  >>
  \layout {}
  \midi {}
}
