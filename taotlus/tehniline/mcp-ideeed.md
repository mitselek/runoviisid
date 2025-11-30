# MCP tööriistade ideed runoviisid projektile

## Põhimõte

**Tööriistad sünnivad tegelikku tööd tehes.**

Kogu importides (2580 viisi) tekivad korduvad mustrid ja vajadused.
Need kodifitseerime MCP tööriistadeks, et:

1. Ise saaksime tööd kiiremini teha
2. Tulevased panustajad saaksid sama töövoogu kasutada
3. Sarnased projektid (nt teised rahvaviisikogud) saaksid tööriistu taaskasutada

## Mis on MCP?

Model Context Protocol - avatud standard, mis võimaldab luua AI-le kohandatud tööriistu.
Tööriistad kirjutatakse TypeScript/Python keeles ja jooksevad lokaalselt.

## Võimalikud tööriistad selle projekti jaoks

### 1. `runoviis-ocr`

Spetsialiseeritud OCR tööriist runoviisidele:

- **Sisend**: Skaneeringu fail + viisi number
- **Väljund**: Struktureeritud andmed (ID, päritolu, sõnad, silbitamine)
- **Eripära**: Treenitud eesti vanal kirjaviisil, tunneb ära spetsiifilisi märke

### 2. `runoviis-omr`

Noodikirja tuvastus (Optical Music Recognition):

- **Sisend**: Skaneeringu fail + viisi number
- **Väljund**: LilyPond kood
- **Eripära**: Treenitud 1930. aastate noodikirjal, üherealised viisid

### 3. `runoviis-validate`

Andmete valideerimine:

- **Sisend**: CSV rida + skaneeringu pilt
- **Väljund**: Vastavuse raport, vead, hoiatused
- **Kasutus**: Kvaliteedikontroll enne avaldamist

### 4. `runoviis-lilypond`

LilyPond genereerimine ja kompileerimine:

- **Sisend**: Struktureeritud andmed (meloodia + sõnad)
- **Väljund**: .ly fail, .pdf, .midi
- **Eripära**: Runoviisidele sobiv mall, eesti keele tugi

### 5. `runoviis-batch`

Partii töötlus:

- **Sisend**: Viisi vahemik (nt 1-100)
- **Väljund**: Töödeldud failid + raport
- **Kasutus**: Massiline töötlus järelevalvega

## Arhitektuur

```text
┌─────────────────┐
│   VS Code AI    │
│   (Claude)      │
└────────┬────────┘
         │ MCP protokoll
         ▼
┌─────────────────┐
│  MCP Server     │
│  (TypeScript)   │
└────────┬────────┘
         │
    ┌────┴────┬──────────┐
    ▼         ▼          ▼
┌───────┐ ┌───────┐ ┌─────────┐
│Tesseract│ │Audiveris│ │LilyPond│
│ (OCR)  │ │ (OMR)  │ │(engrave)│
└───────┘ └───────┘ └─────────┘
```

## Arenduse sammud

1. **Prototüüp** - Üks tööriist (nt validate) käsitsi töövoo testimiseks
2. **MCP server** - Põhiline infrastruktuur
3. **Integratsioon** - Ühendamine olemasolevate tööriistadega
4. **Dokumentatsioon** - Jätkupanustajatele

## Ressursid

- MCP spetsifikatsioon: https://modelcontextprotocol.io/
- MCP SDK (TypeScript): https://github.com/modelcontextprotocol/typescript-sdk
- MCP SDK (Python): https://github.com/modelcontextprotocol/python-sdk

## Märkused

See on projekti **jätkusuutlikkuse** oluline osa:

- Töövoog on dokumenteeritud ja korratav
- Uued panustajad saavad kasutada samu tööriistu
- AI saab aidata ilma et peaks kõike nullist õppima
