import scrapy
import requests
from lxml import etree

base_urls = 'http://www.biquge.com.tw/1_1999/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}
response = requests.get(base_urls,headers = headers)
html = etree.HTML(response.text)
if response.status_code == 200:
    print('111')
    ips = []
    charptersip = html.xpath('//div[@id="list"]//dd/a/@href')
    print(type(charptersip))
    if charptersip:
        for charptes in charptersip:
            #print(charptes)
            base = 'http://www.biquge.com.tw'
            ips.append(base + charptes)
print(ips)