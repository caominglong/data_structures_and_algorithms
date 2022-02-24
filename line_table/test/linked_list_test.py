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

if __name__ == '__main__':
    main()
