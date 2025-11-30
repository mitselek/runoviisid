\version "2.24.3"

#(set-default-paper-size "a4")

number = "0021"
title = "Rõuge, 1909"
subtitle = "J. Gutvejs (29)"
source = "Armas Launis – Eesti runoviisid (1930)"

melody = \relative c' {
  \key g \major
  \time 4/4
  \autoBeamOff
  a8[ a] a8[ fis] e4 fis8[ e] |
  fis8[ g] a4 a8[ g] fis8[ e] |
  d4 e8[ a] a8[ g] fis4 |
  e8[ d] fis8[ e] d2 \bar "|."
}

words = \lyricmode {
  A -- ra u -- ni mol -- lõ tul -- gu,
  hai -- ku mol -- lõ ha -- ri -- ne -- gu;
  as -- tu e -- si a -- ja -- mat -- ta,
  tui -- lõ ü -- les tuus -- ti -- mat -- ta.
}

\score {
  <<
    \new Staff \with { instrumentName = #number } { \melody }
    \addlyrics { \words }
  >>
  \layout {}
  \midi {}
}
