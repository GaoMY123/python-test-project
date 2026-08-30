import unittest
import requests
from ddt import ddt,data
@ddt
class TestComment(unittest.TestCase):
    # def setUp(self,):
    #     self.header={"Content-Type":"application/json"}
    #     self.cookie={"session":"e62c3598-7055-4302-998b-a2de82e9a3e8.o4--mAFLmSWy0Q8O0CwU6hYayCk"}
    @data("悲秋","伤春"," __ ")
    def test_case1(self,text):
        """
        评论中文
        :return:
        """
        header={"Content-Type":"application/json"}
        date=('{"news_id":200,"comment":"%s"}' % text).encode("utf-8")
        cookie={"session":"e62c3598-7055-4302-998b-a2de82e9a3e8.o4--mAFLmSWy0Q8O0CwU6hYayCk"}
        response=requests.post("http://info.ybbms.com/news/news_comment",headers=header,data=date,cookies=cookie)
        assert response.json()["errno"]=="0" and response.json()["errmsg"]=="OK" and response.json()["data"]["content"]== text

    # def test_case2(self):
    #     """
    #     评论英文
    #     :return:
    #     """
    #     # header={"Content-Type":"application/json"}
    #     date='{"news_id":200,"comment":"This is a comment"}'.encode("utf-8")
    #     # cookie = {"session": "e62c3598-7055-4302-998b-a2de82e9a3e8.o4--mAFLmSWy0Q8O0CwU6hYayCk"}
    #     response = requests.post("http://info.ybbms.com/news/news_comment", headers=self.header, data=date, cookies=self.cookie)
    #     assert response.json()["errno"]=="0" and response.json()["errmsg"]=="OK"  and response.json()["data"]["content"]=="This is a comment"
    # def test_case3(self):
    #     """
    #     评论特殊字符
    #     :return:
    #     """
    #     # header={"Content-Type":"application/json"}
    #     date='{"news_id":200,"comment":"！！"}'.encode("utf-8")
    #     # cookie = {"session": "e62c3598-7055-4302-998b-a2de82e9a3e8.o4--mAFLmSWy0Q8O0CwU6hYayCk"}
    #     response = requests.post("http://info.ybbms.com/news/news_comment", headers=self.header, data=date, cookies=self.cookie)
    #     assert response.json()["errno"]=="0" and response.json()["errmsg"]=="OK" and response.json()["data"]["content"]=="！！"
