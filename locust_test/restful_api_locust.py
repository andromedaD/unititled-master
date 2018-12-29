# -*- coding: utf-8 -*-
'''
@File  : restful_api_locust.py
@Author: 王治本
@Contact : 568898699@qq.com
@Date  : 2018/12/27 0027 18:07
'''

from locust import HttpLocust,TaskSet,task

class UserBehavior(TaskSet):
    @task(2)
    def test_users(self):
        self.client.get('/user/',auth=('wangzhiben','123456'))

    @task(1)
    def test_group(self):
        self.client.get('/groups/',auth=('wangzhiben','123456'))

class WebsiteUser(HttpLocust):
    task_set=UserBehavior
    min_wait = 3000
    max_wait = 6000
