import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
base_url='http://httpbin.org'
# #basic_auth验证
r=requests.get(base_url+"/basic-auth/wangzhiben/888",auth=HTTPBasicAuth('wangzhiben','888'))
print(r.text)
print(r.status_code)
# #digest_auth验证
r=requests.get(base_url+"/digest-auth/auth/wangzhiben/888",auth=HTTPDigestAuth('wangzhiben','888'))
print(r.text)
print(r.status_code)

