# -*- coding: utf-8 -*-

# Scrapy settings for wangyi project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'wangyi'

SPIDER_MODULES = ['wangyi.spiders']
NEWSPIDER_MODULE = 'wangyi.spiders'

ITEM_PIPELINES = {
    'wangyi.pipelines.WangyiPipeline': 1
}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wangyi (+http://www.yourdomain.com)'
