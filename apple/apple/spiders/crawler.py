import scrapy
import sys
from bs4 import BeautifulSoup
from apple.items import AppleItem
#from scrapy.spiders import CrawlSpider, Rule
#from scrapy.linkextractors import LinkExtractor

class AppleCrawler(scrapy.Spider):
    name = 'apple'
    start_urls = [
        'https://tw.buy.yahoo.com/help/helper.asp?p=sitemap'
    ]
    #rules = [
    #    Rule(LinkExtractor(allow=('/new/realtime/.*$')), callback='parse_list', follow=True)
    #]
    
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
        for items in res.select('#cl-hotrank .brand'):
			#print items.select('a')[0]['href']
			yield scrapy.Request(items.select('a')[0]['href'], self.parse_detail)
			
    def parse_detail(self, response):
		reload(sys)
		sys.setdefaultencoding('utf-8')
		res = BeautifulSoup(response.body)
		appleitem = AppleItem()
		appleitem['title'] = res.select('h1')[0].text
		appleitem['price'] = res.select('.priceinfo .price')[0].text
		appleitem['category'] = res.select('#cl-breadcrumbs h3')[0].text
		print res.select('#cl-breadcrumbs h3')[0].text
		print res.select('#cl-breadcrumbs h3')[1].text
		print res.select('#cl-breadcrumbs h3')[2].text
		return appleitem
