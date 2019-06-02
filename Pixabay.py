import os
import re
import time
import requests
from bs4 import BeautifulSoup



def search(url, keyword):
    headers = {
				"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
                
            }   

    req = requests.get(url, f'{keyword}/', headers=headers, cookies=cookies)
    if req.status_code == 200:
        return req.text
    else:
        print("Error")

def cookie_to_dict(cookie):
    cookie_dict = {}
    items = cookie.split(';')
    for item in items:
        key = item.split('=')[0].replace(' ', '')
        value = item.split('=')[1]
        cookie_dict[key] = value
    return cookie_dict

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
    headers = {
			"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
		}
    r = search(url,keyword = input("搜索关键字:"))
    img_list = Download_keyword(r, img_name)
    Download_list = list(set(img_list))
    if os.path.exists(fd) == False:
        os.makedirs(fd)
    os.chdir(fd)
    for i in Download_list:
        count = 0
        images_url = f'http://pixabay.com/images/download/{i}.jpg?attachment'
        r = requests.get(images_url, headers=headers, cookies=cookies)
        with open(i, 'wb' ) as f:
            f.write(r.content)
            os.rename(i, i+".jpg")
        print(i + "下载完成")
        count += 1
        time.sleep(1)
        if os._exit:
            print(f'下载了{count}张图片')
    



if __name__ == '__main__':  
    cookie = '__cfduid=d476148e04aa58d08facc3a27073791be1554723437; _ga=GA1.2.1919911062.1554723437; is_human=1; csrftoken=hWaOybG4RRxZdMxdo1uMei79cklvDZsAApDC1NkZEx1QiuRd4tDgJXKSkkpdpOHs; agreements_seen=1; _gid=GA1.2.701785517.1559391386; sessionid=".eJxVjMsOwiAQRf-FtWkstjz8GTIOQ4p9YGBIF8Z_F7swur3nnvMUDipPrhbKboIyiavQ3odR9jdAYwapbNBwNh5tsGYMxhocMIBWUpwEU2FMaY7UvD3lmXxbf5LRN9DLXlolL_-o9WfaPvyR052Qu8pxKR3Wwmk9jl08rhus5FJ2tEJcvt7rDbFuQGU:1hX34G:LhQhff0TN5mRlm9nOf3_pYzik78"; client_width=1694; _gat_UA-20223345-1=1'
    cookies = cookie_to_dict(cookie)
    url = 'https://pixabay.com/images/search/'
    img_name = []
    try:
        download_picture(img_name, "images")
    except KeyboardInterrupt:
        print("已退出下载")