#JSON是一种用于存储和交换数据的语法
#可以导入一个内置的包来处理JSON的数据
import json
#解析JSON，将JSON转换为Python
#json.loads()
#JSON转PYthon,支持的数据类型为字符串、数字、布尔值、空值、列表、元组、字典
x='{"name":"张三","age":30,"city":"北京"}'
y=json.loads(x)
print(y["name"])
#Python转换为JSON，使用json.dumps()，将其转换为JSON字符串
#python转JSON
x={
    "name":"张三",
    "age":30,
    "city":"北京"
}
y=json.dumps(x)
print(y)
#可以将字典、列表、元组、字符串、int、浮点、True、False、None转换为JSON字符串
print(json.dumps({"name":"张三","age":18}))
print(json.dumps(["apple","bananas"]))
print(json.dumps(("apple","bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
#将Python转换为JSON时，Python对象将被转换为JSON的等效对象
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))
print(type(x))
#可以使用indent参数来定义缩进次数
#可以使用separators()参数更改默认分隔符
#可以使用sort_keys参数指定结果是否应该排序