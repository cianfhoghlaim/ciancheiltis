---
title: Getting started with Gaois open data resources
shortTitle: Getting started
description: Information you need to know before interacting with Gaois open data resources
keywords: Gaois, API, authentication, terms, Fiontar & Scoil na Gaeilge, DCU
public: true
---

The [Gaois research group](https://www.gaois.ie) in [Fiontar & Scoil na Gaeilge](https://www.dcu.ie/fiontar_scoilnagaeilge/), DCU, in collaboration with our project partners, is making a number of open data resources available to the public. These include RESTful Application Programming Interfaces (APIs) and other data artifacts. Each of these resources is released under specific licencing conditions⁠: please read the appropriate licencing information, which accompanies the documentation for each resource on this website, before making use of the data.

The [Logainm API](/en/data/logainm/v1.0/api) is now publicly available and provides programmatic access to the Placenames Database of Ireland. Another API for the [Dúchas](/en/data/duchas/v0.5/api) project is currently in advanced development and a prerelease version is available. It is hoped to make further resources available in the future.

Gaois APIs share common usage, authentication, versioning and data protection patterns. The remainder of this document describes these patterns and should be read before proceeding to the specific documentation for each resource.

## API overview

Gaois APIs provide access to a number of resources by means of a defined URL schema. Specific resources are accessed via unique paths appended to the main website host. In some cases the resources that are returned may be filtered using optional query parameters. Attempts to access a resource provided by the API are referred to as requests. Following a successful request, resources are returned in the form of JSON. An unsuccessful attempt to access a resource will receive, at a minimum, a relevant HTTP status code in response to the request. An example of a valid API request is as follows:

> `https://www.logainm.ie/api/v1.0/1375542`

Users or applications (clients) requesting a resource via the API must authenticate their identity. This is achieved by providing an API Key with each request. Each client must obtain a unique API Key prior to interacting with the interface. Authentication is required to prevent abuse of the service and to track general usage statistics. Further details are provided below.

Gaois open data APIs support [Cross-Origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (CORS), meaning they can be used by client-side applications and in mobile browser environments. 

## API versioning

Multiple API versions are facilitated for all of our REST APIs. This means that more than one version of each API may be accessible at the same time. Newer API versions may offer additional resources or functionalities but may require a different request syntax to older versions. The target API version is indicated by the second path parameter in the request URL:

> /api/**v1.0**/glossary

Older versions will be supported for developer convenience: without versioning, changes to API syntax might cause dependent client applications to malfunction. We will endeavour to add new resources incrementally and will implement breaking changes only as a last resort. The API is versioned using [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) (semver) and follows the semver specification. For brevity, however, only major and minor version points are reflected in request URLs.

After a period of time it may become necessary to deprecate older API versions for maintenance or performance reasons. When you register for your Gaois developer account (see below), you will be asked if you are willing to receive communications from the Gaois research group from time to time. Agreeing to receive such communication means you will receive advance notice of any such changes.

**Note:** Prerelease API versions (i.e. < v1.0) are for testing purposes and will not be maintained once a v1.0 release has been reached.

## API authentication

Clients requesting a resource via the API are required to authenticate their identity. This is achieved by passing an API Key to the service with each request. Authentication offers some protection to the service provider from abuse of the API involving request overloads. It also allows us to retain some usage statistics, with a view to performance monitoring and service enhancement. Learn more about the data we retain in the following sections.

### How to obtain your API Key

Visit the 'Gaois Developer Hub' at [gaois.ie](https://www.gaois.ie/en/technology/developers/). Log in or register to create an account and you will be able to generate an API Key.

### How to pass your API Key

Your API Key may be passed to the service in a few different ways. Choose whichever method is easiest for you.

#### HTTP header

Pass the API Key into an `X-Api-Key` header:

> `'X-Api-Key: <API_KEY_HERE>' 'https://www.logainm.ie/api/v1.0/1384618'`

#### GET query parameter

Pass the API Key into an `apiKey` GET query string parameter:

> `'https://www.logainm.ie/api/v1.0/1384618?apiKey=API_KEY_HERE'`

**Note:** The GET query parameter may be used for non-GET requests (such as POST and PUT).

#### HTTP Basic Authentication

As an alternative, pass the API Key as the username (with an empty password) using HTTP basic authentication:

> `'https://API_KEY_HERE@www.logainm.ie/api/v1.0/1384618'`

## Security

The API is served over a HTTPS protocol. Though HTTP requests to the service are automatically redirected to HTTPS, you should only ever interact with the API using HTTPS-prefixed URLs.

While HTTPS offers a significant level of security, we would stress that the basic authentication methods described above do not amount to end-to-end encryption. **You should only ever pass your API Key to the service** — never include sensitive data, particularly passwords, as part of your requests.

## HTTP status codes

The status of all API requests will be communicated, in the first instance, via standard HTTP status codes. We recommend that any applications interacting with our APIs handle the following status codes:

| Code  | Definition            | Further information |
| :---- | :-------------------- | :------------------ |
| 200   | OK                    | One or more JSON objects will be returned. |
| 400   | BAD REQUEST           | The request syntax was invalid — a JSON object describing the error may be returned. |
| 401   | UNAUTHORISED          | A valid API Key was not provided. |
| 404   | NOT FOUND             | The resource does not exist. |
| 500   | INTERNAL SERVER ERROR | Please contact us at [gaois@dcu.ie](mailto:gaois@dcu.ie) quoting the request path. |

## Data retention and data protection

We store the following data every time a request is made to one of our APIs:

1. Request path
2. Response status code
3. Result count
4. Query response time
5. Client ID (obtained with reference to the provided API Key)

The client ID links your request to the data you have stored in the 'Gaois Developer Hub' (the data you provided when you signed up for the service, for example). You can view all of the above data at any time in the 'Gaois Developer Hub'. These data are stored by the Gaois research group, Fiontar & Scoil na Gaeilge, DCU in a GDPR-compliant manner.

We reserve the right to report and/or publish aggregated or anonymised API query metrics. We will not report, publish or share any specific client data (i.e. your client ID or any associated client identification data) with any third party. We reserve the right to retain data items 1–4, listed above, indefinitely for the purposes of performance monitoring, research and service enhancement.

You are entitled to have your personal data removed from our systems at any time. This means deleting your name, password, e-mail address, organisational affiliation and association with stored requests, completely and permanently. You can delete your developer account, and all associated personal data, on the ['Gaois Developer Hub'](https://www.gaois.ie/en/technology/developers/).

By accessing any of our APIs you agree to abide by all policies and practices outlined in this document.
