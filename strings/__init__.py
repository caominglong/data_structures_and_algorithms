# dp = [{i: 0 for i in 'ababc'} for i in range(5)]
# print(dp)
#
# dp = [{i: 0 for i in range(5)} for i in range(5)]
# print(dp)

# class kmp:
#
#     def __init__(self, pat):
#         self.pat = pat
#
#     def kmp(self):
#         pat = self.pat
#         m = len(pat)
#         dp = [{i: 0 for i in pat} for i in range(len(pat))]
#         print(dp)
#         # dp = [[0 for i in range(1, m)] for i in range(256)]
#         dp[0][pat[0]] = 1
#         # 影子状态X
#         x = 0
#         # 当前状态 j 从 1 开始
#         for j in range(1, m):
#             for c in pat:
#                 if pat[j] == c:
#                     dp[j][c] = j + 1
#                 else:
#                     dp[j][c] = dp[x][c]
#             # 更新影子状态
#             x = dp[x][pat[j]]
#         return dp
#
# kmm = kmp('acacb')
# dp = kmm.kmp()
# print(dp)


def match_string(txt, pat):
    i, j = 0, 0
    m, n = len(pat), len(txt)
    k_dict = get_k_dict(pat)
    k = 0
    while j < m and i < n:
        k = k + 1
        if txt[i] == pat[j]:
            # 相等，则txt与pat的下标都往后推移，继续匹配
            j = j + 1
        else:
            if pat.find(txt[i]) == -1:
                # 如果txt当前元素不在pat中，那么将pat设置为0下标,txt继续往后匹配
                j = 0
            if pat.find(txt[i]) >= 0:
                # 获取pat下标移动位置
                j = k_dict[j][txt[i]]
        if j == m:
            return i - m
        i = i + 1
    return -1


def get_k_dict(pat):
    m = len(pat)
    # 如果pi之前的所有匹配串字符与目标串字符的比较都没有价值，则将k设置为-1，代表的是当k为-1时，txt的下标加1，pat的下标归0
    dp = [-1] * m
    # 设置k的起始态
    k = -1
    # 从pat的第二个元素下标元素开始找k
    for j in range(1, m):
        # 更新k
        if k == -1:
            # k等于-1的话，证明还没有最长相等前后缀的串，
            # if pat[j] == pat[0]:
            k = 0
            dp[j] = k
        else:
            dp[j] = k
            # k不等于-1的话，证明已经存在最长相等前后缀的串了
            # k下标需要回退
            if pat[j] == pat[k]:
                k = k + 1
            else:
                k = dp[k]
    return dp


dp = get_k_dict('abbcabcaabbcaa')
# dp = {str(i): 0 for i in range(len('abbcabcaabbcaa'))}
print(dp)


def get_pnext(p):
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m - 1:
        if k == -1 or p[i] == p[k]:
            i, k = i + 1, k + 1
            pnext[i] = k
        else:
            k = pnext[k]
    return pnext


dp2 = get_pnext('abac')
print(dp2)
