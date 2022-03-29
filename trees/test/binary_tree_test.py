# 二叉树的测试
from trees.binary_tree import binNode


def main():
    binNode1 = binNode(13, binNode(24, binNode(33)), binNode(40))
    # binNode1.preorder(binNode1, lambda x:print(x, end=" "))
    # binNode1.print_BinTNodes(binNode1)
    # binNode1.levelorder(binNode1)
    binNode1.preorder_nonrec(binNode1, lambda x:print(x, end=" "))

if __name__ == '__main__':
    main()