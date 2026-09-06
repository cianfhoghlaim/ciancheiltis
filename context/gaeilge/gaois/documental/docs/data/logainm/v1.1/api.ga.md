---
title: Comhéadan feidhmchláir Logainm (Leagan 1.1)
shortTitle: Comhéadan feidhmchláir
description: Doiciméadacht forbróra i gcomhair API Logainm
keywords: Logainm, API, logainmneacha, logainmníocht, ainmeolaíocht, Gaeilge, Fiontar & Scoil na Gaeilge, DCU
resource: Logainm
order: 1
public: true
---

## Réamhrá

Chruthaigh grúpa taighde Gaois in [Fiontar & Scoil na Gaeilge](https://www.dcu.ie/fiontar_scoilnagaeilge/gaeilge/index.shtml) Bunachar Logainmneacha na hÉireann i gcomhar leis [an mBrainse Logainmneacha](https://www.chg.gov.ie/gaeltacht/the-irish-language/the-placenames-branch/) (An Roinn Cultúir, Oidhreachta agus Gaeltachta). Áis chuimsitheach bhainistíochta í seo chun sonraí agus taifid chartlainne, mar aon le taighde logainmneacha an Stáit, a riar. Áis don phobal atá inti, d'Éireannaigh sa bhaile agus thar lear, agus spreagann sí spéis i saibhreas agus i saíocht logainmneacha na hÉireann. Seoladh an bunachar sonraí ar shuíomh gréasáin poiblí [logainm.ie](https://www.logainm.ie) in 2008. Déantar cur síos sa doiciméad seo ar Chomhéadan Feidhmchláir (API) gréasánbhunaithe a nochtann a bhfuil sa bhunachar sonraí d’iarratais ó ríomhchláir. Tá [foclóir sonraí](../data) ar fáil chun cabhrú le húsáideoirí torthaí a fhaightear ón API a pharsáil.  
 
## Eolas ginearálta faoi API

Téigh i gcomhairle leis an [mbuntreoir](/ga/data/getting-started) i dtaca le hacmhainní sonraí oscailte Gaois sula léann tú an chuid eile de na doiciméid a bhaineann le API Logainm. Déantar cur síos sa treoir ar an gcaoi a bhfaightear faisnéis aitheantais an úsáideora agus ar an gcaoi a gcuirtear eolas tábhachtach úsáide ar fáil.

## Cosáin acmhainne

Faightear rochtain ar na hacmhainní a chuireann an API ar fáil trí na cosáin uathúla atá iarcheangailte le hóstainm an phríomhshuímh gréasáin. Liostaítear thíos gach cosán iarratais atá ar fáil faoi láthair. Tá [foclóir sonraí](../data) ar fáil chun cabhrú le húsáideoirí torthaí a fhaightear ón API a pharsáil.

**Nua**: Anois is féidir API Logainm a cheadú trí úsáid a bhaint as comhéadan grafach darb ainm [Swagger UI](https://www.logainm.ie/api/swagger/index.html) (eochair API ag teastáil).

| Modh        | Cosán                         | Acmhainn                  |
| :---------- | :---------------------------- | :------------------------ |
| GET         | `/api`                        | Meiteashonraí ginearálta API.     |
| GET         | `/api/v1.1`                   | Liosta áiteanna agus meiteashonraí gaolmhara.**\*** |
| GET         | `/api/v1.1/{id}`              | Meiteashonraí a bhaineann le háit ar leith. |
| GET         | `/api/v1.1/administrative-units` | Liosta tagartha de mheiteashonraí a bhaineann le [haonaid riaracháin na hÉireann](https://www.logainm.ie/ga/inf/help-categs). Is féidir na haitheantóirí aonaid sa liosta seo a úsáid chun áiteanna a scagadh de réir `CategoryID`. |
| GET         | `/api/v1.1/features`          | Liosta tagartha de mheiteashonraí a bhaineann le gnéithe geografacha. Is féidir na haitheantóirí gné sa liosta seo a úsáid chun áiteanna a scagadh de réir `CategoryID`. |
| GET         | `/api/v1.1/glossary`          | Liosta tagartha de na [focail choitianta i logainmneacha na hÉireann](https://www.logainm.ie/ga/gls/) agus de mheiteashonraí gaolmhara. Is féidir na haitheantóirí gluaise sa liosta seo a úsáid chun áiteanna a scagadh de réir `GlossaryID`. |
| GET         | `/api/v1.1/counties`          | Liosta tagartha de mheiteashonraí a bhaineann le contaetha. Is féidir na haitheantóirí áite sa liosta seo a úsáid chun áiteanna a scagadh de réir `PlaceID`. |

### Paraiméadair chosáin URL

| Ainm          | Cineál        | Cur síos       |
| :------------ | :------------ | :------------- |
| `id`          | slánuimhir    | ID na hacmhainne.   |

### Paraiméadair iarratais URL 

Úsáid na paraiméadair iarratais seo chun na torthaí a fhaightear ón API a scagadh.

| Ainm          | Cineál          | Cur síos       |
| :------------ | :-------------- | :------------- |
| `Page`        | slánuimhir      | Sonraítear an uimhir leathanaigh reatha. Tosaíonn uimhreacha leathanach ar a haon (i.e. níl leathanaigh náid-innéacsaithe). |
| `PerPage`     | slánuimhir      | Sonraítear líon na dtorthaí a thugtar in aghaidh an leathanaigh mar fhreagra ar iarratas a bhfuil uimhriú leathanach i bhfeidhm air. Is é 1,000 an luach réamhshocraithe. Is é 1,000 an t-uasluach atá ceadaithe. |
| `PlaceID`     | slánuimhir      | Scag de réir aitheantóir áite. Mar shampla, tagtar ar gach áit i gContae Dhún na nGall ach `PlaceID` de `100013` a chur isteach. |
| `CategoryID`  | teaghrán        | Scag de réir aitheantóir na catagóire áite, lena n-áirítear aonad riaracháin nó gné gheografach. |
| `GlossaryID`  | slánuimhir      | Scag de réir aitheantóir na hiontrála gluaise. |
| `ExcludeStreets` | Boole          | Má tá sé fíor, ná cuir áiteanna a bhfuil `CategoryID` de `SR` (sráideanna) ón tacar torthaí leo. D'fhéadfadh sráideanna cur go mór le méid an tacair torthaí agus, dá bharr sin, d'fhéadfadh sé cur leis an aga freagartha a bhaineann le háiteanna a gcuimsítear iontu ceantair mhóra uirbeacha. |
| `Latitude`    | float           | Scag de réir comhordanáid domhanleithid. Caithfear é a úsáid i gcomhar le luach `Longitude`. |
| `Longitude`   | float           | Scag de réir comhordanáid domhanfhaid. Caithfear é a úsáid i gcomhar le luach `Latitude`. |
| `Accurate`    | Boole           | Má tá sé fíor, ná cuir ach áiteanna a gcreidtear go bhfuil a gcuid comhordanáidí geografacha beacht ar ais. Má tá sé bréagach, ná cuir ach áiteanna a bhfuarthas a gcuid comhordanáidí geografacha trí eachtarshuí ó áiteanna in aice láimhe, nó ar díorthaíodh a gcuid comhordanáidí ó thagairt de chuid Eangach na hÉireann, ar ais. |
| `Radius`      | slánuimhir      | Sonraítear méid an gha a bhaineann leis an iarratas geografach i méadair. Is é 15,000 an t-uasmhéid do gha ar bith. Is é 3,000 an luach réamhshocraithe. |
| `Query`       | teaghrán        | Scag de réir téarma(í) cuardaigh. Tá cuardaigh théacs íogair ó thaobh an tsínte fhada de, mar shampla, faightear torthaí difriúla ó na téarmaí cuardaigh 'Rath' agus 'Ráth'. Tabhair faoi deara nach bhfaightear ach meaitseálacha cruinne ar théarmaí iarratais trí chuardaigh théacs. D'fhéadfadh meaitseálacha páirteacha nó tuairimeacha a bheith sa réimse freagartha `SimilarNames`. |
| `Gaeltacht`   | Boole           | Má tá sé fíor, ná cuir ach áiteanna atá i gceantar Gaeltachta ar ais. Má tá sé bréagach, ná cuir áiteanna atá i gceantair Ghaeltachta san áireamh sa tacar torthaí. |
| `PostOffice`  | Boole           | Má tá sé fíor, ná cuir ach áiteanna ina bhfuil, nó ina raibh, oifig an phoist ar ais. Má tá sé bréagach, ná cuir áiteanna ina bhfuil, nó ina raibh, oifig an phoist san áireamh sa tacar torthaí. |
| `NorthernIreland` | Boole          | Má tá sé fíor, ná cuir ach áiteanna atá i dTuaisceart Éireann ar ais. Má tá sé bréagach, ná cuir áiteanna atá i dTuaisceart Éireann san áireamh sa tacar torthaí. |
| `CreatedBefore` | am-dháta ISO 8601 | Aisghabh taifid a cruthaíodh roimh dháta ar leith i bhformáid `YYYY-MM-DD`. |
| `CreatedSince` | am-dháta ISO 8601 | Aisghabh taifid a cruthaíodh i ndiaidh dáta ar leith i bhformáid `YYYY-MM-DD`. |
| `ModifiedBefore` | am-dháta ISO 8601 | Aisghabh taifid a nuashonraíodh roimh dháta ar leith i bhformáid `YYYY-MM-DD`. |
| `ModifiedSince` | am-dháta ISO 8601 | Aisghabh taifid a nuashonraíodh i ndiaidh dáta ar leith i bhformáid `YYYY-MM-DD`. |

## Uimhriú leathanach

Nuair a thugtar liosta oibiachtaí mar fhreagra ar iarratas ar API Logainm cuirtear uimhriú leathanach i bhfeidhm ar an liosta. Sa chás go bhfuil níos mó torthaí ann ná uaslíon torthaí réamhshocraithe déantar na torthaí a roinnt ina ‘leathanaigh’. Seoltar iarratas API ar leith i gcás gach leathanaigh. Cinntíonn an t-uimhriú leathanach go mbaineann feidhmíocht chobhsaí iontaofa leis an API, is cuma cad é an líon iomlán torthaí a aimsítear. Mura socraítear paraiméadair leathanaigh ar bith tabharfar an chéad leathanach torthaí mar fhreagra agus uaslíon 1,000 toradh in aghaidh an leathanaigh i bhfeidhm. Is féidir líon na dtorthaí a thugtar in aghaidh an leathanaigh a chumrú ach an paraiméadar iarratais `PerPage` a shocrú. 

## Sórtáil

Nuair a fhaightear sonraí a bhaineann le níos mó ná áit amháin mar fhreagra ar iarratas, sórtáiltear de réir an aitheantóra áite, in ord ardaitheach, iad. An t-aon eisceacht uaidh seo ná iarratais gheografacha, ina sonraítear na paraiméadair iarratais `Latitude` agus `Longitude`. Sa chás seo, liostaítear áiteanna de réir gaireachta do na comhordanáidí sonraithe agus liostaítear na háiteanna is gaire ar dtús.  

## Samplaí léiritheacha

Seo thíos liosta, nach bhfuil uileghabhálach, d'aimsitheoirí aonfhoirmeacha acmhainne bailí mar léiriú ar iarratais API:

- `https://www.logainm.ie/api/v1.1/?PlaceID=100013&Page=2&PerPage=200`
- `https://www.logainm.ie/api/v1.1/?PlaceID=100009&CategoryID=PAR`
- `https://www.logainm.ie/api/v1.1/?PlaceID=100002&ModifiedSince=2022-01-01`
- `https://www.logainm.ie/api/v1.1/?PlaceID=100001&CategoryID=SRB&ModifiedSince=2021-01-01`
- `https://www.logainm.ie/api/v1.1/?Latitude=53.3693445&Longitude=-6.271958104774972&Radius=10000&CategoryID=PAR`
- `https://www.logainm.ie/api/v1.1/?GlossaryID=58`
- `https://www.logainm.ie/api/v1.1/?PlaceID=100024&Gaeltacht=true`
- `https://www.logainm.ie/api/v1.1/?PlaceID=100010&ExcludeStreets=true`
- `https://www.logainm.ie/api/v1.1/?Query=Carrick&PlaceID=100029`
- `https://www.logainm.ie/api/v1.1/1412322`
- `https://www.logainm.ie/api/v1.1/1411548`
- `https://www.logainm.ie/api/v1.1/14448`
- `https://www.logainm.ie/api/v1.1/1384618`
- `https://www.logainm.ie/api/v1.1/26783`
- `https://www.logainm.ie/api/v1.1/1375542`
- `https://www.logainm.ie/api/v1.1/2425`
- `https://www.logainm.ie/api/v1.1/administrative-units/`
- `https://www.logainm.ie/api/v1.1/features/`
- `https://www.logainm.ie/api/v1.1/glossary/`
- `https://www.logainm.ie/api/v1.1/counties/`
