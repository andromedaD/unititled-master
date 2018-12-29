import requests
#cookie设置
base_url='http://httpbin.org'

#获取cookie
# r=requests.get("http://www.baidu.com")
# print(r.cookies)
# print(type(r.cookies))
# for key,value in r.cookies.items():
#     print(key+':'+value)
#

#超时,设置timreout参数设置等待响应时间
# cookie={'user':'wangzhiben'}
# r=requests.get(base_url+'/get',cookies=cookie,timeout=1)#s设置0.001会报错，用以模拟等待超时
# print(r.text)

#文件上传
# file={'file':open('test.jpg','rb')}
# r=requests.post(base_url+'/post',files=file)
# print(r.text)

