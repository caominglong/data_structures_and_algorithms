class priorityQueueError(ValueError):
    pass


class priorityQueue:
    """
    用堆实现的优先队列类
    """

    def __init__(self, elist=[]):
        self._elems = list(elist)
        if elist:
            self.buildheap()

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise priorityQueueError("in peek")
        return self._elems[0]

    def enqueue(self, e):
        """
        入队操作
        :return:
        :param e 添加的元素
        """
        # 加入一个假元素
        self._elems.append(None)
        self.siftup(e, len(self._elems) - 1)

    def siftup(self, e, last):
        """
        往优先队列里插入数据，调整堆序
        :param e: 元素
        :param last: 结束
        :return: None
        """
        elems, i, j = self._elems, last, (last - 1) // 2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i = j
            j = (j - 1) // 2
        elems[i] = e

    def dequeue(self):
        """
        出队
        :return:
        """
        if self._elems is None:
            raise priorityQueueError("in dequeue")
        # 弹出首端元素
        elems = self._elems
        e0 = elems[0]
        prio_elem = elems.pop()
        # 重新构建堆序
        if len(elems) == 0:
            raise priorityQueueError("no more elements")
        self.siftdown(prio_elem, 0, len(elems))
        return e0

    def siftdown2(self):
        """
        弹出首端元素后，构建堆序
        思路：每次都补前面的一个坑。直到到达堆的尾部
        缺陷：到了叶子结点的时候，有三种情况需要判断，逻辑复杂
        情况1：如果只有一个结点的话，直接将此结点放入坑中即可。
        情况2：如果有两个结点， 需要选一个较小的结点去填坑
        情况3：如果选择的结点为右结点，结束即可，如果选择的结点为左结点，则需要将右结点左移一位，用于补位
        :return:
        """
        elems = self._elems
        i, j = 2 * parent_index + 1, 2 * parent_index + 2
        parent_index = 0
        while 2 * parent_index + 1 < len(elems) - 1:
            if elems[i] <= elems[j]:
                elems[parent_index] = elems[i]
                parent_index = i
            else:
                elems[parent_index] = elems[j]
                parent_index = j
            i, j = 2 * parent_index + 1, 2 * parent_index + 2
        temp = 2 * parent_index + 1
        elem = elems.pop()
        if 2 * parent_index + 1 < len(elems) - 1:
            elem2 = elems.pop()
            if elem2 < elem:
                elems[parent_index] = elem2
                elems[2 * parent_index + 1] = elem
            else:
                elems[parent_index] = elem
                elems[2 * parent_index + 1] = elem

    def buildheap(self):
        """
        初始化构建堆
        :return:
        """
        end = len(self._elems)
        for i in range(end // 2, -1, -1):
            self.siftdown(self._elems[i], i, end)

    def siftdown(self, e, begin, end):
        """
        构建堆，在begin起始点添加一个堆顶，将以下的子堆关联起来共同构建一个更大的子堆
        :param e: 需要添加到堆顶的元素
        :param begin: 堆顶元素的下标
        :param end: 堆的最大下标
        :return:
        """
        elems = self._elems
        i, j = begin, begin * 2 + 1
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:
                # 存在右边结点，并右边结点小于当前结点
                j += 1
            if e < elems[j]:
                # 构建结束，已经找到e需要插入的点了
                break
            # 如果当前e不是最小的，将j位置的元素放到e位置中,e的位置继续往下找
            elems[i] = elems[j]
            i, j = j, 2 * j + 1
        elems[i] = e
