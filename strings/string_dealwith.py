# 字符串处理

# 简单串匹配算法
def simple_match(main_str: str, pattern_str: str):
    """
    算法总共要循环的次数，假设main_str的长度为m，pattern_str的长度为n，最坏情况下，比较次数为n(m-n+1)次
    参考，00000001与0001
    :param main_str:
    :param pattern_str:
    :return:
    """
    print('简单匹配算法开始执行！！！')
    m, n = len(pattern_str), len(main_str)
    i, j = 0, 0
    while i < n and j < m:
        if main_str[i] != pattern_str[j]:
            # 如果第一个字符不相等，则将main_str下标往后推一位， j不变
            i = i - j + 1  # 关键语句，主串的索引可以根据模式串索引计算出来
            j = 0
        else:
            j += 1
            i += 1
    if j == m:
        return i - j
    return -1


def simple_match2(main_str: str, pattern_str: str):
    """
    可以匹配多个子串的位置
    :param main_str:
    :param pattern_str:
    :return:
    """
    print('简单匹配算法开始执行！！！')
    m, n = len(pattern_str), len(main_str)
    i, j = 0, 0
    list1 = []
    while i < n and j < m:
        if main_str[i] != pattern_str[j]:
            # 如果第一个字符不相等，则将main_str下标往后推一位， j不变
            i = i - j + 1  # 关键语句，主串的索引可以根据模式串索引计算出来
            j = 0
        else:
            j += 1
            i += 1
        if j == m:
            list1.append(i - j)
            j = 0
    return list1


def simple_match3(main_str: str, pattern_str: str):
    """
    可以匹配多个子串的位置
    :param main_str:
    :param pattern_str:
    :return:
    """
    print('简单匹配算法开始执行！！！')
    m, n = len(pattern_str), len(main_str)
    i, j = 0, 0
    list1 = []
    while i < n and j < m:
        if main_str[i] != pattern_str[j]:
            # 如果第一个字符不相等，则将main_str下标往后推一位， j不变
            i = i - j + 1  # 关键语句，主串的索引可以根据模式串索引计算出来
            j = 0
        else:
            j += 1
            i += 1
        if j == m:
            list1.append(i - j)
            i = i - j + 1
            j = 0
    return list1


# KMP算法


def main():
    print(simple_match3('abababab', 'abab'))


if __name__ == '__main__':
    main()

def init(pat: str):
    """
    方法核心：找到pat中每个元素对应的移动位置
    :param pat:
    :return:
    """
    loc_dict = {}
    k = 0
    for i in pat:
        if i == pat[0:k]:
            loc_dict[i] = k + 1
        else:
            loc_dict[i] = k + 1



def search(pat: str, Ti: str):
    if Ti not in pat:
        return -1
    if Ti in pat:
        pass


def get_pat_subscript(pj, ti):
    """

    :param pj: pat当前元素
    :param ti: txt当前元素
    :return:
    """
