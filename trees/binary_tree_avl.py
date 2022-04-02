# 平衡二叉排序树
from trees.binary_sort_tree import BinarySortTree, BinNode2, Assoc


class AVLNode(BinNode2):
    def __init__(self, data):
        BinNode2.__init__(self, data)
        # 初始时平衡因子默认为0
        self.bf = 0


class BinaryTreeAvlDict(BinarySortTree):
    def __init__(self):
        BinarySortTree.__init__(self)

    def insert(self, key, value):
        """
        插入步骤：
        1、如果树中为空，直接插入树中
        2、如果树中不为空，插入元素后，更新元素后，看是否有平衡因子绝对值不在[0,1]之间的，如果树已不平衡，进行调整
        :param key:
        :param value:
        :return:
        """
        fixed_root = self._root
        root = self._root
        if root is None:
            root = AVLNode(Assoc(key, value))
            return
        # 树中结点不为空
        # 首先找到元素要插入的位置
        parent_node = None
        left_or_right = 0   # 0代表左边，1代表右边，代表着新插入的元素插入到根结点的哪一边了
        update_root = None
        while root is not None:
            data = root.data
            if key > data.key:
                left_or_right = 1
                update_root = fixed_root.right
            else:
                update_root = fixed_root.left
            break
        while root is not None:
            data = root.data
            if key < data.key:
                # 往左找
                if root.left is None:
                    root.left = AVLNode(Assoc(key, value))
                    # 更新路径上的所有元素的平衡因子
                    if root.bf != 0:
                        # 不等于0代表不是叶子结点,这时平衡因子只会响应root结点
                        root.bf = 0
                    else:
                        # 当前已知信息为，插入结点插到了左边的叶子结点
                        if left_or_right == 0 and fixed_root.bf == 1:
                            # 表示平衡树左边的高度高1，并且数据插到了根结点的左子树上
                            while update_root != root:
                                # 更新从根结点的左子树结点到当前路径上的所有bf
                                if key < update_root.data.key:
                                    update_root.bf = 1  # 设置为1，因为左边高度高1，往左边加结点后进行调整，左边维持高度高1
                                    update_root = update_root.left
                                else:
                                    update_root.bf = -1  # 设置为-1，因为左边高度高1，往左边加结点后进行调整，左边维持高度高1
                                    update_root = update_root.right

                        elif left_or_right == 0 and fixed_root.bf == -1:
                            # 数据插到了根结点的左子树上，但是平衡树的右子树高度高1，这是平衡树趋向平衡了，将根结点的bf设置为0
                            fixed_root.bf = 0
                        elif left_or_right == 1 and fixed_root.bf == 1:
                            # 数据插到了根结点的右子树上，表示平衡树左边的高度高1，这是平衡树趋向平衡了，将根结点的bf设置为0
                            fixed_root.bf = 0
                        elif left_or_right == 1 and fixed_root.bf == -1:
                            # 数据插到了根结点的右子树上，表示平衡树右边的高度高1
                            # 表示平衡树左边的高度高1，并且数据插到了根结点的左子树上
                            while update_root != root:
                                # 更新从根结点的左子树结点到当前路径上的所有bf
                                if key < update_root.data.key:
                                    update_root.bf = 1  # 设置为1，因为左边高度高1，往左边加结点后进行调整，左边维持高度高1
                                    update_root = update_root.left
                                else:
                                    update_root.bf = -1  # 设置为-1，因为左边高度高1，往左边加结点后进行调整，左边维持高度高1
                                    update_root = update_root.right
                    self.LL(parent_node, root)
                    break
                parent_node = root
                root = root.left
            if key > data.key:
                # 往右找
                if root.right is None:
                    root.right = AVLNode(Assoc(key, value))
                    # 更新路径上的所有元素的平衡因子
                    break
                    return
            else:
                root.data.value = value
                return

    def LL(self, parent_node, a):
        # a的左子树较高，新结点插入在a的左子树的左子树
        # 进行旋转
        parent_node.left = None
        a.right = parent_node