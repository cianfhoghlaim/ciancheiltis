---
title: Comhéadan feidhmchláir Dúchas (Leagan 0.6)
shortTitle: Comhéadan feidhmchláir
description: Doiciméadacht forbróra i gcomhair API Dúchas
keywords: Dúchas, comhéadan feidhmchláir, béaloideas, stair, scéalaíocht, Fiontar & Scoil na Gaeilge, DCU
resource: Dúchas
order: 1
public: true
---

**Tabhair faoi deara:** Déantar cur síos sa doiciméad seo ar leagan **réamheisiúna** de API Dúchas. Tá gnéithe á gcur leis ar bhonn leanúnach. Déanfar athbhreithniú ar an doiciméad seo roimh eisiúint v1.0. Cuirimid fáilte roimh aiseolas ag <gaois@dcu.ie>.

## Réamhrá

Cuireadh tionscadal Dúchas ar bun chun tús a chur le digitiú [Chnuasach Bhéaloideas Éireann](https://www.ucd.ie/irishfolklore/ga) (CBÉ), atá á choinneáil sa Choláiste Ollscoile, Baile Átha Cliath, Éire. Cuireadh torthaí na hoibre go dtí seo ar fáil go poiblí ar [duchas.ie](https://www.duchas.ie) agus tá siad á gcartlannú faoi láthair ag [Leabharlann Dhigiteach UCD](https://digital.ucd.ie/) chun iad a chaomhnú. Cuireann grúpa taighde Gaois in [Fiontar & Scoil na Gaeilge](https://www.dcu.ie/fiontar_scoilnagaeilge/), Ollscoil Chathair Bhaile Átha Cliath, an réiteach teicniúil seo ar fáil. Déantar cur síos sa doiciméad seo ar Chomhéadan Feidhmchláir (API) gréasánbhunaithe a nochtann an t-ábhar foilsithe ó d’iarratais ó ríomhchláir a dhéantar ar an mBailiúchán. Tá [foclóir sonraí](../data) ar fáil chun cabhrú le húsáideoirí torthaí a fhaightear ón API a pharsáil.      

### Cnuasach Bhéaloideas Éireann agus na bailiúcháin

Tá sonraí ó thrí cinn de na cúig mhórbhailiúchán béaloidis atá ag Cnuasach Bhéaloideas Éireann ar fáil tríd an ardán seo faoi láthair. Ach tuiscint a bheith agat ar a bhfuil sna bailiúcháin seo, cabhróidh sé leat úsáid a bhaint as an API. Tabhair faoi deara go dtagraítear do na bunachair sonraí a bhaineann leis na bailiúcháin seo i ngearrscríobh go minic ach acrainmneacha leithéid CBÉS, CBÉG, etc. a úsáid. Cruthaítear na hacrainmneacha seo de ghnáth ón ainm Gaeilge *Cnuasach Bhéaloideas Éireann* agus litir amháin ina dhiaidh sin a sheasann don bhunachar sonraí atá i gceist. Tagraíonn CBÉ do Phríomhbhailiúchán Lámhscríbhinní Chnuasach Bhéaloideas Éireann.  

#### An Príomhbhailiúchán Lámhscríbhinní (CBÉ)

Tá 2,400 imleabhar ceangailte le hábhar a bailíodh ó 1932 i leith sa Phríomhbhailiúchán Lámhscríbhinní. Thiomsaigh bailitheoirí lánaimseartha agus páirtaimseartha an chuid is mó de na himleabhair faoi choimirce Choimisiún Béaloideasa Éireann (1935-1971). Tá thart ar dhá thrian den ábhar as Gaeilge agus cuimsítear ann gach gné de thraidisiún béil na hÉireann. Tá digitiú á dhéanamh ar an mBailiúchán seo faoi láthair agus foilsíodh 337 imleabhar ar líne go dtí seo.  

#### Bailiúchán na Scol (CBÉS)

Thiomsaigh daltaí as 5,000 bunscoil i Saorstát Éireann tuairim is 740,000 leathanach (288,000 leathanach i mbunchóipleabhair na ndaltaí; 451,000 leathanach in imleabhair cheangailte) de bhéaloideas agus de sheanchas áitiúil idir 1937 agus 1939 mar chuid de *Scéim na Scol*. Tugtar ‘Bailiúchán na Scol’ ar an scéim seo go hiondúil. Tá 1,128 n-imleabhar, iad uimhrithe agus ceangailte, i mBailiúchán na Scol agus digitíodh iad ar fad.

#### An Bailiúchán Grianghraf (CBÉG)

Tá suas le 80,000 grianghraf i mbailiúchán Chnuasach Bhéaloideas Éireann, a bhformhór ó thréimhse Choimisiún Béaloideasa Éireann (1935-70) agus a chomharba, lena n-áirítear foireann CBÉ. Bíonn caomhnú agus digitiú an bhailiúcháin ar siúl i gcónaí.

#### An Bunachar Daoine (CBÉD)

Aithnítear daoine a ainmnítear laistigh de mheiteashonraí CBÉ agus CBÉG ach tagairt a dhéanamh d'oibiachtaí sa bhunachar sonraí seo. Ní mhapálann CBÉD go díreach le bailiúchán fisiciúil ar bith de chuid CBÉ. Ina áit sin, ós rud é go luaitear go leor daoine sna bailiúcháin éagsúla de chuid CBÉ – tá roinnt grianghrafadóirí in CBÉG ina mbailitheoirí in CBÉ, mar shampla – tá sé i gceist ag an mBunachar Daoine a bheith ina fhoinse aonair fírinne le haghaidh meiteashonraí pearsanta ar fud an tacair iomláin sonraí. Faoi láthair, cuimsíonn an Bunachar Daoine gach duine atá i gcodanna digitithe in CBÉ agus CBÉG. De bharr scóip thionscadal digitithe Bhailiúchán na Scol, ní raibh sé indéanta go dtí seo tacar normalaithe meiteashonraí pearsanta a bhaint - táthar ag súil go dtabharfar faoin obair seo arís amach anseo, áfach.

Tá tuilleadh eolais faoi CBÉ agus faoi na bailiúcháin ar fáil [anseo](https://www.duchas.ie/ga/info/cbe). 

## Eolas ginearálta API 

Téigh i gcomhairle leis an [mbuntreoir](/ga/data/getting-started) i dtaca le hacmhainní sonraí oscailte Gaois sula léann tú an chuid eile de na doiciméid a bhaineann le API Dúchas. Déantar cur síos sa treoir ar an gcaoi a bhfaightear faisnéis aitheantais an úsáideora agus ar an gcaoi a gcuirtear eolas tábhachtach úsáide ar fáil.  

## Pribhléidí rochtana API

Freastalaíonn API Dúchas ar chineálacha éagsúla tomhaltóirí, lena n-áirítear úsáideoirí poiblí, úsáideoirí cartlainne agus cliaint inmheánacha. Mar thoradh air seo, tugtar cead rochtana do gach úsáideoir API — a aithnítear óna Eochair API — de réir ár dTéarmaí Seirbhíse. Tá rochtain ag tomhaltóirí faoi phribhléid ar ábhar nach bhfuil réidh go fóill, nó a mheastar a bheith mí-oiriúnach, le foilsiú, agus ar mheiteashonraí inmheánacha eagarthóireachta. Is féidir leo freisin torthaí iarratais a scagadh de réir paraiméadair áirithe bhreise. Sna doiciméid a bhaineann leis an API, tugtar 'Faoi Phribhléid' ar mheiteashonraí agus ar pharaiméadair iarratais nach bhfuil ar fáil do thomhaltóirí poiblí. Má tá ceist ar bith agat maidir le do chuid pribhléidí reatha rochtana, [déan teagmháil linn](mailto:gaois@dcu.ie) le do thoil.  

## Cosáin acmhainne

Faightear rochtain ar acmhainní a chuireann an API ar fáil trí chosáin uathúla atá iarcheangailte le URL an phríomhshuímh gréasáin. Liostaítear na cosáin iarratais ar fad atá ar fáil faoi láthair thíos. Tá [foclóir sonraí](../data) ar fáil chun cabhrú le húsáideoirí torthaí a fhaightear ón API a pharsáil.  

| Modh        | Cosán                         | Bailiúchán     | Acmhainn                          |
| :---------- | :---------------------------- | :------------- | :-------------------------------- |
| GET         | `/api`                        | N/A            | Meiteashonraí ginearálta API.     |
| GET         | `/api/v0.6`                   | N/A            | Meiteashonraí ginearálta API.     |
| GET         | `/api/v0.6/cbe`               | CBÉ            | Liosta imleabhar lámhscríbhinne agus meiteashonraí gaolmhara.* |
| GET         | `/api/v0.6/cbe/volumes`       | CBÉ            | Innéacs imleabhar lámhscríbhinne agus meiteashonraí achoimre. |
| GET         | `/api/v0.6/cbed`              | CBÉD           | Liosta daoine agus meiteashonraí gaolmhara. |
| GET         | `/api/v0.6/cbed/{id}`         | CBÉD           | Meiteashonraí a bhaineann le duine ar leith. |
| GET         | `/api/v0.6/cbed/occupations`  | CBÉD           | Liosta tagartha de mheiteashonraí a bhaineann le gairmeacha. |
| GET         | `/api/v0.6/cbeg`              | CBÉG           | Liosta grianghraf agus meiteashonraí gaolmhara.** |
| GET         | `/api/v0.6/cbeg/{id}`         | CBÉG           | Meiteashonraí a bhaineann le grianghraf ar leith. |
| GET         | `/api/v0.6/cbeg/topics/handbook`   | CBÉG           | Liosta tagartha de cheannteidil ábhair ([topaicí](https://www.duchas.ie/ga/tpc/cbeg)) in *A Handbook of Irish Folklore* le Seán Ó Súilleabháin. |
| GET         | `/api/v0.6/cbes`              | CBÉS           | Liosta imleabhar lámhscríbhinne agus meiteashonraí gaolmhara.*** |
| GET         | `/api/v0.6/cbes/volumes`      | CBÉS           | Innéacs imleabhar lámhscríbhinne agus meiteashonraí achoimre. |
| GET         | `/api/v0.6/cbes/topics`       | CBÉS           | Liosta tagartha de thopaicí ó [Chlár Ábhar Bhailiúchán na Scol](https://www.duchas.ie/ga/tpc/cbes).
| GET         | `/api/v0.6/counties`          | N/A            | Liosta tagartha de mheiteashonraí a bhaineann le contaetha na hÉireann. |
| GET         | `/api/v0.6/countries`         | N/A            | Liosta tagartha de mheiteashonraí a bhaineann le tíortha. |

**\*** Caithfear iarratas ar an gcríochphointe `/api/v0.6/cbe` a scagadh de réir ceann amháin, ar a laghad, de na paraiméadair seo a leanas: `VolumeID`, `VolumeNumber`, `PageID`, `PartID`, `ItemID`,`CountyID`, `PlaceID`, `Country`, `GeoNameID`, `CollectorID`, `InformantID` nó `PersonID`.

**\*\*** Caithfear iarratas ar an gcríochphointe `/api/v0.6/cbeg` a scagadh de réir ceann amháin, ar a laghad, de na paraiméadair seo a leanas: `CountyID`, `PlaceID`, `Country`, `GeoNameID`, `PhotographerID`, `RelevantPersonID` nó `PersonID`.

**\*\*\*** Caithfear iarratas ar an gcríochphointe `/api/v0.6/cbes` a scagadh de réir ceann amháin, ar a laghad, de na paraiméadair seo a leanas: `VolumeID`, `VolumeNumber`, `PageID`, `PartID`, `ItemID`, `SchoolCountyID`, `SchoolPlaceID`, `TeacherID`, `CountyID`, `PlaceID`, `Country`, `GeoNameID`, `CollectorID`, `InformantID` nó `PersonID`.

### Paraiméadair chosáin URL

| Ainm          | Cineál           | Cur síos       |
| :------------ | :--------------- | :------------- |
| `id`          | slánuimhir       | ID na hacmhainne.    |

### Paraiméadair iarratais URL

Úsáid na paraiméadair iarratais seo chun na torthaí a fhaightear ón API a scagadh. 

#### An Príomhbhailiúchán Lámhscríbhinní (CBÉ)

| Ainm          | Cineál           | Cur síos       |
| :------------ | :--------------- | :------------- |
| `Status`      | slánuimhir       | Scag de réir an stádais eagarthóireachta (0-4). **(Faoi phribhléid)** |
| `VolumeNumber` | teaghrán        | Scag de réir thagairt cartlainne an imleabhair lámhscríbhinne (e.g. 0154). |
| `VolumeID`    | slánuimhir       | Scag de réir aitheantóir an imleabhair lámhscríbhinne. |
| `PageID`      | slánuimhir       | Scag de réir aitheantóir leathanaigh na lámhscríbhinne. |
| `PartID`      | slánuimhir       | Scag de réir aitheantóir coda na lámhscríbhinne. |
| `ItemID`      | slánuimhir       | Scag de réir aitheantóir míre na lámhscríbhinne. |
| `CollectorID` | slánuimhir       | Scag de réir aitheantóir CBÉD an bhailitheora. |
| `InformantID` | slánuimhir       | Scag de réir aitheantóir CBÉD an fhaisnéiseora. |
| `RelevantPersonID` | slánuimhir       | Scag de réir aitheantóir CBÉD an duine. |
| `PersonID` | slánuimhir       | Scag de réir aitheantóir CBÉD an duine. Cuimsíonn an scagaire seo gach cineál duine (i.e. bailitheoir, faisnéiseoir, duine ábhartha). |
| `CountyID`    | slánuimhir       | Scag de réir contae ach aitheantóir [logainm.ie](https://www.logainm.ie) a úsáid.  |
| `PlaceID`     | slánuimhir       | Scag de réir áite ach aitheantóir [logainm.ie](https://www.logainm.ie) a úsáid.  |
| `Country`     | ISO 3166 cód tíre* | Scag de réir tíre ach cód ISO a úsáid (e.g. `DE`, `US`, `GB-ENG`). |
| `GeoNameID`   | slánuimhir       | Scag de réir áite ach aitheantóir [GeoName](https://www.geonames.org) a úsáid.  |
| `Language`    | teaghrán         | Scag míreanna de réir teanga ach cód teanga ISO 639-1 a úsáid. |
| `DateFrom`    | slánuimhir**     | Aisghabh taifid a bhaineann leis an mbliain seo nó le blianta ina diaidh. |
| `DateTo`      | slánuimhir**     | Aisghabh taifid a bhaineann leis an mbliain seo nó le blianta roimhe sin. |
| `DateAccuracy` | teaghrán        | Scag de réir chruinneas dháta an taifid (i.e. `APPROX`, `INFER`, `QUESTION`). |
| `CreatedBefore` | am-dháta ISO 8601 | Aisghabh taifid a cruthaíodh roimh dháta ar leith i bhformáid `YYYY-MM-DD`. |
| `CreatedSince` | am-dháta ISO 8601 | Aisghabh taifid a cruthaíodh i ndiaidh dáta ar leith i bhformáid `YYYY-MM-DD`. |
| `ModifiedBefore` | am-dháta ISO 8601 | Aisghabh taifid a nuashonraíodh roimh dháta ar leith i bhformáid `YYYY-MM-DD`. |
| `ModifiedSince` | am-dháta ISO 8601 | Aisghabh taifid a nuashonraíodh i ndiaidh dáta ar leith i bhformáid `YYYY-MM-DD`. |

**\*Tabhair faoi deara:** Bíonn na cóid tíre, a bhfuil dhá litir iontu agus a nglacann an paraiméadar `Country` leo, de réir chaighdeán [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html). Glactar le ceithre chód bhreise ISO 3166-2, áfach, chun idirdhealú idir Sasana, Tuaisceart Éireann, Albain agus an Bhreatain Bheag a éascú. Seo a leanas na cóid faoi seach: `GB-ENG`, `GB-NIR`, `GB-SCT` agus `GB-WLS`.

**\*\*Tabhair faoi deara:** Glacann paraiméadair `DateFrom` agus `DateTo` le blianta i bhformáid `YYYY` amháin faoi láthair.

#### Bailiúchán na Scol (CBÉS)

| Ainm          | Cineál           | Cur síos       |
| :------------ | :--------------- | :------------- |
| `Status`      | slánuimhir       | Scag de réir an stádais eagarthóireachta (0-4). **(Faoi phribhléid)** |
| `VolumeNumber` | teaghrán        | Scag de réir thagairt cartlainne an imleabhair lámhscríbhinne (e.g. 0154). |
| `VolumeID`    | slánuimhir       | Scag de réir aitheantóir an imleabhair lámhscríbhinne. |
| `PageID`      | slánuimhir       | Scag de réir aitheantóir leathanaigh na lámhscríbhinne. |
| `PartID`      | slánuimhir       | Scag de réir aitheantóir coda na lámhscríbhinne. |
| `ItemID`      | slánuimhir       | Scag de réir aitheantóir míre na lámhscríbhinne. |
| `SchoolCountyID`    | slánuimhir       | Scag scoileanna (i.e. codanna lámhscríbhinne) de réir contae ach aitheantóir [logainm.ie](https://www.logainm.ie) a úsáid.  |
| `SchoolPlaceID`     | slánuimhir       | Scag scoileanna (i.e. codanna lámhscríbhinne) de réir áite ach aitheantóir [logainm.ie](https://www.logainm.ie) a úsáid.  |
| `TeacherID`   | slánuimhir       | Scag scoileanna (i.e. codanna lámhscríbhinne) de réir aitheantóir CBÉS an mhúinteora. |
| `CollectorID` | slánuimhir       | Scag de réir aitheantóir CBÉS an bhailitheora. |
| `InformantID` | slánuimhir       | Scag de réir aitheantóir CBÉS an fhaisnéiseora. |
| `PersonID`    | slánuimhir       | Scag de réir aitheantóir CBÉS an duine. Cuimsíonn an scagaire seo bailitheoirí agus faisnéiseoirí araon. |
| `CountyID`    | slánuimhir       | Scag de réir contae ach aitheantóir [logainm.ie](https://www.logainm.ie) a úsáid.  |
| `PlaceID`     | slánuimhir       | Scag de réir áite ach aitheantóir [logainm.ie](https://www.logainm.ie) a úsáid.  |
| `TopicID`     | slánuimhir       | Scag de réir topaice ach aitheantóir CBÉS topaice a úsáid. |
| `Language`    | teaghrán         | Scag míreanna de réir teanga ach cód teanga ISO 639-1 a úsáid. |
| `CreatedBefore` | am-dháta ISO 8601 | Aisghabh taifid a cruthaíodh roimh dháta ar leith i bhformáid `YYYY-MM-DD`. |
| `CreatedSince` | am-dháta ISO 8601 | Aisghabh taifid a cruthaíodh i ndiaidh dáta ar leith i bhformáid `YYYY-MM-DD`. |
| `ModifiedBefore` | am-dháta ISO 8601 | Aisghabh taifid a nuashonraíodh roimh dháta ar leith i bhformáid `YYYY-MM-DD`. Áirítear leis seo tras-scríbhinní nua nó nuashonraithe leathanaigh. |
| `ModifiedSince` | am-dháta ISO 8601 | Aisghabh taifid a nuashonraíodh i ndiaidh dáta ar leith i bhformáid `YYYY-MM-DD`. Áirítear leis seo tras-scríbhinní nua nó nuashonraithe leathanaigh. |

#### An Bailiúchán Grianghraf (CBÉG)

| Ainm          | Cineál           | Cur síos       |
| :------------ | :--------------- | :------------- |
| `Status`      | slánuimhir       | Scag de réir an stádais eagarthóireachta (0-4). **(Faoi phribhléid)** |
| `Digitized`   | Boole            | Scag de réir an stádais digitithe. |
| `Copyright`   | teaghrán         | Scag de réir an tsealbhóra chóipchirt (e.g. `CBE`, `UNK`). |
| `Condition`   | slánuimhir       | Scag de réir bail fhisiciúil (0-3). |
| `HandbookTopic` | teaghrán        | Scag de réir chód ábhair [*A Handbook of Irish Folklore*](https://www.duchas.ie/ga/tpc/cbeg) (e.g. B005). |
| `PersonID`    | slánuimhir       | Scag de réir aitheantóir CBÉD an duine. |
| `PhotographerID` | slánuimhir       | Scag de réir aitheantóir CBÉD an ghrianghrafadóra. |
| `RelevantPersonID` | slánuimhir       | Scag de réir aitheantóir CBÉD an duine. |
| `CountyID`    | slánuimhir       | Scag de réir contae ach aitheantóir [logainm.ie](https://www.logainm.ie) a úsáid.  |
| `PlaceID`     | slánuimhir       | Scag de réir áite ach aitheantóir [logainm.ie](https://www.logainm.ie) a úsáid.  |
| `Country`     | cód tíre ISO 3166* | Scag de réir tíre ach cód ISO a úsáid (e.g. `DE`, `US`, `GB-ENG`). |
| `GeoNameID`   | slánuimhir       | Scag de réir áite ach aitheantóir [GeoName](https://www.geonames.org) a úsáid.  |
| `DateFrom`    | slánuimhir**     | Aisghabh taifid a bhaineann leis an mbliain seo nó le blianta ina diaidh. |
| `DateTo`      | slánuimhir**     | Aisghabh taifid a bhaineann leis an mbliain seo nó le blianta roimhe sin. |
| `DateAccuracy` | teaghrán        | Scag de réir chruinneas dháta an taifid (i.e. `APPROX`, `INFER`, `QUESTION`). |
| `CreatedBefore` | am-dháta ISO 8601 | Aisghabh taifid a cruthaíodh roimh dháta ar leith i bhformáid `YYYY-MM-DD`. |
| `CreatedSince` | am-dháta ISO 8601 | Aisghabh taifid a cruthaíodh i ndiaidh dáta ar leith i bhformáid `YYYY-MM-DD`. |
| `ModifiedBefore` | am-dháta ISO 8601 | Aisghabh taifid a nuashonraíodh roimh dháta ar leith i bhformáid `YYYY-MM-DD`. |
| `ModifiedSince` | am-dháta ISO 8601 | Aisghabh taifid a nuashonraíodh i ndiaidh dáta ar leith i bhformáid `YYYY-MM-DD`. |

**\*Tabhair faoi deara:** Bíonn na cóid tíre, a bhfuil dhá litir iontu agus a nglacann an paraiméadar `Country` leo, de réir chaighdeán [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html). Glactar le ceithre chód bhreise ISO 3166-1, áfach, chun idirdhealú idir Sasana, Tuaisceart Éireann, Albain agus an Bhreatain Bheag a éascú. Seo a leanas na cóid faoi seach: `GB-ENG`, `GB-NIR`, `GB-SCT` agus `GB-WLS`.  

**\*\*Tabhair faoi deara:** Glacann paraiméadair `DateFrom` agus `DateTo` le blianta i bhformáid `YYYY` amháin faoi láthair.

#### An Bunachar Daoine (CBÉD)

| Ainm          | Cineál           | Cur síos       |
| :------------ | :--------------- | :------------- |
| `Gender`      | teaghrán         | Scag de réir inscne an duine (b, f).  |
| `AinmID`      | slánuimhir       | Scag de réir ID iontráil [ainm.ie](https://www.ainm.ie).  |
| `ViafID`      | slánuimhir       | Scag de réir ID iontráil [VIAF](https://viaf.org/).  |
| `CountyID`    | slánuimhir       | Scag de réir contae ach aitheantóir [logainm.ie](https://www.logainm.ie) a úsáid.  |
| `PlaceID`     | slánuimhir       | Scag de réir áite ach aitheantóir [logainm.ie](https://www.logainm.ie) a úsáid.  |
| `Country`     | ISO 3166 cód tíre* | Scag de réir tíre ach cód ISO a úsáid (e.g. `DE`, `US`, `GB-ENG`). |
| `GeoNameID`   | slánuimhir       | Scag de réir aitheantóir [GeoName](https://www.geonames.org).  |
| `Occupation`  | teaghrán         | Scag de réir gairme (e.g. `IASC`, `FEIRM`). |
| `BirthDateFrom` | slánuimhir**     | Aisghabh taifid a bhaineann leis an mbliain bhreithe seo nó le blianta ina diaidh. |
| `BirthDateTo` | slánuimhir**     | Aisghabh taifid a bhaineann leis an mbliain bhreithe seo nó le blianta roimhe sin. |
| `BirthDateAccuracy` | teaghrán       | Scag de réir chruinneas an dáta breithe (i.e. `APPROX`, `INFER`, `QUESTION`). |
| `DeathDateFrom` | slánuimhir**     | Aisghabh taifid a bhaineann leis an mbliain bháis seo nó le blianta ina diaidh. |
| `DeathDateTo` | slánuimhir**     | Aisghabh taifid a bhaineann leis an mbliain bháis seo nó le blianta roimhe sin. |
| `DeathDateAccuracy` | teaghrán       | Scag de réir chruinneas an dáta báis (i.e. `APPROX`, `INFER`, `QUESTION`). |
| `CreatedBefore` | am-dháta ISO 8601 | Aisghabh taifid a cruthaíodh roimh dháta ar leith i bhformáid `YYYY-MM-DD`. |
| `CreatedSince` | am-dháta ISO 8601 | Aisghabh taifid a cruthaíodh i ndiaidh dáta ar leith i bhformáid `YYYY-MM-DD`. |
| `ModifiedBefore` | am-dháta ISO 8601 | Aisghabh taifid a nuashonraíodh roimh dháta ar leith i bhformáid `YYYY-MM-DD`. |
| `ModifiedSince` | am-dháta ISO 8601 | Aisghabh taifid a nuashonraíodh i ndiaidh dáta ar leith i bhformáid `YYYY-MM-DD`. |

**\*Tabhair faoi deara:** Bíonn na cóid tíre, a bhfuil dhá litir iontu agus a nglacann an paraiméadar `Country` leo, de réir chaighdeán [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html). Glactar le ceithre chód bhreise ISO 3166-1, áfach, chun idirdhealú idir Sasana, Tuaisceart Éireann, Albain agus an Bhreatain Bheag a éascú. Seo a leanas na cóid faoi seach: `GB-ENG`, `GB-NIR`, `GB-SCT` agus `GB-WLS`.  

**\*\*Tabhair faoi deara:** Glacann paraiméadair `DateFrom` agus `DateTo` le blianta i bhformáid `YYYY` amháin faoi láthair.

### Samplaí léiritheacha

Seo thíos liosta, nach bhfuil uileghabhálach, d'aimsitheoirí aonfhoirmeacha acmhainne bailí maidir le hiarratais API:

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
