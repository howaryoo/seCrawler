import json
import logging

import subprocess

logger = logging.getLogger(__name__)


def search(keyword, limit, sengine):
    # FIXME: NOT THREAD SAFE.
    # TODO ASAP: change implementation
    """
    source: https://stackoverflow.com/questions/36384286/how-to-integrate-flask-scrapy
    Run spider in another process, store items in file and read output to client.
    """
    logging.info('searching for %s using %s...', keyword, sengine)

    spider_name = 'keywordSpider'
    subprocess.check_output(['scrapy', 'crawl',
                             spider_name,
                             '-a', 'keyword='+keyword,
                             '-a', 'se='+sengine,
                             '-a', 'pages='+str(limit)])
    with open("items.jl") as items_file:
        response = json.load(items_file)

    if response:
        return response, 200
    return 'Not found', 404
