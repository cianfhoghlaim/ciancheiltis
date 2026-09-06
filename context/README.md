# context/gaeilge/

Reference corpus of upstream open-source repos from the
[Gaois research group](https://www.gaois.ie/) (Fiontar & Scoil na Gaeilge, DCU)
plus reference PDFs / data dumps for the ciancheiltis DLT pipeline.

## Vendored upstream repos (under `context/gaeilge/gaois/*`)

Read-only mirrors of upstream GitHub repos, captured by stripping the embedded
`.git/` directories (see `2026-08-27-kcg-rename-v1` change).

| Repo | What it is | URL |
|---|---|---|
| `gaois/DuchasAPI-docs` | Dúchas API reference docs (archived) | https://github.com/gaois/DuchasAPI-docs |
| `gaois/Gaois.Localizer` | .NET globalization NuGet | https://github.com/gaois/Gaois.Localizer |
| `gaois/Gaois.QueryLogger` | ASP.NET query logger for SQL Server | https://github.com/gaois/Gaois.QueryLogger |
| `gaois/GeoNames2Sql` | GeoNames gazetteer → SQL Server | https://github.com/gaois/GeoNames2Sql |
| `gaois/IrishSurnameIndex` | Surnames XML (Irish Folklore Commission) | https://github.com/gaois/IrishSurnameIndex |
| `gaois/LogainmAPI-docs` | Logainm API reference docs (archived) | https://github.com/gaois/LogainmAPI-docs |
| `gaois/Nationalist` | ISO country-list generator (.NET) | https://github.com/gaois/Nationalist |
| `gaois/PublicDocs` | Gaois public docs repo | https://github.com/gaois/PublicDocs |
| `gaois/Tearma` | téarma.ie source code | https://github.com/gaois/Tearma |
| `gaois/documental` | Multilingual technical docs platform | https://github.com/gaois/documental |
| `gaois/gaoisalign` | Irish/English parallel-text aligner | https://github.com/gaois/gaoisalign |
| `gaois/screenful` | Generic JS/CSS record-editor templates | https://github.com/gaois/screenful |
| `gaois/sloinnte` | Database of Irish-Language Surnames (XML) | https://github.com/gaois/sloinnte |
| `gaois/terminologue` | Terminology management tool source | https://github.com/gaois/terminologue |

## Download-on-demand assets (gitignored — fetch from upstream)

These are intentionally **not** committed to the repo. Re-fetch before each
BAML extraction or DLT run:

```bash
# Tearma data dumps (versioned by date — refresh from tearma.ie)
# https://www.tearma.ie/ioslodail.html
curl -O https://www.tearma.ie/ioslodail/$(date +%y.%m.%d)-tearma.ie-concepts.tbx.zip \
  -o context/gaeilge/gaois/Tearma/TearmaWeb/wwwroot/ioslodail/$(date +%y.%m.%d)-tearma.ie-concepts.tbx.zip
curl -O https://www.tearma.ie/ioslodail/$(date +%y.%m.%d)-tearma.ie-concepts.txt.zip \
  -o context/gaeilge/gaois/Tearma/TearmaWeb/wwwroot/ioslodail/$(date +%y.%m.%d)-tearma.ie-concepts.txt.zip

# Linguistic study PDFs (DCU Gaois)
curl -O https://www.gaois.ie/ga/gaois/PDF/Linguistic-Study-of-the-Use-of-Irish-in-the-Gaeltacht.pdf \
  -o context/gaeilge/Linguistic-Study-of-the-Use-of-Irish-in-the-Gaeltacht.pdf
curl -O https://www.gaois.ie/ga/gaois/PDF/update-to-the-comprehensive-linguistic-study-on-the-usage-of-irish-in-the-gaeltacht-20.pdf \
  -o context/gaeilge/update-to-the-comprehensive-linguistic-study-on-the-usage-of-irish-in-the-gaeltacht-20.pdf
```

## Size budget

After the `2026-08-27-kcg-rename-v1` cruft-strip, the `context/gaeilge/*`
contribution to `b39a4a9` is **~9 MB raw** (vs ~32 MB before stripping).
Vendored libs / data dumps / PDFs / design assets (~33 MB) live outside git.
