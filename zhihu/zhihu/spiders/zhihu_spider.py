# coding: utf-8
__author__ = 'cloudlite'

from urlparse import urlparse

from scrapy.selector import Selector

try:
    from scrapy.spider import Spider
except ImportError:
    from scrapy.spider import BaseSpider as Spider

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle

from zhihu.items import *


class ZhihuCrawler(CrawlSpider):
    name = "zhihu"
    allowed_domains = ["zhihu.com"]
    start_urls = "http://www.zhihu.com/people/jin-xi-he-20"

    rules = [Rule(sle(allow=("/people/[^/]+/followees$")), callback='parse_followees'),
             Rule(sle(allow=("/people/[^/]+/followers$")), callback='parse_followers'),
             Rule(sle(allow=("/people/[^/]+$", )), callback='parse_people_with_rules', follow=True)
    ]