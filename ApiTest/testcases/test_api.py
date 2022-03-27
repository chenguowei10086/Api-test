import pytest
import json


# fixture 用于在部分用例之前和之后执行数据库操作
from common.request_util import RequestUtil
from common.yaml_util import write_yaml, read_yaml, read_testcase


class TestRequest:
    # 全局变量调用


    def setup_class(self):
        print('在每一个类执行前的初始化的工作：创建日志对象，创建数据库对象')

    def setup(self):
        print('\n在执行测试用例之前初始化的代码：打开浏览器')

    def teardown(self):
        print('\n在执行测试用例之后：关闭浏览器')

    def teardown_class(self):
        print('在每一个类执行完了的销毁工作：销毁日志对象，销毁数据库对象')

    @pytest.mark.smoke
    @pytest.mark.parametrize("args_name",read_testcase('testcases/get_token.yaml'))
    # get请求:获取接口统一鉴权码token接口
    def test_get_token(self,args_name):
        # print(args_name)
        url =args_name['request'] ['url']
        data =args_name['request'] ['data']
        method =args_name['request']['method']

        res =RequestUtil().send_request(method=method,url=url,datas=data)
        print(res.json())#返回值转化成dict对象
        write_yaml({"access_token":res.json()['access_token']})#登录状态
        # print(res.text)#返回成文本
        # print(res.content)#字节数据
        # print(res.reason)
#         print(res.cookies)
        # print(res.encoding)
        # print(res.headers)
    # url ="https://api.weixin.qq.com/cgi-bin/token"
    # # url ="https://api.tttt.one/rest-v2/todo"
    # params={
    #     "grant_type":"client_credential",
    #     "appid":"wx74a8627810cfa308",
    #     "secret":"e40a02f9d79a8097df497e6aaf93ab80"
    # }
    @pytest.mark.smoke
    @pytest.mark.parametrize("args_name", read_testcase('testcases/a.yaml'))
    # post请求:编辑标签接口
    def test_edit_flag(self,args_name):
        # print(args_name)
        url = args_name['request']['url']+read_yaml("access_token")
        data = args_name['request']['data']
        method = args_name['request']['method']
        # url ="https://api.weixin.qq.com/cgi-bin/tags/update?access_token= "+read_yaml("access_token")
        # data = {"tag":{"id":134,"name":"广东人"}}
        # str_data =json.dumps(data)
        res = RequestUtil().send_request(method=method,url=url,datas=data)
        print(res.json())

    # 文件上传
    def test_file_upload(self):
        url = "https://api.weixin.qg.com/cgi-bin/media/uploadimg?access_token=" + read_yaml("access_token")
        data = {
            "media": open(r"E:\shu.png", "rb")
        }
        res = RequestUtil().send_request(method="post", url=url, datas=data)
        print(res.json())

if __name__ == '__main__':
    pytest.main([])
