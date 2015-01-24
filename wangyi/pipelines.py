# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from models import Ios, db_connect, create_ios_table

class WangyiPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_ios_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        ios = Ios(**item)
        session.add(ios)
        session.commit(ios)
        return item
