---
title: Dúchas Application Programming Interface (Version 0.6)
shortTitle: API
description: Developer documentation for the Dúchas API
keywords: Dúchas, API, folklore, history, storytelling, Irish language, Fiontar & Scoil na Gaeilge, DCU
resource: Dúchas
order: 1
public: true
---

**Note:** This documentation describes a **prerelease** version of the Dúchas API. Features are being added on an ongoing basis. This documentation will be revised in advance of the v1.0 release. We welcome feedback at <gaois@dcu.ie>.

## Introduction

Dúchas is a project to initiate the digitization of the [National Folklore Collection](https://www.ucd.ie/irishfolklore/en) (NFC), held at University College Dublin (UCD), Ireland. The results of the work to date have been made publicly available at [duchas.ie](https://www.duchas.ie) and are in the process of being archived for preservation by the [UCD Digital Library](https://digital.ucd.ie/). The technical solution is provided by the Gaois research group in [Fiontar & Scoil na Gaeilge](https://www.dcu.ie/fiontar_scoilnagaeilge/), Dublin City University (DCU). This documentation describes a web-based Application Programming Interface (API) that exposes the published content from the Collection to programmatic queries. A [data dictionary](../data) is available to assist users in parsing results returned by the API.

### The National Folklore Collection and its collections

Data from three of the five major collections of folklore held by Cnuasach Bhéaloideas Éireann/the National Folklore Collection are currently accessible via this platform. An understanding of the composition of these collections will aid your use of the API. Note that the databases associated with these collections are commonly referred to in shorthand form using acronyms such as CBÉS, CBÉG, etc. These acronyms are generally formed from the Irish-language name of the NFC, *Cnuasach Bhéaloideas Éireann*, followed by a single letter that denotes the database in question. The database of the NFC's Main Manuscript Collection is simply referred to as CBÉ.

#### The Main Manuscript Collection (CBÉ)

The Main Manuscript Collection comprises 2,400 bound volumes of material collected since 1932. Full- and part-time collectors compiled the majority of these under the auspices of the Irish Folklore Commission (1935–1971). Approximately two thirds of the material is in Irish and it includes every aspect of the Irish oral tradition. This Collection is in the process of digitization with 337 volumes published online to date.

#### The Schools' Collection (CBÉS)

Approximately 740,000 pages (288,000 pages in the pupils’ original exercise books; 451,000 pages in bound volumes) of folklore and local tradition were compiled by pupils from 5,000 primary schools in the Irish Free State between 1937 and 1939. This scheme, known as *Scéim na Scol*, is generally referred to as ‘Bailiúchán na Scol’ or ‘The Schools’ Collection’. There are 1,128 volumes, numbered and bound, in the Collection, all of which have been digitised.

#### The Photographic Collection (CBÉG)

The National Folklore Collection’s photographic collection consists of some 80,000 photographs, the majority of which were taken by members of the Irish Folklore Commission (1935-70) and its successors, including staff of the NFC. The process of digitising and conserving the collection continues apace.

#### The Persons Database (CBÉD)

Persons named within the CBÉ and CBÉG metadata are identified by reference to objects in this database. CBÉD does not map directly to any physical collection held by the NFC. Rather, given that many persons appear in several NFC collections — some photographers in CBÉG are also collectors in CBÉ, for example — the Persons Database is designed to serve as a single source of truth for personal metadata across the entire data set. At present, the Persons Database comprises all persons in the digitised portions of CBÉ and CBÉG. Due to the scope of the Schools' Collection digitisation project, it has not yet been feasible to extract a normalised set of personal metadata - it is hoped to revisit this work in the future, however.

Further information regarding the NFC and its collections is available [here](https://www.duchas.ie/en/info/cbe).

## General API information

Please consult the [getting started guide](/en/data/getting-started) for Gaois open data resources before reading the rest of the documentation for the Logainm API. The getting started guide describes how to obtain your unique user credentials as well as providing important general usage information.

## API access privileges

The Dúchas API caters to a number of different consumer types, including public users, archival users and internal clients. As a result of this, each API user — identified through their associated API Key — is granted access permissions in accordance with our Terms of Service. Privileged consumers have access to material that is not yet ready, or is deemed unsuitable, for publication as well as  internal editorial metadata. They can also filter query results according to certain additional parameters. Metadata and query parameters which are unavailable to public consumers are labelled 'Privileged' in the API documentation. Generally speaking, only internal clients in UCD and DCU are privileged consumers. If you have any questions regarding your current access privileges please [contact us](mailto:gaois@dcu.ie).

## Resource paths

The resources provided by the API are accessed via unique paths appended to the main website URL. All currently-available request paths are listed below. A [data dictionary](../data) is available to assist users in parsing results returned by the API.

| Method      | Path                          | Collection     | Resource                  |
| :---------- | :---------------------------- | :------------- | :------------------------ |
| GET         | `/api`                        | N/A            | General API metadata.     |
| GET         | `/api/v0.6`                   | N/A            | General API metadata.     |
| GET         | `/api/v0.6/cbe`               | CBÉ            | List of manuscript volumes and associated metadata.* |
| GET         | `/api/v0.6/cbe/volumes`       | CBÉ            | Index of manuscript volumes and summary metadata. |
| GET         | `/api/v0.6/cbed`              | CBÉD           | List of persons and associated metadata. |
| GET         | `/api/v0.6/cbed/{id}`         | CBÉD           | Metadata associated with an individual person. |
| GET         | `/api/v0.6/cbed/occupations`  | CBÉD           | Reference list of metadata associated with occupations. |
| GET         | `/api/v0.6/cbeg`              | CBÉG           | List of photographs and associated metadata.** |
| GET         | `/api/v0.6/cbeg/{id}`         | CBÉG           | Metadata associated with an individual photograph. |
| GET         | `/api/v0.6/cbeg/topics/handbook`   | CBÉG           | Reference list of subject headings ([topics](https://www.duchas.ie/en/tpc/cbeg)) in Seán Ó Súilleabháin's *A Handbook of Irish Folklore*. |
| GET         | `/api/v0.6/cbes`              | CBÉS           | List of manuscript volumes and associated metadata.*** |
| GET         | `/api/v0.6/cbes/volumes`      | CBÉS           | Index of manuscript volumes and summary metadata. |
| GET         | `/api/v0.6/cbes/topics`       | CBÉS           | Reference list of topics from the [Schools' Collection Subject List](https://www.duchas.ie/en/tpc/cbes).
| GET         | `/api/v0.6/counties`          | N/A            | Reference list of metadata associated with Irish counties. |
| GET         | `/api/v0.6/countries`         | N/A            | Reference list of metadata associated with countries. |

**\*** Requests to the `/api/v0.6/cbe` endpoint must be filtered by at least one of the following parameters: `VolumeID`, `VolumeNumber`, `PageID`, `PartID`, `ItemID`,`CountyID`, `PlaceID`, `Country`, `GeoNameID`, `CollectorID`, `InformantID` or `PersonID`.

**\*\*** Requests to the `/api/v0.6/cbeg` endpoint must be filtered by at least one of the following parameters: `CountyID`, `PlaceID`, `Country`, `GeoNameID`, `PhotographerID`, `RelevantPersonID` or `PersonID`.

**\*\*\*** Requests to the `/api/v0.6/cbes` endpoint must be filtered by at least one of the following parameters: `VolumeID`, `VolumeNumber`, `PageID`, `PartID`, `ItemID`, `SchoolCountyID`, `SchoolPlaceID`, `TeacherID`, `CountyID`, `PlaceID`, `Country`, `GeoNameID`, `CollectorID`, `InformantID` or `PersonID`.

### URL path parameters

| Name          | Type          | Description    |
| :------------ | :------------ | :------------- |
| `id`          | integer       | Resource ID.    |

### URL query parameters

Use these query parameters to filter the results returned by the API.

#### The Main Manuscript Collection (CBÉ)

| Name          | Type          | Description    |
| :------------ | :------------ | :------------- |
| `Status`      | integer       | Filter by editorial status (0-4). **(Privileged)** |
| `VolumeNumber` | string        | Filter by manuscript volume archival reference (e.g. 0154). |
| `VolumeID`    | integer       | Filter by manuscript volume identifier. |
| `PageID`      | integer       | Filter by manuscript page identifier. |
| `PartID`      | integer       | Filter by manuscript part identifier. |
| `ItemID`      | integer       | Filter by manuscript item identifier. |
| `CollectorID` | integer       | Filter by collector's CBÉD identifier. |
| `InformantID` | integer       | Filter by informant's CBÉD identifier. |
| `RelevantPersonID` | integer       | Filter by person's CBÉD identifier. |
| `PersonID` | integer       | Filter by person's CBÉD identifier. This filter encompasses all person types (i.e. collector, informant, relevant person). |
| `CountyID`    | integer       | Filter by county using [logainm.ie](https://www.logainm.ie) placename identifier.  |
| `PlaceID`     | integer       | Filter by place using [logainm.ie](https://www.logainm.ie) placename identifier.  |
| `Country`     | ISO 3166 country code* | Filter by country using ISO code (e.g. DE, US, GB-ENG). |
| `GeoNameID`   | integer       | Filter by place using [GeoName](https://www.geonames.org) placename identifier.  |
| `Language`    | string        | Filter items by language using ISO 639-1 language code |
| `DateFrom`    | integer**     | Retrieve records associated with this year or later. |
| `DateTo`      | integer**     | Retrieve records associated with this year or earlier. |
| `DateAccuracy` | string       | Filter by accuracy of date record (i.e. `APPROX`, `INFER`, `QUESTION`). |
| `CreatedBefore` | ISO 8601 datetime | Retrieve records created before a given date in `YYYY-MM-DD` format. |
| `CreatedSince` | ISO 8601 datetime | Retrieve records created after a given date in `YYYY-MM-DD` format. |
| `ModifiedBefore` | ISO 8601 datetime | Retrieve records last updated before a given date in `YYYY-MM-DD` format. |
| `ModifiedSince` | ISO 8601 datetime | Retrieve records last updated after a given date in `YYYY-MM-DD` format. |

**\*Note:** The two-letter country codes accepted by the `Country` parameter conform to the [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html) standard. However, four additional ISO 3166-2 codes are accepted to facilitate differentiation between England, Northern Ireland, Scotland and Wales. These are, respectively: `GB-ENG`, `GB-NIR`, `GB-SCT` and `GB-WLS`.

**\*\*Note:** The `DateFrom` and `DateTo` parameters currently only accept years in `YYYY` format.

#### The Schools' Collection (CBÉS)

| Name          | Type          | Description    |
| :------------ | :------------ | :------------- |
| `Status`      | integer       | Filter by editorial status (0-4). **(Privileged)** |
| `VolumeNumber` | string        | Filter by manuscript volume archival reference (e.g. 0154). |
| `VolumeID`    | integer       | Filter by manuscript volume identifier. |
| `PageID`      | integer       | Filter by manuscript page identifier. |
| `PartID`      | integer       | Filter by manuscript part identifier. |
| `ItemID`      | integer       | Filter by manuscript item identifier. |
| `SchoolCountyID`    | integer       | Filter schools (i.e. manuscript parts) by county using [logainm.ie](https://www.logainm.ie) placename identifier.  |
| `SchoolPlaceID`     | integer       | Filter schools (i.e. manuscript parts) by place using [logainm.ie](https://www.logainm.ie) placename identifier.  |
| `TeacherID`   | integer       | Filter schools (i.e. manuscript parts) by teacher's CBÉS identifier. |
| `CollectorID` | integer       | Filter items by collector's CBÉS identifier. |
| `InformantID` | integer       | Filter items by informant's CBÉS identifier. |
| `PersonID`    | integer       | Filter items by person's CBÉS identifier. This filter encompasses both collectors and informants. |
| `CountyID`    | integer       | Filter items by county using [logainm.ie](https://www.logainm.ie) placename identifier.  |
| `PlaceID`     | integer       | Filter items by place using [logainm.ie](https://www.logainm.ie) placename identifier.  |
| `TopicID`     | integer       | Filter items by topic using CBÉS topic identifier. |
| `Language`    | string        | Filter items by language using ISO 639-1 language code. |
| `CreatedBefore` | ISO 8601 datetime | Retrieve records created before a given date in `YYYY-MM-DD` format. |
| `CreatedSince` | ISO 8601 datetime | Retrieve records created after a given date in `YYYY-MM-DD` format. |
| `ModifiedBefore` | ISO 8601 datetime | Retrieve records last updated before a given date in `YYYY-MM-DD` format. This includes new or updated page transcripts. |
| `ModifiedSince` | ISO 8601 datetime | Retrieve records last updated after a given date in `YYYY-MM-DD` format. This includes new or updated page transcripts. |

#### The Photographic Collection (CBÉG)

| Name          | Type          | Description    |
| :------------ | :------------ | :------------- |
| `Status`      | integer       | Filter by editorial status (0-4). **(Privileged)** |
| `Digitized`   | boolean       | Filter by digitization status. |
| `Copyright`   | string        | Filter by copyright holder (e.g. `CBE`, `UNK`). |
| `Condition`   | integer       | Filter by physical condition (0-3). |
| `HandbookTopic` | string        | Filter by *A Handbook of Irish Folklore* [subject code](https://www.duchas.ie/en/tpc/cbeg) (e.g. B005). |
| `PersonID`    | integer       | Filter by person's CBÉD identifier. |
| `PhotographerID` | integer       | Filter by photographer's CBÉD identifier. |
| `RelevantPersonID` | integer       | Filter by person's CBÉD identifier. |
| `CountyID`    | integer       | Filter by county using [logainm.ie](https://www.logainm.ie) placename identifier.  |
| `PlaceID`     | integer       | Filter by place using [logainm.ie](https://www.logainm.ie) placename identifier.  |
| `Country`     | ISO 3166 country code* | Filter by country using ISO code (e.g. DE, US, GB-ENG). |
| `GeoNameID`   | integer       | Filter by place using [GeoName](https://www.geonames.org) placename identifier.  |
| `DateFrom`    | integer**     | Retrieve records associated with this year or later. |
| `DateTo`      | integer**     | Retrieve records associated with this year or earlier. |
| `DateAccuracy` | string       | Filter by accuracy of date record (i.e. APPROX, INFER, QUESTION). |
| `CreatedBefore` | ISO 8601 datetime | Retrieve records created before a given date in `YYYY-MM-DD` format. |
| `CreatedSince` | ISO 8601 datetime | Retrieve records created after a given date in `YYYY-MM-DD` format. |
| `ModifiedBefore` | ISO 8601 datetime | Retrieve records last updated before a given date in `YYYY-MM-DD` format. |
| `ModifiedSince` | ISO 8601 datetime | Retrieve records last updated after a given date in `YYYY-MM-DD` format. |

**\*Note:** The two-letter country codes accepted by the `Country` parameter conform to the [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html) standard. However, four additional ISO 3166-2 codes are accepted to facilitate differentiation between England, Northern Ireland, Scotland and Wales. These are, respectively: `GB-ENG`, `GB-NIR`, `GB-SCT` and `GB-WLS`.

**\*\*Note:** The `DateFrom` and `DateTo` parameters currently only accept years in `YYYY` format.

#### The Persons Database (CBÉD)

| Name          | Type          | Description    |
| :------------ | :------------ | :------------- |
| `Gender`      | string        | Filter by person's gender (f, m).  |
| `AinmID`      | integer       | Filter by [ainm.ie](https://www.ainm.ie) entry ID.  |
| `ViafID`      | integer       | Filter by [VIAF](https://viaf.org/) entryID.  |
| `CountyID`    | integer       | Filter by county using [logainm.ie](https://www.logainm.ie) placename identifier.  |
| `PlaceID`     | integer       | Filter by place using [logainm.ie](https://www.logainm.ie) placename identifier.  |
| `Country`     | ISO 3166 country code* | Filter by country ISO code (e.g. `DE`, `US`, `GB-ENG`). |
| `GeoNameID`   | integer       | Filter by [GeoName](https://www.geonames.org) placename identifier.  |
| `Occupation`  | string        | Filter by occupation (e.g. `IASC`, `FEIRM`). |
| `BirthDateFrom` | integer**     | Retrieve records associated with this birth year or later. |
| `BirthDateTo` | integer**     | Retrieve records associated with this birth year or earlier. |
| `BirthDateAccuracy` | string       | Filter by accuracy of birth date record (i.e. APPROX, INFER, QUESTION). |
| `DeathDateFrom` | integer**     | Retrieve records associated with this death year or later. |
| `DeathDateTo` | integer**     | Retrieve records associated with this death year or earlier. |
| `DeathDateAccuracy` | string       | Filter by accuracy of death date record (i.e. APPROX, INFER, QUESTION). |
| `CreatedBefore` | ISO 8601 datetime | Retrieve records created before a given date in `YYYY-MM-DD` format. |
| `CreatedSince` | ISO 8601 datetime | Retrieve records created after a given date in `YYYY-MM-DD` format. |
| `ModifiedBefore` | ISO 8601 datetime | Retrieve records last updated before a given date in `YYYY-MM-DD` format. |
| `ModifiedSince` | ISO 8601 datetime | Retrieve records last updated after a given date in `YYYY-MM-DD` format. |

**\*Note:** The two-letter country codes accepted by the `Country` parameter conform to the [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html) standard. However, four additional ISO 3166-2 codes are accepted to facilitate differentiation between England, Northern Ireland, Scotland and Wales. These are, respectively: `GB-ENG`, `GB-NIR`, `GB-SCT` and `GB-WLS`.

**\*\*Note:** The `DateFrom` and `DateTo` parameters currently only accept years in `YYYY` format.

### Illustrative examples

Below is a non-exhaustive list of valid API request URLs, provided for demonstration purposes:

- `https://www.duchas.ie/api/v0.6/cbe/?VolumeID=7000256`
- `https://www.duchas.ie/api/v0.6/cbe/?PersonID=315678581`
- `https://www.duchas.ie/api/v0.6/cbed/315678333`
- `https://www.duchas.ie/api/v0.6/cbed/1740563`
- `https://www.duchas.ie/api/v0.6/cbed/?ModifiedSince=2019-01-01`
- `https://www.duchas.ie/api/v0.6/cbed/?PlaceID=35176`
- `https://www.duchas.ie/api/v0.6/cbed/?Gender=f&CountyID=100013`
- `https://www.duchas.ie/api/v0.6/cbed/?Country=AU`
- `https://www.duchas.ie/api/v0.6/cbed/?GeoNameID=2177413`
- `https://www.duchas.ie/api/v0.6/cbed/?PlaceID=130443&Occupation=IASC`
- `https://www.duchas.ie/api/v0.6/cbeg/974`
- `https://www.duchas.ie/api/v0.6/cbeg/?CountyID=100009&ModifiedSince=2018-09-01`
- `https://www.duchas.ie/api/v0.6/cbeg/?Status=4&CountyID=100023`
- `https://www.duchas.ie/api/v0.6/cbeg/?Copyright=UNK&PhotographerID=93573082`
- `https://www.duchas.ie/api/v0.6/cbeg/?HandbookTopic=E&PhotographerID=93573082&Digitized=false`
- `https://www.duchas.ie/api/v0.6/cbeg/?HandbookTopic=B006&CountyID=100023`
- `https://www.duchas.ie/api/v0.6/cbeg/?CountyID=100024&DateFrom=1960&DateTo=1969&DateAccuracy=APPROX`
- `https://www.duchas.ie/api/v0.6/cbes/?VolumeNumber=0133`
- `https://www.duchas.ie/api/v0.6/cbes/?CountyID=100002&TopicID=5192275&Language=en`
- `https://www.duchas.ie/api/v0.6/cbes/?PlaceID=18689`
- `https://www.duchas.ie/api/v0.6/cbes/topics`
- `https://www.duchas.ie/api/v0.6/counties`
