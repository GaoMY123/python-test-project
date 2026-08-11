#完成一个学生管理系统定义一个字典，用于保存所有的学生信息
from re import match
from time import sleep
student_dict={}
#主菜单
def menu():
    print("-"*10)
    print("学生管理系统")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.查找学生信息")
    print("5.显示所有学生信息")
    print("6.退出系统")
    print("-"*10)
    s=int(input("请输入您的选择："))
    if s in range(1,7):
        return s
    else:
        print("您的选择有误,请重新输入")
        return menu()
    #retutn s if s in range(1,7) else print("您的输入有误"),menu()

#添加学生信息
def add_student():
    print("----添加学生信息----")
    name=input("请输入学生姓名：")
    if not match(r"[\u4e00-\u9fa5]+",name):
        print("姓名输入错误")
        print("请重新输入")
        return add_student()
    age=int(input("请输入学生的年龄："))
    if age<0 or age>120:
        print("年龄输入错误")
        print("请重新输入")
        return add_student()
    cla=input("请输入学生的班级：")
    if not match(r"[a-zA-Z0-9]",cla):
        print("班级输入错误")
        print("请重新输入")
        return add_student()
    stuNo=input("请输入学生的学号：")
    if stuNo in student_dict:
        print("该学号已存在")
        print("请重新输入")
        return add_student()
    else:
        student_dict[stuNo]={"name":name,"age":age,"cla":cla,"stuNo":stuNo}
        print("添加成功")

#删除学生信息
def del_student():
    print("----删除学生信息----")
    if not student_dict:
        print("当前没有学生信息")
        return
    stuNO=input("请输入要删除的学生学号：")
    if stuNO in student_dict:
        del student_dict[stuNO]
        print("删除成功")
    else:
        print("该学号不存在，请重新输入")
# 修改学生信息
def mof_student():
    print("----修改学生信息----")
    if not student_dict:
        print("当前没有学生信息")
        return
    stuNO = input("请输入要修改的学生学号：")
    if stuNO in student_dict:
        print(student_dict[stuNO])#这是一个字典，不能直接打印，需要通过键来访问值
        print("请输入新的学生信息")
        name = input("请输入新的学生姓名：")
        age = int(input("请输入新的学生年龄："))
        cla = input("请输入新的学生班级：")
        stuNo = input("请输入新的学生学号：")
        del student_dict[stuNO]
        student_dict[stuNo] = {"name": name, "age": age, "cla": cla, "stuNo": stuNo}
        print("修改成功")
    else:
        print("该学号不存在")
# 查找学生信息
def find_student():
    print("----查找学生信息----")
    stuNo=input("请输入要查找的学号：")
    if stuNo in student_dict:
        print("姓名\t年龄\t班级\t学号")
        print(student_dict[stuNo]['name'],student_dict[stuNo]['age'],student_dict[stuNo]['cla'],student_dict[stuNo]['stuNo'])
    else:
        print("该学号不存在")



# 显示所有学生信息
def show_all_student():
    if len(student_dict)>0:
        print("姓名\t年龄\t班级\t学号")
        for i in student_dict:
            print(student_dict[i]["name"],student_dict[i]["age"],student_dict[i]["cla"],student_dict[i]["stuNo"])
    else:
        print("当前没有学生信息")
#退出系统
def exit_system():
    print("谢谢使用")

def main():
    while True:
        choice = menu()
        if choice == 1:
            add_student()
        elif choice == 2:
            del_student()
        elif choice == 3:
            mof_student()
        elif choice == 4:
            find_student()
        elif choice == 5:
            show_all_student()
        elif choice == 6:
            exit_system()
            print("正在退出...")
            sleep(3)
            break
if __name__ == "__main__":
    main()