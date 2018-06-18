# -*- coding: utf-8 -*-
import scrapy


class LambdaCallbackSpider(scrapy.Spider):
    name = 'lambda-callback'
    start_urls = ['https://example.org/']

    def parse(self, response):
        data = [response.url]
        callback = lambda response: self.parse_additional(response, data)
        return scrapy.Request('https://example.com', callback=callback)

    def parse_additional(self, response, data):
        data.append(response.url)
        return {'data': data}
