import requests
base_url='http://httpbin.org'
#Requests可以为HTTPS请求验证SSL证书就像web浏览器一样，
#SSL证书默认是开启的,如果证书验证失败，会抛出SSLError
#如果不想验证证书，将verify=False
#下面是12306网站证书,12306证书是自己给自己颁发的
#错误是正常的
# r=requests.get('http://www.12306.cn',verify=False)
# print(r.text)

#代理设置
#允许一个网络终端（客户端）通过这个服务与另一个网络终端（一般为服务器）
#进行非直接连接
#代理推荐网站    西刺免费代理IP（http://www.xicidili.com/nn）,如http://119.101.112.20:9999
# proxies={'http':'http://119.101.112.20:9999'}
# r=requests.get(base_url+'/get',proxies=proxies)
# print(r.text)
