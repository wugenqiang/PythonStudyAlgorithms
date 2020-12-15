#!usr/bin/env python
# encoding:utf-8

# 结点类
class Node(object):

    # 单个节点 初始化 输入一个值data，将值变为一个节点
    def __init__(self, data):
        self.data = data
        self.next = None

    # 打印对象中具体的属性值
    def __str__(self):
        return self.data


class SingleLinkedList(object):

    # 创建一个单链表
    def __init__(self):
        self.head = None

    # 判断链表是否为空
    def is_empty(self):
        return self.head is None

    # 获取链表的长度
    def length(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    # 头部添加元素
    def add_fist(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    # 尾部添加元素
    def add_last(self, data):
        node = Node(data)
        # 如果链表为空，需要特殊处理
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            # 退出循环的时候，curl指向尾结点
            cur.next = node

    # 在指定位置添加元素
    def insert_node(self, index, data):
        node = Node(data)
        if index < 0 or index > self.length():
            return False
        elif index == 0:
            self.add_fist()
        elif index == self.length():
            self.add_last()
        else:
            cur = self.head
            count = 0
            while count < (index - 1):
                count += 1
                cur = cur.next
            # 退出循环的时候，cur指向index的前一个位置
            node.next = cur.next
            cur.next = node

    # 删除指定节点
    def remove_node(self, data):
        cur = self.head  # 指针指向的结点
        pre = None  # 指针指向结点的前一个
        if self.head == data:
            self.head.next = self.head
        else:
            while cur.data is not data:
                # 不是要找的元素，移动游标
                pre = cur
                cur = cur.next
            pre.next = cur.next

    # 查找节点
    def search_node(self, data):
        cur = self.head
        while cur is not None:
            if cur.data == data:
                return True
            else:
                cur = cur.next
        return False

    # 遍历 打印链表
    def traverse_to_print_node(self):
        # cur = self.head
        # while cur is not None:
        #     print(cur.data, end = " ")
        #     cur = cur.next
        print_list = []
        cur = self.head
        while cur is not None:
            print_list.append(str(cur.data))
            cur = cur.next
        print('->'.join(print_list))

# 测试
if __name__ == '__main__':
    list = SingleLinkedList()
    list.add_fist(2)
    list.add_fist(1)
    list.add_last(4)
    list.insert_node(2, 3)
    list.traverse_to_print_node()
    print(list.is_empty())
    print(list.length())
    list.remove_node(4)
    print(list.search_node(3))
    list.traverse_to_print_node()
