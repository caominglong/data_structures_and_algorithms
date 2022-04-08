from sorts.record import Record
from sorts.sort_do import SortDo


def main():
    # 插入排序测试
    a1 = Record(1, 1)
    a2 = Record(2, 2)
    a3 = Record(2, 4)
    a4 = Record(5, 5)
    a5 = Record(4, 4)
    a6 = Record(6, 6)
    a7 = Record(3, 3)
    aa = [a1, a2, a3, a4, a5, a6, a7]
    sort = SortDo()
    sort.insert_sort(aa)
    for a in aa:
        print(a.datum, end=',')



if __name__ == '__main__':
    main()
