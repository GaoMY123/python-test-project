# 有列表li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]，求编写代码求出值中出现1的元素的个数

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# count = 0
# for num in li:
#     if "1" in str(num):   # 把每个元素单独转成字符串来判断
#         count += 1
# print(count)  # 输出 6

count=len([i for i in li if "1" in str(i)])
print(count)  # 输出 6
