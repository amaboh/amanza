import scrapy


class EquityspiderSpider(scrapy.Spider):
    name = "equityspider"
    allowed_domains = ["ngxgroup.com"]
    start_urls = ["https://ngxgroup.com/exchange/data/equities-price-list/"]

    def parse(self, response):
        # Get all rows from the table 
        rows = response.xpath('//tbody[@id="ngx_equities_trading_statistics"]//tr')
        for row in rows:
            yield {
            'Company': row.xpath('./td[1]/text()').get(),
            'Previous Closing Price': row.xpath('./td[2]/text()').get(),
            'Opening Price': row.xpath('./td[3]/text()').get(),
            'High': row.xpath('./td[4]/text()').get(),
            'Low': row.xpath('./td[5]/text()').get(),
            'Close': row.xpath('./td[6]/text()').get(),
            'Change': row.xpath('./td[7]/text()').get(),
            'Trades': row.xpath('./td[8]/text()').get(),
            'Volume': row.xpath('./td[9]/text()').get(),
            'Value': row.xpath('./td[10]/text()').get(),
            'Trade Date': row.xpath('./td[11]/text()').get(),
        }

