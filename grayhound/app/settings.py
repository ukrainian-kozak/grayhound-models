import environ

env = environ.Env(
    DEBUG=(bool, False)
)

environ.Env.read_env()

SCRAPER_API_KEY = env('SCRAPER_API_KEY')

LOG_FILE = 'scrapy_log.txt'

BOT_NAME = "grayhound"

SPIDER_MODULES = ["grayhound.app.spiders"]
NEWSPIDER_MODULE = "grayhound.app.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "grayhound (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

RETRY_ENABLED = True
RETRY_TIMES = 10
RETRY_HTTP_CODES = [502, 503, 504, 522, 524, 408]

DOWNLOAD_DELAY = 2.0
# RANDOMIZE_DOWNLOAD_DELAY = True

SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True



DOWNLOADER_MIDDLEWARES = {
    'grayhound.app.middlewares.ScrapeOpsFakeUserAgentMiddleware': 400,
    'grayhound.app.middlewares.TooManyRequestsRetryMiddleware': 500,

}



# ITEM_PIPELINES = {
#     'grayhound.pipelines.GrayhoundPipeline': 300,
#     'grayhound.pipelines.SaveToMySQLPipeline': 400,
#     'grayhound.pipelines.RaceMeetingPipeline': 400,
# }




# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "grayhound.middlewares.GrayhoundSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "grayhound.middlewares.GrayhoundDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
