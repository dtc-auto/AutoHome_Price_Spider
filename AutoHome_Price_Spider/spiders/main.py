# coding:utf-8
from scrapy import cmdline
import AutoHome_Price_Spider.settings
import datetime
def main():
    create_time = datetime.date.today()
    Spider_name = AutoHome_Price_Spider.settings.STAR_SPIDER_NAME
    log_name = Spider_name+str(create_time)
    star_spider = "scrapy crawl %s -s LOG_FILE=%s.log" %(Spider_name, log_name)

    cmdline.execute(star_spider.split())

if 1:    main()