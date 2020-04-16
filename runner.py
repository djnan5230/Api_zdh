import unittest
import time
import os
import logging
import HTMLTestRunner


# 获取项目的路径
test_dir = os.path.join(os.getcwd())
print(test_dir)


# 自动搜索项目根目录下的所有case，构造测试集；返回TestSuite对象
discover = unittest.defaultTestLoader.discover(test_dir,pattern ='test_*.py')

now = time.strftime('%Y-%m-%d %H_%M_%S') # 获取当前时间
result = test_dir + '/log/'+now+'_result.html' # 报告的完整路径
print(result)
log = test_dir+'/log/'+now+'_log.txt'  #日志的完整路径

logging.basicConfig(filename=log,level=logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s') #filename 日志文件路径 level 日志的级别 format 格式

fp = open(result, 'wb')  # wb方式写入
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='aguest_master项目用例执行情况',verbosity=2)  #构造runner

# 使用run()方法运行测试套件（即运行测试套件中的所有用例）
runner.run(discover)