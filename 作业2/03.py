#3.有字典 d = {"name": "张三", "age": 18}，如何将 age 及其对应的值从字典中移除
def main():
    d={
        "name":"张三",
        "age":"18"
    }
    d.pop("age")
    print(d)
if __name__=="__main__":
    main()
