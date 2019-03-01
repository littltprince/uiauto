#! /user/bin/evn python
# coding:utf-8

from common.interfaceList import *
from common.publicClass import getToken

class RefreshToken(unittest.TestCase):

    def setUp(self):
        self.url = url_RefreshToken
        self.headers = {}
        self.headers["header"] = ""
        self.headers["Authorization"] = "Bearer"+getToken()

    def tearDown(self):

        pass

    def test_001_RefreshToken(self):

        res = requests.post(url=self.url,headers= self.headers).json()
        #print(res)
        self.assertEqual(res.get(u"message"),u"success")




if __name__ == '__main__':
    unittest.main

