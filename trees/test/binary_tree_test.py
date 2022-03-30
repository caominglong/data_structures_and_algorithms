from trees.binary_tree import BinTree
from trees.binary_tree_node import BinNode
def main():
    binTree = BinTree()
    binTree.set_root(BinNode(13))
    binTree.set_left(BinNode(33, BinNode(49, BinNode(99), BinNode(64)), BinNode(45)))
    binTree.set_right(BinNode(24, BinNode(77), BinNode(49)))
    binTree.middle_elem(binTree.root())

if __name__ == '__main__':
    main()