# import traceback
from bs4 import BeautifulSoup
# import pymysql
import requests


def getHtmlCode(url):
    headers = {
        "Host": "www.cncn.org.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Referer": "http://www.cncn.org.cn/shequ315/",
    }
    r = requests.get(url, headers=headers)
    r.encoding = 'UTF-8'
    page = r.text
    return page;


def __parseHtml():
    file_write_obj = open("e:\\dest.txt", 'w');
    for num in range(1, 36):
        url = 'http://www.cncn.org.cn/shequ315/';
        if num > 1:
            url = url + "index_"+str(num)+".html"
        page = getHtmlCode(url)
        print(url)
        soup = BeautifulSoup(page, 'html.parser')
        for li in soup.select('#list_main2 li a'):
            print(li.text)
            file_write_obj.writelines(li.text)
            file_write_obj.write('\n')
    file_write_obj.close()


if __name__ == '__main__':
    __parseHtml()
