import requests

base_url='http://httpbin.org'
# #发送GET类型请求
# r=requests.get(base_url+'/get')
# print(r.status_code)
#
# #发送POST类型请求
# r=requests.post(base_url+"/post")
# print(r.status_code)
#
# #发送put类型请求
# r=requests.put(base_url+'/put')
# print(r.status_code)
#
# #发送delete类型请求
# r=requests.delete(base_url+'/delete')
# print(r.status_code)

#参数传递
# param_data={'uesr':'wangzhiben','password':'6666'}
# r=requests.get(base_url+'/get',params=param_data)
# print(r.url)
# print(r.status_code)

#传递body中的data
# form_data={'user':'wangzhiben','password':'123456'}
# r=requests.post(base_url+'/post',data=form_data)
# print(r.text)

#如果想为请求添加HTTP请求头，只要简单传递一个dict给headers参数就可以了
# form_data={'user':'wangzhiben','password':'123456'}
# header={'user-agent':'Mozilla/5.0'}
# r=requests.post(base_url+'/post',data=form_data,headers=header)
# print(r.text)
# print(r.json())#返回json格式
#很多爬虫程序都会定制headers来避免被封，如下面爬取知乎页面元素就设置了请求头
# header={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',}
#关闭证书验证.因为,如果不关闭,请求总是失败,不能获取到重定向的信息
#方法一、在进行GET时,指定SSL证书,[各浏览器的User-Agent] http://www.useragentstring.com/pages/useragentstring.php
#方法二、[SSL 证书验证] http://docs.python-requests.org/zh_CN/latest/user/advanced.html#ssl
# r=requests.get(base_url+'/get',headers=header)
# print(r.text)
# print(r.headers)





