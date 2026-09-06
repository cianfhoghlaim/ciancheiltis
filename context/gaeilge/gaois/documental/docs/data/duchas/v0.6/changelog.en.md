---
title: Changelog
shortTitle: Changelog
description: A record of changes to the Dúchas API
keywords: Dúchas, API, folklore, history, storytelling, Irish language, Fiontar & Scoil na Gaeilge, DCU
resource: Dúchas
order: 4
toc: false
public: true
---

## **v0.6.0** / 2021-01-22

### Changed

Breaking change:

- The `editorsPick` property associated with `photograph` and manuscript `item` objects now has a cardinality of 'none or one or many' (previously 'none or one') and is represented by an array in JSON. This accounts for the fact that these types of entries may be selected as an editor's pick on more than one occasion.

## **v0.5.3** / 2020-02-08

### Added

- The Dúchas API now supports [Cross-Origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (CORS).

### Changed

- Updated the [getting started](/en/data/getting-started) documentation to reflect CORS support.

---

## **v0.5.2** / 2019-10-24

### Changed

- The API is now accessible via the production www.duchas.ie domain. The documentation has been updated to remove references to the test domain.

---

## **v0.5.1** / 2019-07-08

### Added

- `DateCreated` and `DateModified` properties to all `page` objects in the Main Manuscript and Schools' Collections.

### Changed

- Fixed issue with slow response times/status 500 errors when querying the Main Manuscript and Schools' Collections using `CreatedBefore`, `CreatedSince`, `ModifiedBefore` or `ModifiedSince` query parameters.
- Queries to the Main Manuscript and Schools' Collections filtered with parameters other than `VolumeID` or `VolumeNumber` return only assigned pages with the response. That is to say, they include only pages which are assigned to a manuscript item or are marked as title pages. Blank pages are excluded from the response. This helps return relevant results and reduces response payload size. For consumers wishing to obtain both assigned and unassigned pages, it is recommended to iterate over the collections by volume ID. An index of volume IDs can be obtained from the `/cbe/volumes` and `/cbes/volumes` endpoints.
