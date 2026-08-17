#__all__用来约束当时用#from 模块名 import * 时可以使用哪些内容（不写能用全部）
#import 模块名
#用法：模块名，全局变量、函数、类名
#from 模块名 import 全局变量、函数、类名
#用法：全局变量，函数，类名
#from 模块名 import *
#用法：全局变量、函数、类名



# import itfeat
# print(itfeat.age)
# print(itfeat.demo())
# import keyword
# print(keyword.kwlist)
# import random
# print(random.randint(1,10))
# import os
# os.rename()
# import copy
# copy.copy()
# from time import sleep
# sleep(1)
# from itfeat import age
# print(age)
# from functools import reduce
# reduce()
from itfeat import *
print(age)
print(demo())
