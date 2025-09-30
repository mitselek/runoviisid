\version "2.24.3"
% automatically converted by musicxml2ly from /tmp/tmpd03ym1e6.musicxml
\pointAndClickOff

\header {
    encodingsoftware =  "MuseScore 3.2.3"
    encodingdate =  "2025-09-30"
    source = 
    "/tmp/audiveris-8ff757ef125b7b244bbdfeca7598bdc8/score.pdf"
    composer =  "Lähteenkorvu (306)"
    poet =  "1. Sangaste"
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
        skipBars = ##t
        autoBeaming = ##f
        }
    }

PartPOneVoiceOne =  \relative d' {
    \clef "treble" \time 3/8 \key g \major | % 1
    R4. | % 2
    \time 2/4  \stemUp <d g>8 \stemUp <d g>8 \stemUp <d fis>8 \stemDown
    d8 | % 3
    \time 3/8  \stemUp d16 \stemUp e16 \stemUp <d g>8 \stemUp <d fis>8 | % 4
    \time 2/4  \stemUp e8 \stemUp d8 \stemUp d4 \bar "|."
    }

PartPOneVoiceOneLyricsOne =  \lyricmode {\set ignoreMelismata = ##t Lii
    -- su -- ke -- "ne," "K: Ut" -- si pruu -- ti Lii -- su -- "ke."
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

