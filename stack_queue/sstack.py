# 定义一个栈
class SStack():
    """
    五类操作：
    1、创建空栈
    2、判断栈是否为空
    3、入栈（将元素压入或推入栈）
    4、出栈，删除栈里最后压入的元素并返回，俗称弹出
    5、取得栈里最后压入的元素，不删除
    """

    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems == []:
            print("空的栈")
        else:
            return self._elems.pop()