---
title: Changelog
shortTitle: Changelog
description: A record of changes to the Logainm API
keywords: Logainm, API, placenames, toponmy, onomastics, Irish language, Fiontar & Scoil na Gaeilge, DCU
resource: Logainm
order: 4
toc: false
public: true
---

## **v1.1.0** / 2024-02-21

This release marks a significant update to the Logainm API's underlying data set. It brings the data made available via the API into alignment with those available on the new [logainm.ie](https://www.logainm.ie) public website, released in May 2022, with both technical solutions now drawing on the same live data source. API users should benefit from:

- More precise and more plentiful geographic data (i.e. centrepoint longitude and latitude coordinates and Irish Grid references) accompanying the place entries.
- Further improved performance.
- [Links](/en/data/logainm/v1.1/data#link) with additional external resources from [Ordnance Survey Northern Ireland](https://www.nidirect.gov.uk/campaigns/ordnance-survey-of-northern-ireland) and [Cavan Townlands](https://cavantownlands.com/).
- [Links](/en/data/logainm/v1.1/data#folklorelink) with three more collections from the [Dúchas](https://www.duchas.ie) project to digitize the National Folklore Collection of Ireland; The Main Manuscript Collection, The Photographic Collection and The Audio Collection. This is in addition to links with the Schools' Collection which were previously available.

### Added

- The API can now be explored using the graphical [Swagger interface](https://www.logainm.ie/api/swagger/index.html) (API key required).
- A new property `Source` was added to the [`geography`](/en/data/logainm/v1.1/data#geography) object. This indicates the source from which, or the means by which, geographic data associated with a place were obtained.

### Changed

- Properties with null values are now omitted from API responses. This reduces the response payload size. As this is [per specification](/en/data/logainm/v1.1/data) it does not constitute a breaking change.

### Deprecated

- Ordnance Survey Ireland (OSI) is now known as [Tailte Éireann](https://tailte.ie/). Future API versions will likely update references to geographic data sources and resource links associated with OSI to reflect this change.

## **v1.0.1** / 2021-01-21

### Changed

Non-breaking changes:

- Fixed an issue where specific queries for individual place records returned an error due to a null `gridReference` property.
- Fixed an issue where queries for individual place records that did not exist returned a 500 HTTP status code instead of the appropiate 404 status code.

### Removed

- Removed support for API v0.9 (pre-release version).

## **v1.0.0** / 2020-07-05

This update marks the official public release of the Logainm API.

### Changed

Breaking changes:

- Pagination is now enforced for all requests to API endpoints returning a list of results. If no page parameters are specified the first page of results will be returned with a maximum count of 1,000 results per page. This helps ensure consistent and reliable performance regardless of the total result count.
- All API endpoints returning a list of objects now provide metadata regarding the total count of results and pagination. For reference lists, returned from the `/api/v1.0/administrative-units`, `/api/v1.0/features`, `/api/v1.0/glossary` and `/api/v1.0/counties` endpoints, this means that results are now nested in a `results` property.
- The `places` property of the [`placeList`](/en/data/logainm/v1.0/data) object has been renamed to `results`. This provides better consistency with other list object types.

Other changes:

- Updated documentation and data dictionary to reflect changes.

### Removed

- Removed support for API v0.5.

### Deprecated

- API v0.9, as a prerelease API version, is now deprecated and will be removed on September 1st, 2020.

---

## **v0.9.3** / 2020-02-08

### Added

- The Logainm API now supports [Cross-Origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (CORS).

### Changed

- Updated the [getting started](/en/data/getting-started) documentation to reflect CORS support.

---

## **v0.9.2** / 2020-01-20

### Changed

- Improved accuracy of geographic queries, particulary in respect of coordinates associated with street names.
- URI strings in `Image` and `Audio` objects are now properly escaped.

---

## **v0.9.1** / 2019-11-18

### Added

- `Page` and `PerPage` query parameters to facilitate pagination of place result sets.
- `TotalPages`, `CurrentPage` and `CountPerPage` properties to the `placeList` result object, to be displayed when the result set is paginated.
- Additional descriptive error messages related to pagination (e.g. for index out of range-type errors).

### Changed

- Updated documentation and data dictionary to reflect the above additions.
- Both 400 and 404 errors now return descriptive error messages in JSON format in addition to the appropriate HTTP status codes.