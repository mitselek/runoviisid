# Projekti skoop

_Mida me teeme? Täidame piiskhaaval, kui vastused selguvad._

---

## Põhiküsimused

### 1. Mis on lõpptulemus?

**Põhitulemid:**

- 2580 runoviisi digitaalsel kujul (LilyPond → PDF, MIDI)
- Struktureeritud andmebaas (metaandmed, sõnad, meloodiad)
- Avalik veebirakendus viisidele ligipääsuks

**Kõrvaltulemid:**

- MCP tööriistad töövoo automatiseerimiseks
- Dokumenteeritud protsess sarnaste projektide jaoks
- Avatud lähtekood jätkupanustajatele

### 2. Milline on ulatus?

**Kogu antoloogia:** 2580 viisi

Skoopi kuulub:

- Masinlugemine (OCR/OMR) skaneeringutest
- Nootide digitaliseerimine
- Laulusõnade digitaliseerimine
- Metaandmete digitaliseerimine

### 3. Kes teeb?

_(Märgi, kui selgub)_

### 4. Mis on ajakava?

_(Märgi, kui selgub)_

---

## Avatud küsimused

_(Lisa küsimusi, millele vastust otsime)_

1. ~~Kes digitaliseeris olemasolevad ~263 viisi MuseScore'i?~~ → Projekti autor (proof of concept)
2. ~~Kas kogu raamat on pildistatud/skaneeritud?~~ → Jah, `files/scans/`, JPG formaat
3. Milline on sihtgrupp – kes seda kasutab?
4. Kas on koostööpartnereid?
5. Millist OMR tööriista kasutada? (Audiveris, muu?)

---

## Otsused

_(Dokumenteerime tehtud otsused koos põhjendustega)_

| Kuupäev    | Otsus                                            | Põhjendus                                                  |
| ---------- | ------------------------------------------------ | ---------------------------------------------------------- |
| 30.11.2025 | Olemasolevad MuseScore failid = proof of concept | Taaskasutatav: skaneeringud ja töövood, mitte .mscz failid |
| 30.11.2025 | Kasutame masinlugemist, mitte käsitsi sisestust  | Käsitöö minimeerimine, kvaliteeti saab hinnata 603 viisiga |
| 30.11.2025 | Kogu 2580 viisi kuulub skoopi                    | Täielik digitaliseerimine                                  |
| 30.11.2025 | Digitaliseerimine kahes etapis: tekst + meloodia | Tekst lihtsam (~90% auto), meloodia keerulisem (~75% auto) |
| 30.11.2025 | Enne lõplikku otsust katsetame tööriistu         | Tegelik kvaliteet selgub alles testimisel                  |

---

## Märkmed

_(Vabad mõtted ja ideed)_

**Olemasolevad ressursid:**

- Skaneeringud: ~200 JPG faili (`files/scans/`)
- Käsitsi sisestatud: 603 viisi CSV-s (metaandmed + sõnad)
- MuseScore failid: ~263 (proof of concept)

**Töövoo idee:**

```text
Skaneeringud → OCR/OMR → Võrdlus 603 viisiga → Vigade parandus → Lõpptulemus
```
