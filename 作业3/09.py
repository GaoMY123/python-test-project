# 9. 将以下匿名函数转成标准函数

"""
lambda x:x if x%2 == 0 else None
"""
def demo(x):
    if x%2==0:
        return x
    else:
        return None
demo(4)
print(demo(4))
