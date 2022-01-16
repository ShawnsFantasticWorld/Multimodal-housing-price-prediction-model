import scrapy


class CrawlerLine1Spider(scrapy.Spider):
    name = 'crawler_line_9'
    allowed_domains = ['www.anjuke.com']
    #start_urls = ['http://www.anjuke.com/']
    #   https://beijing.anjuke.com/sale/ditiefang-l6/p1
    base_url = 'https://beijing.anjuke.com/sale/ditiefang-l13/p'
    offset = 1

    start_urls = [base_url + str(offset)]

    def parse(self, response):
        ul_list = response.xpath('//div[@class="property"]')
        #print("2222")
        for ul in ul_list:
            item = {}
            item["name"] = ul.xpath(".//div[@class='property-content-info property-content-info-comm']/p[1]/text()").extract_first()
            item["district"] = ul.xpath(".//div[@class='property-content-info property-content-info-comm']/p[2]/span[1]/text()").extract_first()
            item["bedroomNum"] = ul.xpath(".//div[@class='property-content-info']/p[1]/span[1]/text()").extract_first()
            item["livingroomNum"] = ul.xpath(".//div[@class='property-content-info']/p[1]/span[3]/text()").extract_first()
            item["bathroomNum"] = ul.xpath(".//div[@class='property-content-info']/p[1]/span[5]/text()").extract_first()
            
            item["area"] = ul.xpath("normalize-space(.//div[@class='property-content-info']/p[2]/text())").extract_first()
            item["type_floorNum"] = ul.xpath("normalize-space(.//div[@class='property-content-info']/p[4]/text())").extract_first()
            item["builtYear"] = ul.xpath("normalize-space(.//div[@class='property-content-info']/p[5]/text())").extract_first()
            item["direction"] = ul.xpath(".//div[@class='property-content-info']/p[3]/text()").extract_first()
            item["distance2SW"] = ul.xpath("normalize-space(.//div[@class='property-extra']/li)").extract_first()
            
            item["price"] = ul.xpath(".//div[@class='property-price']//p/span[1]/text()").extract_first()

            yield item
        print("Finished......")
        if self.offset < 50:
            print("********************************************************")
            print("Start_Next......")
            self.offset += 1
            url =self.base_url + str(self.offset)
            #print(url)
            yield scrapy.Request(url, callback=self.parse,dont_filter=True)