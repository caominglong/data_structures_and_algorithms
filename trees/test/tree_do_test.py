from trees.tree_do import PriorityQueue


def main():
    # 优先队列
    prioQueue = PriorityQueue([33, 64, 24, 49, 13, 77, 49, 99, 6])
    # for i in prioQueue._elems:
    #     print(i)
    prioQueue.enqueue(45)
    for i in prioQueue._elems:
        print(i, end=',')
    node = prioQueue.dequeue()
    print(str(node)+"sssss", end="\n")
    for i in prioQueue._elems:
        print(i, end=',')

if __name__ == '__main__':
    main()