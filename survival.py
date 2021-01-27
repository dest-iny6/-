# coding=gbk
import requests
import xlrd
import os
import xlwt
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

wbook = xlwt.Workbook(encoding='utf-8',style_compression = 0)
wtable = wbook.add_sheet('sheet1',cell_overwrite_ok = True)


count = 0
count = int(count)
def get_title(url):

    global count
    try:

        # res = requests.get(url)
        proxies = {
            'http': 'http://127.0.0.1:8080'
        }
        headers = {

            'Connection' : 'Keep-Alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',

        }
        requests.packages.urllib3.disable_warnings()
        res = requests.get(url, headers=headers, timeout=5, verify=False)
        res.encoding = res.apparent_encoding

        # res.encoding = 'utf-8'  #
        soup = BeautifulSoup(res.text, 'lxml')
        wtable.write(count, 0, url)
        wtable.write(count, 1, res.status_code)
        if soup.title is not None:
            wtable.write(count, 2, soup.title.text)
        count = count + 1
        print(res.status_code)
        if soup.title is not None:
            print(soup.title.text)
    except RequestException:
        wtable.write(count, 0, url)
        wtable.write(count, 1, '访问超时')
        count = count + 1
        print( url+':'+'无法访问')
        return None

# get_title('https://')
def gobackcode(file):
    with open(file, 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')
            get_title(line)

if __name__ == '__main__':
    if os.path.exists('./done.xls'):
        os.remove('./done.xls')
    gobackcode('./url.txt')
    wbook.save(r'./done.xls')
