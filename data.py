import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DataSpider(CrawlSpider):
    name = 'data'
    allowed_domains = ['w3schools.com']
    start_urls = ['https://www.w3schools.com/xml/xquery_intro.asp']


    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@id='leftmenuinnerinner']/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="(//a[@class='w3-right w3-btn'])[1]"))
    )

    def parse_item(self, response):
        yield {
       'H1_leftside_heading': response.xpath("//div[@class='w3-col l10 m12']/h1/text()").getall(),
       'H1_rightside_heading': response.xpath("//span[@class='color_h1']/text()").getall(),
       'H2':response.xpath("//div[@class='w3-col l10 m12']/h2/text()").getall(),
       'H3':response.xpath("//div[@class='w3-example']/h3/text()").getall(),
       'All_para':response.xpath("//div[@class='w3-col l10 m12']/p/text()").getall(),
       'li':response.xpath("//ul/li/text()").getall(),
       'div':response.xpath("//div[@class='w3-code notranslate htmlHigh']/text()").getall(),
       'div_2':response.xpath("//div[@style='font-size:20px;padding:10px;margin-bottom:10px;']/text()").getall()
        }
