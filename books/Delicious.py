#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return Delicious

class Delicious(BaseFeedBook):
    title                 = 'Delicious'
    description           = u'聚合最爱文章'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 9
    oldest_article        = 2
    mastheadfile          = "mh_dapenti.gif"
    coverfile             = "cv_dapenti.jpg"
    network_timeout       = 60
    feeds = [
            ('36kr', 'http://www.36kr.com/feed?1.0'),
            (u'TechCrunch 中国', 'http://techcrunch.cn/feed/'),
            (u'爱范儿', 'http://www.ifanr.com/feed'),
           ]
                
