\version "2.24.3"
% automatically converted by musicxml2ly from /tmp/tmpgbmeh01l.musicxml
\pointAndClickOff

\header {
    encodingsoftware =  "MuseScore 3.2.3"
    encodingdate =  "2025-09-30"
    source = 
    "/tmp/audiveris-8ff757ef125b7b244bbdfeca7598bdc8/score.pdf"
    composer =  "Lähteenkorvu (303)"
    poet =  "2. Sangaste. 1877."
    }

#(set-global-staff-size 17.714285714285715)
\paper {
    
    paper-width = 21.0\cm
    paper-height = 5.0\cm
    top-margin = 1.0\cm
    bottom-margin = 0.8\cm
    left-margin = 1.0\cm
    right-margin = 1.0\cm
    indent = 1.6153846153846154\cm
    }
\layout {
    \context { \Score
        autoBeaming = ##f
        }
    }
PartPOneVoiceOne =  \relative d' {
    \clef "treble" \time 3/8 \key g \major | % 1
    \stemUp d16 \stemUp d16 \stemUp g8 \stemUp g8 | % 2
    \time 2/4  \stemUp g8 \stemUp g8 \stemUp fis8 \stemDown d8 | % 3
    \time 3/8  \stemUp d16 \stemUp e16 \stemUp g8 \stemUp fis8 | % 4
    \time 2/4  \stemUp e8 \stemUp d8 \stemUp d4 \bar "|."
    }

PartPOneVoiceOneLyricsOne =  \lyricmode {\set ignoreMelismata = ##t
    "E: Lä" -- ki ü -- les mä -- ki pää -- "le," "K: Lä" -- ki ü -- les
    mä -- ki "pääl."
    }


% The score definition
\score {
    <<
        
        \new Staff
        <<
            \set Staff.instrumentName = "Voice"
            
            \context Staff << 
                \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                \context Voice = "PartPOneVoiceOne" {  \PartPOneVoiceOne }
                \new Lyrics \lyricsto "PartPOneVoiceOne" { \set stanza = "1." \PartPOneVoiceOneLyricsOne }
                >>
            >>
        
        >>
    \layout {}
    % To create MIDI output, uncomment the following line:
    %  \midi {\tempo 4 = 100 }
    }

