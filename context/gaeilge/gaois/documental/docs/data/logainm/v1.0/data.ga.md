---
title: Foclóir sonraí (Leagan 1.0)
shortTitle: Foclóir sonraí
description: Foclóir sonraí i gcomhair API Logainm
keywords: Logainm, API, logainmneacha, logainmníocht, ainmeolaíocht, Gaeilge, Fiontar & Scoil na Gaeilge, DCU
resource: Logainm
order: 2
public: true
---

Déantar cur síos sa doiciméad seo ar struchtúr sonraí na dtorthaí a chuirtear ar fáil trí Chomhéadan Feidhmchláir (API) Logainm. Áis chuimsitheach bhainistíochta í seo chun sonraí logainmneacha agus taifid chartlainne, mar aon le taighde logainmneacha Rialtas na hÉireann, a riar. Téigh i gcomhairle le [doiciméid an fhorbróra](../api) chun eolas ginearálta ar API agus treoirlínte an fhorbróra a fháil.

## `placeList`

Gheofar oibiacht `placeList` ón gcuid is mó d'iarratais API. Tá liosta ina bhfuil áit amháin nó níos mó, má aimsítear iad, agus meiteashonraí breise a bhaineann leis an iarratas san oibiacht seo.  

| Ainm an airí    | Cineál              | Bunuimhreacht       | Cur síos               |
| :-------------- | :------------------ | :------------------ | :--------------------- |
| TotalCount      | slánuimhir          | ceann amháin        | Líon iomlán na dtaifead áite a aisghabhadh. |
| TotalPages      | slánuimhir          | ceann amháin        | Líon iomlán na leathanach sa tacar torthaí. |
| CurrentPage     | slánuimhir          | ceann amháin        | An uimhir leathanaigh reatha. |
| CountPerPage    | slánuimhir          | ceann amháin        | An t-uaslíon torthaí a thugtar in aghaidh an leathanaigh. |
| Results         | [`place`](#place)     | ceann ar bith nó ceann amháin nó go leor | Na taifid áite a aisghabhadh. |
| SimilarNames    | teaghrán            | ceann ar bith nó ceann amháin nó go leor | Tacar ainmneacha a bhfuil an litriú atá orthu cosúil le téacs an iarratais (más cuardach téacs atá i gceist). Mar shampla, má chuardaíonn tú 'Ballybunion', molfar 'Ballybunnion.' |
| RelatedNames    | teaghrán            | ceann ar bith nó ceann amháin nó go leor | Tacar ainmneacha atá bainteach le téacs an iarratais. Mar shampla, má chuardaíonn tú 'Lismore', molfar 'Lismore and Mocollop', 'Lismore Demesne' agus 'Lismore Road' i liosta na logainmneacha gaolmhara. |

## `place`

Tá an oibiacht `place` i gcroílár API Logainm. Léiríonn sí suíomh geografach agus áirítear léi meiteashonraí logainmníochta, léacsacha agus eile. Ach iarratas a dhéanamh ina sonraítear aitheantóir áite sa chosán iarratais, gheofar oibiacht `place` amháin (má tá ceann ann) agus d'fhéadfadh iarratais níos leithne oibiacht `place` amháin nó níos mó a thabhairt sa chorp freagartha.

| Ainm an airí    | Cineál              | Bunuimhreacht                        | Cur síos                  |
| :-------------- | :------------------ | :----------------------------------- | :------------------------- |
| ID              | slánuimhir          | ceann amháin                         | Aitheantóir uathúil áite. |
| ReplacementID   | slánuimhir          | ceann ar bith nó ceann amháin        | Má tá an luach seo socraithe, cumascadh an taifead áite a iarradh le taifead eile sa bhunachar sonraí. Is é an luach an t-aitheantóir ionaid taifid. |
| DateCreated     | am-dháta ISO 8601   | ceann amháin                         | An dáta agus an t-am a cruthaíodh an iontráil.  |
| DateModified    | am-dháta ISO 8601   | ceann ar bith nó ceann amháin        | Dáta agus am an mhionathraithe is déanaí a rinneadh ar an iontráil.  |
| Permalink       | teaghrán            | ceann amháin                         | Hipearnasc statach buan ina bhféadfadh léitheoir daonna tuilleadh eolais a fháil ar an áit. Téann sé seo go dtí an leagan Gaeilge nó Béarla de leathanach eolais na háite go huathoibríoch. |
| Featured        | am-dháta ISO 8601   | ceann ar bith nó ceann amháin nó go leor | Seasann sé seo don dáta, nó do na dátaí, nuair a úsáideadh an áit seo mar 'logainm an lae' ar [logainm.ie](https://www.logainm.ie), má úsáideadh í. |
| Cluster         | [`cluster`](#cluster) | ceann ar bith nó ceann amháin | Meiteashonraí a léiríonn grúpa áiteanna, a bhfuil an áit seo mar chuid de, a roinneann logainmneacha agus atá comhshuite nó atá gar dá chéile. |
| Placenames      | [`placename`](#placename) | ceann amháin nó go leor | Logainm amháin nó níos mó, agus meiteashonraí gaolmhara, a thugtar ar an áit seo. |
| Glossary        | [`glossary`](#glossary) | ceann ar bith nó ceann amháin | Déanann sé cur síos ar fhocail a fhaightear go minic i logainmneacha na hÉireann agus atá i logainmneacha a bhaineann leis an áit seo. |
| Categories        | [`category`](#category) | ceann ar bith nó ceann amháin nó go leor | Déanann sé cur síos ar chatagóirí a bhaineann leis an áit seo. Ní bhaineann níos mó ná catagóir amháin le háiteanna ach amháin i gcásanna eisceachtúla. |
| IncludedIn      | [`placeSummary`](#placesummary) | ceann ar bith nó ceann amháin nó go leor | Eolas achomair maidir leis na haonaid riaracháin (contaetha, paróistí sibhialta, etc.) a gcuimsítear iontu an áit seo. |
| Includes        | [`category`](#category) | ceann ar bith nó ceann amháin nó go leor | Déanann sé cur síos ar chatagóirí áite atá laistigh de theorainneacha na háite seo. |
| Geography       | [`geography`](#geography) | ceann amháin nó go leor | Suíomh geografach na háite ó thaobh comhordanáidí domhanleithid agus domhanfhaid de. |
| GridReferences  | [`gridReference`](#gridreference) | ceann ar bith nó ceann amháin nó go leor | Suíomh geografach na háite i gcomhordanáidí [Chóras Tagraíochta Eangaí na hÉireann](https://www.osi.ie/resources/reference-information-2/irish-grid-reference-system/). |
| Gaeltacht       | [`placeProperty`](#placeproperty) | ceann ar bith nó ceann amháin | Cuireann sé in iúl go bhfuil an áit sa Ghaeltacht. |
| PostOffice      | [`placeProperty`](#placeproperty) | ceann ar bith nó ceann amháin | Cuireann sé in iúl go bhfuil, nó go raibh, oifig an phoist san áit seo. |
| NorthernIreland | [`placeProperty`](#placeproperty) | ceann ar bith nó ceann amháin | Cuireann sé in iúl go bhfuil an áit i dTuaisceart Éireann. |
| Images          | [`image`](#image)   | ceann ar bith nó ceann amháin | Déanann sé cur síos ar thaifead amháin, nó níos mó, a scanadh ó chartlann an Bhrainse Logainmneacha a bhaineann leis an áit seo. |
| Resources       | [`resource`](#resource) | ceann ar bith nó ceann amháin nó go leor | Déanann sé cur síos ar acmhainn logainmníochta amháin, nó níos mó, a bhaineann leis an áit seo agus atá ar fáil ar [logainm.ie](https://www.logainm.ie). |
| Links           | [`link`](#link) | ceann ar bith nó ceann amháin nó go leor | Cuireann sé nasc amháin, nó níos mó, ar fáil le sonraí gaolmhara in acmhainní seachtracha. Áirítear le hacmhainní seachtracha [OSI](https://www.osi.ie/), [Logainmneacha Thuaisceart Éireann](http://www.placenamesni.org/), [Wikipedia](https://www.wikipedia.org/), [Geonames](http://www.geonames.org/), etc. |
| BornHere        | [`biographyLink`](#biographylink) | ceann ar bith nó ceann amháin nó go leor | Cuireann sé nasc ar fáil le sonraí beathaisnéiseacha ó [ainm.ie](https://www.ainm.ie) a bhaineann le duine ar bith a rugadh san áit seo, má tá siad ar fáil. |
| Folklore        | [`folkloreLink`](#folklorelink) | ceann ar bith nó ceann amháin nó go leor | Cuireann sé nasc ar fáil le sonraí béaloidis ó [dúchas.ie](https://www.duchas.ie) a bhaineann leis an áit seo, má tá siad ar fáil. |
| SameAs          | [`sameAs`](#sameas) | ceann ar bith nó ceann amháin nó go leor | Sonraíonn sé comhthagairt amháin, nó níos mó, don áit seo i dtacair shonraí eile seachas i mBunachar Logainmneacha na hÉireann. De réir mhíniú [SameAs](https://www.w3.org/TR/owl-ref/) Ointeolaíocht OWL. |

### `cluster`

Meiteashonraí a léiríonn grúpa áiteanna a roinneann logainmneacha agus atá comhshuite nó atá gar dá chéile.

| Ainm an airí    | Cineál              | Bunuimhreacht       | Cur síos                  |
| :-------------- | :------------------ | :------------------ | :------------------------ |
| FocusID         | slánuimhir          | ceann amháin        | Aithníonn sé an áit a gcruthaíonn ‘fócas’ an bhraisle. Seans go léiríonn sé an chatagóir áite is mó a bhaineann le logainm ar leith nó go bhfuil an tacar is saibhre meiteashonraí i measc na mball braisle ar fad ann. |
| Members         | [`clusterMember`](#clustermember) | ceann amháin nó go leor         | Léiríonn sé na háiteanna aonair atá sa bhraisle. |

### `clusterMember`

Léiríonn sé ball de `cluster`.

| Ainm an airí    | Cineál              | Bunuimhreacht       | Cur síos                  |
| :-------------- | :------------------ | :------------------ | :------------------------ |
| PlaceID         | slánuimhir          | ceann amháin        | An t-aitheantóir áite.    |
| Category        | [`category`](#category) | ceann ar bith nó ceann amháin         | Catagóir na háite.      |

### `placename`

Léiríonn sé logainm a bhaineann le háit amháin nó níos mó.

| Ainm an airí    | Cineál              | Bunuimhreacht          | Cur síos                  |
| :-------------- | :------------------ | :--------------------- | :------------------------ |
| ID              | slánuimhir          | ceann amháin           | Aitheantóir an logainm. |
| Language        | cód teanga ISO 639-1 | ceann ar bith nó ceann amháin          | Léiríonn sé teanga an logainm, má tá sé ar eolas. |
| Wording         | teaghrán            | ceann amháin           | An logainm féin.     |
| Genetive        | teaghrán            | ceann ar bith nó ceann amháin         | I gcás logainmneacha Gaeilge, sonraíonn sé seo foirm ghramadaí an logainm sa tuiseal ginideach.     |
| Main            | Boole               | ceann amháin           | Má tá sé fíor, is é seo príomhainm/ainm canónta an logainm. Níl sé seo tábhachtach ach amháin má tá níos mó ná ainm amháin ag an áit sa teanga chéanna. |
| Acceptability   | [`acceptability`](#acceptability) | ceann ar bith nó ceann amháin         | Léiríonn sé stádas taighde agus faofa an logainm. |
| Audio           | [`audio`](#audio)   | ceann ar bith nó ceann amháin         | Déanann sé cur síos ar chomhad fuaime ina ndéantar fuaimniú táscach ar an logainm. |
| SubNames        | [`subName`](#subname) | ceann ar bith nó go leor      | Liosta de dhá logainm scoite nó níos mó. Cuirtear ar fáil é nuair atá dhá ainm nó níos mó atá cónasctha sa phríomhlogainm e.g. '[Rathgarvan or Clifden](https://www.logainm.ie/26783.aspx)', nó nuair atá ról cáilithe nó imdhealaithe ag an bpríomhlogainm. |

### `acceptability`

Léiríonn sé an [stádas taighde agus faofa](https://www.logainm.ie/ga/inf/help-notes) a bhaineann le logainm.

| Ainm an airí    | Cineál              | Bunuimhreacht                         | Cur síos                  |
| :-------------- | :------------------ | :------------------------------------ | :------------------------ |
| ID              | slánuimhir          | ceann amháin                          | Aitheantóir an stádais inghlacthachta. |
| TextEN          | teaghrán            | ceann ar bith nó ceann amháin         | Lipéad Béarla a dhéanann cur síos ar an stádas inghlacthachta. |
| TextGA          | teaghrán            | ceann ar bith nó ceann amháin         | Lipéad Gaeilge a dhéanann cur síos ar an stádas inghlacthachta. |

### `audio`

Déanann sé cur síos ar chomhad fuaime ina ndéantar fuaimniú táscach ar an logainm.

| Ainm an airí    | Cineál              | Bunuimhreacht       | Cur síos                  |
| :-------------- | :------------------ | :------------------ | :------------------------ |
| FileName        | teaghrán            | ceann amháin        | Ainm an chomhaid fuaime.  |
| Uri             | teaghrán            | ceann amháin        | URI an chomhaid fuaime.   |

### `subName`

Ainm scoite a d'fhéadfaí a úsáid chun logainmneacha níos faide a chumadh.  

| Ainm an airí    | Cineál              | Bunuimhreacht       | Cur síos                  |
| :-------------- | :------------------ | :------------------ | :------------------------ |
| Text            | teaghrán            | ceann amháin        | Téacs an ainm.            |
| Disambiguates   | Boole               | ceann amháin        | Má tá sé fíor, cuireann an t-ainm seo cineál uath-imdhealaithe éigin ar fáil maidir leis an bpríomhlogainm. D'fhéadfadh `subName` imdhealaithe, mar shampla, idirdhealú a dhéanamh idir an príomhlogainm agus ainmneacha eile atá cosúil leis. |

### `placeSummary`

Eolas achomair maidir le háit ar leith.

| Ainm an airí    | Cineál              | Bunuimhreacht                         | Cur síos                  |
| :-------------- | :------------------ | :------------------------------------ | :------------------------ |
| ID              | slánuimhir          | ceann amháin                          | An t-aitheantóir áite.    |
| NameEN          | teaghrán            | ceann ar bith nó ceann amháin         | An logainm Béarla.   |
| NameGA          | teaghrán            | ceann ar bith nó ceann amháin         | An logainm Gaeilge.  |
| Category        | [`category`](#category) | ceann ar bith nó ceann amháin          | Catagóir na háite.      |

### `geography`

Léiríonn sé suíomh geografach i gcomhordanáidí domhanleithid agus domhanfhaid.

| Ainm an airí    | Cineál              | Bunuimhreacht       | Cur síos                  |
| :-------------- | :------------------ | :------------------ | :------------------------ |
| Accurate        | Boole               | ceann amháin        | Léiríonn sé cé acu a chreidtear go bhfuil na comhordanáidí beacht nó nach gcreidtear. Is ionann comhordanáidí míchruinne agus comhordanáidí a fuarthas trí eachtarshuí ó áiteanna in aice láimhe. |
| Coordinates     | [`coordinates`](#coordinates) | ceann amháin nó go leor        | Péire amháin comhordanáidí domhanleithid agus domhanfhaid, nó níos mó. Léiríonn péire amháin comhordanáidí an chuid is mó de na háiteanna. D'fhéadfadh dhá phéire nó níos mó a bheith ag gnéithe áirithe geografacha, áfach, go háirithe aibhneacha nó oileáin. |

### `coordinates`

Léiríonn sé péire comhordanáidí geografacha.

| Ainm an airí    | Cineál              | Bunuimhreacht       | Cur síos                       |
| :-------------- | :------------------ | :------------------ | :----------------------------- |
| Latitude        | dúbailte            | ceann amháin        | An chomhordanáid domhanleithid. |
| Longitude       | dúbailte            | ceann amháin        | An chomhordanáid domhanfhaid.  |

### `gridReference`

Suíomh geografach na háite i gcomhordanáidí [Chóras Tagraíochta Eangaí na hÉireann](https://www.osi.ie/resources/reference-information-2/irish-grid-reference-system/).

| Ainm an airí    | Cineál              | Bunuimhreacht                    | Cur síos                  |
| :-------------- | :------------------ | :------------------------------- | :------------------------ |
| Square          | teaghrán            | ceann amháin                     | Sonraíonn sé an chearnóg eangaí. |
| Easting         | fada                | ceann ar bith nó ceann amháin    | Sonraíonn sé an oirlíne sa chearnóg. |
| Northing        | fada                | ceann ar bith nó ceann amháin    | Sonraíonn sé an tuaidhlíne sa chearnóg. |

### `placeProperty`

Déanann sé cur síos ar airí a bhaineann le háit ar leith.

| Ainm an airí    | Cineál              | Bunuimhreacht        | Cur síos                  |
| :-------------- | :------------------ | :------------------- | :------------------------ |
| Extent          | teaghrán            | ceann amháin         | Sonraíonn sé baint an airí le háit ar leith. Más `all` atá ann, baineann an t-airí leis an áit uile. Más `part` atá ann, ní bhaineann an t-airí ach le cuid den áit. |

### `image`

Déanann sé cur síos ar thaifead scanta ó chartlann an Bhrainse Logainmneacha.  

| Ainm an airí    | Cineál              | Bunuimhreacht                         | Cur síos                     |
| :-------------- | :------------------ | :------------------------------------ | :--------------------------- |
| FileName        | teaghrán            | ceann amháin                          | Ainm an chomhaid íomhá.      |
| LabelEN         | teaghrán            | ceann ar bith nó ceann amháin         | Cur síos Béarla ar chatagóir na híomhá, má tá sé ar eolas. |
| LabelGA         | teaghrán            | ceann ar bith nó ceann amháin         | Cur síos Gaeilge ar chatagóir na híomhá, má tá sé ar eolas. |
| Uri             | teaghrán            | ceann amháin                          | URI na híomhá.            |

### `resource`

Déanann sé cur síos ar acmhainn logainmníochta atá ar fáil ar [logainm.ie](https://www.logainm.ie). 

| Ainm an airí    | Cineál              | Bunuimhreacht                         | Cur síos                  |
| :-------------- | :------------------ | :------------------------------------ | :------------------------ |
| ID              | slánuimhir          | ceann amháin                          | Aitheantóir na hacmhainne.  |
| TypeID          | teaghrán            | ceann amháin                          | Aithníonn sé an cineál acmhainne atá ann. |
| TitleEN         | teaghrán            | ceann ar bith nó ceann amháin         | Teideal Béarla na hacmhainne. |
| TitleGA         | teaghrán            | ceann ar bith nó ceann amháin         | Teideal Gaeilge na hacmhainne. |
| PageReference   | teaghrán            | ceann ar bith nó ceann amháin         | Sonraíonn sé an leathanach, nó na leathanaigh, laistigh den acmhainn a bhaineann le háit ar leith, más bainteach. |
| Supplier        | [`supplier`](#supplier) | ceann ar bith nó ceann amháin        | Meiteashonraí a bhaineann le foilsitheoir/soláthraí na hacmhainne. |

#### `TypeID`

Seo a leanas luachanna féideartha an airí `TypeID`:

| Luach           | Cur síos                  |
| :-------------- | :------------------------ |
| jpg             | Íomhá JPEG.               |
| pdf             | Doiciméad PDF.            |
| zip             | Zipchomhad.               |

### `supplier`

Meiteashonraí a bhaineann le foilsitheoir/soláthraí na hacmhainne logainmníochta.  

| Ainm an airí    | Cineál              | Bunuimhreacht                         | Cur síos                  |
| :-------------- | :------------------ | :------------------------------------ | :------------------------ |
| ID              | slánuimhir          | ceann amháin                          | Aitheantóir an tsoláthraí.  |
| NameEN          | teaghrán            | ceann ar bith nó ceann amháin         | Ainm Béarla an tsoláthraí. |
| NameGA          | teaghrán            | ceann ar bith nó ceann amháin         | Ainm Gaeilge an tsoláthraí. |

### `link`

Cuireann sé nasc ar fáil le sonraí gaolmhara in acmhainn sheachtrach.  

| Ainm an airí    | Cineál              | Bunuimhreacht       | Cur síos                  |
| :-------------- | :------------------ | :------------------ | :------------------------ |
| Type            | teaghrán            | ceann amháin        | Cineál na hacmhainne seachtraí. Áirítear le hacmhainní seachtracha [OSI](https://www.osi.ie/), [Logainmneacha Thuaisceart Éireann](http://www.placenamesni.org/), [Wikipedia](https://www.wikipedia.org/), [Geonames](http://www.geonames.org/), etc. |
| Target          | teaghrán            | ceann amháin        | Sprioc an naisc. D'fhéadfadh URI, URL nó aitheantóir eile a bheith i gceist leis seo, ag brath ar an gcineál acmhainne atá ann. |

#### `Type`

Seo a leanas luachanna féideartha airí an chineáil naisc:

| Luach           | Cur síos                  |
| :-------------- | :------------------------ |
| Geonames        | Is URL iontráil [Geonames](http://www.geonames.org/) é an nasc. |
| Osi             | Is aitheantóir acmhainne de chuid [Shuirbhéireacht Ordanáis Éireann](https://www.osi.ie/) é an nasc. |
| PlacenamesNi    | Is aitheantóir acmhainne de chuid [Logainmneacha Thuaisceart Éireann](http://www.placenamesni.org/) é an nasc. |
| WikipediaEn     | Is URL le haghaidh iontráil Bhéarla [Wikipedia](https://www.wikipedia.org/) é an nasc. |
| WikipediaGa     | Is URL le haghaidh iontráil Ghaeilge [Wikipedia](https://www.wikipedia.org/) é an nasc. |

### `biographyLink`

Cuireann sé naisc ar fáil le sonraí beathaisnéiseacha ó [ainm.ie](https://www.ainm.ie) a bhaineann le haon duine a rugadh in áit ar leith.  

| Ainm an airí    | Cineál              | Bunuimhreacht       | Cur síos                       |
| :-------------- | :------------------ | :------------------ | :----------------------------- |
| ID              | teaghrán            | ceann amháin        | Aitheantóir ainm.ie na beathaisnéise.  |
| Title           | slánuimhir          | ceann amháin        | Teideal na beathaisnéise.      |
| Uri             | slánuimhir          | ceann amháin        | URI bheathaisnéis ainm.ie. |

### `folkloreLink`

Cuireann sé nasc ar fáil le sonraí béaloidis ó [dúchas.ie](https://www.duchas.ie) a bhaineann le háit ar leith.  

| Ainm an airí    | Cineál              | Bunuimhreacht       | Cur síos                  |
| :-------------- | :------------------ | :------------------ | :------------------------ |
| Type            | teaghrán            | ceann amháin        | Cineál na hacmhainne seachtraí. Faoi láthair, déanfaidh sé seo cur síos i gcónaí ar acmhainní ó thionscadal Dúchas. |
| UriEN           | teaghrán            | ceann amháin        | URI acmhainn na sonraí béaloidis (comhéadan Béarla). |
| UriGA           | teaghrán            | ceann amháin        | URI acmhainn na sonraí béaloidis (comhéadan Gaeilge). |

### `sameAs`

Sonraíonn sé comhthagairt d'áit ar leith i dtacair sonraí seachas Bunachar Logainmneacha na hÉireann. I gcomhréir le míniú [SameAs](https://www.w3.org/TR/owl-ref/) Ointeolaíocht OWL.

| Ainm an airí    | Cineál              | Bunuimhreacht       | Cur síos                  |
| :-------------- | :------------------ | :------------------ | :------------------------ |
| Uri             | teaghrán            | ceann amháin        | URI na hacmhainne seachtraí. |

## `referenceList`

Tá liosta ina bhfuil oibiacht tagartha amháin nó níos mó, má aimsítear iad, agus meiteashonraí breise a bhaineann leis an iarratas san oibiacht seo.

| Ainm an airí    | Cineál              | Bunuimhreacht       | Cur síos                  |
| :-------------- | :------------------ | :------------------ | :------------------------ |
| TotalCount      | slánuimhir          | ceann amháin        | Líon iomlán na dtaifead a aisghabhadh. |
| TotalPages      | slánuimhir          | ceann amháin        | Líon iomlán na leathanach sa tacar torthaí. |
| CurrentPage     | slánuimhir          | ceann amháin        | An uimhir leathanaigh reatha. |
| CountPerPage    | slánuimhir          | ceann amháin        | An t-uaslíon torthaí a thugtar in aghaidh an leathanaigh. |
| Results         | [`category`](#category) nó [`glossary`](#glossary) nó [`place`](#place) | ceann ar bith nó ceann amháin nó go leor | Na taifid a aisghabhadh. |

## `category`

Déanann sé cur síos ar chatagóir áite. Cuimsíonn catagóirí [aonaid riaracháin](https://www.logainm.ie/ga/inf/help-categs) agus gnéithe geografacha. D'fhéadfadh catagóir amháin, nó níos mó, teacht ar ais mar chuid d'oibiacht `place` nó d'fhéadfaí teacht ar liosta tagartha d'oibiachtaí `category` ón [gcríochphointe](/ga/data/logainm/v0.9/api/#cosain-acmhainne) API cuí.
 
| Ainm an airí    | Cineál              | Bunuimhreacht                     | Cur síos                  |
| :-------------- | :------------------ | :-------------------------------- | :------------------------ |
| ID              | teaghrán            | ceann amháin                      | Aitheantóir na catagóire. |
| NameEN          | teaghrán            | ceann ar bith nó ceann amháin     | Ainm Béarla na catagóire. |
| NameGA          | teaghrán            | ceann ar bith nó ceann amháin     | Ainm Gaeilge na catagóire. |
| NamePluralEN    | teaghrán            | ceann ar bith nó ceann amháin     | Uimhir iolra ainm Béarla na catagóire. |
| NamePluralGA    | teaghrán            | ceann ar bith nó ceann amháin     | Uimhir iolra ainm Gaeilge na catagóire. |
| Count           | slánuimhir          | ceann ar bith nó ceann amháin     | Líon na logainmneacha a bhaineann leis an gcatagóir seo, má tá sé ar eolas. |

## `glossary`

Déanann sé cur síos ar thacar d'fhocail ghaolmhara a fhaightear go minic i logainmneacha na hÉireann. D'fhéadfadh iontráil gluaise amháin, nó níos mó, teacht ar ais mar chuid d'oibiacht `place` nó d'fhéadfaí liosta tagartha d'oibiachtaí `glossary` ón [gcríochphointe](/ga/data/logainm/v0.9/api/#cosain-acmhainne) API cuí a fháil.

| Ainm an airí    | Cineál              | Bunuimhreacht                            | Cur síos                  |
| :-------------- | :------------------ | :--------------------------------------- | :------------------------ |
| ID              | slánuimhir          | ceann amháin                             | Aitheantóir na hiontrála gluaise.  |
| Headword        | teaghrán            | ceann amháin                             | Ceannfhocal na hiontrála gluaise. |
| Translation     | teaghrán            | ceann ar bith nó ceann amháin            | Aistriúchán Béarla ar cheannfhocal na gluaise. |
| Forms           | teaghrán            | ceann ar bith nó ceann amháin nó go leor | Litrithe eile ar cheannfhocal na gluaise. |
| Count           | slánuimhir          | ceann ar bith nó ceann amháin            | Líon na logainmneacha a bhaineann leis an iontráil ghluaise seo, má tá sé ar eolas. |
