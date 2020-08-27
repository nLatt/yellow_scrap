import scrapy

class BusinessSpider(scrapy.Spider):
    search_terms = input("Enter your search terms: ").replace(" ", "+")
    name = "businesses"
    start_urls = [
        "https://www.yellowpages.com/search?search_terms={}&geo_location_terms=Los+Angeles%2C+CA".format(search_terms),
    ]

    def parse(self, response):
        for business in response.css("div.result"):
            yield {
                "name": business.css("a.business-name span::text").get(),
                "primary-info": {
                    "categories": business.css("div.categories a::text").getall(),
                    # "ratings" : business.css("div.ratings div.result-rating::attr(class)").get().split(" ")[1]
                    "links": {
                        "website": business.css("a.track-visit-website::attr(href)").get(),
                        "coupons": business.css("a.track-coupon::attr(href)").get(),
                        "menu": business.css("a.menu::attr(href)").get()
                        } # link to website, coupons and then menus
                    },
                "secondary-info": {
                    "phone-number": business.css("div.phones::text").get(),
                    "street-address": business.css("div.street-address::text").get(),
                    "locality": business.css("div.locality::text").get()
                }

            }
