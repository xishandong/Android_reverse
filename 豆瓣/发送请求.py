import base64
import hashlib
import hmac
import time
from urllib.parse import urlparse, quote

import requests


def sha1_base64(url, method):
    path = urlparse(url).path
    encoded_path = quote(path, safe='')
    timestamp = str(int(time.time()))
    key = b'bf7dddc7c9cfe6f7'
    message = '&'.join([method, encoded_path, timestamp])
    hmac_sha1 = hmac.new(key, message.encode('utf-8'), hashlib.sha1)
    hashed_data = hmac_sha1.digest()
    return base64.b64encode(hashed_data).decode('utf-8'), timestamp


headers = {
    "User-Agent": "Rexxar-Core/0.1.3 api-client/1 com.douban.frodo/7.18.0(230) Android/28 product/beyond1qlteue vendor/samsung model/SM-G977N brand/samsung  rom/android  network/wifi  udid/81c09b13e49151d13ed4d8d3817b99c45cf0d399  platform/mobile nd/1 com.douban.frodo/7.18.0(230) Rexxar/1.2.151  platform/mobile 1.2.151",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}

url = "https://frodo.douban.com/api/v2/movie/hot_gaia"
sig_ts = sha1_base64(url, 'GET')
params = {
    "area": "全部",
    "sort": "time",
    "playable": "0",
    "loc_id": "0",
    "start": "0",
    "count": "20",
    "udid": "81c09b13e49151d13ed4d8d3817b99c45cf0d399",  # 和请求头的一致
    "rom": "android",
    "apikey": "", # 需填写你的key，暂时没分析出生成逻辑
    "s": "rexxar_new",
    "channel": "Yingyongbao_Market",
    "timezone": "Asia/Shanghai",  # 时区
    "device_id": "",  # 设备id
    "os_rom": "android",
    "apple": "",  # 暂未分析，多次固定不变
    "sugar": "46007",
    "_sig": sig_ts[0],
    "_ts": sig_ts[1]
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)

