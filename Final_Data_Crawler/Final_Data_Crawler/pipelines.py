# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

client = MongoClient()

#1-5
collection1  = client["houseInfo"]["line_1"]
collection2  = client["houseInfo"]["line_2"]
collection3  = client["houseInfo"]["line_4"]
collection4  = client["houseInfo"]["line_5"]
collection5  = client["houseInfo"]["line_6"]

#6-10
collection6  = client["houseInfo"]["line_7"]
collection7  = client["houseInfo"]["line_8_n"]
collection8  = client["houseInfo"]["line_8_s"]
collection9  = client["houseInfo"]["line_9"]
collection10 = client["houseInfo"]["line_10"]

#11-15
collection11 = client["houseInfo"]["line_13"]
collection12 = client["houseInfo"]["line_14_e"]
collection13 = client["houseInfo"]["line_14_w"]
collection14 = client["houseInfo"]["line_15"]
collection15 = client["houseInfo"]["line_16"]

#16-20
collection16 = client["houseInfo"]["line_batong"]
collection17 = client["houseInfo"]["line_changping"]
collection18 = client["houseInfo"]["line_daxingjichang"]
collection19 = client["houseInfo"]["line_fangshan"]
collection20 = client["houseInfo"]["line_jichang"]

#21-24
collection21 = client["houseInfo"]["line_s1"]
collection22 = client["houseInfo"]["line_xijiao"]
collection23 = client["houseInfo"]["line_yanfang"]
collection24 = client["houseInfo"]["line_yizhuang"]





class FinalDataCrawlerPipeline:
    def process_item(self, item, spider):
        #1-5
        if spider.name == 'crawler_line_1':
            collection1.insert(item)
        elif spider.name == 'crawler_line_2':
            collection2.insert(item)
        elif spider.name == 'crawler_line_4':
            collection3.insert(item)
        elif spider.name == 'crawler_line_5':
            collection4.insert(item)
        elif spider.name == 'crawler_line_6':
            collection5.insert(item)
        
        #6-10
        elif spider.name == 'crawler_line_7':
            collection6.insert(item)
        elif spider.name == 'crawler_line_8_n':
            collection7.insert(item)
        elif spider.name == 'crawler_line_8_s':
            collection8.insert(item)
        elif spider.name == 'crawler_line_9':
            collection9.insert(item)
        elif spider.name == 'crawler_line_10':
            collection10.insert(item)
        
        #11-15
        elif spider.name == 'crawler_line_13':
            collection11.insert(item)
        elif spider.name == 'crawler_line_14_e':
            collection12.insert(item)
        elif spider.name == 'crawler_line_14_w':
            collection13.insert(item)
        elif spider.name == 'crawler_line_15':
            collection14.insert(item)
        elif spider.name == 'crawler_line_16':
            collection15.insert(item)
        
        #16-20
        elif spider.name == 'crawler_line_batong':
            collection16.insert(item)
        elif spider.name == 'crawler_line_changping':
            collection17.insert(item)   
        elif spider.name == 'crawler_line_daxingjichang':
            collection18.insert(item)
        elif spider.name == 'crawler_line_fangshan':
            collection19.insert(item)
        elif spider.name == 'crawler_line_jichang':
            collection20.insert(item)

        #21-24
        elif spider.name == 'crawler_line_s1':
            collection21.insert(item)
        elif spider.name == 'crawler_line_xijiao':
            collection22.insert(item)   
        elif spider.name == 'crawler_line_yanfang':
            collection23.insert(item)
        elif spider.name == 'crawler_line_yizhuang':
            collection24.insert(item)

        return item
