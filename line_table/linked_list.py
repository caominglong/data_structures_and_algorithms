# 链表

# 结点
class LNode:
    """结点"""
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

# 单链表
class Llist:
    """单链表"""
    def __init__(self):
        """创建空链表"""
        self._head = None

    def clear_llist(self):
        """清空链表"""
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def append(self, elem):
        """
        在表尾插入
        :param elem: 待插入的元素
        :return:
        """
        if self._head is None:
            self._head = LNode(elem)
            return
        temp_p = self._head
        while temp_p.next is not None:
            temp_p = temp_p.next
        temp_p.next = LNode(elem)

    def preappend(self, elem):
        """
        在表首插入，self._head初始存的是下一个结点，将它复制给LNode中的next
        """
        self._head = LNode(elem, self._head)

    def insert(self, elem, loc_elem):
        """
        确定要插入的位置，将实际要插入的元素插入到指定元素位置的后面
        :param elem: 要插入的元素
        :param loc_elem: 要插入的位置的前一个元素
        :return:
        """

        if self.is_empty():
            raise LinkedListUnderflow('in insert')
        temp_p = self._head
        while temp_p.next == loc_elem:
            temp_p = temp_p.next
            temp_p.next = LNode(elem, temp_p.next)
            return

    def preremove(self):
        """
        在表首删除，并返回表首元素
        :return: LNode
        """
        if self.is_empty():
            raise LinkedListUnderflow('in preremove')
        temp_p = self._head
        self._head = temp_p.next
        return temp_p

    def postremove(self):
        """
        在表尾删除，并返回表尾元素
        :return: LNode
        """
        if self.is_empty():
            raise LinkedListUnderflow('in postremove')
        temp_p = self._head
        last_node = None
        while temp_p.next is not None:
            last_node = temp_p
            temp_p = temp_p.next
        last_node.next = None
        return last_node

    def remove(self, loc_elem):
        temp_p = self._head
        while temp_p.next == loc_elem:
            temp_p.next = temp_p.next.next
            return

    def pop(self):
        """
        弹出表头结点
        :return:
        """
        if self.is_empty():
            raise LinkedListUnderflow('in pop')
        e = self._head.elem
        self._head = self._head.next
        return e

    def pop_last(self):
        """
        弹出最后一个元素
        :return:
        """
        if self.is_empty():
            raise LinkedListUnderflow('in pop')
        temp_p = self._head
        # 表中只有一个元素
        if temp_p.next is None:
            self._head = None
            return temp_p.elem

        while temp_p.next.next is not None:
            temp_p = temp_p.next
        temp_p.next = None
        return temp_p.next.elem

    def for_each(self, proc):
        p = self._head
        while p is not None:
            proc(p.elem)
            p = p.next

    def elements(self):
        """
        生成一个迭代器
        :return:
        """
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end=' ')
            if p.next is not None:
                print(", ", end='')
            p = p.next
        print('')

class LinkedListUnderflow(ValueError):
    """空表访问时，抛出异常"""
    pass