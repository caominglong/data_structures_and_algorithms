class SortDo:
    def __init__(self):
        pass

    def insert_sort(self, lst):
        """
        插入排序：不断把一个个元素插入一个序列中，最终得到排序序列
        :param lst: 需要排序的列表
        :return:
        """
        # 遍历列表元素，从第二个元素开始，第一个元素自身已经是排序好的序列了
        for i in range(1, len(lst)):
            # 找到新元素的插入位置，如果需要后移元素，则循环后移
            x = lst[i]
            j = i
            # 将已经排序好的序列的元素，逐个往后比较，大于当前元素的key的都往后移动一位，
            # 将坑位让出来，直到找到小于当前元素的key时停止，这时待插入元素的坑就构造出来了
            while j > 0 and lst[j - 1].key > x.key:
                lst[j] = lst[j - 1]
                j = j - 1
            # 将当前元素插入具体的坑位
            lst[j] = x

    def select_sort(self, lst):
        """
        选择排序：不断取出lst中的最小元素，然后顺序插入一个序列中即可
        :param lst:
        :return:
        """
        for i in range(len(lst) - 1):
            # 1 取出序列中的最小元素
            min_index = i
            for j in range(i, len(lst)):
                if lst[j].key < lst[min_index].key:
                    min_index = j
            # 2 将最小元素与当前i位置的元素调换
            if i != min_index:
                temp_e = lst[i]
                lst[i] = lst[min_index]
                lst[min_index] = temp_e

    def heap_sort(self, lst):
        """
        堆排序：不停弹出堆顶元素，直至堆中只剩一个元素为止
        :param lst:
        :return:
        """

    def siftdown(self, e, begin, end):
        """
        重新构造堆, e为堆尾元素，或者称为数组尾端元素，当从堆顶推出一个元素后，将堆尾元素推到堆顶，然后重新构造堆
        :param e: 堆尾元素
        :param begin:
        :param end:
        :return:
        """
