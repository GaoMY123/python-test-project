## 将以下两个字典进行合并到一起【注：不使用字典的update方法】

# d1 = {"name": "wj", "age": 22}
# d2 = {"male": "famle"}
def main():
    d1={
        "name":"wj",
        "age":"22"
    }
    d2={
        "male":"famle"
    }
    d3={}
    for key in d1:
        d3[key]=d1[key]
    for key in d2:
        d3[key]=d2[key]
    print(d3)
if __name__=="__main__":
    main()

