from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy.conf import settings
import time
import sys
class DouBanImage(BaseSpider):
   name = "zerodm"
   start_urls = ["http://dmxz.zerodm.net/xiazai/2000.html",
                 "http://dmxz.zerodm.net/xiazai/2017.html"]
   download_delay = 1
   filename = 'download_url.txt'
   f = open(filename,"wb")
 
   def parse(self, response):
       req = []
       hxs = HtmlXPathSelector(response)
       urls = hxs.select("//div[@class='numlist']/ul/li/a/@href").extract()
       for url in urls:
           if url.find("xunlei") > 0:
               r = Request(url, callback=self.parse_GetDownload_URL)
               req.append(r)
       return req
    
   def parse_GetDownload_URL(self, response):
       reload(sys)
       sys.setdefaultencoding('utf-8')
       hxs = HtmlXPathSelector(response)
       urls = hxs.select("//ul//li//a[@class='file_name']/@href").extract()
       for url in urls:
           self.f.write(url+"\n")
    