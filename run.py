import unittest  # 导入单元测试框架
from 接口自动化框架.ulit.HTMLTestReportCN import HTMLTestRunner
from 接口自动化框架.ulit.ulit import get_time,CASEPATH,REPORTPATH
dt = get_time()  # 获取时间
# discover()方法，用于加载指定目录下所有以test开头的用例文件中的测试用例
tests = unittest.defaultTestLoader.discover(CASEPATH)
f = open(REPORTPATH+'/'+dt + '.html', 'wb')  # 已二进制写的方式打开文件test_result.html
runner = HTMLTestRunner(stream=f, title='接口自动化测试报告', tester='刘')
runner.run(tests)   # 执行测试
f.close()