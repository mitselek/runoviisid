\version "2.24.3"

#(set-default-paper-size "a4")

number = "0022"
title = "Koeru ja Järva-Jaani"
subtitle = "Martin-Rosenstrauch (231)"
source = "Armas Launis – Eesti runoviisid (1930)"

melody = \relative c'' {
  \key g \major
  \time 6/8
  \autoBeamOff
  g16[ g g g g g] g8[ fis16 e d e] |
  fis16[ e fis g fis e] d8[ d16 e fis g] |
  a16[ a a a a a] a8[ g16 fis e fis] |
  g16[ fis g a g fis] e8[ e16 fis g a] |
  b8[ b16 a g fis] g8[ a16 g fis e] |
  d8[ e16 d cis b] cis8[ d16 cis b a] |
  b16[ a b cis d e] fis8[ e16 d cis b] |
  a4. r8 r r \bar "|."
}

words = \lyricmode {
  A -- ni Pee -- ter võt -- tis nai -- se _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
}

\score {
  <<
    \new Staff \with { instrumentName = #number } { \melody }
    \addlyrics { \words }
  >>
  \layout {}
  \midi {}
}
