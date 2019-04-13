import requests

r = requests.get("http://www.baidu.com")
r.encoding = 'UTF-8'                        #更换编码
"""
print(r.status_code)                        #200表示成功
print(type(r))                              #返回类型
print(r.headers)                            #header属性信息
print(r.content)                            #二进制文件信息(图片)
print(r.encoding)                           #编码信息
print(r.text)                               #页面信息
print(r.apparent_encoding)                  #分析网页内容的编码
"""

#异常捕获
def getHtmlText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status() #如果状态不是200 引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(getHtmlText(url))
    