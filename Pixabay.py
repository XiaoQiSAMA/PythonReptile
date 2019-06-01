import os
import requests
import re
import time
from PIL import Image
from bs4 import BeautifulSoup


def search(url, keyword):
    req = requests.post(url, f'{keyword}/')
    if req.status_code == 200:
        return req.text
    else:
        print("Error")

def page_change(url, page):
    #?pagi=_  为页数后缀
    if page == 0:
        pass
    else:
        for i in page:
            url += f'?pagi={i}'

def Download_keyword(url_text, img_name):
    #通过bf4库对提取网页中图片的名字
    bf4 = BeautifulSoup(url_text, 'lxml')
    target = str(bf4.find_all('img'))
    pattern = re.compile(r'[a-z]{3,7}-\d{7}')
    #str_target = "".join(target)
    img_name += pattern.findall(target)
    return img_name

def download_picture(img_name, fd):
    r = search(url,keyword = input("搜索关键字:"))
    img_list = Download_keyword(r, img_name)
    Download_list = list(set(img_list))
    if os.path.exists(fd) == False:
        os.makedirs(fd)
    for i in Download_list:
        images_url = f'pixabay.com/images/download/{i}.jpg?attachment'
        with open("i", 'wb' ) as f:
            f.write(images_url)
        time.sleep(1)

if __name__ == '__main__':  
    url = 'https://pixabay.com/images/search/'
    img_name = []
    download_picture(img_name, "images")
    




