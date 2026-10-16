# Quickguide til DOTE 2.0

<!-- usage note: do not edit this section -->

[![HTML Manuscript](https://img.shields.io/badge/manuscript-HTML-blue.svg)](https://codeslayer84.github.io/DOTEQUICK/)
[![PDF Manuscript](https://img.shields.io/badge/manuscript-PDF-blue.svg)](https://codeslayer84.github.io/DOTEQUICK/manuscript.pdf)
[![GitHub Actions Status](https://github.com/codeslayer84/DOTEQUICK/workflows/Manubot/badge.svg)](https://github.com/codeslayer84/DOTEQUICK/actions)

<!-- DOI badge: paste the Zenodo concept-DOI badge here after the first release -->

## Om guiden

En dansk quickguide til [DOTE](https://www.dote.aau.dk) (Distributed Open Transcription Environment).
Guiden er *permanent beta* og bliver opdateret løbende.

Den nyeste version ligger altid her:

+ **HTML** – <https://codeslayer84.github.io/DOTEQUICK/>
+ **PDF** – <https://codeslayer84.github.io/DOTEQUICK/manuscript.pdf>

Forslag til forbedringer modtages gerne som [issues](https://github.com/codeslayer84/DOTEQUICK/issues), pull requests eller på mail til <jdavidsen@ikk.aau.dk>.

## Sådan redigerer du

Teksten ligger som Markdown i [`content`](content), én fil per afsnit:

| Fil | Indhold |
|---|---|
| `content/metadata.yaml` | Titel, forfattere, sprog |
| `content/01.forord.md` | Forord |
| `content/10.installer.md` | Installer DOTE og aktiver licens |
| `content/20.interface-top.md` | Top bjælken |
| `content/30.paneler.md` | Panelerne |
| `content/40.nyt-projekt.md` | Start nyt projekt |
| `content/50.importer-eksporter.md` | Import og eksport |
| `content/60.tips.md` | Tips og tricks |
| `content/manual-references.json` | Referencer der ikke kan slås op automatisk |
| `content/images/` | Skærmbilleder |

Hvert push til `main` bygger guiden via GitHub Actions og lægger HTML/PDF på `gh-pages`-branchen.
Se [`USAGE.md`](USAGE.md) for Manubots Markdown-syntaks (figurer, citationer m.m.).

## Manubot

Guiden er bygget med [Manubot](https://manubot.org/), som er en workflow til at skrive manuskripter i Markdown med automatisk build og versionering.
Skabelonen kommer fra [manubot/rootstock](https://github.com/manubot/rootstock); se [`SETUP.md`](SETUP.md) for teknisk opsætning.
Skabelonen kan opdateres med:

```sh
git fetch rootstock main
git merge rootstock/main
```

## Licens

Se [`LICENSE.md`](LICENSE.md). Medmindre andet er angivet, er teksten under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
