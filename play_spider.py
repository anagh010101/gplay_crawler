from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

import scrapy
import urlparse


class MySpider(CrawlSpider):
  name = "gplay"
  allowed_domains = ["play.google.com"]
  # start_urls = ["https://play.google.com/store/apps/details?id=org.telegram.messenger"
  #                , "https://play.google.com/store/apps/details?id=com.ludo.king"

  #               ]
  start_urls = ["https://play.google.com/store/apps/new"]

  rules = [
            Rule(LinkExtractor(allow=(r'apps',),deny=(r'reviewId')),follow=True,callback='parse_url')
          ]

  def abs_url(url, response):
      """Return absolute link"""
      base = response.xpath('//head/base/@href').extract()
      if base:
        base = base[0]
      else:
        base = response.url
      return urlparse.urljoin(base, url)
    
  def parse_url(self,response):
        self.log('Crawling file %s' % response.url)
        try:
          app_name = response.css('h1.AHFaub span::text').getall()[0]
          try:
              category = response.css('div.qQKdcc a::text').getall()[1]
          except:
              category = "NULL"

          avg_rating = response.css('div.BHMmbe::text').get()

          try:
              num_ratings = response.css('div.K9wGie span.EymY4b span::attr(aria-label)').get().split(' ')[0]
          except:
              num_ratings = "NULL"

          update_date = response.css('div.IQ1z0d span.htlgb::text').get()

          try:
              installs = response.css('div.IQ1z0d span.htlgb::text').getall()[2]
          except:
              installs = "NULL"

          yield{
          'App_Name' : app_name
          ,'Category' : category
          ,'Avg_Rating' : avg_rating
          , 'Num_Ratings' : num_ratings
          , "Update_Date" : update_date
          , "Installs" : installs
          }
        except:  
          yield {}
          

