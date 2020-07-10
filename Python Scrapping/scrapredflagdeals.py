import scrapy


class DealSpider(scrapy.Spider):
    name = 'dealspider'
    start_urls = ['https://forums.redflagdeals.com/hot-deals-f9']

    def parse(self, response):
        for deal in response.css('h3.topictitle.topictitle_has_retailer'):
            yield {
                'retailer': deal.css('.topictitle_retailer::text').extract_first(),
                'title': deal.css('.topic_title_link::text').extract_first()
            }
            next = response.css('.pagination_next_set.pagination_button_set > a ::attr(href)').extract_first()
            if next:
                yield response.follow(next, self.parse)

# scrapy runspider -o deal.csv scrapredflagdeals.py
