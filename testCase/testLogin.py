#! /user/bin/evn python
# coding:utf-8

from common.interfaceList import *
#from common.Log import MyLog

class Login (unittest.TestCase):

    def setUp(self):
        #self.log = MyLog.get_log()
        #self.loger = self.log.get_logger()

        self.url = url_Login
        self.headers = ""
        self.data = {"mobile":"15800000001","password":"111111","code":""}

    def tearDown(self):

        pass

        #self.log.build_case_line(self.case_name, self.code, self.msg)

    def test_001_login(self): #正常传参,code为空

        res = requests.post(url=self.url,headers=self.headers,data=self.data).json()
        print(res)
        self.assertEqual(res.get(u'message'),u'登录成功')


