import base64
import time

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import hashlib


def get_newSign(search_dict: dict) -> tuple[str, str]:
    new_dict = {
        'uuid': '',
        'timestamp': str(int(time.time() * 1000)),
        'loginToken': '',
        'platform': 'android'
    }
    new_dict.update(search_dict)
    str_to_encode = ''.join(
        [f'{k}{v}' for k, v in sorted(new_dict.items(), key=lambda item: item[0])]
    )
    newSign = encrypt(str_to_encode)
    md5_hash = hashlib.md5()
    md5_hash.update(newSign.encode())
    return md5_hash.hexdigest(), new_dict['timestamp']


def encrypt(plaintext):
    cipher = AES.new("d245a0ba8d678a61".encode('utf-8'), AES.MODE_ECB)
    padded_plaintext = pad(plaintext.encode('utf-8'), AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    ciphertext = str(base64.encodebytes(ciphertext), 'utf-8').replace('\n', '')
    return ciphertext


if __name__ == '__main__':
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
    print(get_newSign(params))


