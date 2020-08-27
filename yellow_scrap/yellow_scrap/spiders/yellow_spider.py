import scrapy

class BusinessSpider(scrapy.Spider):
    name = "businesses"
    start_urls = [
        "https://www.yellowpages.com/search?search_terms=Bakeries&geo_location_terms=Los+Angeles%2C+CA",
    ]

    def parse(self, response):
        for business in response.css("div.result"):
            yield {
                "primary-info": {
                "name": business.css("a.business-name span::text").get(),
                "categories" : business.css("div.categories a::text").getall(),
                "links": {
                    "website" : business.css("a.track-visit-website::attr(href)").getall()
                    } # link to website, coupons and then menus
                },
                # "ratings" : business.css("div.ratings div.result-rating::attr(class)").get().split(" ")[1]
            }
