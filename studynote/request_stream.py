import requests
import json
base_url='http://httpbin.org'
#流式请求
#有些结果返回并不是一个单独结果，会有很多结果dynamic_data
#如在浏览器打开httpbin.org，点击dynamic_data->get/stream/{n}->点击"Try it out"->输入栏输入10->点击"execute",以下是返回结果
'''
{"url": "http://httpbin.org/stream/10", "args": {}, "headers": {"Host": "httpbin.org", "Connection": "close", "Accept": "application/json", "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36", "Referer": "http://httpbin.org/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1"}, "origin": "49.74.85.242", "id": 0}
{"url": "http://httpbin.org/stream/10", "args": {}, "headers": {"Host": "httpbin.org", "Connection": "close", "Accept": "application/json", "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36", "Referer": "http://httpbin.org/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1"}, "origin": "49.74.85.242", "id": 1}
{"url": "http://httpbin.org/stream/10", "args": {}, "headers": {"Host": "httpbin.org", "Connection": "close", "Accept": "application/json", "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36", "Referer": "http://httpbin.org/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1"}, "origin": "49.74.85.242", "id": 2}
{"url": "http://httpbin.org/stream/10", "args": {}, "headers": {"Host": "httpbin.org", "Connection": "close", "Accept": "application/json", "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36", "Referer": "http://httpbin.org/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1"}, "origin": "49.74.85.242", "id": 3}
{"url": "http://httpbin.org/stream/10", "args": {}, "headers": {"Host": "httpbin.org", "Connection": "close", "Accept": "application/json", "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36", "Referer": "http://httpbin.org/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1"}, "origin": "49.74.85.242", "id": 4}
{"url": "http://httpbin.org/stream/10", "args": {}, "headers": {"Host": "httpbin.org", "Connection": "close", "Accept": "application/json", "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36", "Referer": "http://httpbin.org/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1"}, "origin": "49.74.85.242", "id": 5}
{"url": "http://httpbin.org/stream/10", "args": {}, "headers": {"Host": "httpbin.org", "Connection": "close", "Accept": "application/json", "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36", "Referer": "http://httpbin.org/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1"}, "origin": "49.74.85.242", "id": 6}
{"url": "http://httpbin.org/stream/10", "args": {}, "headers": {"Host": "httpbin.org", "Connection": "close", "Accept": "application/json", "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36", "Referer": "http://httpbin.org/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1"}, "origin": "49.74.85.242", "id": 7}
{"url": "http://httpbin.org/stream/10", "args": {}, "headers": {"Host": "httpbin.org", "Connection": "close", "Accept": "application/json", "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36", "Referer": "http://httpbin.org/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1"}, "origin": "49.74.85.242", "id": 8}
'''
#针对这种接口类型，需要使用迭代方法iter_lines来处理
# r=requests.get(base_url+'/stream/10',stream=True)
#
# if r.encoding is None:
#     r.encoding='utf-8'
# for line in r.iter_lines(decode_unicode=True):
#     if line:
#         data=json.loads(line)
#         print(data['url'])

r=requests.get(base_url+'/stream/10',stream=True)

if r.encoding is None:
    r.encoding='utf-8'
for line in r.iter_lines(decode_unicode=True):
    data=json.loads(line)
    print(data['headers'])