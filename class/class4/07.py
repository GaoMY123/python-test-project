#完成一个学生管理系统
#定义一个空字典来保存数据
from time import sleep

from numpy.random.mtrand import choice

stu_dict={}
#定义一个界面
def menu():
    print("-"*10)
    print("学生管理系统")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.查找学生信息")
    print("5.显示所有学生信息")
    print("6.退出系统")
    print("-" * 10)
    a=int(input("请输入您的选择："))
    if a in range(1,7):
        return a
    else:
        print("您的选择有误，请重新输入")
        return menu()


#添加学生数据
def add_student():
    n=input("请输入学生的学号")
    if n in stu_dict:
        print("该学号已存在")
        print("请重新输入")
        return add_student()
    else:
        name=input("请输入学生姓名：")
        age=input("请输入学生的年龄：")
        cl=input("请输入学生的班级：")
        stu_dict[n]={"name":name,"age":age,"cl":cl,"n":n}
        print("添加成功")

# 删除数据
def del_student():
    n=input("请输入学生的学号")
    if n in stu_dict:
        del stu_dict[n]
        print("删除成功")
        return
    else:
        print("该学号不存在，请重新输入")
        return
# 修改学生信息
def gr_student():
    no=input("请输入要修改的学生学号：")
    if no in stu_dict:
        print(stu_dict[no])
        print("请输入新的学生信息")
        name=input("请输入新的名字：")
        age=input("请输入新的年龄：")
        cl=input("请输入新的班级")
        no=input("请输入新的学号")
        del stu_dict[no]
        stu_dict[no]={"name":name,"age":age,"cl":cl,"no":no}
#查找学生信息
def find_student():
    no=input("请输入要查找的学号")
    if no in stu_dict:
        print("姓名\t年龄\t班级\t学号")
        print(stu_dict[no]['name'],stu_dict[no]['age'],stu_dict[no]['cl'],stu_dict[no]['no'])
    else:
        print("该学号不存在")
#查看全部的学生信息
def show_student():
    if len(stu_dict)>0:
        print("姓名\t年龄\t班级\t学号")
        for i in stu_dict:
            print(stu_dict[i]['name'],stu_dict[i]['age'],stu_dict[i]['cla'],stu_dict[i]['no'])
#退出系统
def exit_system():
    print('谢谢使用')
def main():
    while True:
        choice=menu()
        if choice ==1:
            add_student()
        elif choice==2:
            del_student()
        elif choice==3:
            gr_student()
        elif choice==4:
            find_student()
        elif choice==5:
            show_student()
        elif choice==6:
            exit_system()
            print("正在退出...")
            sleep(3)
            break
if __name__=="__main__":
        main()