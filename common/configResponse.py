import requests
import os
import json
import warnings


class Runmain(object):


    headers = {"Content-Type": "application/json"}

    #封装post方法
    def send_post(self,url,data,headers):
        warnings.simplefilter('ignore',ResourceWarning)
        response = requests.post(url=url,data=data,headers=headers)
        return response.json()

    #封装get方法
    def send_get(self,url,data,headers):
        warnings.simplefilter('ignore',ResourceWarning)
        response = requests.post(url=url,data=data,headers=headers)
        return response.json()
    #平时用这个方法请求接口，resources目录下为接口API信息
    def run_main(self,TestApi,data,headers=headers):
        warnings.simplefilter('ignore',ResourceWarning)

        test_dir = os.path.abspath(os.path.dirname(os.getcwd()))
        # 获取resources文件夹绝对路径
        TestApiPath = test_dir + '/resources/'
        # 根据方法传入的文件名称获取内容
        TestApiData = open(os.path.join(TestApiPath, TestApi))
        Apidata = json.load(TestApiData)
        apiPath = Apidata["test"]["protocol"] + '://' + Apidata['test']['host'] + Apidata['test']['path']
        apiMethod = Apidata['test']['method'].upper()

        if apiMethod == 'GET':
            response = requests.get(url=apiPath,data=data,headers=headers)
        else:
            response = requests.post(url=apiPath,data=data,headers=headers)
        return response.json()


