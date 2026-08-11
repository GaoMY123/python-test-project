
#提示用户在控制台输入一个天数，然后把天数折算成秒数，并在控制台输出。要求输出内容格式：xx天等于xx秒
def main():
    days=int(input("请输入一个天数："))
    minoutes=days*24*60*60
    print(days,"天等于",minoutes,"秒")

if __name__=="__main__":
     main()
