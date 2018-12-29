import requests
#session对象存储特定用户会话所需的属性及配置信息,第二个接口获取第一个接口属性
#通常用以模拟用户登录成功后模拟下一步的操作
base_url='http://httpbin.org'

s=requests.Session()
r=s.get(base_url+'/cookies/set/user/wanghzhiben')
print(r.text)
r=s.get(base_url+'/cookies')
print(r.text)

