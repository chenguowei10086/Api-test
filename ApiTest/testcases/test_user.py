import pytest
import requests

from common.request_util import RequestUtil
from common.yaml_util import write_yaml, read_yaml
import re
class TestUser:
    csrf_token = ""
    sess = requests.session()
    # 访问首页接口

    def test_start(self):

        url = "http://47.107.116.139/phpwind/"
        # res = requests.request(method="get", url=url)
        res = RequestUtil().send_request(method="get", url=url)
        print(res.text)
        # 正则提取
        obj = re.search('name="csrf_token" value="(.*?)"', res.text)
        write_yaml({"csrf_token":obj.group(1)})
        # print(obj.group(1))
        # 提取cookie


    # 登录接口
    def test_login(self):

        url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
        data = {
            "username": "admim",
            "password": "admim123",
            "csrf_token": read_yaml("csrf_token"),
            "backurl": "http://47.107.116.139/phpwind/",
            "invite": ""
        }
        header ={
            "Accept": "application/json, text/javascript, /; q=0.01",
            "X-Requested-With": "XMLHttpRequest"
        }

        # res=requests.request(method="post",url=url,data=data,header=header,cookies=TestRequest.php_cookie)
        res=RequestUtil().send_request(method="post",url=url,datas=data,headers=header)
        # res=TestUser.sess.request(method="post",url=url,data=data,headers=header)
        print("---")
        print(res.json())
if __name__ == '__main__':
    pytest.main([])
    # TestRequest().test_login()