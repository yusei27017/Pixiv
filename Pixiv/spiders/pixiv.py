# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
import urllib.request
import ssl
import json
import re

class PixivSpider(scrapy.Spider):
    name = 'pixiv'
    allowed_domains = ['pixiv.com']

    def start_requests(self):
        yield scrapy.Request(
            ##輸入作者 ID https://www.pixiv.net/ajax/user/作者id/profile/all?lang=zh_tw            
            url="https://www.pixiv.net/ajax/user/36000426/profile/all?lang=zh_tw",
            headers={"Content-Type" : "application/json"},
            ##請輸入保存的cookie     '40userID_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
            cookies={'PHPSESSID': 'userID_php_session_id'},
            callback = self.detail_requests
        )

    def detail_requests(self, response):
        yield SplashRequest(response.request.url,self.deep_request,meta={'url':response.request.url},
        endpoint='render.html',
        dont_filter=True)  

    def deep_request(self, response):
        my_json = response.body.decode('utf8').replace("'", '"')
        select_json = re.findall('pre-wrap;">(.*?)</pre>', my_json)[0]
        json_data = json.loads(select_json)
        print(json_data)
        
        #獲取作者作品 ID
        for key in json_data['body']['illusts']:
            url_origin = "https://www.pixiv.net/ajax/illust/" + key + "/pages?lang=zh_tw"
            print(url_origin)
            yield SplashRequest(url_origin,self.final_requset,meta={'url':url_origin},
            endpoint='render.html',
            dont_filter=True)

    def final_requset(self, response):
        print(response.url)
        jpg_id = re.findall('/illust/(.*?)/pages', response.url)
        print(jpg_id)
        myJson = response.body.decode('utf8').replace("'", '"')
        selectJson = re.findall('pre-wrap;">(.*?)</pre>', myJson)[0]

        jsonData = json.loads(selectJson)
        count = 0
        for url in jsonData['body']:
            count += 1
            urls = url['urls']['original']
            
            ssl._create_default_https_context = ssl._create_unverified_context
            header = "https://www.pixiv.net/artworks/" + jpg_id[0]
            opener = urllib.request.build_opener()
            opener.addheaders=[("Referer", header)]
            urllib.request.install_opener(opener)
            ## 保存圖片之路徑
            jpgName = "/Users/lintengzhu/Desktop/gitPush/Pixiv/Pixiv/imgs/" + jpg_id[0] + str(count) + ".jpg"
            print(jpgName)
            urllib.request.urlretrieve(urls,jpgName)

