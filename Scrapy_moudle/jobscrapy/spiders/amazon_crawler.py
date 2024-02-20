import scrapy

url = "https://www.amazon.com/-/zh_TW/s?k=%E6%89%8B%E6%A9%9F&i=mobile&rh=n%3A7072561011&dc&language=zh_TW&crid=2FI25L7UURJFL&qid=1707743372&rnid=113334702011&sprefix=%2Caps%2C452&ref=sr_nr_p_n_feature_thirty-nine_browse-bin_5&ds=v1%3Ax2zp%2BgVbZzVa1f%2BghTAstSKozXK%2B%2FFtqHOUytl3PcDY"

class AmazonCrawlerSpider(scrapy.Spider):
    name = "amazon_crawler"
    allowed_domains = ["www.amazon.com"]
    start_urls = [url]

    def parse(self, response):
        smartphone_brands_level_one = response.css("div[id = 'brandsRefinements']")
        smartphone_brands = smartphone_brands_level_one.css('span[data-csa-c-type="element"][data-csa-c-slot-id="nav-pkr"]')

        for smartphone_brand in smartphone_brands:
            try:
                smartphone_brand_text = smartphone_brand.css('span[class="a-size-base a-color-base"]::text').get()
                smartphone_brand_url = smartphone_brand.css('a.a-link-normal.s-navigation-item::attr(href)').get()

                yield {
                    'smartphone_brand': smartphone_brand_text,
                    'smartphone_brand_url': "https://www.amazon.com" + smartphone_brand_url
                }
            except :
                smartphone_brand_text = None
                smartphone_brand_url = None
                yield {
                    'smartphone_brand': smartphone_brand_text,
                    'smartphone_brand_url': smartphone_brand_url
                }
        pass
