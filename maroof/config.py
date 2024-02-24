BASE_URL: str = "https://api.thiqah.sa/maroof/public/api/app/business"

HEADERS: dict = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ar",
    "Connection": "keep-alive",
    "Content-type": "Application/json",
    "Host": "api.thiqah.sa",
    "Origin": "https://maroof.sa",
    "Referer": "https://maroof.sa/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "Sec-GPC": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "apiKey": "c1qesecmag8GSbxTHGRjfnMFBzAH7UAN",
    "sec-ch-ua": '"Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
}

PARAMS: dict = {
    "keyword": "",
    "businessTypeId": "",
    "businessTypeSubCategoryId": "",
    "regionId": "",
    "cityId": "",
    "certificationType": "",
    "sortBy": "2",
    "sortDirection": "2",
    "sorting": "",
    "maxResultCount": "40",
}