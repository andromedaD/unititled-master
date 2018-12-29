# -*- coding: utf-8 -*-
'''
@File  : weather_api_unittest.py
@Author: 王治本
@Contact : 568898699@qq.com
@Date  : 2018/12/25 0025 12:24
'''
import unittest
import requests
from time import sleep

class Weather(unittest.TestCase):
    def setUp(self):
        self.url='http://t.weather.sojson.com/api/weather/city/'
        self.header={'User-Agent':'Mozilla/5.0'}

    def test_weather_pass(self,city_code='101190101'):
        r=requests.get(self.url+city_code,headers=self.header,verify=False)
        result=r.json()
        self.assertEqual(result['status'],200)
        self.assertEqual(result['cityInfo']['city'],'南京市')

    def test_weather_error(self,city_code='123'):
        r=requests.get(self.url+city_code,headers=self.header,verify=False)
        result=r.json()
        self.assertEqual(result['status'],404)

    def test_weather_loss(self,city_code=''):
        r=requests.get(self.url+city_code,headers=self.header,verify=False)
        result=r.json()
        self.assertEqual(result['status'],404)

if __name__ == '__main__':
    unittest.main()