#-*- coding:utf-8 -*-

import requests
import unittest

class demo(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_01(self):
        test_limit= [11,30,100,300]
        url = "http://tech.bidinghuo.cn/wapi/statistics/rank.json"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'Content-Type': "application/x-www-form-urlencoded",
            'Cookie': "Hm_lvt_05675c012364ae735418a432fd3f32fb=1521770515; PHPSESSID=b32df9dc308fb291e9ce1fa1c855dc76; laravel_session=T3EPdjSZcJs87TwhJksKxLlFx5Xp6J1NeIkF9S1m",
            'Cache-Control': "no-cache",
            'Postman-Token': "c21cc760-5b41-49b6-922c-199e18d691e8"
            }

        for limit in test_limit:
            payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"attributes\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"limit\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"sort\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"type\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"offset\"\r\n\r\n0\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"%limit
            response = requests.request("POST", url, data=payload, headers=headers)
            self.assertEqual(response.status_code,200,'返回状态为200')
            data = response.json()['data']
            if response.json()['data']:
                self.assertEqual(len(data),limit,str(len(data))+':'+str(limit)+',返回数据大小与请求不一致')





    def test_02(self):
        url = "https://www.bidinghuo.cn/api/backend/login.json"
        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\n潘益芳\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\npyf123456\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'Content-Type': "application/json",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
            'Authorization': "Basic WMqzOnB5ZjEyMzQ1Ng==",
            'Cache-Control': "no-cache",
            'Postman-Token': "cad7bd34-17ae-4b7d-8374-b6ea0883baf8"
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)