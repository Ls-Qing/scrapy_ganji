# -*- coding: utf-8 -*-
import re
import scrapy
#有js界面，换种方式爬数据
from scrapy_splash import SplashRequest as Request
# from scrapy import Request
from ganjixq.items import GanjixqItem

class GanjiSpider(scrapy.Spider):
    name = 'ganji'
    allowed_domains = ['ganji.com']
    start_urls = ['http://www.ganji.com/index.htm']

    def parse(self, response):
        ds = response.xpath('/html/body/div[1]/div[3]/dl/dd/a')
        for item in ds:
            mc = item.xpath('text()').extract_first()
            if mc != '钓鱼岛':
                url = item.xpath('@href').extract_first() + 'xiaoqu/'
                yield Request(url,callback=self.genurl,meta = {'dsmc':mc,
                                                                'dycs':0})
    # 获取各城市小区页面链接
    def genurl(self,response):
        dsmc = response.meta['dsmc']
        dycs = response.meta['dycs']
        bash_url = response.url
        xqs = int(response.xpath('/html/body/div[3]/div[2]/span/strong/text()').extract_first().replace('条',''))
        #赶集每次最多可翻100页对于小于2000个小区的城市可以直接取
        #多于2000的需要获取街道链接然后调用getxq1函数
        if dycs == 0:
            if xqs <= 2000:
                for i in range(0,xqs,20):
                    url = bash_url + 'f%d/'%(i)
                    yield Request(url,callback=self.get_xq,meta = {'dsmc':dsmc})
            else:
                jiedaos = response.xpath('/html/body/div[3]/div[3]/div/dl[2]/dd/div/a[@rel="nofollow"]')
                for jd in jiedaos:
                    url = bash_url + jd.xpath('@href').extract_first().split('/')[2]
                    yield Request(url,callback=self.genurl,meta = {'dsmc':dsmc,
                                                                   'dycs':9999})
        else:
            xqs = 2000 if xqs>2000 else xqs
            for i in range(0,xqs,20):
                url = bash_url + 'f%d/'%(i)
                yield Request(url,callback=self.get_xq,meta = {'dsmc':dsmc})
    def get_xq(self,response):
        #
        item = GanjixqItem()
        item['dsmc'] = response.meta['dsmc']
        item['url']  = response.url
        xqxxs = response.xpath('/html/body/div[3]/div[4]/div[3]/ul/li')
        for xq in xqxxs:
            item['xqmc'] = xq.xpath('div[2]/div/a/text()').extract_first()
            item['xqdz'] = re.sub('\s','',''.join(xq.xpath('div[2]/p[1]/text()').extract()))
            item['esf']  = xq.xpath('div[2]/p[2]/span[1]/a/text()').extract_first()
            item['czf']  = xq.xpath('div[2]/p[2]/span[2]/a/text()').extract_first()
            item['fj']   = xq.xpath('div[3]/p[1]/b/text()').extract_first()
            item['qs']   = xq.xpath('div[3]/p[2]/span/@class').extract_first()
            item['sl']   = xq.xpath('div[3]/p[2]/span/i[2]/text()').extract_first()
              
            yield item
            