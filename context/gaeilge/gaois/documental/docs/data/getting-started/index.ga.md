---
title: Buntreoir maidir le hacmhainní sonraí oscailte Gaois a úsáid
shortTitle: Buntreoir
description: Eolas a theastaíonn sula mbaintear leas as acmhainní sonraí oscailte Gaois
keywords: Gaois, API, fíordheimhniú, téarmaí, Fiontar & Scoil na Gaeilge, DCU
public: true
---

Tá [grúpa taighde Gaois](https://www.gaois.ie) in [Fiontar & Scoil na Gaeilge](https://www.dcu.ie/fiontar_scoilnagaeilge/), DCU, i gcomhar lenár bpáirtnéirí tionscadail, ag cur roinnt acmhainní sonraí oscailte ar fáil don phobal. Áirítear leo Comhéadain Feidhmchláir (API) a bhaineann leas as cur chuige REST agus déantáin eile sonraí. Eisítear gach ceann de na hacmhainní seo faoi choinníollacha sonracha ceadúnaithe: léigh an t-eolas cuí ceadúnaithe, atá ar fáil ar an suíomh gréasáin seo sna doiciméid a ghabhann le gach acmhainn, sula mbaineann tú úsáid as na sonraí.  

Tá [API Logainm](/en/data/logainm/v1.0/api) ar fáil go poiblí anois agus tugann sé seo rochtain chláir ar Bhunachar Logainmneacha na hÉireann. Tá cuid mhór den obair chun API eile a bhaineann le tionscadal [Dúchas](/en/data/duchas/v0.5/api) a fhorbairt i gcrích faoi seo agus tá leagan réamheisiúna ar fáil anois. Táthar ag súil go gcuirfear tuilleadh acmhainní ar fáil amach anseo.

Baineann patrúin choiteanna maidir le húsáid, fíordheimhniú, leaganú agus cosaint sonraí le comhéadain feidhmchláir Gaois. Déantar cur síos sa chuid eile den doiciméad seo ar na patrúin seo agus ba cheart iad a léamh sula leantar ar aghaidh go dtí na doiciméid ar leith a bhaineann le gach acmhainn.  

## Forléargas ar API

Tugann Comhéadain Feidhmchláir Gaois rochtain ar roinnt acmhainní trí scéimre URL sainithe. Faightear rochtain ar acmhainní ar leith trí chosáin uathúla atá iarcheangailte leis an óstainm. I gcásanna áirithe, d'fhéadfaí na hacmhainní a thagann ar ais a scagadh ach paraiméadair roghnacha iarratais a úsáid. Má éiríonn leis an iarratas, cuirtear acmhainní ar ais i bhfoirm JSON. Mura n-éiríonn leis an iarratas rochtain a fháil ar acmhainn, gheofar, ar a laghad, cód stádais HTTP mar fhreagra ar an iarratas. Seo a leanas sampla d'iarratas bailí API:  

> `https://www.logainm.ie/api/v1.0/1375542`

Ní mór d'úsáideoirí nó d'fheidhmchláir (cliaint) a iarrann acmhainn trí API a n-aitheantas a fhíordheimhniú. Déantar é seo ach Eochair API a thabhairt le gach iarratas. Ní mór do gach cliant Eochair uathúil API a fháil sula n-idirghníomhaíonn sé/sí leis an gcomhéadan. Teastaíonn fíordheimhniú chun mí-úsáid seirbhíse a chosc agus chun staitisticí ginearálta úsáide a rianú. Tá tuilleadh eolais thíos.

Tá [Comhroinnt Sócmhainní Tras-Fhoinse](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (CORS) cumasaithe i dtaca leis na comhéadain feidhmchláir de chuid Gaois a chuireann sonraí oscailte ar fáil. Fágann sé seo gur féidir na sonraí a úsáid i bhfeidhmchláir ar thaobh an chliaint agus ar bhrabhsálaithe móibíleacha.

## Leaganú API

Éascaítear leaganacha éagsúla API le haghaidh gach API REST. Is ionann seo agus a rá gur féidir rochtain a fháil ar níos mó ná leagan amháin de gach API ag an am céanna. D'fhéadfadh leaganacha nua API acmhainní nó feidhmiúlachtaí breise a chur ar fáil ach seans go dteastódh comhréir dhifriúil iarratais uathu i gcomparáid le leaganacha níos sine. Léiríonn an dara paraiméadar cosáin in URL an iarratais an spriocleagan API:  

> /api/**v1.0**/glossary

Tacófar le leaganacha níos sine ar mhaithe le héascaíocht an fhorbróra: gan leaganú, d'fhéadfadh feidhmchláir spleácha de chuid cliant cliseadh de bharr athruithe ar chomhréir API. Déanfaimid ár ndícheall acmhainní nua a chur leis an suíomh de réir a chéile agus ní chuirfimid athruithe briste i bhfeidhm ach amháin mura bhfuil aon rogha eile ann. Déantar leaganacha API trí [Leaganú Séimeantach 2.0.0](https://semver.org/spec/v2.0.0.html) (semver) a úsáid agus leantar sonraíocht semver. Ar mhaithe le gontacht, áfach, ní léirítear ach pointí mórleaganacha agus mionleaganacha in aimsitheoirí aonfhoirmeacha acmhainne a bhaineann le hiarratais.

Tar éis tamaill, seans go gcinnfear fáil réidh le seanleaganacha API ar chúiseanna cothabhála nó feidhmíochta. Nuair a chláraíonn tú le haghaidh cuntas forbróra de chuid Gaois (féach thíos), cuirfear ceist ort maidir le cumarsáid a fháil ó ghrúpa taighde Gaois ó am go ham. Ach glacadh le cumarsáid a fháil, cuirfear ar an eolas go luath thú maidir le hathruithe dá leithéid.

**Tabhair faoi deara:** Ar mhaithe le tástáil amháin atá leaganacha réamheisiúna API (i.e. < v1.0) agus ní dhéanfar cothabháil orthu tar éis do leagan 1.0 a bheith eisithe.

## Fíordheimhniú API 

Ní mór do chliaint a bhfuil acmhainn á hiarraidh acu tríd an API a n-aitheantas a fhíorhdeimhniú. Déantar é seo ach Eochair API a chur ar aghaidh chuig an tseirbhís le gach iarratas. Tugann fíordheimhniú cosaint éigin don soláthraí seirbhíse ar mhí-úsáid a bhaintear as API a bhfuil rólódáil iarratais i gceist léi. Ligeann sé seo dúinn roinnt staitisticí úsáide a choinneáil freisin ar mhaithe le monatóireacht feidhmíochta agus feabhsú seirbhíse. Is féidir tuilleadh a fhoghlaim faoi na sonraí a choinnímid sna míreanna seo a leanas.  

### Conas Eochair API a fháil 

Téigh chuig 'Mol na bhForbróirí' ar [gaois.ie](https://www.gaois.ie/ga/technology/developers/). Logáil isteach nó cláraigh chun cuntas a chruthú agus beidh tú in ann Eochair API a ghiniúint.

### Conas d'Eochair API a chur ar aghaidh 

Is féidir d'Eochair API a chur ar aghaidh chuig an tseirbhís ar bhealaí éagsúla. Roghnaigh an modh is fusa duitse.  

#### Ceanntásc HTTP 

Cuir an Eochair API i gceanntásc `X-Api-Key`: 

> `'X-Api-Key: <API_KEY_HERE>' 'https://www.logainm.ie/api/v1.0/1384618'`

#### Paraiméadar iarratais GET

Cuir an Eochair API i bparaiméadar `apiKey` um theaghrán iarratais GET: 

> `'https://www.logainm.ie/api/v1.0/1384618?apiKey=API_KEY_HERE'`

**Tabhair faoi deara:** Is féidir an paraiméadar iarratais GET seo a úsáid le haghaidh iarratas nach mbaineann le GET (POST agus PUT san áireamh).

#### Fíordheimhniú Bunúsach HTTP

Mar rogha eile, cuir an Eochair API ar aghaidh mar ainm úsáideora (agus pasfhocal folamh leis) ach fíordheimhniú bunúsach HTTP a úsáid:  

> `'https://API_KEY_HERE@www.logainm.ie/api/v1.0/1384618'`

## Slándáil

Freastalaítear an API le prótacal HTTPS. Cé go n-atreoraítear iarratais HTTP a chuirtear chuig an tseirbhís go dtí HTTPS go huathoibríoch, níor cheart duit idirghníomhú leis an API ach amháin má bhaineann tú úsáid as aimsitheoirí aonfhoirmeacha acmhainne a bhfuil an réimír HTTPS leo.  

Cé go gcuireann HTTPS leibhéal suntasach slándála ar fáil, chuirfimis béim ar an gcaoi nach ionann na modhanna bunúsacha fíordheimhnithe a luadh thuas agus criptiú ó cheann ceann. **Ba cheart duit Eochair API amháin a chur ar aghaidh chuig an tseirbhís** — ná cuir sonraí íogaire, go háirithe pasfhocail, sna hiarratais riamh.  

## Cóid stádais HTTP

Cuirfear an stádas a bhaineann le gach iarratas API in iúl ar an gcéad dul síos trí chóid chaighdeánacha stádais HTTP. Molaimid go láimhseálann aon fheidhmchlár a idirghníomhaíonn lenár gcomhéadain feidhmchláir na cóid stádais seo a leanas:

| Cód   | Sainmhíniú                        | Tuilleadh eolais    |
| :---- | :-------------------------------- | :------------------ |
| 200   | OK                                | Cuirfear oibiacht JSON amháin nó níos mó ar ais. |
| 400   | DROCHIARRATAS                     | Bhí comhréir an iarratais neamhbhailí — b'fhéidir go gcuirfí oibiacht JSON a dhéanann cur síos ar an earráid ar ais. |
| 401   | NEAMHÚDARAITHE                    | Níor cuireadh Eochair bhailí API ar fáil. |
| 404   | NÍ bhFUARTHAS                     | Níl an acmhainn ann. |
| 500   | EARRAID INMHEÁNACH SA FHREASTALAÍ | Déan teagmháil linn ag [gaois@dcu.ie](mailto:gaois@dcu.ie) agus an cosán iarratais á lua agat. |

## Coinneáil sonraí agus cosaint sonraí 

Stórálaimid na sonraí seo a leanas gach uair a dhéantar iarratas le ceann dár gcomhéadain feidhmchláir:  

1. Cosán iarratais
2. Cód freagartha stádais
3. Áireamh torthaí
4. Aga freagartha an iarratais
5. Aitheantas an chliaint (a fhaightear ach tagairt a dhéanamh don Eochair API a chuirtear ar fáil)  

Nascann aitheantas an chliaint d'iarratas leis na sonraí a stóráil tú i 'Mol Forbróra Gaois' (na sonraí a chuir tú ar fáil nuair a chláraigh tú don tseirbhís, mar shampla). Is féidir leat breathnú ar na sonraí thuas am ar bith i 'Mol Forbróra Gaois'. Stórálann grúpa taighde Gaois, Fiontar & Scoil na Gaeilge, DCU na sonraí seo ar bhealach a chomhlíonann RGCS.

Coimeádaimid an ceart againn féin méadracht chomhiomlán nó anaithnid a bhaineann le hiarratas API a thuairisciú agus/nó a fhoilsiú. Ní thuairisceoimid, ní fhoilseoimid ná ní roinnfimid sonraí ar leith ó chliant (i.e. aitheantas an chliaint nó sonraí eile aitheantais dá c(h)uid) le tríú páirtí ar bith. Coimeádaimid an ceart againn féin míreanna sonraí 1-4, a liostaíodh thuas, a choinneáil go deo ar mhaithe le monatóireacht feidhmíochta, taighde agus feabhsuithe seirbhíse.   

Tá tú i dteideal do chuid sonraí pearsanta a bhaint dár gcórais am ar bith. Scriosfar d'ainm, pasfhocal, seoladh ríomhphoist, cleamhnacht eagraíochtúil agus an ceangal le hiarratais stóráilte, go hiomlán agus go buan. Is féidir do chuntas forbóra, agus na sonraí pearsanta uile a mbaineann leis, a scriosadh ar ['Mol na bhForbóirí'](https://www.gaois.ie/ga/technology/developers/) ar shuíomh Gaois.

Ach rochtain a fháil ar cheann ar bith dár gcomhéadain feidhmchláir, aontaíonn tú go gcloífidh tú leis na polasaithe agus leis na cleachtais ar fad a luaitear sa doiciméad seo.  
