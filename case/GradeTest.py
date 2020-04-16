# -*- coding:utf-8 -*-
import requests
import unittest
import json
from common.configResponse import Runmain
import warnings


class BaseInfo_grade (unittest.TestCase):

    header_data = {
        "checkSum": "8c3b5214aa3f8d0d2bdb216dfe3b4a2c",
        "aid": "wx070844b9f4056167",
        "25Wq5VWY": "qFqjgs3hzP-3WVcvnjZZKbnF95OQ",
        'Content-Type': 'application/json'
    }

    def test_a(self):

        data = {
                "dateTime": "2020-4-11",
                "gradeId": "1",
                "areaCode": "010",
                "pageNo": 1,
                "pageSize": 10
                }
        data_1 = json.dumps(data)

        response = Runmain().run_main(TestApi='GradeTestApi.json', data=data_1, headers=BaseInfo_grade.header_data)
        print(response)
        self.assertEqual(response['error_code'],'0')


    # def test_b(self):
    #
    #     r = requests.post(url=BaseInfo_grade.url_1, data=BaseInfo_grade.data_1, headers=BaseInfo_grade.now_header)
    #
    #     print(r.url)
    #     print(r.json()["error_code"])
    #
    #     x = r.json()["error_code"]
    #     self.assertEqual(r.status_code,"200")
    #     self.assertEqual(x,'1')





if __name__ == "__main__":
    unittest.main()