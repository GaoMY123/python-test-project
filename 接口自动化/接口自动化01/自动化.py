#导包
import requests

#发送请求
# response=requests.get("https://www.baidu.com/")
#
# #修改编码格式
# response.encoding="utf-8"
#
#
# #打印响应
# print(response)
# #<Response [200]> 表示的是请求成功
# #发送完毕请求之后，响应头、响应体、响应状态码是分开存放的
# #打印响应头，响应头里是一个字典，可以使用键值对的方式获取到响应头里的值
# print(response.headers)
# print(response.headers["Cache-Control"])
# #打印响应体
# print(response.text)
# #打印状态码
# print(response.status_code)
# #打印编码格式
# print(response.encoding)
#
# print(type(response.text))
#
#
# print(response.json())
# response=requests.get("http://info.ybbms.com/news_list?cid=1&page=1")

#将json转为python对象,换行打印
# print(response.json()["data"])
# print(response.json()["data"])

#超时
# response=requests.get("https://www.baidu.com/",timeout=10)
# print(response.text)

#下载文件


# response=requests.get("https://img2.baidu.com/it/u=262673177,4128172311&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=929")
# #打印的是图片的二进制数据
# print(response.content)
#
# with open("img.jpg","wb") as f:
#     f.write(response.content)

#获取参数
# response=requests.get("http://info.ybbms.com/news/json/200")
# print(response.json())
# #query参数
# # response=requests.get("http://info.ybbms.com/news_list?cid=1&page=1")方式一
# #方式二
# data={"cid":1,"page":1}
# response=requests.get("http://info.ybbms.com/news_list",params=data)
# print(response.json())
#form参数
# data={"mobile":"15133715209","password":"123456"}
# response=requests.post("http://info.ybbms.com/passport/login",data=data)
# print(response.json())
#添加header、cookie、纯文本请求体
# header={"Content-Type":"application/json"}
# data='{"news_id":"200","comment":"我是李少琛"}'.encode("utf-8")
# cookie={"session":"09a34841-2dd6-407f-a292-16d2053dfed7.b0jTA0uIFj6B2iGavO7_c8ii3k4"}
# response=requests.post("http://info.ybbms.com/news/news_comment",headers=header,data=data,cookies=cookie)
# print(response.json())

#form文件
# cookie={"session":"09a34841-2dd6-407f-a292-16d2053dfed7.b0jTA0uIFj6B2iGavO7_c8ii3k4"}
# with open("img.jpg","rb") as f:
#     files={"avatar": f}
#     response=requests.post("http://info.ybbms.com/user/pic_info",files=files,cookies=cookie)
#     print(response.json())

#接口关联
#评论
# header={"Content-Type":"application/json"}
# data='{"news_id":"200","comment":"我是李少琛"}'.encode("utf-8")
# cookie={"session":"09a34841-2dd6-407f-a292-16d2053dfed7.b0jTA0uIFj6B2iGavO7_c8ii3k4"}
# response=requests.post("http://info.ybbms.com/news/news_comment",headers=header,data=data,cookies=cookie)
# print(response.json())
# comment_id=response.json()["data"]["id"]
# print(comment_id)
#
#
# #点赞
# # header={"Content-Type":"application/json"}
# date ='{"comment_id": %s,"action": "add"}' % comment_id #格式化字符串，将comment_id插入到字符串中
# # cookie={"session":"09a34841-2dd6-407f-a292-16d2053dfed7.b0jTA0uIFj6B2iGavO7_c8ii3k4"}
# response=requests.post("http://info.ybbms.com/news/comment_like",headers=header,data=date,cookies=cookie)
# print(response.json())
