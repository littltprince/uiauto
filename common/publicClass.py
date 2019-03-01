#! /user/bin/evn python
# coding:utf-8

from common.interfaceList import *
import requests

def getToken():  #主管账号登录获取token
    url = url_Login
    headers = {"Content-Type":"application/x-www-form-urlencoded"}
    data = {"mobile":"15800000001","password":"111111","code":""}

    res = requests.post(url=url, headers=headers, data=data).json()
    token = res.get(u'data').get(u'user').get(u'token')
    return token

def getToken2():  #顾问账号登录获取token
    url = url_Login
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"mobile": "15800000002", "password": "111111", "code": ""}

    res = requests.post(url=url, headers=headers, data=data).json()
    token = res.get(u'data').get(u'user').get(u'token')
    return token


if __name__ == '__main__':
    unittest.main
