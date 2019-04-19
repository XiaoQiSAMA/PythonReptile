import requests
import re

def getHTMLText(url):
    try:
        kv = {'Cookie': 'thw=cn; cna=B34PFeox8ikCAd/wKlWCAyok; t=8ada0cc426b5a8535e3e0b5a2d98ea76; tg=0; enc=s3QPpA4yWs0JojK%2B9J0nP3DWrKdbz1VA3l9H1iUhRP4tOmWF9BlfD2D4pDCCM29QDMvye1%2Fpm9gfBoEO3I8pAw%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; tracknick=%5Cu5C0F%5Cu4E030811; lgc=%5Cu5C0F%5Cu4E030811; v=0; cookie2=160d27c5978a0c038fd2f98a43a8aa91; _tb_token_=1a31d73bf93e; unb=3351247170; sg=108; _l_g_=Ug%3D%3D; skt=b24d64473869d95b; cookie1=BxSiZ1GJgpzVhArIuxF2xbHZornh5sGBWeyK5PePsbU%3D; csg=4988f102; uc3=vt3=F8dByEfJo6SgheM4Uv8%3D&id2=UNN4B9v9TgN82w%3D%3D&nk2=sym0kU308x8%3D&lg2=UtASsssmOIJ0bQ%3D%3D; existShop=MTU1NTY1NDE2Nw%3D%3D; _cc_=VT5L2FSpdA%3D%3D; dnk=%5Cu5C0F%5Cu4E030811; _nk_=%5Cu5C0F%5Cu4E030811; cookie17=UNN4B9v9TgN82w%3D%3D; mt=ci=24_1&np=; whl=-1%260%260%261555654171896; l=bB_8YYKnvGIAloNpBOfwNuI8UF79CIOf1sPzw49GzICP_yCp5B2dWZ_6KhY9C3GNa6Ge-389RZ5UB0TbMyURg; uc1=cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie21=VT5L2FSpccLuJBreK%2BBd&cookie15=WqG3DMC9VAQiUQ%3D%3D&existShop=false&pas=0&cookie14=UoTZ4SPb6ghvCQ%3D%3D&cart_m=0&tag=8&lng=zh_CN; isg=BCMjHYKue7OHtDeKKrfjhUl9sm4NsLUvdKla41WAfwL5lEO23ehHqgFGimyaNA9S'}
        r = requests.get(url, timeout = 30, headers = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parserPage(ilt, html):
    try:
        plt = re.findall(r'"price":"[\d]*"', html)
        tlt = re.findall(r'"title":".*?"', html)
        for i in range(len(plt)):
            price = eval(tlt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        return ""

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count += 1
        print(tplt.format(count, g[0], g[1]))
    
def main():
    goods = "书包"
    depth = 3
    start_url = "https://s.taobao.com/search?q=" + goods
    infolist = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(i * 44)
            html = getHTMLText(url)
            parserPage(infolist, html)
        except:
            continue
    #print(html)
    printGoodsList(infolist)

main()




"""
https://s.taobao.com/search?q=fgo&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=4&p4ppushleft=1%2C48&ntoffset=4&s=0
https://s.taobao.com/search?q=fgo&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=4&p4ppushleft=1%2C48&s=44&ntoffset=4
https://s.taobao.com/search?q=fgo&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=1&p4ppushleft=1%2C48&ntoffset=1&s=88
"""