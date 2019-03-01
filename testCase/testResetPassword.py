#! /user/bin/evn python
# coding:utf-8

from common.interfaceList import *
from common.publicClass import getToken

class ResetPassword(unittest.TestCase):

    def setUp(self):
        self.url = url_ResetPassword
        self.headers = {}
        self.headers["header"] = ""
        self.headers["Authorization"] = "Bearer"+getToken()

    def tearDown(self):

        pass

    def test_001_ResetPassword(self):  #验证码无效
        self.data = {}
        self.data["mobile"] = 15800000001
        self.data["password"] = 123456
        self.data["confirm_password"] = 123456
        self.data["code"] = 1111

        res = requests.post(url=self.url,headers=self.headers,data=self.data).json()
        #print(res)
        self.assertEqual(res.get(u'message'),u'验证码无效')



