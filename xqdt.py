# import traceback
from bs4 import BeautifulSoup
# import pymysql
import requests
import random

def getHtmlCode(url):
    headers = {
        "Host": "house.leju.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Referer": "http://house.leju.com/es137578/dongtai",
    }
    r = requests.get(url, headers=headers)
    r.encoding = 'UTF-8'
    page = r.text
    return page;


def __parseHtml():
    # file_write_obj = open("e:\\dest.txt", 'w');
    sql = "";
    for num in range(1, 46):
        url = 'http://house.leju.com/es137578/dongtai/'+str(num)+'/';
        page = getHtmlCode(url)
        soup = BeautifulSoup(page, 'html.parser')
        for li in soup.select('.ty_CpicM2 ul li'):
            # print(li.select(".pic a img"))
            # print(li.select(".pic a img")[0].attrs['src'])
            # print(li.select("a h3")[0].get_text())
            # print(li.select("p")[0].get_text())
            # print(li.select("span")[0].get_text())
            s=li.select("span")[0].get_text().split()
            sql+="INSERT INTO `xg_dt` (`avatar`,`title`, `content`, `view_num`, `status`,  `create_date`, `del_flag`,`source`) VALUES (%s, %s, %s,%s, 1, %s,0, %s);\n"% \
                 ("'"+li.select(".pic a img")[0].attrs['src']+"'", "'"+li.select("a h3")[0].get_text()+"'","'"+li.select("p")[0].get_text()+"'",random.randint(10,1000),"'"+"'"+s[1]+" "+s[2]+"'",s[0]+"'")
    print(sql)


if __name__ == '__main__':
    __parseHtml()
