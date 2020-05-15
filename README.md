# gplay_crawler
Crawl apps from the Google Play Store

This is a Scrapy crawler written in Python. I have omitted the items, pipelines and other files from the repository.
Users can configure their item list/pipelines according to their use cases.

Scrapy tutorial:https://docs.scrapy.org/en/latest/intro/tutorial.html

Instructions to run: 
1. Create a scrapy directory following above tutorial
2. Replace settings and spider files with this repo's code.
3. Run "scrapy crawl gplay" from the command line in created directory
4. Set of crawled apps will be returned in python-dic format.
