import re

import os
import requests
from bs4 import BeautifulSoup

# 对图片路径拼接
BASE_DIR = os.path.dirname(os.path.abspath(__name__))
PIC = os.path.join(BASE_DIR, 'pic')

HEADER = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko)"
                        " Chrome/55.0.2883.87 Safari/537.36"}


# 对html 文件DOM化
def get_page(url,):
    resp = requests.get(url,headers=HEADER)
    html = resp.content.decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    return soup


def main():
    soup = get_page('http://m.xxxiao.com/')
    pic_urls = soup.select('a[aria-label]')
    for url in pic_urls:
        girl_type_url = url.attrs['href']
        soup = get_page(girl_type_url)
        # 对DOM 对象筛选
        girl_children_urls = soup.select('a[class=local-link]')
        for girl_children_url in girl_children_urls:
            # 筛选
            girl_children_url = girl_children_url.attrs['href']
            # 对url筛选
            re_url = r'^http://m.xxxiao.com/+[0-9]*$'
            if re.match(re_url, girl_children_url):
                soup = get_page(girl_children_url)
                urls = soup.select('a[data-rel=rgg]')
                for url in urls:
                    url = url.attrs['data-src']
                    resp = requests.get(url,headers=HEADER)
                    # 对图片路径切片用已当做图片名称
                    filename = url[url.rfind('/') + 1:]
                    try:
                        #  对文件写入某个指定路径
                        with open(PIC + '\\' + filename, 'wb') as f1:
                            f1.write(resp.content)
                    except:
                        print('保存失败')
                    print('保存成功')


if __name__ == '__main__':
    main()
