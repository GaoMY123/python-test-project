#完成一个学生管理系统定义一个字典，用于保存所有的学生信息
from re import match
import json
import os
from time import sleep
student_dict={}
DATA_FILE=os.path.join(os.path.dirname(os.path.abspath(__file__)),"students.json")
#定义一个函数，用于整数的输入，如果输入的不是整数，或者是不在指定范围内，提示用户重新输入
def input_int(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("输入不是整数，请重新输入")
            continue
        if (min_value is None or value >= min_value) and (max_value is None or value <= max_value):
            return value
        print("输入无效，请重新输入")
#JSON文件的写入
def save_data():
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(student_dict, f, ensure_ascii=False, indent=2)
    except OSError as e:
        print("保存学生信息失败：", e)
#JSON文件的读取
def load_data():
    global student_dict
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            student_dict = json.load(f)
    except FileNotFoundError:
        student_dict = {}
    except (json.JSONDecodeError, OSError) as e:
        print("读取学生信息失败：", e)
        student_dict = {}

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
    s=input_int("请输入您的选择：",1,6)
    return s

#添加学生信息
def add_student():
    print("----添加学生信息----")
    while True:
        name=input("请输入学生姓名：").strip()
        if match(r"[\u4e00-\u9fa5]+\Z", name):
            break
        print("姓名输入错误")
        print("请重新输入")
    age=input_int("请输入学生的年龄：",0,120)
    while True:
        cla=input("请输入学生的班级：").strip()
        if match(r"[a-zA-Z0-9\u4e00-\u9fa5]+\Z", cla):
            break
        print("班级输入错误")
        print("请重新输入")
    while True:
        stuNo=input("请输入学生的学号：").strip()
        if not stuNo:
            print("学号不能为空")
            print("请重新输入")
        elif stuNo in student_dict:
            print("该学号已存在")
            print("请重新输入")
        else:
            break
    student_dict[stuNo]={"name":name,"age":age,"cla":cla,"stuNo":stuNo}
    save_data()
    print("添加成功")

#删除学生信息
def del_student():
    print("----删除学生信息----")
    if not student_dict:
        print("当前没有学生信息")
        return
    while True:
        stuNO=input("请输入要删除的学生学号：").strip()
        if not stuNO:
            print("已取消删除")
            return
        if stuNO in student_dict:
            del student_dict[stuNO]
            save_data()
            print("删除成功")
            return
        print("该学号不存在，请重新输入")

# 修改学生信息
def mof_student():
    print("----修改学生信息----")
    if not student_dict:
        print("当前没有学生信息")
        return
    while True:
        stuNO = input("请输入要修改的学生学号：").strip()
        if not stuNO:
            print("已取消修改")
            return
        if stuNO in student_dict:
            break
        print("该学号不存在")
    print(student_dict[stuNO])
    print("请输入新的学生信息")
    while True:
        name = input("请输入新的学生姓名：").strip()
        if match(r"[\u4e00-\u9fa5]+\Z", name):
            break
        print("姓名输入错误")
        print("请重新输入")
    age = input_int("请输入新的学生年龄：",0,120)
    while True:
        cla = input("请输入新的学生班级：").strip()
        if match(r"[a-zA-Z0-9\u4e00-\u9fa5]+\Z", cla):
            break
        print("班级输入错误")
        print("请重新输入")
    while True:
        stuNo = input("请输入新的学生学号：").strip()
        if not stuNo:
            print("学号不能为空")
            print("请重新输入")
        elif stuNo in student_dict and stuNo != stuNO:
            print("该学号已存在")
            print("请重新输入")
        else:
            break
    del student_dict[stuNO]
    student_dict[stuNo] = {"name": name, "age": age, "cla": cla, "stuNo": stuNo}
    save_data()
    print("修改成功")

# 查找学生信息
def find_student():
    print("----查找学生信息----")
    while True:
        stuNo=input("请输入要查找的学号：").strip()
        if not stuNo:
            print("已取消查找")
            return
        if stuNo in student_dict:
            print(student_dict[stuNo])
            return
        print("该学号不存在")



# 显示所有学生信息
def show_all_student():
    if not student_dict:
        print("当前没有学生信息")
        return
    print("学号\t姓名\t年龄\t班级")
    for i in student_dict:
        print(student_dict[i]["stuNo"],student_dict[i]["name"],student_dict[i]["age"],student_dict[i]["cla"],sep="\t")
#退出系统
def exit_system():
    save_data()
    print("谢谢使用")

def main():
    load_data()
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
