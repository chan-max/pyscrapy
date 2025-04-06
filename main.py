import scrapy
from scrapy.crawler import CrawlerProcess

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['https://quotes.toscrape.com']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

# 配置并运行爬虫
process = CrawlerProcess(settings={
    "FEEDS": {
        "quotes.json": {"format": "json"},
    },
})


process.crawl(QuotesSpider)
process.start()
