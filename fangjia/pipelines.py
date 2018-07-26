# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.conf import settings
from scrapy import signals
import json
import codecs
class JsonWithEncodingCnblogsPipeline(object):
    def __init__(self):
        self.file = codecs.open('cnblogs.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()
		
class FangjiaPipeline(object):
    def process_item(self, item, spider):
        print(item)
        return item

class Fangjia_Pipeline(object):
	def process_item(self, item, spider):
		host=settings['MYSQL_HOSTS']
		user=settings['MYSQL_USER']
		psd=settings['MYSQL_PASSWORD']
		db=settings['MYSQL_DB']
		c=settings['CHARSET']
		port=settings['MYSQL_PORT']
		con=pymysql.connect(host=host,user=user,passwd=psd,db=db,charset=c,port=port)
		cue=con.cursor()
		print("mysql connect succes")
		try:
			cue.execute("insert into fangjia (FANGJIA_ADDRESS,FANGJIA_NAME,FANGJIA_PRICE,FANGJIA_URL) values(%s,%s,%s,%s)",[ item['FANGJIA_ADDRESS'],item['FANGJIA_NAME'],item['FANGJIA_PRICE'],item['FANGJIA_URL'] ])
			print("insert success")#测试语句
		except Exception as e:
			print('Insert error:',e)
			con.rollback()
		else:
			con.commit()
		con.close()
		return item