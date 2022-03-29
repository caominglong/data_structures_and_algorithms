from line_table.linked_list import Llist, L1list, LClist, DLlist, DLClist


def main():
    list = Llist()
    list.append(1)
    list.append(3)
    list.append(2)
    list.append(9)
    list.append(7)
    list.append(6)
    print("print append operation")
    list.printall()

    # rev_list = list.rev()
    # print("print rev operation")
    # rev_list.printall()

    list.sort_insert()
    list.printall()

    # list.preappend(4)
    # list.preappend(5)
    # print("print preappend operation")
    # list.printall()
    #
    # print(f"链表是否为空:{list.is_empty()}")
    #
    # list.insert(6, 4)
    # print("print insert operation")
    # list.printall()
    #
    # list.pop()
    # list.pop_last()
    # print("print pop and pop_last operation")
    # list.printall()
    #
    # list.remove(6)
    # print("print remove operation")
    # list.printall()
    #
    # print("print elements operation")
    # for x in list.elements():
    #     print(x)
    #
    # print("print for_each operation")
    # list.for_each(print)
    #
    # print("print find operation")
    # print(list.find(lambda x: x == 6))
    #
    # print("print filter operation")
    # for x in list.filter(lambda x: x > 3):
    #     print(x)
    #
    # print("print clear_llist operation")
    # list.clear_llist()
    # list.printall()


def main2():
    l1list = L1list()
    l1list.append(1)
    l1list.append(2)
    l1list.append(3)
    l1list.append(4)
    print("print append operation")
    l1list.printall()

    l1list.preappend(5)
    l1list.preappend(6)
    print("print preappend operation")
    l1list.printall()

    l1list.pop_last()
    print("print pop_last operation")
    l1list.printall()

    l1list.pop()
    print("print pop operation")
    l1list.printall()


def main3():
    lclist = LClist()
    lclist.append(1)
    lclist.append(2)
    lclist.append(3)
    lclist.append(4)
    print("print append operation")
    lclist.printall()

    lclist.preappend(5)
    lclist.preappend(6)
    print("print preappend operation")
    lclist.printall()

    lclist.pop_last()
    print("print pop_last operation")
    lclist.printall()

    lclist.pop()
    print("print pop operation")
    lclist.printall()


def main4():
    """
    双向链表的测试
    :return:
    """
    dllist = DLlist()
    dllist.append(1)
    dllist.append(2)
    dllist.append(3)
    dllist.append(4)
    print("print append operation")
    dllist.printall()

    dllist.preappend(5)
    dllist.preappend(6)
    print("print preappend operation")
    dllist.printall()

    dllist.pop()
    print("print pop operation")
    dllist.printall()

    dllist.pop_last()
    print("print pop_last operation")
    dllist.printall()

    dllist.insert(7, 1)
    print("print insert operation")
    dllist.printall()


def main5():
    """
    双向循环链表的测试
    :return:
    """
    dlclist = DLClist()
    dlclist.append(1)
    dlclist.append(2)
    dlclist.append(3)
    dlclist.append(4)
    print("print append operation")
    dlclist.printall()

    dlclist.preappend(5)
    dlclist.preappend(6)
    print("print preappend operation")
    dlclist.printall()

    dlclist.pop()
    print("print pop operation")
    dlclist.printall()

    dlclist.pop_last()
    print("print pop_last operation")
    dlclist.printall()

    dlclist.insert(7, 1)
    print("print insert operation")
    dlclist.printall()


def main7():
    # 用数组实现
    # josephus_A(5, 2, 3)
    josephus_L(5, 2, 3)


def josephus_A(n, k, m):
    """
    使用数组的方式解决
    约瑟夫环问题
    计算以下函数的时间复杂度：
    在m=n时，整个计算中，i+1的次数为n2 + logn
    :param n: 人数
    :param k: 第几个人开始报数
    :param m: 报到第几个数的时候，退出
    :return:
    """
    people = list(range(1, n + 1))  # 创建n个人的列表
    i = k - 1  # 数组的初始下标，从此下标开始报数
    for k in range(n):
        count = 0  # 每次循环重新计数
        # 每次报数到了之后，退出一个人，于是需要循环退出n次
        while count < m:
            # 当报的数还没到m的时候，推动people的数组下标往后走
            # 判断当前元素不等于0，才表示一个人报数
            if people[i] > 0:
                count += 1
            if count == m:
                print(i)
                people[i] = 0
            # 需要考虑列表走到尽头之后，需要重头开始报数
            i = (i + 1) % n


def josephus_L(n, k, m):
    """
    用链表来实现约瑟夫环
    :param n: 人数
    :param k: 从第几个人开始报数
    :param m: 报数到几个数时此人退出
    :return:
    """
    people = list(range(1, n + 1))
    num, i = n, k - 1
    # while people:
    #     count = 0
    #     while count < m:
    #         count += 1
    #         if count == m:
    #             print(people[i])
    #             # 删掉指定位置的元素
    #             people.pop(i)
    #         if people:
    #             i = (i+1) % len(people)
    # print(list(range(n, 0, -1)))
    # for num in range(n, 0, -1):
    #     i = (i + m - 1) % num
    #     print(people.pop(i),
    #           end=("," if num > 1 else "\n"))
    b = 0
    aaa = 'kk' if b != 0 else '11'
    print(aaa)
    return

def josephus_CL():
    """
    基于循环单链表
    :return:
    """

if __name__ == '__main__':
    main7()
