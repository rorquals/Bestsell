# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#import sqlite3
import csv
import sys

class ApplePipeline(object):
	#def open_spider(self, spider):
		#self.conn = sqlite3.connect('apple.sqlite')
		#self.cur = self.conn.cursor()
		#self.cur.execute('create table if not exists apple(title varchar(100), content text, time varchar(50));')
		#pass

	#def close_spider(self, spider):
		#self.conn.commit()
		#self.conn.close()
		#pass

	def process_item(self, item, spider):
		reload(sys)
		sys.setdefaultencoding('utf-8')
		#col = ','.join(item.keys())
		#placeholders = ','.join(len(item) * '?')
		#sql = 'insert into apple({}) values({})'
		#self.cur.execute(sql.format(col, placeholders), item.values())
		f = file('bestsell.csv','a+') 
		writer = csv.writer(f) 
		writer.writerow((item['title'],item['price'],item['category'],item['topsell'],item['link']))
		return item