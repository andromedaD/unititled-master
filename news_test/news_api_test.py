# -*- coding: utf-8 -*-
'''
@File  : news_api_test.py
@Author: 王治本
@Contact : 568898699@qq.com
@Date  : 2018/12/28 0028 12:10
'''
from ShowapiRequest import ShowapiRequest
# ,"84518","4eca2eacd9944a92bf52ebef2841bde7"

r=ShowapiRequest("http://route.showapi.com/109-35","84518","4eca2eacd9944a92bf52ebef2841bde7")
res=r.get()
print(res.status_code)

