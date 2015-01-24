# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request
import json
import os.path
class WangyiPipeline(object):

    def __init__(self):
        self.conn = MySQLdb.connect(user='root', passwd='123', db='meipin', host='localhost', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()
    #log data to json file

    def process_item(self, item, spider):
#        if url is None:
        for i in xrange(0,len(item['url'])):
            sql = "insert ignore into ios(`title`,`url`,`pic`) values ('%s','%s','%s')" %(item['title'][i],item['url'][i],item['pic'][i])
            self.cursor.execute(sql)

            self.conn.commit()
        #else:
        #    for i in xrange(0,len(item['url'])):
        #        sql = "UPDATE `apple` SET `count` = {0} WHERE `title` = {1}".format(item['count'] ,item['title'])
        #        self.cursor.execute(sql)
        #        self.conn.commit()

        return item

