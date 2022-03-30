# 二叉树
from collections import deque

from stack_queue.sstack import SStack


class BinNode:
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

    def postorder_nonrec(self, t, proc):
        """
        后序根遍历，非递归方式
        后序根的意思就是：左节点->右结点->根结点
        :param t:
        :param proc:
        :return:
        """
        s = SStack()
        while t is not None or not s.is_empty():
            # 内层循环，一直往左边往下找
            while t is not None:
                # 将t入栈，秉着后进先出的规则，往根结点的左边一直遍历下去，
                # 直到树为空的时候，跳出循环
                s.push(t)
                t = t.left if t.left is not None else t.right
            # 从上面的循环结束后，s里面就存有根结点的左边所有结点的数据，挨个出栈即可。
            node = s.pop()
            proc(node.data)
            # 根结点的右边结点还没有遍历呢，这时需要进行判断
            if not s.is_empty() and node == s.top().left:
                # 如果出栈的结点是根结点的左子结点，那么就需要去遍历根结点的右边部分
                t = s.top().right
            else:
                t = None
