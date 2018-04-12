import scrapy
import csv
import sys
from bs4 import BeautifulSoup
from apple.items import AppleItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AppleCrawler(CrawlSpider):
    name = 'apple'
    start_urls = [
        'https://tw.buy.yahoo.com/help/helper.asp?p=sitemap'
    ]
    rules = [
        #Rule(LinkExtractor(allow=('/tw\.buy\.yahoo\.com/\?sub\=(\d*$|\d*\&sort\=\-ptime\&pg\=\d$)')), callback='parse_list', follow=True)
    ]
    
    def parse(self, response):
        domain = 'https://tw.buy.yahoo.com'
        res = BeautifulSoup(response.body)
        #for categorys in res.select('.yui3-g'):
			#print domain + categorys.select('a')[0]['href']
        for categorys in res.select('.site-list'):
			#print domain + categorys.select('a')[0]['href']
			yield scrapy.Request(domain + categorys.select('a')[0]['href'], self.parse_categorys)

    def parse_categorys(self, response):
        domain = 'https://tw.buy.yahoo.com/gdsale'
        res = BeautifulSoup(response.body)
        #for categorys in res.select('.yui3-g'):
			#print domain + categorys.select('a')[0]['href']
        for rankitems in res.select('#cl-hotrank .brand'):
			#print rankitems.select('a')[0]['href']
			yield scrapy.Request(rankitems.select('a')[0]['href'], self.parse_detail)
        for items in res.select('#srp_result_list'):
			yield scrapy.Request(items.select('a')[0]['href'], self.parse_all)
			
    def parse_detail(self, response):
		reload(sys)
		sys.setdefaultencoding('utf-8')
		res = BeautifulSoup(response.body)
		appleitem = AppleItem()
		appleitem['title'] = res.select('h1')[0].text
		appleitem['price'] = res.select('.priceinfo .price')[0].text
		appleitem['category'] = res.select('#cl-breadcrumbs h3')[0].text + ' / ' + res.select('#cl-breadcrumbs h3')[1].text + ' / ' + res.select('#cl-breadcrumbs h3')[2].text
		appleitem['link'] = response.url
		appleitem['topsell'] = 'Y'
		return appleitem

    def parse_all(self, response):
		reload(sys)
		sys.setdefaultencoding('utf-8')
		res = BeautifulSoup(response.body)
		appleitem = AppleItem()
		appleitem['title'] = res.select('h1')[0].text
		appleitem['price'] = res.select('.priceinfo .price')[0].text
		appleitem['category'] = res.select('#cl-breadcrumbs h3')[0].text + ' / ' + res.select('#cl-breadcrumbs h3')[1].text + ' / ' + res.select('#cl-breadcrumbs h3')[2].text
		appleitem['link'] = response.url
		appleitem['topsell'] = 'N'
		return appleitem
