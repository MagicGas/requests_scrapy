#!/usr/bin/env python
# -*- conding:utf-8 -*-
import re
import requests
import os

def scapy():
    image_urls=[]
    for i in  range(1,4):
        url="http://www.yggk.net/xiaohua/xiaohua/list{}.html".format(i)
        ret = requests.get(url).text
        ret1 = re.findall('(http://www.yggk.net/xiaohua/uploads/allimg/.*\.jpg)',ret)
        image_urls.extend(ret1)
    return image_urls
def download(image_urls):
    for item in range(len(image_urls)):
        print(item)
        image = requests.get(image_urls[item]).content

        filename = os.path.join(os.path.dirname(__file__),'images/{}.jpg').format(item)
        with open(filename,'wb') as file:
            file.write(image)

def main():
    url = scapy()
    download(url)
if __name__=='__main__':
    main()

