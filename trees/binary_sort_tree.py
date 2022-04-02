# 二叉排序树
from stack_queue.sstack import SStack

class Assoc:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class BinNode2:
    def __init__(self, data: Assoc, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySortTree():
    """
    二叉排序树
    """

    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def bt_print(self, btree):
        bt = btree
        if bt is None:
            return
        self.bt_seatch(bt.left)
        print(bt.data)
        self.bt_search(bt.right)

    def bt_search(self, btree, key):
        """
        二叉排序树遍历方法
        :param btree:
        :param key:
        :return:
        """
        bt = btree
        while bt is not None:
            data = bt.data
            if data.key > key:
                # 往左边找
                self.bt_search(bt.left, key)
            elif data.key < key:
                # 往左边找
                self.bt_search(bt.right, key)
            else:
                return data.value
        return None


    def insert(self, key, value):
        """
        往二叉排序树插入一个结点
        :param key:
        :param value:
        :return:
        """
        bt = self._root
        if bt is None:
            # 如果树为空，当前插入的结点为首结点
            self._root = BinNode2(Assoc(key, value))
            return
        # 当往下找插入位置时，如果发现为空树时则找到插入位置
        while True:
            data = bt.data
            if key < data.key:
                # 往左节点找
                if bt.left is None:
                    bt.left = BinNode2(Assoc(key, value))
                    return
                bt = bt.left
            elif key > data.key:
                # 往右边找
                if bt.right is None:
                    bt.right = BinNode2(Assoc(key, value))
                    return
                bt = bt.right
            else:
                # 如果key值相等，value将被覆盖
                data.value = value
                return

    def delete(self, key):
        """
        通过key从二叉排序树字典中删除元素
        思想：当从树中删除掉某结点后，需要调整树的结构，局部调整
        :param key:
        :return:
        """
        root = self._root
        parent_root = None
        if root is None:
            pass
        # 开始删除，首先找到删除的点
        while root is not None:
            data = root.data
            if key < data.key:
                parent_root = root
                root = root.left
            elif key > data.key:
                parent_root = root
                root = root.right
            else:
                break
        # 找到要删除的点了，删除后，进行调整结构
        if root.left is None:
            if parent_root.left == root:
                parent_root.left = root.right
            if parent_root.right == root:
                parent_root.right = root.right
            return

        # 如果要删除的结点存在左子结点，那么找此结点的左子节点的最右边结点
        r = root.left
        while r.right is not None:
            r = r.right
        # 将要删除结点的右子结点设置为r的右子结点
        r.right = root.right
        # 以下是将要删除元素的左子结点设置为父结点的左子结点，或则设置为父结点右子结点
        if parent_root is None:
            self._root = root.left
        elif parent_root.left is root:
            parent_root.left = root.left
        else:
            parent_root.right = root.left


    def entries(self):
        t, s = self._root, SStack()
        while t is not None or not s.is_empty():
            while t is not None:
                # 一直往下走，将根结点与左边结点加入栈里
                s.push(t)
                t = t.left
            t = s.pop()
            yield t.data.key, t.data.value
            t = t.right

    def print(self):
        for k, v in self.entries():
            print(k, v)