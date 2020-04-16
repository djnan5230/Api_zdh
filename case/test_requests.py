#coding:utf-8
import unittest
import requests
import json


class BaseInfo_grade (unittest.TestCase):

    def setUp(self) -> None:
        pass


    def test_a(self):
        url_1 = ''

        data_1 = {

                "dateTime": "2020-4-11",
                "gradeId": "1",
                "areaCode": "010",
                "pageNo": 1,
                "pageSize": 10
                }
        data = json.dumps(data_1)

        now_header = {

        }
        print(type(data))
        r = requests.post(url=url_1,data=data,headers = now_header)

        print(r.url)
        print(r.text)
        print(r.json()["error_code"])

        x = r.json()["error_code"]
        self.assertEqual(r.status_code,0)
        self.assertEqual(x,'0')








if __name__ == "__main__":
    unittest.main()

