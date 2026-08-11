#python中的日期不是一个独立的数据类型，但是可以导入一个datetime的模块来将日期作为如期对象来进行操作
import datetime
x=datetime.datetime.now()
print(x)
#日期的输出:：
print(x.year)
print(x.strftime("%Y-%M-%d-%A"))
z=datetime.datetime(2026,8,8)
print(z)
#strftime()方法可以将日期格式化为指定的字符串格式
print(z.strftime("%Y-%M-%d-%A"))
