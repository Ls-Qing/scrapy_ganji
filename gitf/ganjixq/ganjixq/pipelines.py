# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2
# from ganjixq import settings 

# PSQL_HOST     = '127.0.0.1'
# PSQL_USER     = 'postgres'
# PSQL_PASSWORD = 'midou@'
# PSQL_PORT     = '5432'
# PSQL_DB       = 'test'
 
# PSQL_HOST      =   settings.PSQL_HOST
# PSQL_USER      =   settings.PSQL_USER
# PSQL_PASSWORD  =   settings.PSQL_PASSWORD
# PSQL_PORT      =   settings.PSQL_PORT
# PSQL_DB        =   settings.PSQL_DB
# 
# cnx = psycopg2.connect(dbname=PSQL_DB, 
#                        user=PSQL_USER,
#                        password=PSQL_PASSWORD, 
#                        host=PSQL_HOST, 
#                        port=PSQL_PORT)
# 
# cur = cnx.cursor()

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
#         self.insert_into(dsmc, url, xqmc, xqdz, esf, czf, fj, qs, sl)
    #写一个函数，将数据存入数据库   
#     def insert_into(self,dsmc,url,xqmc,xqdz,esf,czf,fj,qs,sl):
#         sql = "INSERT INTO gjxq (dsmc,url,xqmc,xqdz,esf,czf,fj,qs,sl) VALUES (%(dsmc)s,%(url)s,%(xqmc)s,%(xqdz)s,%(esf)s,%(czf)s,%(fj)s,%(qs)s,%(sl)s)"
#         value = {'dsmc':dsmc,
#                  'url' :url ,
#                  'xqmc':xqmc,
#                  'xqdz':xqdz,
#                  'esf' :esf ,
#                  'czf' :czf ,
#                  'fj'  :fj  ,
#                  'qs'  :qs  ,
#                  'sl'  :sl}
#         cur.execute(sql,value)
#         cnx.commit()