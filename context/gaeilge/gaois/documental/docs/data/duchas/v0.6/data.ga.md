---
title: Foclóir sonraí (Leagan 0.6)
shortTitle: Foclóir sonraí
description: Foclóir sonraí i gcomhair API Dúchas
keywords: Dúchas, comhéadan feidhmchláir, béaloideas, stair, scéalaíocht, Fiontar & Scoil na Gaeilge, DCU
resource: Dúchas
order: 2
public: true
---

**Tabhair faoi deara:** Déantar cur síos sa doiciméad seo ar leagan **réamheisiúna** de API Dúchas. Tá gnéithe á gcur leis ar bhonn leanúnach. Déanfar athbhreithniú ar an doiciméad seo roimh eisiúint v1.0. Cuirimid fáilte roimh aiseolas ag <gaois@dcu.ie>.

Déantar cur síos sa doiciméad seo ar struchtúr sonraí na dtorthaí a chuirtear ar fáil trí Chomhéadan Feidhmchláir (API) Dúchas. Is tionscadal é Dúchas a chuir tús le digitiú [Chnuasach Bhéaloideas Éireann](https://www.ucd.ie/irishfolklore/ga) (CBÉ). Téigh i gcomhairle le [doiciméid an fhorbróra](../api) chun eolas ginearálta ar API agus treoirlínte an fhorbróra a fháil.

## An Príomhbhailiúchán Lámhscríbhinní (CBÉ)

Tá scéalta, cuntais, ceistneoirí, dialanna agus ábhar eile a ceanglaíodh ina n-imleabhair sa Phríomhbhailiúchán Lámhscríbhinní. Seasann eintiteas `volume` do gach imleabhar sa tacar sonraí agus seasann eintiteas `page` do gach leathanach. Tá tagairt i ngach eintiteas `page` freisin a aithníonn an íomhá scanta den leathanach. Le chéile, seasann eintitis `volume` agus `page` do **struchtúr fisiciúil** an bhailiúcháin. Tá **struchtúr loighciúil** ann chomh maith a anótálann agus a innéacsaíonn an struchtúr fisiciúil. Tá eintitis `part` agus `item` ann.  

Seasann eintiteas `part` do chuid ar leith laistigh d'imleabhar lámhscríbhinne agus seans go raibh sé scartha ó ábhar eile san imleabhar ar dtús. Tagann sé le ball [`msPart`](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#mspt) a shonraítear i dTreoirlínte P5 Text Encoding Initiative (TEI). Seasann eintiteas `item` d'obair scoite, amhail scéal nó iontráil dialainne. Tagann sé le ball TEI [`msItem`](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#mscoit). Tabhair faoi deara go bhfuil an mhapáil idir míreanna agus leathanaigh mórán le mórán: d'fhéadfadh mír roinnt leathanach a chuimsiú agus d'fhéadfadh leathanach roinnt míreanna a chur san áireamh. Tá sonraí mionsonraithe in eintiteas `item` ar na daoine a scríobh é, chomh maith leis an ábhar lena mbaineann sé agus sonraí eile.  

D'fhéadfaí oibiacht `volume` amháin, nó níos mó, a fháil ó iarratais ar an bPríomhbhailiúchán Lámhscríbhinní. Déantar cur síos san eolas thíos ar airíonna an chineáil oibiachta seo.  

### An Príomhbhailiúchán `volume`

| Ainm an airí    | Cineál              | Bunuimhreacht                           | Cur síos                  |
| :-------------- | :------------------ | :-------------------------------------- | :------------------------ |
| ID              | slánuimhir          | ceann amháin                            | Aitheantóir an imleabhair (uathúil laistigh den bhailiúchán). |
| DateCreated     | am-dháta ISO 8601   | ceann ar bith nó ceann amháin           | An dáta agus an t-am a cruthaíodh an iontráil.  |
| DateModified    | am-dháta ISO 8601   | ceann ar bith nó ceann amháin           | Dáta agus am an mhionathraithe is déanaí a rinneadh ar an iontráil. Léiríonn sé seo na nuashonruithe is déanaí ar chodanna agus ar mhíreanna na lámhscríbhinne, chomh maith le nuashonruithe ar mheiteashonraí an imleabhair féin.  |
| VolumeNumber    | teaghrán            | ceann ar bith nó ceann amháin           | Uimhir tagartha cartlainne CBÉ an imleabhair. |
| Status          | slánuimhir          | ceann amháin                            | Sonraíonn sé [stádas](#status) eagarthóireachta na hiontrála. **(Faoi phribhléid)**  |
| Pages           | [`page`](#an-priomhbhailiuchan-page)     | ceann amháin                          | Meiteashonraí a dhéanann cur síos ar leathanaigh fhisiciúla an imleabhair. |
| Parts           | [`part`](#an-priomhbhailiuchan-part)     | ceann ar bith nó ceann amháin         | Meiteashonraí a dhéanann cur síos ar na codanna loighciúla a fhoroinneann imleabhar na lámhscríbhinne agus a bhfuil ann. |

### An Príomhbhailiúchán `page`

| Ainm an airí    | Cineál              | Bunuimhreacht                           | Cur síos                  |
| :-------------- | :------------------ | :-------------------------------------- | :------------------------ |
| ID              | slánuimhir          | ceann amháin                            | Aitheantóir an leathanaigh (uathúil laistigh den bhailiúchán). |
| DateCreated     | am-dháta ISO 8601   | ceann ar bith nó ceann amháin           | An dáta agus an t-am a cruthaíodh an iontráil.  |
| DateModified    | am-dháta ISO 8601   | ceann ar bith nó ceann amháin           | Dáta agus am an mhionathraithe is déanaí a rinneadh ar an iontráil.  |
| PageNumber      | teaghrán            | ceann amháin                            | Uimhir an leathanaigh.     |
| ListingOrder    | teaghrán            | ceann amháin                            | Ord liostaithe an leathanaigh laistigh den bhailiúchán. Bíonn sé seo díreach mar an gcéanna le huimhir an leathanaigh atá scríofa ar an leathanach féin de ghnáth, ach ní bhíonn sé amhlaidh i gcónaí. |
| TitlePage       | Boole               | ceann ar bith nó ceann amháin           | Léiríonn sé gur leathanach teidil é seo a bhaineann le cuid de lámhscríbhinn. |
| ImageFileName   | teaghrán            | ceann amháin                            | Ainm an chomhaid a aithníonn an íomhá scanta den leathanach. |
| Sensitive       | Boole               | ceann amháin                            | Má tá sé fíor, tá ábhar íogair ar an leathanach agus níor cheart é a chur ar fáil go poiblí. **(Faoi phribhléid)** |

### An Príomhbhailiúchán `part`

| Ainm an airí    | Cineál                | Bunuimhreacht                            | Cur síos                  |
| :-------------- | :-------------------- | :--------------------------------------- | :------------------------ |
| ID              | slánuimhir            | ceann amháin                             | Aitheantóir na coda (uathúil laistigh den bhailiúchán). |
| DateCreated     | am-dháta ISO 8601     | ceann ar bith nó ceann amháin            | An dáta agus an t-am a cruthaíodh an iontráil.  |
| DateModified    | am-dháta ISO 8601     | ceann ar bith nó ceann amháin            | Dáta agus am an mhionathraithe is déanaí a rinneadh ar an iontráil.  |
| ListingOrder    | teaghrán              | ceann amháin                             | Ord liostaithe na coda den lámhscríbhinn laistigh den imleabhair. |
| TitlePages      | slánuimhir            | ceann ar bith nó ceann amháin nó go leor | Seasann sé do leathanaigh theidil a bhaineann leis an gcuid den lámhscríbhinn. D’fhéadfadh teideal ginearálta, eolas ar bhailitheoirí nó focail réamhráiteacha eile a bheith ar na leathanaigh theidil. |
| Date            | [`date`](#date)       | ceann ar bith nó ceann amháin            | Meiteashonraí a bhaineann leis an dáta nó leis an tréimhse inar tiomsaíodh an chuid den lámhscríbhinn, má tá sé ar eolas. |
| Counties        | [`county`](#county)   | ceann ar bith nó ceann amháin nó go leor | Seasann sé don chontae, nó do na contaetha, in Éirinn a bhaineann leis an gcuid den lámhscríbhinn. |
| LocationsIreland | [`locationIreland`](#locationireland)  | ceann ar bith nó ceann amháin nó go leor | Seasann sé do shuíomh, nó do shuíomhanna, in Éirinn a bhaineann leis an gcuid den lámhscríbhinn. |
| Countries       | [`country`](#country) | ceann ar bith nó ceann amháin nó go leor | Seasann sé do thír, nó do thíortha, seachas Éire, a bhaineann leis an gcuid den lámhscríbhinn. |
| LocationsAbroad | [`locationAbroad`](#locationabroad) | ceann ar bith nó ceann amháin nó go leor | Seasann sé do shuíomh, nó do shuíomhanna, lasmuigh d'Éirinn a bhaineann leis an gcuid den lámhscríbhinn. |
| Collectors      | [`person`](#person)   | ceann ar bith nó ceann amháin nó go leor | Seasann sé do dhuine, nó do dhaoine, a bhfuil baint acu leis an ábhar a bhailiú. |
| Informants      | [`person`](#person)   | ceann ar bith nó ceann amháin nó go leor | Seasann sé do dhuine, nó do dhaoine, óna bhfuarthas ábhar agus an chuid den lámhscríbhinn á tiomsú. |
| RelevantPersons | [`person`](#person)   | ceann ar bith nó ceann amháin nó go leor | Seasann sé do dhuine, nó do dhaoine, a ndéantar tagairt dóibh laistigh den chuid den lámhscríbhinn, nó a bhaineann léi.  |
| ExtraInfoStatus | teaghrán              | ceann ar bith nó ceann amháin            | Sonraíonn sé [stádas](#extrainfostatus) foilsithe na réimsí `ExtraInfoEN` agus `ExtraInfoGA`. |
| ExtraInfoEN     | teaghrán              | ceann ar bith nó ceann amháin            | Tráchtaireacht saorthéacs ar an gcuid den lámhscríbhinn (i mBéarla). Scríobhadh mar chuid de thionscadal Dúchas iad. |
| ExtraInfoGA     | teaghrán              | ceann ar bith nó ceann amháin            | Tráchtaireacht saorthéacs ar an gcuid den lámhscríbhinn (i nGaeilge). Scríobhadh mar chuid de thionscadal Dúchas iad. |
| Items           | [`item`](#an-priomhbhailiuchan-item)       | ceann ar bith nó ceann amháin nó go leor | Meiteashonraí a dhéanann cur síos ar mhíreanna scoite atá sa chuid den lámhscríbhinn. |

### An Príomhbhailiúchán `item`

| Ainm an airí    | Cineál                | Bunuimhreacht                            | Cur síos                  |
| :-------------- | :-------------------- | :--------------------------------------- | :------------------------ |
| ID              | slánuimhir            | ceann amháin                             | Aitheantóir na míre (uathúil laistigh den bhailiúchán). |
| DateCreated     | am-dháta ISO 8601     | ceann ar bith nó ceann amháin            | An dáta agus an t-am a cruthaíodh an iontráil.  |
| DateModified    | am-dháta ISO 8601     | ceann ar bith nó ceann amháin            | Dáta agus am an mhionathraithe is déanaí a rinneadh ar an iontráil.  |
| EditorsPick     | am-dháta ISO 8601     | ceann ar bith nó ceann amháin nó go leor | Seasann sé don dáta ar úsáideadh an mhír mar '[Rogha na Seachtaine](https://www.duchas.ie/ga/ftr/)' ar dúchas.ie, má úsáideadh í. |
| Sensitive       | Boole                 | ceann amháin                             | Má tá sé fíor, tá ábhar íogair sa mhír agus níor cheart í a chur ar fáil go poiblí. **(Faoi phribhléid)** |
| ListingOrder    | teaghrán              | ceann ar bith nó ceann amháin            | Ord liostaithe na míre laistigh den lámhscríbhinn ina bhfaightear í. Cinntear ord na míreanna, ar an gcéad ásc, ach uimhir thosaigh an leathanaigh a úsáid ach d’fhéadfaí an t-airí `listingOrder` a úsáid, mar shampla, chun ord dhá mhír, nó níos mó, ar leathanach amháin a léiriú. |
| Date            | [`date`](#date)       | ceann ar bith nó ceann amháin            | Meiteashonraí a bhaineann leis an dáta nó leis an tréimhse inar tiomsaíodh an mhír den lámhscríbhinn, má tá sé ar eolas. |
| Title           | teaghrán              | ceann ar bith nó ceann amháin            | Teideal na míre, má chuirtear ar fáil é. |
| Extract         | teaghrán              | ceann ar bith nó ceann amháin            | Sliocht gairid ó théacs na míre. Cuirtear ar fáil de ghnáth é mura féidir airí `title` a shonrú. |
| Pages           | slánuimhir            | ceann amháin nó go leor                  | Sonraíonn sé aitheantóir(í) an leathanaigh a bhaineann leis an mír. |
| FirstPageID     | slánuimhir            | ceann amháin                             | Aithníonn sé an leathanach tosaigh a bhaineann leis an mír. Tabhair faoi deara mura gcuimsíonn an mhír níos mó ná leathanach amháin, beidh an luach céanna uirthi agus atá ar `LastPageID`. |
| LastPageID      | slánuimhir            | ceann amháin                             | Aithníonn sé an leathanach deiridh a bhaineann leis an mír. Tabhair faoi deara mura gcuimsíonn an mhír níos mó ná leathanach amháin, beidh an luach céanna uirthi agus atá ar `FirstPageID`. |
| ContentType     | teaghrán              | ceann ar bith nó ceann amháin            | [`contenttype`](#contenttype) na míre den lámhscríbhinn. |
| ContentModes    | teaghrán              | ceann ar bith nó ceann amháin nó go leor | Seasann sé do [`contentmode`](#contentmode) nó do mhodh(anna) scríbhneoireachta na míre den lámhscríbhinn.   |
| ContentScripts  | ISO 15924 cód scripte | ceann ar bith nó ceann amháin nó go leor | Seasann sé do scripteanna scríbhneoireachta na míre den lámhscríbhinn. |
| Languages       | cód teanga ISO 639-1  | ceann ar bith nó ceann amháin nó go leor | Seasann sé do theanga(cha) scríbhneoireachta na míre den lámhscríbhinn. |
| Counties        | [`county`](#county)   | ceann ar bith nó ceann amháin nó go leor | Seasann sé do chontae, nó do chontaetha, riaracháin in Éirinn a bhaineann leis an mír den lámhscríbhinn. |
| LocationsIreland | [`locationIreland`](#locationireland)  | ceann ar bith nó ceann amháin nó go leor | Seasann sé do shuíomh, nó do shuíomhanna, in Éirinn a bhaineann leis an mír den lámhscríbhinn. |
| Countries       | [`country`](#country) | ceann ar bith nó ceann amháin nó go leor | Seasann sé do thír, nó do thíortha, seachas Éire, a bhaineann leis an mír den lámhscríbhinn. |
| LocationsAbroad | [`locationAbroad`](#locationabroad) | ceann ar bith nó ceann amháin nó go leor | Seasann sé do shuíomh, nó do shuíomhanna, lasmuigh d'Éirinn a bhaineann leis an mír den lámhscríbhinn. |
| Collectors      | [`person`](#person)   | ceann ar bith nó ceann amháin nó go leor | Seasann sé do dhuine, nó do dhaoine, a bhfuil baint acu leis an ábhar a bhailiú. |
| Informants      | [`person`](#person)   | ceann ar bith nó ceann amháin nó go leor | Seasann sé do dhuine, nó do dhaoine, óna bhfuarthas ábhar agus an mhír den lámhscríbhinn á tiomsú. |
| RelevantPersons | [`person`](#person)   | ceann ar bith nó ceann amháin nó go leor | Seasann sé do dhuine, nó do dhaoine, a ndéantar tagairt dóibh laistigh den mhír den lámhscríbhinn, nó a bhaineann léi.  |
| LinkedItems     | [`ManuscriptItemLink`](#manuscriptitemlink) | ceann ar bith nó ceann amháin nó go leor | Seasann sé do mhír amháin, nó níos mó, de lámhscríbhinn a bhaineann go díreach leis an mír seo. Nascann caidreamh seicheamhach na míreanna le chéile de ghnáth (e.g. tagann na míreanna eile roimh an mír reatha nó i ndiaidh na míre reatha i sraith scéalta leanúnacha nó gaolmhara). | 
| ExtraInfoStatus | teaghrán              | ceann ar bith nó ceann amháin            | Sonraíonn sé [stádas](#extrainfostatus) foilsithe na réimsí `ExtraInfoEN` agus `ExtraInfoGA`. **(Faoi phribhléid)** |
| ExtraInfoEN     | teaghrán              | ceann ar bith nó ceann amháin            | Tráchtaireacht saorthéacs ar an mír den lámhscríbhinn (i mBéarla). Scríobhadh mar chuid de thionscadal Dúchas iad. |
| ExtraInfoGA     | teaghrán              | ceann ar bith nó ceann amháin            | Tráchtaireacht saorthéacs ar an mír den lámhscríbhinn (i nGaeilge). Scríobhadh mar chuid de thionscadal Dúchas iad. |

#### `contentType`

| Luach           | Cur síos                  |
| :-------------- | :------------------------ |
| SEAN            | Seanchas.                 |
| CÍN-LAE         | Iontráil dialainne.       |
| CEIST           | Ceistneoir.               |
| COMH            | Comhfhreagras.            |

#### `contentMode`

| Luach           | Cur síos                  |
| :-------------- | :------------------------ |
| LÁMH            | Téacs lámhscríofa.        |
| CLÓ             | Téacs clóscríofa.         |
| LÍN             | Líníocht.                 |

### `manuscriptItemLink`

Seasann sé do chaidreamh díreach idir dhá am lámhscríbhinne. Nascann caidreamh seicheamhach na míreanna le chéile de ghnáth (e.g. tagann na míreanna eile roimh an mír reatha nó i ndiaidh na míre reatha i scéalta leanúnacha nó gaolmhara). 

| Ainm an airí    | Cineál              | Bunuimhreacht                         | Cur síos                  |
| :-------------- | :------------------ | :------------------------------------ | :------------------------ |
| PartID          | slánuimhir          | ceann amháin                          | An t-aitheantóir `part` a bhaineann leis an mír den lámhscríbhinn nasctha. |
| PageID          | slánuimhir          | ceann amháin                          | An t-aitheantóir `page` a bhaineann leis an leathanach tosaigh den mhír den lámhscríbhinn nasctha. |
| ItemID          | slánuimhir          | ceann amháin                          | Aitheantóir `item` na lámhscríbhinne nasctha. |
| Sequence        | teaghrán            | ceann ar bith nó ceann amháin         | Déanann sé cur síos ar chaidreamh seicheamhach na míre nasctha (`PREV` má thagann an mhír nasctha roimh an mír reatha sa seicheamh; `NEXT` má thagann an mhír nasctha ina diaidh). |

## Bailiúchán na Scol (CBÉS)

Tá scéalta agus cuntais a ceanglaíodh ina n-imleabhair i mBailiúchán na Scol. Seasann eintiteas `volume` do gach imleabhar sa tacar sonraí agus seasann eintiteas `page` do gach leathanach. Tá tagairt i ngach eintiteas `page` freisin a aithníonn an íomhá scanta den leathanach. Le chéile, seasann eintitis `volume` agus `page` do **struchtúr fisiciúil** an bhailiúcháin. Tá **struchtúr loighciúil** ann chomh maith a anótálann agus a innéacsaíonn an struchtúr fisiciúil. Tá eintitis `part` agus `item` ann.   

Seasann eintiteas `part` do chuid ar leith laistigh d'imleabhar lámhscríbhinne agus seans go raibh sé scartha ó ábhar eile san imleabhar ar dtús. Tagann sé le ball [`msPart`](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#mspt) a shonraítear i dTreoirlínte P5 Text Encoding Initiative (TEI). I mBailiúchán na Scol, cuimsíonn `part` ábhar a bhailigh scoil amháin. I gcás scoileanna inar ghlac múinteoirí agus/nó grúpaí ranga éagsúla páirt i *Scéim na Scol*, d’fhéadfadh eintitis éagsúla `part` a bheith bainteach le scoil amháin. San API XML-bhunaithe a bhí ann roimhe seo, tugadh **caibidlí** ar chodanna lámhscríbhinne.

Seasann eintiteas `item` do shaothar scoite, ar nós scéil. Tagann sé le ball TEI [`msItem`](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html#mscoit). Tabhair faoi deara go bhfuil an mhapáil idir míreanna agus leathanaigh mórán le mórán: d'fhéadfadh mír roinnt leathanach a chuimsiú agus d'fhéadfadh leathanach roinnt míreanna a chur san áireamh. Tá sonraí mionsonraithe in eintiteas `item` ar na daoine a scríobh é, chomh maith leis an ábhar lena mbaineann sé agus sonraí eile. San API XML-bhunaithe a bhí ann roimhe seo, tugadh **scéalta** ar mhíreanna lámhscríbhinne.

D'fhéadfaí oibiacht `volume` amháin, nó níos mó, a fháil ó iarratais ar Bhailiúchán na Scol. Déantar cur síos san eolas thíos ar airíonna an chineáil oibiachta seo.

### Bailiúchán na Scol `volume`

| Ainm an airí    | Cineál              | Bunuimhreacht                         | Cur síos                  |
| :-------------- | :------------------ | :------------------------------------ | :------------------------ |
| ID              | slánuimhir          | ceann amháin                          | Aitheantóir an imleabhair (uathúil laistigh den bhailiúchán).  |
| DateCreated     | am-dháta ISO 8601   | ceann ar bith nó ceann amháin         | An dáta agus an t-am a cruthaíodh an iontráil.  |
| DateModified    | am-dháta ISO 8601   | ceann ar bith nó ceann amháin         | Dáta agus am an mhionathraithe is déanaí a rinneadh ar an iontráil. Léiríonn sé seo na nuashonruithe is déanaí ar chodanna na lámhscríbhinne, ar mhíreanna na lámhscríbhinne, agus ar thras-scríbhinní nua nó nuashonraithe  leathanaigh, chomh maith le nuashonruithe ar mheiteashonraí an imleabhair féin. |
| VolumeNumber    | teaghrán            | ceann ar bith nó ceann amháin         | Uimhir tagartha cartlainne CBÉ an imleabhair. |
| Status          | slánuimhir          | ceann amháin                          | Sonraíonn sé [stádas](#status) eagarthóireachta na hiontrála. **(Faoi phribhléid)**  |
| Type            | teaghrán            | ceann amháin                          | Déanann sé idirdhealú idir an [cineál](#type) imleabhair de chuid Bhailiúchán na Scol atá ann. |
| Pages           | [`page`](#bailiuchan-na-scol-page)     | ceann amháin                          | Meiteashonraí a dhéanann cur síos ar leathanaigh fhisiciúla an imleabhair. |
| Parts           | [`part`](#bailiuchan-na-scol-part)     | ceann ar bith nó ceann amháin         | Meiteashonraí a dhéanann cur síos ar na codanna loighciúla a fhoroinneann imleabhar na lámhscríbhinne agus a bhfuil ann. |

#### `type`

| Luach           | Cur síos                  |
| :-------------- | :------------------------ |
| bound-volume    | Tá codanna a bhí scartha ar dtús ach a ceanglaíodh le chéile san imleabhar. |
| copybook-package | Tá na bunchóipleabhair a d’úsáid na páistí chun ábhair béaloidis a thras-scríobh san imleabhar. |
| volume          | Tá an t-imleabhar ar aon dul leis na himleabhair a cruthaíodh mar chuid de scéim bailithe *Scéim na Scol*. |

### Bailiúchán na Scol `page`

| Ainm an airí    | Cineál              | Bunuimhreacht                         | Cur síos                  |
| :-------------- | :------------------ | :------------------------------------ | :------------------------ |
| ID              | slánuimhir          | ceann amháin                          | Aitheantóir an leathanaigh (uathúil laistigh den bhailiúchán). |
| DateCreated     | am-dháta ISO 8601   | ceann ar bith nó ceann amháin         | An dáta agus an t-am a cruthaíodh an iontráil.  |
| DateModified    | am-dháta ISO 8601   | ceann ar bith nó ceann amháin         | Dáta agus am an mhionathraithe is déanaí a rinneadh ar an iontráil.  |
| PageNumber      | teaghrán            | ceann amháin                          | Uimhir an leathanaigh.     |
| ListingOrder    | teaghrán            | ceann amháin                          | Ord liostaithe an leathanaigh laistigh den bhailiúchán. Bíonn sé seo díreach mar an gcéanna le huimhir an leathanaigh atá scríofa ar an leathanach féin de ghnáth, ach ní bhíonn sé amhlaidh i gcónaí. |
| TitlePage       | Boole               | ceann ar bith nó ceann amháin         | Léiríonn sé gur leathanach teidil é seo a bhaineann le cuid de lámhscríbhinn. |
| ImageFileName   | teaghrán            | ceann amháin                          | Ainm an chomhaid a aithníonn an íomhá scanta den leathanach. |
| Sensitive       | Boole               | ceann amháin                          | Má tá sé fíor, tá ábhar íogair ar an leathanach agus níor cheart é a chur ar fáil go poiblí. **(Faoi phribhléid)** |
| Transcripts     | [`transcript`](#transcript) | ceann ar bith nó ceann amháin nó go leor | Tras-scríbhinn amháin, nó níos mó, den ábhar ar leathanach na lámhscríbhinne a chuir baill de thionscadal tras-scríofa [Meitheal Dúchas.ie](https://www.duchas.ie/ga/meitheal/) ar fáil. |

### Bailiúchán na Scol `part`

| Ainm an airí    | Cineál              | Bunuimhreacht                            | Cur síos                  |
| :-------------- | :------------------ | :--------------------------------------- | :------------------------ |
| ID              | slánuimhir          | ceann amháin                             | Aitheantóir na coda (uathúil laistigh den bhailiúchán). |
| DateCreated     | am-dháta ISO 8601   | ceann ar bith nó ceann amháin            | An dáta agus an t-am a cruthaíodh an iontráil.  |
| DateModified    | am-dháta ISO 8601   | ceann ar bith nó ceann amháin            | Dáta agus am an mhionathraithe is déanaí a rinneadh ar an iontráil.  |
| ListingOrder    | teaghrán            | ceann amháin                             | Ord liostaithe na coda den lámhscríbhinn laistigh den imleabhair. |
| TitlePages      | slánuimhir          | ceann ar bith nó ceann amháin nó níos mó | Seasann sé do leathanaigh theidil a bhaineann leis an gcuid den lámhscríbhinn. De ghnáth, bíonn eolas ar an scoil agus ar an gceantar áitiúil ar na leathanaigh theidil. |
| School          | [`school`](#school) | ceann ar bith nó ceann amháin            | Meiteashonraí a dhéanann cur síos ar an scoil a bhaineann leis an gcuid den lámhscríbhinn. |
| Teachers        | [`person`](#bailiuchan-na-scol-person) | ceann ar bith nó ceann amháin nó go leor | Seasann sé do mhúinteoir, nó do mhúinteoirí, scoile a thiomsaigh an t-ábhar laistigh den chuid den lámhscríbhinn. |
| Items           | [`item`](#bailiuchan-na-scol-item)     | ceann ar bith nó ceann amháin nó go leor | Meiteashonraí a dhéanann cur síos ar mhíreanna scoite atá sa chuid den lámhscríbhinn. |

### Bailiúchán na Scol `item`

| Ainm an airí    | Cineál                 | Bunuimhreacht                         | Cur síos               |
| :-------------- | :--------------------- | :------------------------------------ | :------------------------ |
| ID              | slánuimhir             | ceann amháin                          | Aitheantóir na míre (uathúil laistigh den bhailiúchán). |
| DateCreated     | am-dháta ISO 8601      | ceann ar bith nó ceann amháin         | An dáta agus an t-am a cruthaíodh an iontráil.  |
| DateModified    | am-dháta ISO 8601      | ceann ar bith nó ceann amháin         | Dáta agus am an mhionathraithe is déanaí a rinneadh ar an iontráil.  |
| EditorsPick     | am-dháta ISO 8601      | ceann ar bith nó ceann amháin nó go leor | Seasann sé don dáta ar úsáideadh an mhír mar '[Rogha na Seachtaine](https://www.duchas.ie/ga/ftr/)' ar dúchas.ie, má úsáideadh í. |
| Sensitive       | Boole                  | ceann amháin                          | Má tá sé fíor, tá ábhar íogair sa mhír agus níor cheart í a chur ar fáil go poiblí. **(Faoi phribhléid)** |
| ListingOrder    | teaghrán               | ceann ar bith nó ceann amháin         | Ord liostaithe na míre laistigh den lámhscríbhinn ina bhfaightear í. Cinntear ord na míreanna, ar an gcéad ásc, ach uimhir thosaigh an leathanaigh a úsáid ach d’fhéadfaí an t-airí `listingOrder` a úsáid, mar shampla, chun ord dhá mhír, nó níos mó, ar leathanach amháin a léiriú. |
| Title           | teaghrán               | ceann ar bith nó ceann amháin         | Teideal na míre, má chuirtear ar fáil é. |
| Extract         | teaghrán               | ceann ar bith nó ceann amháin         | Sliocht gairid ó théacs na míre. Cuirtear ar fáil de ghnáth é mura féidir airí `title` a shonrú. |
| Pages           | slánuimhir             | ceann amháin nó go leor               | Sonraíonn sé aitheantóir(í) an leathanaigh a bhaineann leis an mír. |
| FirstPageID     | slánuimhir             | ceann amháin                          | Aithníonn sé an leathanach tosaigh a bhaineann leis an mír. Tabhair faoi deara mura gcuimsíonn an mhír níos mó ná leathanach amháin, beidh an luach céanna uirthi agus atá ar `LastPageID`.  |
| LastPageID      | slánuimhir             | ceann amháin                          | Aithníonn sé an leathanach deiridh a bhaineann leis an mír. Tabhair faoi deara mura gcuimsíonn an mhír níos mó ná leathanach amháin, beidh an luach céanna uirthi agus atá ar `FirstPageID`.  |
| Topics          | [`topic`](#bailiuchan-na-scol-topic) | ceann ar bith nó ceann amháin    | Topaic, nó topaicí, ó [Chlár Ábhar Bhailiúchán na Scol](https://www.duchas.ie/ga/tpc/cbes) a bhaineann leis an mír seo.  |
| Languages       | cód teanga ISO 639-1   | ceann ar bith nó ceann amháin nó go leor | Seasann sé do theanga(cha) scríbhneoireachta na míre den lámhscríbhinn. |
| Counties        | [`county`](#county)    | ceann ar bith nó ceann amháin nó go leor | Seasann sé do chontae, nó do chontaetha, riaracháin in Éirinn a bhaineann leis an mír den lámhscríbhinn seachas na contaetha a bhaineann leis an scoil nó le háit chónaithe an fhaisnéiseora. |
| LocationsIreland | [`locationIreland`](#locationireland)  | ceann ar bith nó ceann amháin nó go leor | Seasann sé do shuíomh, nó do shuíomhanna, in Éirinn a bhaineann leis an mír den lámhscríbhinn, seachas na suíomhanna a bhaineann leis an scoil nó le háit chónaithe an fhaisnéiseora. |
| Collectors      | [`person`](#bailiuchan-na-scol-person) | ceann ar bith nó ceann amháin nó go leor | Seasann sé do dhuine, nó do dhaoine, a bhfuil baint acu leis an mír den lámhscríbhinn a bhailiú. |
| Informants      | [`person`](#bailiuchan-na-scol-person) | ceann ar bith nó ceann amháin nó go leor | Seasann sé do dhuine, nó do dhaoine, óna bhfuarthas an mhír den lámhscríbhinn. |

### Bailiúchán na Scol `person`

De bharr scóip thionscadal digitithe Bhailiúchán na Scoil, ní raibh sé indéanta go fóill tacar normalaithe meiteashonraí pearsanta a asbhaint. Ina ionad sin, bhí sé mar aidhm ag céimeanna tosaigh an tionscadail eolas a fháil ar na daoine a dtagraítear dóibh laistigh den bhailiúchán 'mar atá'. Mar sin de, tá seans ann go ndéanfaí tagairt don duine céanna le níos mó ná eintiteas `person` amháin.

| Ainm an airí    | Cineál                | Bunuimhreacht                            | Cur síos                  |
| :-------------- | :-------------------- | :--------------------------------------- | :------------------------ |
| ID              | slánuimhir            | ceann amháin                             | Aitheantóir an duine.     |
| Names           | [`name`](#name)       | ceann amháin nó go leor                  | Ainmneacha a bhaineann leis an duine.  |
| Gender          | teaghrán              | ceann ar bith nó ceann amháin            | Inscne an duine (`b` nó `f`). |
| Age             | [`age`](#bailiuchan-na-scol-age) | ceann ar bith nó ceann amháin  | Meiteashonraí maidir le haois an duine. |
| AddressesIreland | [`locationIreland`](#locationireland) | ceann ar bith nó ceann amháin nó go leor | Seasann sé do shuíomh, nó do shuíomhanna, in Éirinn a thugtar mar sheoladh an duine. |
| Occupations     | teaghrán              | ceann ar bith nó ceann amháin nó go leor | Gairmeacha a bhaineann leis an duine. Níl na gairmeacha nasctha le foclóir rialaithe: taifeadann siad gairmeacha an duine de réir mar a scríobhadh síos iad agus d’fhéadfadh siad a bheith i mBéarla nó i nGaeilge. |
| CollectorRelationship | teaghrán          | ceann ar bith nó ceann amháin         | Más faisnéiseoir é an duine seo, léiríonn an t-airí seo an caidreamh (teaghlaigh nó eile) atá ag an bhfaisnéiseoir maidir leis an duine a bhailíonn an t-ábhar. |

#### `CollectorRelationship`

| Luach           | Cur síos                  |
| :-------------- | :------------------------ |
| GRPAR           | Seantuismitheoir an bhailitheora atá i gceist.   |
| PAR             | Tuismitheoir an bhailitheora atá i gceist. |
| REL             | Tá gaol ag an duine leis an mbailitheoir (tá an caidreamh neamhshonraithe). |
| UNK             | Tá an caidreamh anaithnid. |
| UNREL           | Níl gaol ag an duine leis an mbailitheoir. |

### Bailiúchán na Scol `age`

| Ainm an airí    | Cineál                 | Bunuimhreacht                         | Cur síos                  |
| :-------------- | :--------------------- | :------------------------------------ | :------------------------ |
| Age             | slánuimhir             | ceann amháin                          | Aois an duine i mblianta, má tá sé ar eolas. |
| Qualifier       | teaghrán               | ceann ar bith nó ceann amháin         | Eolas breise maidir le haois an duine. |
| RangeMax        | slánuimhir             | ceann ar bith nó ceann amháin         | Mura bhfuil sé ar neamhní, sonraítear sa luach seo uasaois fhéideartha an duine, i.e. más ionann `age` an duine agus 50 agus más ionann an `RangeMax` agus 60, tá aois an duine sa raon idir 50-60 bliain. |

#### `Qualifier`

| Luach           | Cur síos                  |
| :-------------- | :------------------------ |
| APPROX          | Garbhaois atá ann.   |
| OVER            | Tá aois cheart an duine níos airde ná luach `age`, e.g. tá an duine 'níos sine ná 60'. |

### `school`

Déanann sé cur síos ar scoil a ghlac páirt i scéim bailithe *Scéim na Scol*.

| Ainm an airí    | Cineál              | Bunuimhreacht                           | Cur Síos               |
| :-------------- | :------------------ | :------------------------------------ | :------------------------ |
| Name            | teaghrán            | ceann amháin                          | Ainm na scoile.           |
| RollNumber      | teaghrán            | ceann ar bith nó ceann amháin         | Uimhir rolla na Roinne Oideachais de chuid na scoile. |
| Locations       | [`locationIreland`](#locationireland) | ceann ar bith nó ceann amháin nó go leor | Suíomh, nó suíomhanna, a bhaineann leis an scoil. |

### Bailiúchán na Scol `topic`

Léiríonn sé topaic ó [Chlár Ábhar Bhailiúchán na Scol](https://www.duchas.ie/ga/tpc/cbes). Tabhair faoi deara go mbíonn na topaicí ordlathach agus go mbeidh sonraí i dtopaic ar leith a bhaineann le catagóirí réamhtheachtacha na topaice, má bhaineann sé le hábhar.

| Ainm an airí    | Cineál              | Bunuimhreacht                         | Cur síos                  |
| :-------------- | :------------------ | :------------------------------------ | :------------------------ |
| ID              | slánuimhir          | ceann amháin                          | Aitheantóir na topaice.     |
| TitleEN         | teaghrán            | ceann amháin                          | Teideal Béarla na topaice. |
| TitleGA         | teaghrán            | ceann amháin                          | Teideal Gaeilge na topaice. |
| SubTopics       | `topic`             | ceann ar bith nó ceann amháin         | Sliochtnóid ordlathacha na topaice seo. |

## An Bailiúchán Grianghraf (CBÉG)

D’fhéadfaí oibiacht `photograph` amháin, nó níos mó, a fháil ó iarratais ar an mBailiúchán Grianghraf. Déantar cur síos san eolas thíos ar airíonna an chineáil oibiachta seo.

### `photograph`

| Ainm an airí   | Cineál                | Bunuimhreacht                              | Cur síos               |
| :-------------- | :------------------ | :--------------------------------------- | :------------------------ |
| ID              | slánuimhir          | ceann amháin                             | Aitheantóir an ghrianghraif (uathúil laistigh de bhailiúchán). |
| DateCreated     | am-dháta ISO 8601   | ceann amháin                             | An dáta agus an t-am a cruthaíodh an iontráil.  |
| DateModified    | am-dháta ISO 8601   | ceann ar bith nó ceann amháin            | Dáta agus am an mhionathraithe is déanaí a rinneadh ar an iontráil.  |
| EditorsPick     | am-dháta ISO 8601   | ceann ar bith nó ceann amháin nó go leor | Seasann sé don dáta ar úsáideadh an mhír mar  '[Rogha na Seachtaine](https://www.duchas.ie/ga/ftr/)' ar dúchas.ie, má úsáideadh í. |
| ReferenceNumber | teaghrán            | ceann ar bith nó ceann amháin            | Tagairt chartlainne CBÉ an ghrianghraif.      |
| Status          | slánuimhir          | ceann amháin                             | Sonraíonn sé [stádas](#status) eagarthóireachta na hiontrála. **(Faoi phribhléid)**  |
| Sensitive       | Boole               | ceann amháin                             | Má tá sé fíor, tá ábhar íogair sa mhír agus níor cheart í a chur ar fáil go poiblí. **(Faoi phribhléid)**  |
| Digitized       | Boole               | ceann amháin                             | Má tá sé fíor, baineann an iontráil le híomhá dhigitithe.  |
| Copyright       | teaghrán            | ceann ar bith nó ceann amháin            | Seasann sé do shealbhóir [cóipchirt](#copyright) na hiontrála.  |
| Condition       | slánuimhir          | ceann ar bith nó ceann amháin            | Seasann sé do [bhail](#condition) nó do shoiléire iomlán na híomhá digitithe a bhaineann leis an iontráil seo.  |
| ConditionDescription | teaghrán              | ceann ar bith nó ceann amháin         | Tráchtaireacht bhreise ar bhail na híomhá, más cuí.  |
| HandbookTopic   | [`handbookTopic`](#handbooktopic)     | ceann ar bith nó ceann amháin         | Seasann sé don cheannteideal ([topaic](https://www.duchas.ie/ga/tpc/cbeg)) gaolmhar ábhair in *A Handbook of Irish Folklore* le Seán Ó Súilleabháin. |
| Date            | [`date`](#date)     | ceann ar bith nó ceann amháin            | Meiteashonraí a bhaineann leis an dáta ar glacadh an grianghraf. |
| Photographer    | [`person`](#person) | ceann ar bith nó ceann amháin            | Seasann sé don duine a ghlac an grianghraf. |
| RelevantPersons | [`person`](#person) | ceann ar bith nó ceann amháin nó go leor | Seasann sé do dhaoine atá le feiceáil sa ghrianghraf, nó atá bainteach ar bhealach eile leis. |
| Counties        | [`county`](#county) | ceann ar bith nó ceann amháin nó go leor | Seasann sé do chontae, nó do chontaetha, riaracháin in Éirinn inar glacadh an grianghraf. |
| LocationsIreland | [`locationIreland`](#locationireland)  | ceann ar bith nó ceann amháin nó go leor | Seasann sé do shuíomh, nó do shuíomhanna, in Éirinn a bhaineann leis an ngrianghraf. |
| Countries       | [`country`](#country) | ceann ar bith nó ceann amháin nó go leor | Seasann sé do thír, nó do thíortha, seachas Éire, a bhaineann leis an ngrianghraf. |
| LocationsAbroad | [`locationAbroad`](#locationabroad) | ceann ar bith nó ceann amháin nó go leor | Seasann sé do shuíomh, nó do shuíomhanna, lasmuigh d'Éirinn a bhaineann leis an ngrianghraf. |
| ArchivedDescriptionStatus | teaghrán        | ceann ar bith nó ceann amháin         | Sonraíonn sé [stádas](#archiveddescriptionstatus) foilsithe an réimse `ArchivedDescription`. **(Faoi phribhléid)**  |
| ArchivedDescription | teaghrán             | ceann ar bith nó ceann amháin         | Cur síos cartlainne saorthéacs ar an ngrianghraf. Iompórtáladh ón gcóras bainistíochta sonraí de chuid CBÉ a bhí ann roimhe seo é ag tús an phróisis digitithe. |
| ExtraInfoStatus | teaghrán            | ceann ar bith nó ceann amháin            | Sonraíonn sé [stádas](#extrainfostatus) na réimsí `ExtraInfoEN` agus `ExtraInfoGA`. **(Faoi phribhléid)** |
| ExtraInfoEN     | teaghrán            | ceann ar bith nó ceann amháin            | Tráchtaireacht saorthéacs ar an ngrianghraf (i mBéarla). Scríobhadh mar chuid de thionscadal Dúchas í. |
| ExtraInfoGA     | teaghrán            | ceann ar bith nó ceann amháin            | Tráchtaireacht saorthéacs ar an ngrianghraf (i nGaeilge). Scríobhadh mar chuid de thionscadal Dúchas í. |
| Formats         | [`format`](#format)             | ceann ar bith nó ceann amháin nó go leor  | Déanann sé cur síos ar fhormáid na híomhá fisiciúla atá ag CBÉ agus a bhaineann leis an iontráil. |
| ArchivedInfo    | [`archivedInfo`](#archivedinfo)      | ceann ar bith nó ceann amháin         | Cuimsíonn sé an t-eolas cartlainne a iompórtáladh ón gcóras bainistíochta sonraí de chuid CBÉ a bhí ann roimhe seo ag tús an phróisis digitithe. **(Faoi phribhléid)** |
| Digitization    | [`digitization`](#digitization)      | ceann ar bith nó ceann amháin         | Meiteashonraí a bhaineann le digitiú íomhá nó íomhánna na cartlainne a bhaineann leis an iontráil. |

#### `copyright`

| Luach           | Cur síos                  |
| :-------------- | :------------------------ |
| CBE             | Is é CBÉ an sealbhóir cóipchirt. |
| OTH             | Tá cóipcheart ag eintiteas eile seachas CBÉ. |
| NOT             | Ní bhaineann cóipcheart le hábhar.  |
| UNK             | Tá an stádas cóipchirt anaithnid. |

#### `condition`

| Luach           | Cur síos                  |
| :-------------- | :------------------------ |
| 0               | Drochbhail.               |
| 1               | Meán-bhail.               |
| 2               | Dea-bhail.                |

#### `archivedDescriptionStatus`

Sonraíonn sé stádas foilsithe an réimse `archivedDescription`.

| Luach           | Cur síos               |
| :-------------- | :------------------------ |
| EDIT            | Níl an réimse `ArchivedDescription` oiriúnach le foilsiú. |
| PUB             | Tá an réimse `ArchivedDescription` oiriúnach le foilsiú. |

### `handbookTopic`

Seasann sé do cheannteideal ([topaic](https://www.duchas.ie/ga/tpc/cbeg)) ábhair in *A Handbook of Irish Folklore* le Seán Ó Súilleabháin. Bhí sé mar chleachtas ag CBÉ grianghraif in CBÉG a cheangal le topaic sa lámhleabhar agus is ionann ID na topaice sa lámhleabhar agus an chéad deighleán de `ReferenceNumber` an ghrianghraif.  

| Ainm an airí    | Cineál              | Bunuimhreacht       | Cur síos                  |
| :-------------- | :------------------ | :------------------ | :------------------------ |
| ID              | teaghrán            | ceann amháin        | Aitheantóir uathúil na topaice. |
| TopicEN         | teaghrán            | ceann amháin        | Catagóir ghinearálta na topaice (i mBéarla). |
| TopicGA         | teaghrán            | ceann amháin        | Catagóir ghinearálta na topaice (i nGaeilge). |
| SubTopicEN      | teaghrán            | ceann amháin        | Catagóir shonrach na topaice (i mBéarla). |
| SubTopicGA      | teaghrán            | ceann amháin        | Catagóir shonrach na topaice (i nGaeilge). |

### `format`

| Ainm an airí    | Cineál                 | Bunuimhreacht                         | Cur síos               |
| :-------------- | :--------------------- | :------------------------------------ | :------------------------ |
| Quantity        | slánuimhir             | ceann ar bith nó ceann amháin         | An méid íomhánna san fhormáid seo atá ag CBÉ. |
| Color           | teaghrán               | ceann ar bith nó ceann amháin         | Cineál datha na híomhá. |
| ColorComment    | teaghrán               | ceann ar bith nó ceann amháin         | Tráchtaireacht bhreise maidir le cineál datha na híomhá. |
| Dimensions      | teaghrán               | ceann ar bith nó ceann amháin         | Toisí na híomhá fisiciúla. |
| DimensionsComment | teaghrán              | ceann ar bith nó ceann amháin         | Tráchtaireacht bhreise maidir le toisí na híomhá. |
| Medium          | teaghrán               | ceann ar bith nó ceann amháin         | Meán na híomhá. |
| MediumComment   | teaghrán               | ceann ar bith nó ceann amháin         | Tráchtaireacht bhreise maidir le meán na híomhá. |
| Physical        | teaghrán               | ceann ar bith nó ceann amháin         | Carachtar fisiciúil na híomhá. |
| PhysicalComment | teaghrán               | ceann ar bith nó ceann amháin         | Tráchtaireacht bhreise maidir le carachtar fisiciúil na híomhá. |

### `archivedInfo`

Mar chuid de thionscadal Dúchas, ionghabhadh meiteashonraí grianghraf ón gcóras bainistíochta sonraí de chuid CBÉ a bhí ann roimhe seo ar mhaithe le cartlannú. Coinníonn an oibiacht `ArchivedInfo` na meiteashonraí seo.  

| Ainm an airí    | Cineál              | Bunuimhreacht                         | Cur síos               |
| :-------------- | :------------------ | :------------------------------------ | :------------------------ |
| Copyright       | teaghrán            | ceann ar bith nó ceann amháin         | Sealbhóir cóipchirt an ghrianghraif. |
| Condition       | teaghrán            | ceann ar bith nó ceann amháin         | Bail fhisiciúil an ghrianghraif. |
| Topic           | teaghrán            | ceann ar bith nó ceann amháin         | Ceannteideal ([topaic](https://www.duchas.ie/ga/tpc/cbeg)) gaolmhar ábhair in *A Handbook of Irish Folklore* le Seán Ó Súilleabháin. |
| Date            | teaghrán            | ceann ar bith nó ceann amháin         | An dáta ar glacadh an grianghraf. |
| Photographer    | teaghrán            | ceann ar bith nó ceann amháin         | Ainm an ghrianghrafadóra. |
| Location        | teaghrán            | ceann ar bith nó ceann amháin         | An áit ar glacadh an grianghraf. |
| Format          | teaghrán            | ceann ar bith nó ceann amháin         | Eolas maidir le formáid na n-íomhánna fisiciúla atá ag CBÉ. |

### `digitization`

| Ainm an airí    | Cineál              | Bunuimhreacht       | Cur síos                |
| :-------------- | :------------------ | :------------------ | :------------------------ |
| DateCaptured    | teaghrán            | ceann amháin        | An dáta ar digitíodh an íomhá. |
| Operator        | teaghrán            | ceann amháin        | Ainm an oibritheora atá freagrach. **(Faoi phribhléid)** |
| CaptureDevice   | teaghrán            | ceann amháin        | An gléas gabhála a úsáideadh. |
| CaptureSoftware | teaghrán            | ceann amháin        | Na bogearraí gabhála a úsáideadh. |
| SourceCondition | teaghrán            | ceann amháin        | Bail na híomhá fisiciúla foinsí. |
| CopyNote        | teaghrán            | ceann amháin        | Cóip déanta den bhuníomhá (tá nó níl). |
| MimeType        | teaghrán            | ceann amháin        | An cineál [MIME](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types) atá san íomhá dhigitithe. |
| ImageBitDepth   | teaghrán            | ceann amháin        | Doimhneacht datha na híomhá digitithe. |
| ImageEditor     | teaghrán            | ceann amháin        | Bogearraí eagarthóireachta íomhánna a úsáideadh. |
| ImageResolution | teaghrán            | ceann amháin        | Taifeach na híomhá digitithe. |
| ImageSize       | teaghrán            | ceann amháin        | Méid picteilíní na híomhá digitithe. |
| FileSize        | teaghrán            | ceann amháin        | Méid comhaid na híomhá digitithe. |
| ComputerOS      | teaghrán            | ceann amháin        | An córas oibriúcháin a úsáideadh. |
| Storage         | teaghrán            | ceann amháin        | Sonraí stórála na híomhá. |

## An Bunachar Daoine (CBÉD)

D'fhéadfaí oibiacht `person` amháin, nó níos mó, a fháil ó iarratais ar an mBunachar Daoine. Déantar cur síos san eolas thíos ar airíonna an chineáil oibiachta seo

### `person`

| Ainm an airí    | Cineál              | Bunuimhreacht                            | Cur síos                  |
| :-------------- | :------------------ | :--------------------------------------- | :------------------------ |
| ID              | slánuimhir          | ceann amháin                             | Aitheantóir an duine (uathúil laistigh den bhailiúchán). |
| DateCreated     | am-dháta ISO 8601   | ceann amháin                             | An dáta agus an t-am a cruthaíodh an iontráil.  |
| DateModified    | am-dháta ISO 8601   | ceann ar bith nó ceann amháin            | Dáta agus am an mhionathraithe is déanaí a rinneadh ar an iontráil.  |
| Names           | [`name`](#name)     | ceann amháin nó go leor                  | Ainmneacha a bhaineann leis an duine.  |
| Gender          | teaghrán            | ceann ar bith nó ceann amháin            | Inscne an duine (`b` nó `f`). |
| AinmID          | slánuimhir          | ceann ar bith nó ceann amháin            | Aitheantóir uathúil an duine i mbunachar sonraí [ainm.ie](https://www.ainm.ie). |
| ViafID          | slánuimhir          | ceann ar bith nó ceann amháin            | Aitheantóir uathúil an duine i mbunachar sonraí [VIAF](https://viaf.org/). |
| BirthDate       | [`date`](#date)     | ceann ar bith nó ceann amháin            | Dáta breithe an duine. |
| DeathDate       | [`date`](#date)     | ceann ar bith nó ceann amháin            | Dáta báis an duine. |
| BirthCounty     | [`county`](#county) | ceann ar bith nó ceann amháin            | An contae inar rugadh an duine, má rugadh in Éirinn  é/í. |
| BirthPlaceIreland | [`locationIreland`](#locationireland) | ceann ar bith nó ceann amháin         | An áit ar rugadh an duine, má rugadh in Éirinn é/í.  |
| BirthCountry    | [`country`](#country) | ceann ar bith nó ceann amháin         | An tír inar rugadh an duine, má rugadh lasmuigh d'Éirinn é/í.  |
| BirthPlaceAbroad | [`locationAbroad`](#locationabroad) | ceann ar bith nó ceann amháin         | An áit ar rugadh an duine, má rugadh lasmuigh d'Éirinn é/í. |
| Counties        | [`county`](#county) | ceann ar bith nó ceann amháin nó go leor | Seasann sé do chontae, nó do chontaetha, riaracháin in Éirinn a bhaineann leis an duine. |
| AddressesIreland | [`locationIreland`](#locationireland) | ceann ar bith nó ceann amháin nó go leor | Seasann sé do shuíomh, nó do shuíomhanna, in Éirinn a bhaineann leis an duine. |
| Countries       | [`country`](#country) | ceann ar bith nó ceann amháin nó go leor | Seasann sé do thír, nó do thíortha, seachas Éire, a bhaineann leis an duine. |
| AddressesAbroad | [`locationAbroad`](#locationabroad) | ceann ar bith nó ceann amháin nó go leor | Seasann sé do shuíomh, nó do shuíomhanna, lasmuigh d'Éirinn a bhaineann leis an duine. |
| Occupations     | [`occupation`](#occupation) | ceann ar bith nó ceann amháin nó go leor | Gairmeacha a bhaineann leis an duine. |

### `name`

| Ainm an airí    | Cineál              | Bunuimhreacht                         | Cur síos                  |
| :-------------- | :------------------ | :------------------------------------ | :------------------------ |
| FirstNames      | teaghrán            | ceann ar bith nó ceann amháin         | Céadainm(neacha), agus lárainm(neacha) nó leasainm(neacha), an duine. |
| Surname         | teaghrán            | ceann ar bith nó ceann amháin         | An sloinne atá ar dhuine.       |
| FullName        | teaghrán            | ceann amháin                          | Ainm iomlán an duine, lena n-áirítear céadainm(neacha) agus sloinne. |

### `occupation`

| Ainm an airí    | Cineál              | Bunuimhreacht         | Cur síos               |
| :-------------- | :------------------ | :------------------ | :------------------------ |
| ID              | teaghrán            | ceann amháin        | Aitheantóir uathúil na gairme. |
| NameEN          | teaghrán            | ceann amháin        | Ainm na gairme (i mBéarla). |
| NameGA          | teaghrán            | ceann amháin        | Ainm na gairme (i nGaeilge). |

## Eintitis choiteanna

Baineann roinnt eintiteas le bailiúcháin éagsúla. Déantar cur síos orthu thíos. 

### `coordinates`

| Ainm an airí    | Cineál              | Bunuimhreacht       | Cur síos                  |
| :-------------- | :------------------ | :------------------ | :------------------------ |
| Latitude        | dúbailte            | ceann amháin        | An chomhordanáid domhanleithid. |
| Longitude       | dúbailte            | ceann amháin        | An chomhordanáid domhanfhaid. |

### `county`

| Ainm an airí    | Cineál              | Bunuimhreacht                | Cur síos                  |
| :-------------- | :------------------ | :--------------------------- | :------------------------ |
| LogainmID       | slánuimhir          | ceann amháin                 | Aitheantóir uathúil an chontae i mbunachar sonraí [logainm.ie](https://www.logainm.ie). |
| NameEN          | teaghrán            | ceann amháin                 | Ainm Béarla an chontae. |
| NameGA          | teaghrán            | ceann amháin                 | Ainm Gaeilge an chontae. |
| QualifiedNameEN | teaghrán            | ceann amháin                 | Ainm Béarla an chontae, a bhfuil an cáilitheoir "Co." mar réimír leis. |
| QualifiedNameGA | teaghrán            | ceann amháin                 | Ainm Gaeilge an chontae, a bhfuil an cáilitheoir "Co." mar réimír leis agus ar cuireadh an cás agus an t-infhilleadh ceart gramadaí i bhfeidhm. |
| Coordinates     | [`coordinates`](#coordinates) | ceann amháin                 | Tacar comhordanáidí geografacha a bhaineann leis an gcontae. |

### `country`

| Ainm an airí    | Cineál              | Bunuimhreacht       | Cur síos                  |
| :-------------- | :------------------ | :------------------ | :------------------------ |
| IsoCode         | teaghrán            | ceann amháin        | Cód tíre ISO 3166 na tíre (féach an nóta thíos). |
| GeoNameID       | slánuimhir          | ceann amháin        | Aitheantóir uathúil na tíre i mbunachar sonraí [geonames.org](http://www.geonames.org). |
| NameEN          | teaghrán            | ceann amháin        | Ainm Béarla na tíre. |
| NameGA          | teaghrán            | ceann amháin        | Ainm Gaeilge na tíre. |
| Coordinates     | [`coordinates`](#coordinates) | ceann amháin        | Tacar comhordanáidí geografacha a bhaineann leis an tír. |

**Tabhair faoi deara:** Cloíonn cóid tíre san airí `IsoCode` le caighdeán ISO 3166-1 ach amháin Sasana (`GB-ENG`), Tuaisceart Éireann (`GB-NIR`), Albain (`GB-SCT`) agus an Bhreatain Bheag (`GB-WLS`) ina n-úsáidtear cód ISO 3166-2. I gcás na dtíortha seo, bhí sé riachtanach taifeach ní b’fhearr ná an taifeach a chuireann caighdeán ISO 3166-1 ar fáil a bheith iontu.  

### `date`

| Ainm an airí    | Cineál              | Bunuimhreacht                         | Cur síos               |
| :-------------- | :------------------ | :------------------------------------ | :------------------------ |
| IsoDate         | am-dháta ISO 8601   | ceann ar bith nó ceann amháin         | Comhiomlánaíonn sé luachanna na n-airíonna `Year`, `Month` agus `Day` thíos i bhfoirm theaghrán am-dháta ISO 8601. |
| IsoStartDate    | am-dháta ISO 8601   | ceann ar bith nó ceann amháin         | Comhiomlánaíonn sé luachanna na n-airíonna `PeriodStartYear`, `PeriodStartMonth` agus `PeriodStartDay` thíos chun an dáta tosaigh a léiriú in eatramh ama. |
| IsoEndDate      | am-dháta ISO 8601   | ceann ar bith nó ceann amháin         | Comhiomlánaíonn sé luachanna na n-airíonna `PeriodEndYear`, `PeriodEndMonth` agus `PeriodEndDay` thíos chun an dáta deiridh a léiriú in eatramh ama. |
| IsoDuration     | am-dháta ISO 8601   | ceann ar bith nó ceann amháin         | Léiríonn sé an tréimhse ama idir na hairíonna `IsoStartDate` agus `IsoEndDate`, más cuí. |
| Accuracy        | teaghrán            | ceann ar bith nó ceann amháin         | Léiríonn sé cruinneas an eolais ar an dáta ach foclóir caighdeánach de chuid [MODS](http://www.loc.gov/standards/mods/) (Scéimre um Chur Síos ar Oibiachtaí Meiteashonraí) maidir leis an gcáilitheoir dáta a úsáid. |
| Year            | slánuimhir          | ceann ar bith nó ceann amháin         | Seasann sé don bhliain i bhformáid `YYYY`. |
| Month           | slánuimhir          | ceann ar bith nó ceann amháin         | Seasann sé don mhí féilire (luachanna 1-12). |
| Day             | slánuimhir          | ceann ar bith nó ceann amháin         | Seasann sé don lá den mhí (luachanna 1-31). |
| PeriodStartYear | slánuimhir          | ceann ar bith nó ceann amháin         | Seasann sé don bhliain tosaigh in eatramh ama i bhformáid `YYYY`. |
| PeriodStartMonth | slánuimhir         | ceann ar bith nó ceann amháin         | Seasann sé don mhí féilire tosaigh (luachanna 1-12) in eatramh ama. |
| PeriodStartDay  | slánuimhir          | ceann ar bith nó ceann amháin         | Seasann sé don lá tosaigh den mhí (luachanna 1-31) in eatramh ama. |
| PeriodEndYear   | slánuimhir          | ceann ar bith nó ceann amháin         | Seasann sé don bhliain deiridh in eatramh ama i bhformáid `YYYY` . |
| PeriodEndMonth  | slánuimhir          | ceann ar bith nó ceann amháin         | Seasann sé don mhí féilire deiridh (luachanna 1-12) in eatramh ama. |
| PeriodEndDay    | slánuimhir          | ceann ar bith nó ceann amháin         | Seasann sé don lá deiridh den mhí (luachanna 1-31) in eatramh ama. |

#### `Accuracy`

Léiríonn an t-airí seo cruinneas an eolais ar an dáta ach foclóir caighdeánach de chuid [MODS](http://www.loc.gov/standards/mods/) (Scéimre um Chur Síos ar Oibiachtaí Meiteashonraí) maidir leis an gcáilitheoir dáta a úsáid.

| Luach           | Cur síos                  |
| :-------------- | :------------------------ |
| APPROX          | Garluach atá ann.         |
| INFER           | Meastachán atá ann.       |
| QUESTION        | Táthar in amhras faoin dáta.  |

### `locationAbroad`

| Ainm an airí    | Cineál              | Bunuimhreacht       | Cur síos               |
| :-------------- | :------------------ | :------------------ | :------------------------ |
| GeoNameID       | slánuimhir          | ceann amháin        | Aitheantóir uathúil an tsuímh i mbunachar sonraí [geonames.org](http://www.geonames.org). |
| NameEN          | teaghrán            | ceann amháin        | Ainm an tsuímh (i mBéarla). |
| NameGA          | teaghrán            | ceann amháin        | Ainm an tsuímh (i nGaeilge). |
| Coordinates     | [`coordinates`](#coordinates) | ceann amháin                 | Comhordanáidí geografacha an tsuímh. |
| Country         | [`country`](#country) | ceann amháin                 | An tír ina bhfuil an suíomh. |

### `locationIreland`

| Ainm an airí    | Cineál              | Bunuimhreacht                | Cur síos                  |
| :-------------- | :------------------ | :--------------------------- | :------------------------ |
| LogainmID       | slánuimhir          | ceann amháin                 | Aitheantóir uathúil an tsuímh i mbunachar sonraí [logainm.ie](https://www.logainm.ie). |
| NameEN          | teaghrán            | ceann amháin                 | Ainm an tsuímh (i mBéarla). |
| NameGA          | teaghrán            | ceann amháin                 | Ainm an tsuímh (i nGaeilge). |
| Coordinates     | [`coordinates`](#coordinates) | ceann amháin                 | Comhordanáidí geografacha an tsuímh. |
| Counties        | [`county`](#county) | ceann amháin nó go leor         | An contae, nó na contaetha, ina bhfuil an suíomh. |

### `transcript`

Tras-scríbhinn d’ábhar ar leathanach lámhscríbhinne a chuir baill den tionscadal tras-scríofa pobail [Meitheal Dúchas.ie](https://www.duchas.ie/ga/meitheal/) ar fáil. Cuirtear an t-ábhar tras-scríofa ar fáil faoi réir cheadúnas [CC-BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).

| Ainm an airí    | Cineál              | Bunuimhreacht                         | Cur síos                  |
| :-------------- | :------------------ | :------------------------------------ | :------------------------ |
| ID              | slánuimhir          | ceann amháin                          | Aitheantóir uathúil na tras-scríbhinne. |
| DateCreated     | am-dháta ISO 8601   | ceann amháin                          | An dáta agus an t-am a cruthaíodh an tras-scríbhinn.  |
| DateModified    | am-dháta ISO 8601   | ceann ar bith nó ceann amháin         | Dáta agus am an mhionathraithe is déanaí a rinneadh ar an tras-scríbhinn.  |
| ItemID          | slánuimhir          | ceann amháin                          | Aithníonn sé `item` na lámhscríbhinne a tras-scríobhadh. |
| Approved        | Boole               | ceann amháin                          | Léiríonn sé ar faomhadh an tras-scríbhinn le haghaidh foilsiú nó nár faomhadh. Ní fhaomhtar tras-scríbhinní ó bhaill shóisearacha de Mheitheal Dúchas.ie go ndéanann ball d’fhoireann eagarthóireachta Dúchas athbhreithniú orthu. **(Faoi phribhléid)** |
| Moderated       | Boole               | ceann amháin                          | Léiríonn sé an ndearna ball d'fhoireann eagarthóireachta Dúchas athbhreithniú ar an tras-scríbhinn nó nach ndearna. **(Faoi phribhléid)** |
| Text            | teaghrán            | ceann amháin                          | Téacs na tras-scríbhinne. |
| Transcribers    | [`transcriber`](#transcriber) | ceann ar bith nó ceann amháin nó go leor | Meiteashonraí a bhaineann le hoibrithe deonacha a chuir leis an tras-scríbhinn. Bíonn an luach seo folamh má rinne rannpháirtithe anaithnide an tras-scríbhinn. |

### `transcriber`

| Ainm an airí    | Cineál              | Bunuimhreacht                         | Cur síos               |
| :-------------- | :------------------ | :------------------------------------ | :------------------------ |
| ID              | slánuimhir          | ceann amháin                          | Aitheantóir uathúil an tras-scríobhaí. |
| Name            | teaghrán            | ceann ar bith nó ceann amháin         | Ainm an tras-scríobhaí. Má scrios an tras-scríobhaí a chuntas ina dhiaidh sin, tá an luach seo ar neamhní. |

## Luachanna coiteanna

Baineann roinnt airíonna a bhfuil luachanna caighdeánaithe orthu le bailiúcháin éagsúla. Déantar cur síos orthu thíos.

### `status`

Sonraíonn sé stádas eagarthóireachta na hiontrála. Ní mheastar go bhfuil ach luach stádais de **4** réidh le foilsiú.

| Luach           | Cur síos                  |
| :-------------- | :------------------------ |
| 0               | Ionghabhadh an iontráil le déanaí. |
| 1               | Cuireadh an chéad scagadh eagarthóireachta i gcrích. |
| 2               | Cuireadh an chéad seiceáil eagarthóireachta i gcrích. |
| 3               | Cuireadh an dara scagadh eagarthóireachta i gcrích. |
| 4               | Cuireadh an dara seiceáil eagarthóireachta i gcrích. |

### `extraInfoStatus`

Sonraíonn sé stádas foilsithe an réimse `extraInfo`.

| Luach           | Cur síos                  |
| :-------------- | :------------------------ |
| EDIT            | Níl an réimse `extraInfo`, má tá sé ann, oiriúnach le foilsiú. |
| PUB             | Tá an réimse `extraInfo`, má tá sé ann, oiriúnach le foilsiú. |
