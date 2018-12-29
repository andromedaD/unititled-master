import requests
from urllib import parse
import json

url='http://t.weather.sojson.com/api/weather/city/'
header={'User-Agent':'Mozilla/5.0'}
city_code='101190101'
r=requests.get(url+'/'+city_code,verify=False,headers=header)
response_data=r.json()
print(response_data)
print(response_data['time'])
print(response_data['cityInfo'])
print(response_data['data'])

#错误示范，下面2条代码
# params={'city_code':'101190101'}
# r=requests.get(url,params=params,headers=header,verify=False)

#没有用到的方法parse，使用如下
# data={'city':'南京'}
# city=parse.urlencode(data).encode('utf-8')
