# 有字符串 mStr = "各个国家有各个国家的国歌"，找出该字符串中所有重复的字或者词
def main():
    mStr="个各国家有各个国家的国歌"
    d=[]
    '''
    mStr = "各个国家有各个国家的国歌"
list=[]
for i in range(len(mStr)): #i控制每次的字数，j来进行切片
    for j in range(len(mStr)-i): #词（i） i是0,1,2,3
        count = mStr.count(mStr[j:j+(i+1)])
        if count>1 and mStr[j:j+(i+1)] not in list:
            list.append(mStr[j:j+(i+1)])
print(list)
    '''
    # for i in mStr:
    #     if mStr.count(i)>1:
    #         d[i]=mStr.count(i)
    # print(d.keys())
    #统计字符串中的重复的词出现的位置
    #切片字符串
    for i in range(len(mStr)):#控制切片的起始位置
        for j in range(i+1,len(mStr)+1):#控制切片的结束位置
            #然后将切片后的字符串与原字符串进行比较
            if mStr.count(mStr[i:j])>1:
                if mStr[i:j] not in d:
                    d.append(mStr[i:j])
    print(d)
if __name__=="__main__":
    main()

