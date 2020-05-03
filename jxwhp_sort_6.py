#!/usr/bin/env python
# -*- encoding: UTF-8 -*- 
"""
#@File        : jxwhp_sort_6.py       
#@ide         : PyCharm
#@E-mail      : jxwhp@163.com
#@Modify time : 2020-05-02:20:59 
-------------------------------------------------
"""
from collections import deque
import operator

# 字符串的逆序输出
def func_chr_1(str):
    """
    ====chr逆序输向====
    传入的是字符串，字符串切片 [::-1]
    :param str:
    :return:
    """
    return str[::-1]
def func_chr_2(str):
    """
    ====chr逆序输出====
    利用列表方法 list.reverse()
    先将字符串转列表，列表逆序，再列表转字符串 ''.join(list)
    :param str:
    :return:
    """
    list_chr = list(str)
    list_chr.reverse()
    return ''.join(list_chr)
def func_chr_3(str):
    """
    ====chr逆序输出====
    1. 创建空列表
    2. 字符串迭代逆序输出  for i in range(len(str)-1,-1,-1)  **步长-1  遵循左闭右开原则  [] 含左不含右
    3. 列表转字符串 ''.join(list)
    :param str:
    :return:
    """
    #chr = '' # local --> enclosing --> global --> build-in   局部 --> 局部的局部 --> 全局 --> 内置函数
    list_chr = [] # local --> enclosing --> global --> build-in   局部 --> 局部的局部 --> 全局 --> 内置函数
    for i in range(len(str)-1,-1,-1):
        list_chr.append(str[i])
    # chr = ''.join(list_chr)
    # print(chr)
    return ''.join(list_chr)
def func_chr_4(str):
    """
    1. 利用内置函数reversed()逆序，sorted()对字符串逆向输出，生成迭代器
    :param str:
    :return:
    """
    chr = ''   # local --> enclosing --> global --> build-in   局部 --> 局部的局部 --> 全局 --> 内置函数
    for i in reversed(str):
        chr += i
    #print(chr)
    return chr
    # 以下迭代为排序
    #chr1 = ''
    # for j in sorted(chr,reverse=True):
    #     chr1 += j
    # print(chr1)
def func_chr_5(str):
    """
    import collections
    利用内置模块collections.deque.extendleft()方法，生成迭代对象
    :param str:
    :return:
    """
    #chr = '' # local --> enclosing --> global --> build-in   局部 --> 局部的局部 --> 全局 --> 内置函数
    deque_1 = deque(str)
    deque_2 = deque()
    for i in deque_1:
        deque_2.extendleft(i)
    # chr = ''.join(deque_2)
    # print(chr)
    return ''.join(deque_2)
def func_chr_6(str):
    """
    递归函数   如果字符串太长，不建议用递归，费内存
    :param str:
    :return:
    """
    if len(str) <= 1:
        return str
    #print(str[-1] + func_chr_6(str[:-1]))
    return str[-1] + func_chr_6(str[:-1])
def func_chr_7(str):
    """
    字符串转列表  **因字符串是不可变类型**
    利用数学交换原理：以中间为基准，交换对称位置的字符
    :param str:
    :return:
    """
    one_str_list = list(str)
    if len(one_str_list) == 0 or len(one_str_list) == 1:
        return one_str_list
    i = 0
    length = len(one_str_list)
    while i < length / 2:
        one_str_list[i], one_str_list[length - i - 1] = one_str_list[length - i - 1], one_str_list[i]
        i += 1
    return ''.join(one_str_list)

# 列表的逆序输出
def func_list_1(li):
    """
    列表直接切片 li[::-1]  -1 从列表的尾部输出
    :param li:
    :return:
    """
    return li[::-1]
def func_list_2(li):
    """
    利用列表的方法 list.reverse()直接逆序输出
    :param li:
    :return:
    """
    li.reverse()
    return li
def func_list_3(li):
    """
    利用内置函数 reversed()直接逆序输出
    :param list:
    :return:
    """
    list_1 = []
    for i in reversed(li):
       list_1.append(i)
    return list_1
def func_list_4(li):
    """
    1. 创建空列表
    2. 列表迭代逆序输出  for i in range(len(str)-1,-1,-1)  **步长-1  遵循左闭右开原则  [] 含左不含右
    :param li:
    :return:
    """
    list_1 = []
    for i in range(len(li)-1,-1,-1):
        list_1.append(li[i])
    return list_1
def func_list_5(li):
    """
    import collections
    利用内置模块collections.deque.extendleft()方法，生成迭代对象
    :param li:
    :return:
    """
    deque_1 = deque(li)
    deque_2 = deque()
    for i in deque_1:
        deque_2.appendleft(i)
    # 如果list()函数转换 deque迭代到列表
    # return deque_2
    return list(deque_2)
def func_list_6(li):
    """
    利用数据互换
    :param li:
    :return:
    """
    if len(li) == 0 or len(li) == 1:
        return li
    i = 0
    while i <= len(li)/2:
        li[i],li[len(li)-i-1] = li[len(li)-i-1],li[i]
        i += 1
    return li

# 字典的排序
def func_dict_1(di_ct):
    """
    import operator
    # 获取对象的维数 如是字典，则维数为key,value值 适用于列表、字典、元组、集合
    # sorted(iterable[,key[,reverse]])
        iterable 可迭代的对象
        key 排序的维数
        reverse 升序 False, 降序  True
    :param di_ct:
    :return:
    """
    sorted_x = sorted(di_ct.items(), key=operator.itemgetter(0))
    return sorted_x
def func_dict_2(di_ct):
    """
    匿名函数取维数排序   lambda x : x[1]
    :param di_ct:
    :return:
    """
    sorted_x = sorted(di_ct.items(),key=lambda x:x[1])
    return sorted_x
def func_dict_3(di_ct):
    """

    :param di_ct:
    :return:
    """
    print(sorted(di_ct.values()))
if __name__ == '__main__':
    di_ct = {1:2, 7:4, 4:3, 2:5, 0:0}
    str_reverse = func_dict_3(di_ct)
    print(str_reverse)
    print(func_dict_3.__doc__)