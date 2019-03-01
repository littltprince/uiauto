#! /user/bin/evn python
# coding:utf-8

import sys
import os
import unittest
import requests
import json
sys.path.append(os.path.abspath('%s../../' % sys.path[0]))

#测试环境
host = "http://dmpadmin.zhuge.com"
#header = ""
#header = "Content-Type":"application/x-www-form-urlencoded"
root_user = ""
root_password = ""
management_user = ""
management_password = ""
counselor_user = ""
counselor_password = ""

#线上环境
#host = ""