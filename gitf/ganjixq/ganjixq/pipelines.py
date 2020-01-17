# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html





class GanjixqPipeline(object):
    def process_item(self, item, spider):
        dsmc  = item['dsmc']
        url   = item['url'] 
        xqmc  = item['xqmc']
        #将小区地址中的 详细地址: 替换为 ， 将 ， 替换为-
        xqdz  = item['xqdz'].replace(',','-').replace('详细地址:',',')
        esf   = item['esf'] 
        czf   = item['czf'] 
        fj    = item['fj']  
        qs    = item['qs']  
        sl    = item['sl']
        with open(r'D:\xqmc.txt','a+') as txt:
            txt.writelines('{},{},{},{},{},{},{},{},{}\n'.format(dsmc, url, xqmc, xqdz, esf, czf, fj, qs, sl))
