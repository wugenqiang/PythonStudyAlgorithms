class SequenceList:

    # 初始化
    def __init__(self):
        self.seqList = [] # 初始化一个空表

    # 创建顺序表
    def CreateSeqList(self):
        element = input("please enter(input #:end):")
        while element != '#':
            self.seqList.append(int(element))
            element = input("please enter(input #:end):")

    # 查找顺序表中某一个元素
    def FindElement(self):
        key = int(input("please enter what you want to find:"))
        if key in self.seqList:
            keyPosition = self.seqList.index(key)
            result = keyPosition
        else:
            result = "none"
        return result

    # 在指定位置上插入元素
    def InsertElement(self):
        postion = int(input("请输入要插入的位置："))
        key = int(input("请输入要插入的值："))
        print("插入前顺序：", self.seqList)
        self.seqList.insert(postion, key)
        print("插入后顺序：", self.seqList)

    # 在指定位置上删除元素
    def DeleteElement(self):
        postion = int(input("请输入要删除元素的位置："))
        print("删除前的顺序表：", self.seqList)
        if postion < len(self.seqList) and postion >= 0:
            del self.seqList[postion]
            return self.seqList
        else:
            print("不存在啊老铁，删除个毛线啊")

    # 遍历顺序表元素
    def TraverseElement(self):
        for i in range(len(self.seqList)):
            print(self.seqList[i], end =' ')

    # 判空
    def IsEmpty(self):
        return len(self.seqList) == 0

    # 销毁顺序表
    def DestorySeqList(self):
        print("销毁前顺序表：", self.seqList)
        self.__init__()
        print("销毁后顺序表：", self.seqList)


# 测试
if __name__ == '__main__':
    list = SequenceList()
    list.CreateSeqList()
    print(list.seqList)
    print(list.FindElement())
    list.InsertElement()
    list.DeleteElement()
    list.TraverseElement()
    list.IsEmpty()
    list.DestorySeqList()
