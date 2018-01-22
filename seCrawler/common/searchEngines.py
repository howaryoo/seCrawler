__author__ = 'tixie'

SearchEngines = {
    'google': 'https://www.google.com/search?q={0}&start={1}',
    'bing': 'http://www.bing.com/search?q={0}&first={1}',
    'baidu': 'http://www.baidu.com/s?wd={0}&pn={1}'
}


SearchEngineResultSelectors= {
    'google': {
        'url': '//h3/a/@href',
        'title': '//h3/a/text()',
        'description': '//p/text()'
    },
   'bing':{
        'url': '//h2/a/@href',
        'title': '//h2/a/text()',
        'description': '//p/text()'
    },
    'baidu': {
        'url': '//h3/a/@href',
        'title': '//h3/a/text()',
        'description': '//p/text()'
    },
}
