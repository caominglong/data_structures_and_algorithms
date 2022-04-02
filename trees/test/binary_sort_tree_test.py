from trees.binary_sort_tree import BinarySortTree


def build_dictBinTree(entries):
    dic = BinarySortTree()
    for k, v in entries.items():
        dic.insert(k, v)
    dic.insert(20, 20)
    return dic


def main():
    dic = build_dictBinTree(
        {57: 57, 36: 36, 89: 89, 7: 7, 43: 43, 65: 65, 96: 96, 18: 18, 52: 52, 60: 60, 74: 74})
    dic.print()


if __name__ == '__main__':
    main()
