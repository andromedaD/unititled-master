# -*- coding: utf-8 -*-
'''
@File  : restful_api_groups.py
@Author: 王治本
@Contact : 568898699@qq.com
@Date  : 2018/12/28 0028 9:06
'''
from locust import HttpLocust,TaskSet,task

class UserBehavior(TaskSet):
    def on_start(self):
        self.users_index=0
        self.groups_index=0

    @task
    def test_users(self):
        user_id=self.locust.id[self.users_index]
        url='/users/'+str(user_id)+'/'
        self.client.get(url,auth=('wangzhiben','123456'))
        self.users_index=(self.users_index+1)%len(self.locust.id)

    @task
    def test_groups(self):
        groups_id=self.locust.id[self.groups_index]
        url='/groups/'+str(groups_id)+'/'
        self.client.get(url,auth=('wangzhiben','123456'))
        self.groups_index=(self.groups_index+1)%len(self.locust.id)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    id=[1,2]
    min_wait = 3000
    max_wait = 6000
    host = 'http://127.0.0.1:8000'
