# -*- coding: utf-8 -*-
import scrapy


class LambdaCallbackBadSpider(scrapy.Spider):
    name = 'lambda-callback-bad'
    start_urls = ['https://example.org/']
    custom_settings = {
        'LOG_LEVEL': 'DEBUG',
        'SCHEDULER_DEBUG': True,
        'JOBDIR': 'lambda-callback-bad-temp',
    }

    def parse(self, response):
        data = [response.url]
        callback = lambda response: self.parse_additional(response, data)
        return scrapy.Request('https://example.com', callback=callback)

    def parse_additional(self, response, data):
        data.append(response.url)
        return {'data': data}


class LambdaCallbackGoodSpider(scrapy.Spider):
    name = 'lambda-callback-good'
    start_urls = ['https://example.org/']
    custom_settings = {
        'LOG_LEVEL': 'DEBUG',
        'SCHEDULER_DEBUG': True,
        'JOBDIR': 'lambda-callback-good-temp',
    }

    def parse(self, response):
        data = [response.url]
        return scrapy.Request('https://example.com', meta={'data': data},
                              callback=self.parse_additional)

    def parse_additional(self, response):
        data = response.meta['data']
        data.append(response.url)
        return {'data': data}
