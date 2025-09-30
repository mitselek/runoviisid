\version "2.24.3"
\pointAndClickOn

\header {
    composer =  "Lähteenkorvu (306)"
    poet =  "1. Sangaste"
}

#(set-global-staff-size 18)

\paper {
    paper-width = 21.0\cm
    paper-height = 5.0\cm
    top-margin = 1.0\cm
    bottom-margin = 0.8\cm
    left-margin = 1.0\cm
    right-margin = 1.0\cm
    indent = 0\cm
    tagline = ##f  % Remove LilyPond footer
}

\layout {
    \context { 
        \Score
        skipBars = ##t        % Show multi-measure rests as numbers instead of many rest symbols
        autoBeaming = ##f     % Turn off automatic note beaming (for vocal music)
    }
}

melody = \relative d' {
    \clef "treble" 
    \time 3/8 
    \key g \major 
    
    % Measure 1
    d16 d16 g8 g8 |
    
    % Measure 2
    \time 2/4  
    <d g>8 <d g>8 <d fis>8 d8 |
    
    % Measure 3
    \time 3/8  
    d16 e16 <d g>8 <d fis>8 |
    
    % Measure 4
    \time 2/4  
    e8 d8 d4 \bar "|."
}

songLyrics = \lyricmode {
    \set ignoreMelismata = ##t
    "E: Ut" -- si pruu -- ti Lii -- su -- ke -- "ne," 
    "K: Ut" -- si pruu -- ti Lii -- su -- "ke."
}

\score {
    \new Staff <<
        \new Voice = "melody" {
            \melody
        }
        \new Lyrics \lyricsto "melody" {
            \songLyrics
        }
    >>
    \layout {}
    % To create MIDI output, uncomment the following line:
    %  \midi {\tempo 4 = 100 }
}

