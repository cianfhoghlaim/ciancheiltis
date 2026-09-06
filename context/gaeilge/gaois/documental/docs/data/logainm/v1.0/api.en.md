---
title: Logainm Application Programming Interface (Version 1.0)
shortTitle: API
description: Developer documentation for the Logainm API
keywords: Logainm, API, placenames, toponmy, onomastics, Irish language, Fiontar & Scoil na Gaeilge, DCU
resource: Logainm
order: 1
public: true
---

## Introduction

The Placenames Database of Ireland was created by the Gaois research group in [Fiontar & Scoil na Gaeilge](https://www.dcu.ie/fiontar_scoilnagaeilge/gaeilge/index.shtml) in collaboration with [The Placenames Branch](https://www.chg.gov.ie/gaeltacht/the-irish-language/the-placenames-branch/) (Department of Culture, Heritage and the Gaeltacht). This is a comprehensive management system for data, archival records and placenames research conducted by the State. It is a public resource for Irish people at home and abroad, and for all those who appreciate the rich heritage of Irish placenames. The database has been accessible via the [logainm.ie](https://www.logainm.ie) public website since 2008. This documentation describes a web-based Application Programming Interface (API) that exposes the database contents to programmatic queries. A [data dictionary](../data) is available to assist users in parsing results returned by the API.

## General API information

Please consult the [getting started guide](/en/data/getting-started) for Gaois open data resources before reading the rest of the documentation for the Logainm API. The getting started guide describes how to obtain your unique user credentials as well as providing important general usage information.

## Resource paths

The resources provided by the API are accessed via unique paths appended to the main website hostname. All currently-available request paths are listed below. A [data dictionary](../data) is available to assist users in parsing results returned by the API.

| Method      | Path                          | Resource                  |
| :---------- | :---------------------------- | :------------------------ |
| GET         | `/api`                        | General API metadata.     |
| GET         | `/api/v1.0`                   | List of places and associated metadata.**\*** |
| GET         | `/api/v1.0/{id}`              | Metadata associated with an individual place. |
| GET         | `/api/v1.0/administrative-units` | Reference list of metadata associated with [Irish administrative units](https://www.logainm.ie/en/inf/help-categs). The unit identifiers in this list can be used to filter places by `CategoryID`. |
| GET         | `/api/1.0/features`          | Reference list of metadata associated with geographical features. The feature identifiers in this list can be used to filter places by `CategoryID`. |
| GET         | `/api/v1.0/glossary`          | Reference list of [words commonly found in Irish placenames](https://www.logainm.ie/en/gls/) and associated metadata. The glossary identifiers in this list can be used to filter places by `GlossaryID`. |
| GET         | `/api/v1.0/counties`          | Reference list of metadata associated with counties. The place identifiers in this list can be used to filter places by `PlaceID`. |

### URL path parameters

| Name          | Type          | Description    |
| :------------ | :------------ | :------------- |
| `id`          | integer       | Resource ID.   |

### URL query parameters

Use these query parameters to filter the results returned by the API.

| Name          | Type          | Description    |
| :------------ | :------------ | :------------- |
| `Page`        | integer       | Specifies the current page number. Page numbers start at one (i.e. pages are not zero indexed). |
| `PerPage`     | integer       | Specifies the count of results to be returned per page in a paginated query. Defaults to 1,000. The maximum value allowed is 1,000. |
| `PlaceID`     | integer       | Filter by place identifier. For example, a `PlaceID` of `100013` returns all of the places in County Donegal. |
| `CategoryID`  | string        | Filter by place category identifier, such as an administrative unit or geographical feature. |
| `GlossaryID`  | integer       | Filter by glossary entry identifier. |
| `ExcludeStreets` | boolean       | If true, exclude places with a `CategoryID` of `SR` (streets) from the result set. Streets can add greatly to the size of the result set and, consequently, the response time when querying places that include large urban areas. |
| `Latitude`    | float         | Filter by latitudinal coordinate. Must be used in conjunction with a `Longitude` value. |
| `Longitude`   | float         | Filter by longitudinal coordinate. Must be used in conjunction with a `Latitude` value. |
| `Accurate`    | boolean       | If true, only return places whose geographic coordinates are believed to be precise. If false, only return places whose geographic coordinates were obtained by extrapolation from neighbouring places. |
| `Radius`      | integer       | Specifies the radius size for a geographic query in metres. The maximum radius is 15,000. Defaults to 3,000 metres. |
| `Query`       | string        | Filter by search term(s). Textual searches are accent sensitive, for example, the search terms 'Rath' and 'Ráth' each return different sets of results. Note that textual searches currently only retrieve exact matches for query terms. Partial or speculative matches may be detailed in the `SimilarNames` response field. |
| `Gaeltacht`   | boolean       | If true, only return places which are in a Gaeltacht area. If false, exclude places in Gaeltacht areas from the result set. |
| `PostOffice`  | boolean       | If true, only return places in which there is, or once was, a post office. If false, exclude places in which there is, or once was, a post office from the result set. |
| `NorthernIreland` | boolean       | If true, only return places which are in Northern Ireland. If false, exclude places which are in Northern Ireland from the result set. |
| `CreatedBefore` | ISO 8601 datetime | Retrieve records created before a given date in `YYYY-MM-DD` format. |
| `CreatedSince` | ISO 8601 datetime | Retrieve records created after a given date in `YYYY-MM-DD` format. |
| `ModifiedBefore` | ISO 8601 datetime | Retrieve records last updated before a given date in `YYYY-MM-DD` format. |
| `ModifiedSince` | ISO 8601 datetime | Retrieve records last updated after a given date in `YYYY-MM-DD` format. |

## Pagination

Where a list of objects is returned in response to a request to the Logainm API the list will be paginated. This means that when the number of results exceeds a certain count the results are split across a number of ‘pages’. Pages are accessed by separate API requests. This helps ensure consistent and reliable performance regardless of the total result count. If no page parameters are specified the first page of results will be returned with a maximum count of 1,000 results per page. The number of results returned per page can be configured via the `PerPage` query parameter.

## Sorting

Where data relating to more than one place is returned in response to a query it is sorted by place identifier, in ascending order. The only exception to this are geographic queries, where the `Latitude` and `Longitude` query parameters are specified, in which case places are listed in order of proximity to the specified coordinates, with the nearest places listed first.

## Illustrative examples

Below is a non-exhaustive list of valid API request URLs, provided for demonstration purposes:

- `https://www.logainm.ie/api/v1.0/?PlaceID=100013&Page=2&PerPage=200`
- `https://www.logainm.ie/api/v1.0/?PlaceID=100009&CategoryID=PAR`
- `https://www.logainm.ie/api/v1.0/?PlaceID=100002&ModifiedSince=2019-01-01`
- `https://www.logainm.ie/api/v1.0/?PlaceID=100001&CategoryID=SRB&ModifiedSince=2017-01-01`
- `https://www.logainm.ie/api/v1.0/?Latitude=53.3693445&Longitude=-6.271958104774972&Radius=10000&CategoryID=PAR`
- `https://www.logainm.ie/api/v1.0/?GlossaryID=58`
- `https://www.logainm.ie/api/v1.0/?PlaceID=100024&Gaeltacht=true`
- `https://www.logainm.ie/api/v1.0/?PlaceID=100010&ExcludeStreets=true`
- `https://www.logainm.ie/api/v1.0/?Query=Carrick&PlaceID=100029`
- `https://www.logainm.ie/api/v1.0/1412322`
- `https://www.logainm.ie/api/v1.0/1411548`
- `https://www.logainm.ie/api/v1.0/14448`
- `https://www.logainm.ie/api/v1.0/1384618`
- `https://www.logainm.ie/api/v1.0/26783`
- `https://www.logainm.ie/api/v1.0/1375542`
- `https://www.logainm.ie/api/v1.0/2425`
- `https://www.logainm.ie/api/v1.0/administrative-units/`
- `https://www.logainm.ie/api/v1.0/features/`
- `https://www.logainm.ie/api/v1.0/glossary/`
- `https://www.logainm.ie/api/v1.0/counties/`
