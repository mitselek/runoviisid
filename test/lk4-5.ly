\version "2.24.0"

% Eesti runoviisid - leheküljed 4-5 (viisid 20-32)
% OCR test: Claude Opus 4.5

% ============================================
% VIIS 20. Harju-Jaani. Viljak-Vilberg (10) [37].
% ============================================
viisKakskymmend = \relative c'' {
  \key g \major
  \time 3/4
  e8 e e d d4 |
  d8 d e4 r4 |
}
\addlyrics {
  Läh- me kii- ke kat- su- mai- e.
}

% ============================================
% VIIS 21. Rõuge, 1909. J. Gutveis (29).
% ============================================
viisKakskymmendyks = \relative c' {
  \key a \minor
  \time 4/4
  a8 a a g a a a g |
  a a a b a g a4 |
  \bar "||"
  a8 a a g a a a g |
  a g a4 r2 |
}
\addlyrics {
  Ä- ra u- ni mul- lõ tul- gu, hai- ku mul- lõ ha- ri- ne- gu;
  as- tu e- si a- ja- mat- ta, tu- lõ ü- les tuus- ti- mat- ta.
}

% ============================================
% VIIS 22. Koeru ja Järva-Jaani. Martin-Rosenstrauch (231).
% ============================================
viisKakskymmendkaks = \relative c'' {
  \key d \major
  \time 2/4
  d8 d d d |
  d cis d4 |
}
\addlyrics {
  A- ni Pee- ter võt- tis nai- se...
}

% ============================================
% VIIS 23. Ridala. Kreek-Mudda (11).
% ============================================
viisKakskymmendkolm = \relative c'' {
  \key g \major
  \time 2/4
  d8 d b d |
  d d d d |
  d d b a |
  g4 r4 |
}
\addlyrics {
  Ann läks al- la me- re ää- re sii- di- tek- ki lo- pu- ta- ma.
}

% ============================================
% VIIS 24. Kuusalu. Viljak-Vilberg (112).
% ============================================
viisKakskymmendneli = \relative c'' {
  \key g \major
  \time 2/4
  b8 b a g |
  a a g4 |
  b8 b a g |
  a4 r4 |
}
\addlyrics {
  Neit- si- ke- ne noo- ru- ke- ne,
  kui si- na ta- had mei- le tul- la...
}

% ============================================
% VIIS 25. Kuusalu. Viljak-Vilberg (131).
% ============================================
viisKakskymmendviis = \relative c'' {
  \key g \major
  \time 2/4
  \partial 8 d8 |
  d d d d |
  d4 b8 a |
  g4 r4 |
}
\addlyrics {
  Ku- ku- me ü- le kol- me kae- vu.
}

% ============================================
% VIIS 26. Väike-Maarja. P. Penna (209).
% ============================================
viisKakskymmendkuus = \relative c'' {
  \key g \major
  \time 2/4
  d8 d d d |
  d d d d |
  d4 r4 |
}
\addlyrics {
  Mul- lu mi- na võt- sin nai- se noo- re...
}

% ============================================
% VIIS 27. Haljala. Viljak-Mark (8) a.
% ============================================
viisKakskymmendseitse = \relative c'' {
  \key g \major
  \time 2/4
  b8 b b b |
  b b a a |
  b b b b |
  b b a g |
  a4 r4 |
}
\addlyrics {
  Nä- gin a- ga nä- gin a- ga ven- ni- ke- ne, 
  nä- gin a- ga nei- ut kas- va- mai- e.
}

% ============================================
% VIIS 28. Kanepi. P. Tatz (47).
% ============================================
viisKakskymmendkaheksa = \relative c'' {
  \key g \major
  \time 2/4
  a8 a a a |
  a g a4 |
  a8 a a a |
  a g a4 |
}
\addlyrics {
  Kui mi- na är- ga ü- te- le- ma, 
  kui mi- na är- ga ü- te- le- ma.
}

% ============================================
% VIIS 29. Avinurme, 1909. M. Sild (1).
% ============================================
viisKakskymmendyheksa = \relative c'' {
  \key a \minor
  \time 2/4
  a8 a a a |
  a a g a |
  a a a a |
  a a g a |
  a a a a |
  a4 r4 |
}
\addlyrics {
  Kes sind käs- kis kos- ja tul- la, kes sind käs- kis kos- ja tul- la,
  Pa- ni a- ga, pa- ni nais- ta võt- ma, pa- ni a- ga, pa- ni nais- ta võt- ma!
}

% ============================================
% VIIS 30. Ambla. J. Välbe (40).
% ============================================
viisKolmkymmend = \relative c'' {
  \key g \major
  \time 2/4
  b8 b b b |
  b a g a |
  b4 r4 |
}
\addlyrics {
  Kes sind käs- kis kos- ja tul- la, pa- ni a- ga, pa- ni nais- ta võt- ma?
}

% ============================================
% VIIS 31. Kuusalu. Viljak-Vilberg (198).
% ============================================
viisKolmkymmendyks = \relative c'' {
  \key g \major
  \time 2/4
  d8 d d d |
  d d d d |
  d4 r4 |
}
\addlyrics {
  U- ra- ge, u- ra- ge, o- med.
}

% ============================================
% VIIS 32. Kuusalu. Viljak-Vilberg (197).
% ============================================
viisKolmkymmendkaks = \relative c'' {
  \key g \major
  \time 2/4
  b8 b b a |
  b b a g |
  a4 r4 |
}
\addlyrics {
  Pe- re tü- tar pii- ma kuo- ki.
}

% ============================================
% KOMPILEERI KÕIK
% ============================================

\score {
  \header { piece = "20. Harju-Jaani" }
  <<
    \new Voice = "mel" \viisKakskymmend
  >>
}
