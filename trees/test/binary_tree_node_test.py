# 二叉树的测试
from trees.binary_tree_node import BinNode


def main():
    BinNode1 = BinNode(13, BinNode(24, BinNode(33), BinNode(34)), BinNode(40))
    # BinNode1.preorder(BinNode1, lambda x:print(x, end=" "))
    # BinNode1.print_BinTNodes(BinNode1)
    # BinNode1.levelorder(BinNode1)
    # BinNode1.preorder_nonrec(BinNode1, lambda x:print(x, end=" "))
    BinNode1.postorder_nonrec(BinNode1, lambda x:print(x, end=" "))

if __name__ == '__main__':
    main()