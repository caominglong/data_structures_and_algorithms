from stack_queue.sstack import SStack


class BinTree:
    """
    二叉树类
    """
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def root(self):
        return self._root

    def leftchild(self):
        return self._root.left

    def rightchild(self):
        return self._root.right

    def set_root(self, rootnode):
        self._root = rootnode

    def set_left(self, leftnode):
        self._root.left = leftnode

    def set_right(self, rightchild):
        self._root.right = rightchild

    def preorder_elements(self, t):
        """
        先序根遍历（递归方式）
        :return:
        """
        root = t
        if root is None:
            return
        print(root.data)
        self.preorder_elements(root.left)
        self.preorder_elements(root.right)

    def preorder_elem_nonrec(self):
        """
        先序根遍历（非递归方式）
        :return:
        """
        root = self._root
        s = SStack()
        t = root
        while t is not None and not s.is_empty():
            while t is not None:
                print(t.data)
                t = t.left
                if t.right is not None:
                    s.push(t.right)
            t = s.pop()

    def postorder_elements(self, t):
        """
        后序根遍历（递归方式）
        :return:
        """
        root = t
        if root is None:
            return
        self.postorder_elements(root.left)
        self.postorder_elements(root.right)
        print(root.data)

    def postorder_elem_nonrec(self):
        """
        后序根遍历，非递归方式
        :return:
        """
        root = self._root
        s = SStack()
        t = root
        # 从根结点开始循环
        while t is not None or not s.is_empty():
            while t is not None:
                # 将当前结点加入栈中，并一直往树的左边找
                s.push(t)
                t = t.left if t.left is not None else t.right
            # 上面循环后，s栈中存的就是根结点的所有待出栈的左边结点
            node = s.pop()
            print(node.data)
            # 判断是否找到了当前栈顶结点的左子结点， 这时候依据后序根遍历，应该去找栈顶结点的右边结点
            if not s.is_empty() and node == s.top().left:
                t = s.top().right
            else:
                t = None

    def middle_elem(self, t):
        """
        中序根遍历（递归方式）
        :return:
        """
        root = t
        if root is None:
            return
        self.middle_elem(root.left)
        print(root.data)
        self.middle_elem(root.right)

    def middle_elem_nonrec(self):
        """
        中序根遍历（非递归方式）
        :return:
        """
        root = self._root
        s = SStack()
        t = root
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t)
                t = t.left
            node = s.pop()
            print(node.data)
            if node.right is not None:
                t = node.right
            else:
                t = None

    def breadth_first(self):
        """
        宽度优先遍历，从左到右依次遍历结点
        :return:
        """
        root = self._root
        # 需要用到队列，以下代码省略
