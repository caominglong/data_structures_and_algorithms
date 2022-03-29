# 二叉树
from collections import deque

from stack_queue.sstack import SStack


class binNode:
    """
    二叉树结点类
    """

    def __init__(self, _data, left=None, right=None):
        # 初始化结点
        self.data = _data
        self.left = left
        self.right = right

    def preorder(self, t, proc):
        """
        先根序遍历（递归方式）
        :param proc: 具体的结点数据操作
        :param t: 是一个具体的树
        :return:
        """
        if t is None:
            return
        proc(t.data)
        self.preorder(t.left, proc)
        self.preorder(t.right, proc)

    def print_BinTNodes(self, t):
        if t is None:
            print("^", end="")
            return
        print("(" + str(t.data), end="")
        self.print_BinTNodes(t.left)
        self.print_BinTNodes(t.right)
        print(")", end="")

    def levelorder(self, t):
        """
        广度优先遍历
        :param t:
        :return:
        """
        qu = deque()
        qu.append(t)
        while qu:
            node = qu.popleft()
            if node is None:
                continue
            print(node.data)
            qu.append(node.left)
            qu.append(node.right)

    def preorder_nonrec(self, t, proc):
        """
        先序根遍历（非递归方式）
        :param t: 树
        :param proc: 对结点进行的操作
        :return:
        """
        s = SStack()
        s.push(t)
        while not s.is_empty():

            proc(node.data)
            while not s.is_empty():
                node = s.pop()
                if node.left is not None:
                    s.push(node.left)

