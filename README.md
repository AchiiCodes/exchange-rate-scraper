# Exchange Rate Scraper
Scrapes the money exchange rate from [pottchange](https://www.pottchange.com/wisselkoersen/) and stores the results into a postgres database.

# Dependencies
```
python -m venv venv
. venv\Script\activate
pip install -r requirements.txt
pip install git+https://github.com/scrapy/scrapyd-client.git
```

# Running Postgress
```
docker-compose up -d  
```

# Running scraper
```
scrapy runspider .\crawl\spiders\pottchange.py     
```

# Local deployment
```
scrapyd
scrapyd-deploy local 
```