#! /user/bin/evn python
# coding:utf-8

import inspect
import unittest
import time
from common import HTMLTestRunner_PY3
import sys
import os
from testCase.testLogin import Login
from testCase.testRefreshToken import RefreshToken
from testCase.testResetPassword import ResetPassword
from testCase.testSupervisorAuthItems import SupervisorAuthItems
sys.path.append(os.path.abspath('%s../../' % sys.path[0]))

def output():

    suite = unittest.TestSuite()  # 集成unittest运行套件
    testClassList = [Login,RefreshToken,ResetPassword,SupervisorAuthItems]

    for eachClass in testClassList:     # 遍历测试类内包含关键字的函数
        ins_class = inspect.getmembers(eachClass, predicate=inspect.isfunction)
        #ClassName = ([x[0] for x in ins_class if x[0].find('normal') != -1])
        ClassName = ([x[0] for x in ins_class if x[0].find('test') != -1])
        for eachName in ClassName:    # 将符合条件的函数添加到测试用例之内
            suite.addTest(eachClass(eachName))

    # 测试报告文件夹名称
    fileSearch = 'RunAllCase-' + time.strftime('%Y-%m', time.localtime(time.time()))
    # fileSearch = 'RunAllCase-'+ '2017-04'
    #print(fileSearch)
    # 测试报告文件时间后缀
    fileSuffix = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    #print(fileSuffix)
    # 测试报告文件的完整路径
    filePath = os.path.abspath('%s../../TestReport' % sys.path[0] + '/' + fileSearch + '/RunAllCaseResult_' + fileSuffix + '.html')

    try:
        fp = open(filePath, 'w',encoding='utf-8') #定义测试报告的标题和内容参数，并存储到相应位置
        # 使用HTMLTestRunner的框架输出报告
        runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=fp, title=u'聚享云接口测试报告',description=u'测试用例执行结果：')
        result = runner.run(suite)
        print(result)
        logfile = open(r'runLog.txt', 'a')
        logfile.write('\n%s' % str(result) + time.strftime(' %Y-%m-%d %H:%M:%S', time.localtime(time.time()))) #运行记录写日志
        logfile.close()

        if (result.failure_count or result.error_count):#控制台输出，只要遇到错误和断言失败，均认为本次测试总结果是失败的
            print('Not pass')
        else:
            print('pass') #全部通过视为通过
    except IOError:
        #print()
        print(os.makedirs(os.path.abspath('%s../../TestReport' % sys.path[0] + '/' + fileSearch))) #发现存储目标文件夹不存在，则创建
        output()


output()


