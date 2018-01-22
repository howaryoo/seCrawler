from __future__ import print_function

import logging

from scrapy.spiders import Spider
from seCrawler.common.searchResultPages import searchResultPages
from seCrawler.common.searchEngines import SearchEngineResultSelectors
from scrapy.selector import  Selector


logger = logging.getLogger(__file__)


class keywordSpider(Spider):
    name = 'keywordSpider'
    allowed_domains = ['bing.com', 'google.com', 'baidu.com']
    start_urls = []
    keyword = None
    searchEngine = None
    selector = None

    def __init__(self, keyword, se='bing', pages=50,  *args, **kwargs):
        super(keywordSpider, self).__init__(*args, **kwargs)
        self.keyword = keyword.lower()
        self.searchEngine = se.lower()
        self.selector = SearchEngineResultSelectors[self.searchEngine]
        pageUrls = searchResultPages(keyword, se, int(pages))
        for url in pageUrls:
            print(url)
            self.start_urls.append(url)

    def parse(self, response):
        urls = Selector(response).xpath(self.selector['url']).extract()
        logger.info('urls %s', len(urls))

        titles = Selector(response).xpath(self.selector['title']).extract()
        logger.info('title %s', len(titles))

        descriptions = Selector(response).xpath(self.selector['description']).extract()
        logger.info('descriptions %s', len(descriptions))

        images = Selector(response).xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "rms_img", " " ))]').extract()
        logger.info('images %s', len(images))

        for url, title, description in zip(urls, titles, descriptions):
            yield {'url': url, 'title': title, 'description': description}

        for image in images:
            yield {'url': image, 'title': 'image', 'description': 'image url'}
