# -*- coding: utf-8 -*-
'''
@File  : runtest.py
@Author: 王治本
@Contact : 568898699@qq.com
@Date  : 2018/12/25 0025 13:02
'''
import os
import time
from  BSTestRunner import BSTestRunner
import unittest

report_dir='../test_report'
case_dir='../studynote'
now=time.strftime('%Y-%m-%d %H_%M_%S')
report_file=report_dir+'/'+now+'result.html'

discover=unittest.defaultTestLoader.discover(case_dir,pattern='weather_api_unittest.py')

with open(report_file,'wb') as fb:
    runner=BSTestRunner(stream=fb,title='weather api test',description='cotain pass error loss')
    runner.run(discover)