#! /user/bin/evn python
# coding:utf-8

#主管，首页授权项目

from common.interfaceList import *
from common.publicClass import getToken,getToken2
import unittest
import requests
class SupervisorAuthItems(unittest.TestCase):

    def setUp(self):
        self.url = url_HomepageAuthItems
        self.headers = {}
        self.headers["Authorization"] = "Bearer"+getToken()
        #self.headers["project_id"] = "117074"

    def tearDown(self):
        pass

    def test_001_SupervisorAuthItems(self): #登录主管账号，调用首页授权
        self.data = {"project_id":"117074"}
        res = requests.get(url=self.url,headers=self.headers,data=self.data).json()
        #print(res)
        self.assertEqual(res.get(u'message'),u'success')
        self.assertEqual(res.get(u"data")[0].get(u"text"),'客户管理')
        self.assertEqual(res.get(u"data")[1].get(u"text"),"顾问管理")
        self.assertEqual(res.get(u"data")[2].get(u"text"),"来电监控")

    def test_002_SupervisorAuthItems(self): #登录顾问账号，调用首页授权

         self.headers = {}
         self.headers["Authorization"] = "Bearer"+getToken2()
         self.data = {"project_id": "117074"}
         res = requests.get(url=self.url, headers=self.headers, data=self.data).json()
        # print(res)

         self.assertEqual(res.get(u"message"),u"不是主管权限")
