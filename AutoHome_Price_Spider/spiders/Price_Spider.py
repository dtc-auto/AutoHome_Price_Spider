# -*- coding: utf-8 -*-
import scrapy
import re
import json
import pandas as pd
from AutoHome_Price_Spider.items import ChexunSpiderPriceItem

global key_id,key_
key_id = 0
class UrlSpiderSpider(scrapy.Spider):

    # global spec_name,miles,ym,spec_price
    MILES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    YEAR = [2012, 2013, 2014, 2015, 2016, 2017]
    MONTH = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    BASE_URL = 'https://pinguapi.che168.com/v1/auto/assessquartercondition.ashx?_appid=pc.pingu&'
    PID_CID = '&pid=110000&cid=110100'
    APP_CALLBACK = '&_appversion=2.04v,2.03v,2.09v&callback=pinggutrend'
    DF = pd.DataFrame()
    list_strat_url = []

    # test
    # spec_name = '测试data_1'
    # miles = '10000'
    # ym = '2012-1'
    # spec_price = '55.03'
    # start_urls = ["https://pinguapi.che168.com/v1/auto/assessquartercondition.ashx?_appid=pc.pingu&&firstregtime=2012-1&pid=110000&cid=110100&mileage=10000&specId=999&_appversion=2.04v,2.03v,2.09v&callback=pinggutrend","https://pinguapi.che168.com/v1/auto/assessquartercondition.ashx?_appid=pc.pingu&&firstregtime=2012-1&pid=110000&cid=110100&mileage=10000&specId=326&_appversion=2.04v,2.03v,2.09v&callback=pinggutrend"]



    data = pd.read_csv('specs.csv', names=['id', 'name', 'brand', 'serie', 'price'], encoding='gbk')
    for item in data.itertuples():
        spec_id = str(item[1])
        spec_price = item[5]
        spec_name = str(item[3]) + ' ' + str(item[4]) + ' ' + str(item[2])

        for mileage in MILES:
            miles = str(mileage * 10000)
            for year in YEAR:
                y = str(year)
                for month in MONTH:
                    try:
                        ym = y + '-' + str(month)
                        url = BASE_URL + '&firstregtime=' + ym + PID_CID + '&mileage=' + miles + '&specId=' + spec_id + APP_CALLBACK

                        list_strat_url.append(url)
                    except Exception as e:
                        print(e)
        print(url)

    start_urls = list_strat_url
    name = "Price_Spider"


    def parse(self, response):
        url = response.url
        key_item = url.split('=')
        ym = key_item[2][:-4]
        spec_id = key_item[6][:-12]
        # if spec_id != key_id:
        #     print(spec_id)
        # key_id = spec_id
        miles = key_item[5][:-7]
        # print(spec_id)
        item = ChexunSpiderPriceItem()
        response = str(response.body.decode('GB2312'))
        response = re.search('pinggutrend\((.*)\)', response)[1]
        data = json.loads(response, encoding='GB2312')
        # write information into pip
        results = data['result']
        for result in results:
            for detail in result['conditon']:
                row = detail
                item['appversion'] = result['appversion']
                item['spec_id'] = spec_id
                item['mileage'] = miles
                item['reg_date'] = ym
                # item['price'] = spec_price
                item['grade'] = row['grade']
                item['q0'] = row['q0']
                item['q1'] = row['q1']
                item['q2'] = row['q2']
                item['q3'] = row['q3']
                item['q4'] = row['q4']
                yield item