"""
def fun_A(x,y=3):
    return x*y
"""
print(list(map(lambda x:x*3,[1,2,3])))
#  print(list(map(lambda x,y: x * y, [1, 2, 3], [4, 5, 6])))
# # 输出: [4, 10, 18]
