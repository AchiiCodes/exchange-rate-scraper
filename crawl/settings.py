import os
from dotenv import load_dotenv

load_dotenv()
BOT_NAME = "crawl"
SPIDER_MODULES = ["crawl.spiders"]
NEWSPIDER_MODULE = "crawl.spiders"
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
    "crawl.pipelines.CrawlPipeline": 300,
}
DATABASE = {
    "drivername": "postgresql",
    "host": os.environ["POSTGRES_HOST"],
    "port": os.environ["POSTGRES_PORT"],
    "username": os.environ["POSTGRES_USER"],
    "password": os.environ["POSTGRES_PASS"],
    "database": os.environ["POSTGRES_DB"],
}
LOG_LEVEL = "INFO"
