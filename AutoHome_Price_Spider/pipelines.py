# -*- coding: utf-8 -*-

import pymssql

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AutohomePriceSpiderPipeline(object):
    def __init__(self, server, user, password, database, host, into_sql, star_spider_name):
        self.server = server
        self.user = user
        self.password = password
        self.database = database
        self.host = host
        self.into_sql = into_sql
        self.star_spider_name = star_spider_name

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            server=crawler.settings.get('DATABASE_SERVER_NAME'),
            user=crawler.settings.get('DATABASE_USER_NAME'),
            password=crawler.settings.get('DATABASE_USER_PASSWORD'),
            database=crawler.settings.get('DATABASE_NAME'),
            host=crawler.settings.get('DATABASE_HOST'),
            into_sql=crawler.settings.get('INTO_SQL'),
            star_spider_name=crawler.settings.get('STAR_SPIDER_NAME')
        )

    def open_spider(self, spider):
        self.conn = pymssql.connect(user=self.user, password=self.password, host=self.host, database=self.database)

    def process_item(self, item, spider):
        if self.into_sql == 1:
            if self.star_spider_name == 'Price_Spider':
                self.price_spider_into(item, spider)
        return item

    def price_spider_into(self, item, spider):
            cur = self.conn.cursor()
            self.conn.autocommit(True)
            appversion=item['appversion']
            spec_id=item['spec_id']
            mileage=item['mileage']
            reg_date=item['reg_date']
            # price=item['price']
            grade=item['grade']
            q0=item['q0']
            q1=item['q1']
            q2=item['q2']
            q3=item['q3']
            q4=item['q4']


            cur.execute("""INSERT INTO [BDCI_AUTOHOME_new].[src].[AutoHome_Price]
                            (appversion, spec_id, mileage, reg_date, grade, q0, q1, q2, q3, q4)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                        , (appversion, spec_id, mileage, reg_date, grade, q0, q1, q2, q3, q4))

            self.conn.autocommit(False)
            self.conn.commit()
