# list = []
# list.append() # 添加元素
# list.insert() # 插入元素
# [] + []
# [x for x in range(10)]
# list(range(10))

import timeit


# 尾部添加元素
def function_1():
    list = []
    for i in range(10):
        list.append(i)


def function_2():
    list = []
    for i in range(10):
        list = list + [i]


def function_3():
    list = [i for i in range(10)]


def function_4():
    li = list(range(10))


# 头部添加元素
def function_5():
    li = []
    for i in range(10):
        li.insert(0, i) # 0 为指定位置


time_1 = timeit.Timer("function_1()", "from __main__ import function_1")
time_2 = timeit.Timer("function_2()", "from __main__ import function_2")
time_3 = timeit.Timer("function_3()", "from __main__ import function_3")
time_4 = timeit.Timer("function_4()", "from __main__ import function_4")
time_5 = timeit.Timer("function_5()", "from __main__ import function_5")

# 测试效率问题
print("append:%f" % time_1.timeit(number=100))
print("[]+[]:%f" % time_2.timeit(number=100))
print("[i for]:%f" % time_3.timeit(number=100))
print("list():%f" % time_4.timeit(number=100))
print("insert:%f" % time_5.timeit(number=100))

# if __name__ == '__main__':