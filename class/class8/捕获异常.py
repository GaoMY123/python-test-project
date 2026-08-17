# try:
#     尝试要捕获的代码
# except:
#     出现异常时的补救代码
#捕获指定类型的异常
li=['a','b','c']
try:
    print(li[10])
    print(li[1])#不会执行
except IndexError:
    print('索引超出范围')
print(li[0])
#捕获多个异常,多个异常之间分开处理
try:
    print(li[10])
except IndexError:
    print('索引超出范围')
except ZeroDivisionError:
    print('除数不能为0')
#多个异常统一处理
try:
    print(li[10])
except (IndexError,ZeroDivisionError):
    print('索引超出范围或除数不能为0')
#捕获未知类型的异常
try:
    print(li[10])
except Exception as e:
    print(e)
#else:没有异常时输出的代码
else:
    print('没有异常')
#finally:无论是否有异常，都会输出的代码
finally:
    print('finally')
'''
try:
    尝试捕获的代码
except:
    出现异常是的补救代码
——————捕获指定类型的异常——————
except 指定类型的异常：
    出现指定类型的异常时的补救代码
——————多个异常分开处理——————
except 异常1：
    出现异常1时的补救代码
except 异常2：
    出现异常2时的补救代码
——————多个异常统一处理——————
except(异常1，异常2)：
    出现异常1或异常2时的补救代码
——————捕获未知类型的异常——————
except Exception as e:
    print(e)
else:
    没有异常时输出的代码
finally:
    无论是否有异常，都会输出的代码
'''

















