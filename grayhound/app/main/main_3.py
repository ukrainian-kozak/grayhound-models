from scrapy.crawler import CrawlerProcess
from grayhound.app.spiders.race_spider import NewRaceSpider
from grayhound.app import settings

def main():

    date = '2024-08-28'
    api_key = settings.SCRAPER_API_KEY

    grayhound_process = CrawlerProcess()
    grayhound_process.crawl(NewRaceSpider, api_key=api_key, date=date)
    grayhound_process.start()
    
if __name__ == "__main__":
    main()