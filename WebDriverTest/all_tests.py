#coding=utf-8
'''
Created on 2017-6-14
@author: 灵枢
Project:通过测试套件执行多个测试用例，并生成报告
'''
import HTMLTestRunnerCN
import unittest
import os,time


listaa = "F:\\pages\\index\\WebDriverTest"
def createsuite1():
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(listaa,pattern='start_*.py',top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit

now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
filename="F:\\pages\\index\\report\\"+now+"_result.html"
fp=open(filename,'wb')

runner=HTMLTestRunnerCN.HTMLTestReportCN(
    stream=fp,
    title=u'搜索功能测试报告',
    description=u'用例执行情况：')

runner.run(createsuite1())

#关闭文件流，不关的话生成的报告是空的
fp.close()