# -*- conding: utf-8 -*-
import json
import requests
"""批量爬取百度图片，获得url后，可以通过迅雷等下载工具批量下载"""


REQUEST_URL = 'http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew'
KEY_WORD = '人脸',
FILE = 'img_url.txt'
START_NUM = 1
END_NUM = 10


def start_get_img(key_word, pn):
    args = {'word': key_word, 'pn': pn}
    r = requests.get(REQUEST_URL, args)

    data = json.loads(r.text)
    imgs = data.get('imgs', [])

    urls = [img.get('objURL', '')+'\n' for img in imgs]
    return urls


if __name__ == '__main__':

    with open(FILE, 'w+') as f:
        pn = START_NUM
        print('Starting...')
        while START_NUM <= END_NUM:
            urls = start_get_img(KEY_WORD, pn)
            f.writelines(urls)
            pn += 30
            print(str(START_NUM) + '/' + str(END_NUM))
            START_NUM += 1

    print('End!')
