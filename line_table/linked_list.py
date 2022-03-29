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
        while temp_p.elem != loc_elem:
            temp_p = temp_p.next
        temp_p.next = LNode(elem, temp_p.next)

    def remove(self, loc_elem):
        """
        删除指定位置的元素
        :param loc_elem: 在指定位置之前的元素
        :return:
        """
        temp_p = self._head
        while temp_p.elem != loc_elem:
            temp_p = temp_p.next
        temp_p.next = temp_p.next.next

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
        e = temp_p.next.elem
        temp_p.next = None
        return e

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
            print(p.elem, end='')
            if p.next is not None:
                print(", ", end='')
            p = p.next
        print('')

    def find(self, pred):
        """
        找到符合条件的元素，并返回
        :param pred: 判断谓词
        :return:
        """
        if self.is_empty():
            raise LinkedListUnderflow('in find')
        p = self._head
        while p.next is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    def filter(self, pred):
        """
        生成器方法
        找到符合条件的一批元素，逐个返回
        :param pred:
        :return:
        """
        if self.is_empty():
            raise LinkedListUnderflow('in find')
        p = self._head
        while p.next is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next

    def rev(self):
        """
        将表的元素反转
        :return:
        """
        re_list = Llist()
        p = self._head
        while p is not None:
            re_list.preappend(p.elem)
            p = p.next
        return re_list

    def sort_insert2(self):
        p = self._head
        if p is None or p.next is None:
            # 如果当前列表为空，或者只有一个元素，那么排序结束
            return
        rem = p.next
        p.next = None
        while rem is not None:
            p = self._head
            q = None
            while p is not None and p.elem <= rem.elem:
                q = p   # q记录的是待插入位置的前一个位置
                p = p.next  # p记录的是待插入位置的后一个位置
            if q is None:
                # 如果往头部插入元素，需要改变头指针
                self._head = rem
            else:
                # 将后置指针指向待插入的元素
                q.next = rem
            # 设置rem的后置指针为p
            q = rem
            rem = rem.next
            q.next = p

    def sort_insert(self):
        """
        将单链表里面的元素按照从小到大排序，使用插入排序方法
        排序过程：将元素里面的值进行比较并替换
        总结：1.直接对象赋值的时候，修改对象的元素，所有赋值过的变量都会受影响
        2.链表进行操作的时候，需要定义一个待操作的链表，供返回结果
        :return:
        """
        p = self._head
        if p is None or p.next is None:
            # 如果当前列表为空，或者只有一个元素，那么排序结束
            return
        # 开始排序
        cur_node = self._head.next
        while cur_node is not None:
            k = self._head
            cur_elem = cur_node.elem
            while k is not cur_node and k.elem <= cur_node.elem:
                # 这个循环主要是忽略前面已经排好序并且小于cur_node的值（已经不需要比较替换）的一些元素，直接将k定位到需要替换的位置
                k = k.next
            while k is not cur_node:
                # 进行比较替换，将当前需要的比较值替换到k的当前位置处
                temp_elem = k.elem
                k.elem = cur_elem
                cur_elem = temp_elem
                k = k.next
            # 回填最后一个元素,因为上面的while循环少了一步填值
            cur_node.elem = cur_elem
            cur_node = cur_node.next


# 单链表加尾指针 用于改善单链表在操作尾表元素的时间复杂度过高的问题
class L1list(Llist):
    def __init__(self):
        Llist.__init__(self)
        self._rear = None

    def preappend(self, elem):
        """
        重新定义表首加入操作
        :param elem:
        :return:
        """
        p = self._head
        if p is None:
            # 空表
            self._head = LNode(elem, self._head)
            # 尾指针与头指针相同
            self._rear = self._head
        # 不是空表
        self._head = LNode(elem, self._head)

    def append(self, elem):
        """
        重新定义表尾加入元素
        :param elem:
        :return:
        """
        p = self._head
        if p is None:
            # 空表
            self._head = LNode(elem, self._head)
            # 尾指针与头指针相同
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    def pop_last(self):
        """
        重新定义从尾端删除
        :return:
        """
        if self.is_empty():
            raise LinkedListUnderflow('in L1list pop_last')
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            self._rear = None
            return e
        # 删除表尾元素的时候，需要找到表尾指针的上一个元素，然后将这个元素赋值给self._rear
        while p.next.next is not None:
            p = p.next
        e = p.elem
        p.next = None
        self._rear = p
        return e


# 单循环链表，将表尾元素的next指向表首第一个结点，并去掉头指针，改为指向表尾元素的尾指针
class LClist:
    """
    单循环链表
    """

    def __init__(self):
        self._rear = None

    def preappend(self, elem):
        if self._rear is None:
            p = LNode(elem)
            self._rear = p
            self._rear.next = p
        else:
            self._rear.next = LNode(elem, self._rear.next)

    def append(self, elem):
        self.preappend(elem)
        # 在单循环链表中表首插入跟表尾插入其实一样，只是在于_rear指定哪个为尾结点
        self._rear = self._rear.next

    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow('in LClist pop')
        p = self._rear.next
        if self._rear is p:
            # 只有一个结点
            self._rear = None
        else:
            self._rear.next = self._rear.next.next
        return p.elem

    def pop_last(self):
        if self._rear is None:
            raise LinkedListUnderflow('in LClist pop_last')
        else:
            e = self._rear.elem
            p = self._rear
            while p.next is not self._rear:
                # 找到自身，则到了列表尾部
                p = p.next
            p.next = self._rear.next
            self._rear = p
            return e

    def printall(self):
        if self._rear is None:
            return
        p = self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                return  # or break
            p = p.next


# 双链表，添加一个前置指针，可以用于反向查找
class DLNode(LNode):
    def __init__(self, elem, prev=None, next_=None):
        LNode.__init__(self, elem, next_)
        self.prev = prev


class DLlist(L1list):
    """
    空表判断、find、filter、printall都可以继承，这些行为不需要修改
    """

    def __init__(self):
        L1list.__init__(self)

    def preappend(self, elem):
        if self._head is None:
            self._head = DLNode(elem)
            self._rear = self._head
            return
        p = DLNode(elem, next_=self._head)
        # 将当前头指针的前置结点设置为要添加进的结点
        self._head.prev = p
        # 将当前结点设置为头结点
        self._head = p

    def append(self, elem):
        if self._head is None:
            self._head = DLNode(elem)
            self._rear = self._head
            return
        p = DLNode(elem, prev=self._rear)
        # 将之前的尾结点的后置结点设置为当前添加的节点
        self._rear.next = p
        # 当当前添加的节点设置为尾结点
        self._rear = p

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow('in DLlist pop')
        p = self._head  # 头结点
        if p.next is None:
            # 只有一个结点
            self._head = None
        else:
            p.next.prev = None  # 设置第二个结点的前驱指针为空
            p = p.next
        return p.elem

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow('in DLlist pop')
        p = self._rear  # 尾结点
        if self._head.next is None:
            # 只有一个结点
            self._head = None
            self._rear = self._head
        else:
            p.prev.next = None  # 设置倒数第二个结点的后指针为空
            p = p.prev
        return p.elem

    def insert(self, elem, loc_elem):
        """
        在某个位置插入元素
        :param elem:
        :param loc_elem: 要插入位置的前一个元素
        :return:
        """
        if self._head is None:
            raise LinkedListUnderflow('in insert pop')
        p = self._head
        while p.elem != loc_elem:
            p = p.next
        node = DLNode(elem, prev=p, next_=p.next)
        p.next.prev = node  # 当前结点p的下一个元素的前置结点设置为要插入的结点
        p.next = node  # 将当前结点p的后置结点设置为要插入的结点


# 循环双链表，在双链表基础上，将尾结点的next设置为头结点，将表首结点的prev设置为尾结点
class DLClist(Llist):

    def __init__(self):
        Llist.__init__(self)

    def append(self, elem):
        if self._head is None:
            # 表为空
            node = DLNode(elem)
            self._head = node
            # 构成环
            self._head.prev = node
            self._head.next = node
            return
        node = DLNode(elem, prev=self._head.prev, next_=self._head)
        # 将之前尾结点的后置指针设置为当前添加进的节点
        self._head.prev.next = node
        # 头结点的前置指针设置为要加入的节点
        self._head.prev = node

    def preappend(self, elem):
        self.append(elem)
        # 将头指针设置为当前结点
        self._head = self._head.prev

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop_last')
        if self._head.next is self._head:
            # 只有一个结点
            e = self._head.elem
            self._head = None
            return e
        # 将尾结点的前一个结点的后置指针设置为头结点
        self._head.prev.prev.next = self._head
        # 将头结点的前置指针设置为尾结点的前一个结点
        self._head.prev = self._head.prev.prev

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop_last')
        if self._head.next is self._head:
            # 只有一个结点
            e = self._head.elem
            self._head = None
            return e
        # 将尾结点的后置指针设置为头结点的下一个结点
        self._head.prev.next = self._head.next
        # 将头结点的下一个结点的前置指针设置为尾结点
        self._head.next.prev = self._head.prev
        # 将头结点的下一个结点设置为头指针
        e = self._head.elem
        self._head = self._head.next
        return e

    def printall(self):
        if self._head is None:
            pass
        else:
            p = self._head
            while p.next is not self._head:
                print(p.elem, sep=',')
                p = p.next
            print(p.elem)


class LinkedListUnderflow(ValueError):
    """空表访问时，抛出异常"""
    pass
