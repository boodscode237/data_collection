import requests
import json

cookies = {
    "_gcl_au": "1.1.566277818.1699705805",
    "cachedPage": "true",
    "_sp_ses.8ab7": "*",
    "initialGeoConfirmationShow": "1",
    "_wss": "654f73d7",
    "_ws": "654f73c90009bc300a0a01956af8a1b1558f90db03654f73d775fa2f096070f4c9a86e532c94792cffa2ddcf71",
    "latestSearchValue": "",
    "_sp_id.8ab7": "a2eba57a-c586-4639-8808-69f04e54250d.1699705808.1.1699705831.1699705808.0c284f34-26e3-407f-9701-d9dcc89caf13",
}

headers = {
    "authority": "russia.superjob.ru",
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    # 'cookie': '_gcl_au=1.1.566277818.1699705805; cachedPage=true; _sp_ses.8ab7=*; initialGeoConfirmationShow=1; _wss=654f73d7; _ws=654f73c90009bc300a0a01956af8a1b1558f90db03654f73d775fa2f096070f4c9a86e532c94792cffa2ddcf71; latestSearchValue=; _sp_id.8ab7=a2eba57a-c586-4639-8808-69f04e54250d.1699705808.1.1699705831.1699705808.0c284f34-26e3-407f-9701-d9dcc89caf13',
    "dnt": "1",
    "referer": "https://russia.superjob.ru/vacancy/search/",
    "sec-ch-ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Opera GX";v="102"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0",
    "x-frontend-project": "desktop",
    "x-page-type": "search-vacancy",
    "x-real-ip": "85.143.144.219",
    "x-requested-with": "XMLHttpRequest",
    "x-requests-group-id": "ce21139b7c08c1c3cb75dbabe7c811fa",
    "x-subdomain": "russia",
}

params = {
    "page[limit]": "40",
    "page[offset]": "0",
    "include": "mainInfo.salary,mainInfo.salary.salaryPeriod,detailInfo,detailInfo.workType,detailInfo.externalResponse,vacancyMetroStations.station,vacancyMetroStations.station.lines,vacancyMetroStations.timeToMetro,town.geo,company.countOfEmployee,company.reviewScore,company.logo,company.groups,companyInfo,companyLink,favoriteVacancy,resumeInteractions.status,resumeInteractions.resume,resumeInteractions.vacancyResponse,resumeInteractions.vacancyResponse.chat,contactInfo,searchHighlights,searchSnippet,searchSnippet.searchSnippetSections.searchHighlight,searchSnippet.searchSnippetSections.vacancySearchSnippetSectionType,requiredExperience,hrInfo.campaigns.campaignType,hrInfo.campaigns.campaignStatus,brandingSnippet.images.image.file.attachInfo,beFirstLabel,vacancyOfTheDay,vacancyTags,searchDiscardedKeywords,watch,trudVsem,trudVsem.state,trudVsem.action,survey.questions,survey.questions.answers,userSurveyAnswer.answers,chatAvailable,viewCount,video,inAnotherCityLabel,vacancyAdditionalFlags,clusterCounter,clusterCounter",
    "filters[allowNeighbourTownSupplement]": "1",
    "filters[forceRemoteWork]": "1",
    "filters[allowSimilarPaymentSupplement]": "1",
    "filters[adaptableKeywords]": "1",
    "filters[country]": "1",
    "filters[domain]": "1462",
    "fields[vacancyMainInfo]": "profession,updatedAt",
    "fields[complaint]": "",
    "fields[vacancyStatusesInfo]": "isArchive",
    "fields[vacancyTagType]": "key,label",
    "fields[address]": "cityName",
    "fields[vacancyDetailInfo]": "isResumeRequired,isRemoteWork,isCallCatching,isBeneficial",
    "fields[company]": "title",
    "fields[reviewScore]": "generalScore",
    "fields[vacancyCompanyInfo]": "name,isAnonymous",
    "fields[town]": "name",
}

response = requests.get(
    "https://russia.superjob.ru/jsapi3/0.1/vacancy/",
    params=params,
    cookies=cookies,
    headers=headers,
)

print(json.loads(response.text))
