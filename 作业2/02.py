#2.有字典 d = {"name": "张三", "age": 18}，如何将 name 对应的值改成张三三？
def main():
    d={
        "name":"张三",
        "age":"18"
    }
    d["name"]="张三三"
    print(d)
if __name__=="__main__":
    main()
