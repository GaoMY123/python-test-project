#冒泡排序思想：重复"遍历"待排序序列，一次比较两个相邻元素，如果它们的顺序错误就把它们交换过来。
# 每一轮遍历都会将当前未排序部分的最大（或最小）元素冒泡到正确位置。
li=[9,5,4,6,1]
#两两比较，将较大的数冒泡到后面
for i in range(len(li)-1):#控制冒泡的次数
    swap = False
    for j in range(len(li)-1-i):#控制冒泡的范围
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
            print(li)
            swap = True
            print("交换了")
            print(li)
    if swap == False:
        print("没有交换")
        print(li)
        print("排序完成")
        break
# 时间复杂度：O(n^2)
# 空间复杂度：O(1)
#时间复杂度：是指算法执行的时间
#空间复杂度：是指算法执行时占用的内存空间
# for i in range(len(li)-1):
#     swap = False
#     for j in range(len(li)-i-1):
#         if li[j]>li[j+1]:
#             li[j],li[j+1]=li[j+1],li[j]
#             print(li)
#             swap = True
#     if not swap:
#         break
