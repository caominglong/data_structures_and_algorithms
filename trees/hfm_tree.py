# 哈夫曼树
from trees.tree_do import PriorityQueue
from trees.binary_tree_node import BinNode


class HTNode(BinNode):
    """
    哈夫曼树扩展的结点类
    """
    def __lt__(self, other):
        """
        比较结点之间的权值大小
        :param other:
        :return:
        """
        return self.data < other.data


class HuffmanPrioQ(PriorityQueue):
    """
    哈夫曼树所使用的优先队列
    """
    def number(self):
        """
        返回当前队列中所剩元素的个数
        :return:
        """
        return len(self._elems)


class HuffmanTree:
    """
    哈夫曼树
    """
    def __init__(self):
        pass

    def huffmanTree(self, weights):
        trees = HuffmanPrioQ()
        for w in weights:
            trees.enqueue(HTNode(w))
        while trees.number() > 1:
            t1 = trees.dequeue()
            t2 = trees.dequeue()
            x = t1.data + t2.data
            trees.enqueue(HTNode(x, t1, t2))
        return trees.dequeue()