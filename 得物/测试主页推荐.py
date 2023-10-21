import requests
from newSign import get_newSign


headers = {
    "User-Agent": "duapp/5.28.0(android;9)",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "cookieToken": "",
    "webua": "Mozilla/5.0 (Linux; Android 9; SM-G977N Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36/duapp/5.28.0(android;9)",
    "duplatform": "android",
    "duv": "5.28.0",
    "duloginToken": "",
    "shumeiid": "",
    "X-Auth-Token": "",
}
cookies = {
    "HWWAFSESTIME": ""
}
url = "https://app.dewu.com/sns-rec/v1/recommend/all/feed"
params = {
    "lastId": "",
    "limit": "20",
    "deliveryProjectId": "0",
    "negativeFeedbackUids": "",
    "negativeFeedbackCids": "",
    "pushChannel": "",
    "pushContentId": "",
    "lastExposureCids": "",
    "abV518Autoplay": "0",
    "ab528feedsCardNewCommodity": "1",
    "deviceNetwork": "WIFI",
    "abVIcon": "2",
    "abCoverReverse": "0",
}
sign_time = get_newSign(params)
params['newSign'] = sign_time[0]
headers['timestamp'] = sign_time[1]
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.json())

