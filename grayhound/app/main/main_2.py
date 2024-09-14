from scrapy.crawler import CrawlerProcess
from grayhound.app.spiders.grayhound_spider import GrayhoundSpider


def main():

    dates = []   # напиши дату в таком формате yyyy-mm-dd
    
    for year in range(1990, 2014):
        for month in range(1, 13):
            for day in range(1, 32):
                dates.append(f'{year}-{month}-{day}')
    
    api_key = ''

    grayhound_process = CrawlerProcess()
    grayhound_process.crawl(GrayhoundSpider, api_key=api_key, dates=dates)
    grayhound_process.start()
    
if __name__ == "__main__":
    main()