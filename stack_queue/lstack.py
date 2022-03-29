# 用链接表实现栈

class Node():

    def __init__(self, elem, _next=None):
        self.elem = elem
        self._next = _next


class LStack():

    def __init__(self):
        self.head = None

    def is_empty(self):
        # 判断头指针是否为None
        return self.head is None

    def top(self):
        if self.head is not None:
            return self.head.elem
        return None


    def push(self, elem):
        # 先创建个新的结点
        new_node = None(elem, self.head)
        # 然后将头指针指向新的结点。因为是往首部插入
        self.head = new_node

    def pop(self):
        if self.head is not None:
            e = self.head.elem
            # 获取当前头指针指向的元素的下一个元素
            next_node = self.head._next
            # 将当前头指针指向的元素的_next设置为空
            self.head._next = None
            # 当前头指针指向下一个元素
            self.head = next_node
            return e

