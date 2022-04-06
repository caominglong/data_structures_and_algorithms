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
        print("开始插入结点！")
        root = self._root
        if root is None:
            self._root = AVLNode(Assoc(key, value))
            return
        # 树中结点不为空
        # 关键的三个结点变量，代表的是被插入元素后受影响的那颗子树的三个结点，进行平衡调整，也是需要调整这三个结点的位置关系
        # 1、parent_node代表的是受影响子树的根结点
        # 2、leaf_node代表的是还未插入时的受影响子树的叶子结点，可以看做是parent_node的孩子结点
        # 3、insert_node代表的是被插入的结点
        parent_node = self._root  # 受影响的子树
        leaf_node = None
        insert_node = None  # 被插入点的父结点
        # 首先找到要插入的位置，并将结点插入当前位置
        while root is not None:
            data = root.data
            if key < data.key:
                # 往左找
                if root.left is None:
                    root.left = AVLNode(Assoc(key, value))
                    insert_node = root.left
                    break
                parent_node = root
                root = root.left
            elif key > data.key:
                # 往右找
                if root.right is None:
                    root.right = AVLNode(Assoc(key, value))
                    insert_node = root.right
                    break
                parent_node = root
                root = root.right
            else:
                # 如果存在key相等，将值覆盖后即可退出
                root.data.value = value
                return

        # 得到新插入结点是插入到parent_node的左子树还是右子树
        update_root = None  # 更新parent_node下到插入结点所经过结点的所有平衡因子bf
        left_or_right = 1  # 1代表左边，-1代表右边，代表着新插入的元素插入到parent_node的哪一边了
        while parent_node is not None:
            data = parent_node.data
            if key > data.key:
                left_or_right = -1
                update_root = parent_node.right
                leaf_node = parent_node.right
            else:
                update_root = parent_node.left
                leaf_node = parent_node.left
            break

        # 更新从parent_node的左子树结点到插入点路径上的所有bf
        while update_root != insert_node:
            if key < update_root.data.key:
                update_root.bf = 1  # 设置为1，往左边加结点后进行调整，左边树高1，则bf为1
                update_root = update_root.left
            else:
                update_root.bf = -1  # 设置为-1，往右边加结点后进行调整，右边树高1，则bf为-1
                update_root = update_root.right
        # 如果parent_node的平衡因子为0，更新parent_node的平衡因子即可
        if parent_node.bf == 0:
            parent_node.bf = left_or_right
            return
        if parent_node.bf == -left_or_right:
            # 新结点插入到了parent_node结点的另一边，那么parent_node趋向平衡
            parent_node.bf = 0
            return
        # 以下是失衡情况
        if left_or_right == 1 and leaf_node.bf == 1:
            # 当插入的结点在parent_node的左子树，且leaf_node等于1，代表新结点插入在parent_node的左子树的左子树
            # LL调整，LL：a的左子树较高，新结点插入在a的左子树的左子树
            print(f"结点{key}进行了LL调整")
            self.LL(parent_node, leaf_node)
        elif left_or_right == -1 and leaf_node.bf == 1:
            # 数据插到了parent_node的右子树上，且leaf_node的平衡因子为1，代表新结点插入在parent_node的右子树的左子树
            # RL调整，RL：a的右子树较高，新结点插入在a的右子树的左子树
            print(f"结点{key}进行了RL调整")
            self.RL(parent_node, leaf_node)
        elif left_or_right == 1 and leaf_node.bf == -1:
            # 数据插到了parent_node的左子树上，且leaf_node的平衡因子为-1，代表新结点插入在parent_node的左子树的右子树
            # LR调整，LR：a的左子树较高，新结点插入在a的左子树的右子树
            print(f"结点{key}进行了LR调整")
            self.LR(parent_node, leaf_node)
        elif left_or_right == -1 and leaf_node.bf == -1:
            # 数据插到了parent_node的右子树上，且leaf_node的平衡因子为-1，代表新结点插入在parent_node的右子树的右子树
            # RR调整，RR：a的右子树较高，新结点插入在a的右子树的右子树
            print(f"结点{key}进行了RR调整")
            self.RR(parent_node, leaf_node)


    def LL(self, parent_node, leaf_node):
        # a的左子树较高，新结点插入在a的左子树的左子树
        # 进行旋转
        parent_node.left = leaf_node.right
        leaf_node.right = parent_node
        leaf_node.bf = parent_node.bf = 0
        return leaf_node

    def RR(self, parent_node, leaf_node):
        parent_node.right = leaf_node.left
        leaf_node.left = parent_node
        parent_node.bf = leaf_node.bf = 0
        return leaf_node

    def LR(self, parent_node, leaf_node):
        c = leaf_node.right
        parent_node.left, leaf_node.left = c.right, c.left
        c.left, c.right = leaf_node, parent_node
        if c.bf == 0:
            # c本身就是插入结点
            parent_node.bf = leaf_node.bf = 0
        elif c.bf == 1:
            # 新结点在c的左子树
            parent_node.bf = -1
            leaf_node.bf = 0
        else:
            # 新结点在c的右子树
            parent_node.bf = 0
            leaf_node.bf = 1
        c.bf = 0
        return c

    def RL(self, parent_node, leaf_node):
        c = leaf_node.left
        parent_node.right, leaf_node.left = c.left, c.right
        c.left, c.right = parent_node, leaf_node
        if c.bf == 0:
            # c本身就是插入结点
            parent_node.bf = leaf_node.bf = 0
        elif c.bf == 1:
            # 新结点在c的左子树
            parent_node.bf = 0
            leaf_node.bf = -1
        else:
            # 新结点在c的右子树
            parent_node.bf = 1
            leaf_node.bf = 0
        c.bf = 0
        return c