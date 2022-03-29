# 括号匹配问题
from stack_queue.sstack import SStack


def check_parens(text):
    """
    匹配括号
    :param text:
    :return:
    """
    # 定义括号的种类
    parens = "()[]{}"
    # 定义所有的左括号
    open_parens = "([{"
    # 定义左括号的匹配括号
    opposite = {")": "(", "]": "[", "}": "{"}
    if text is None or len(text) == 0:
        return text
    def parentheses(text):
        """
        括号生成器，每次调用返回text里的下一个括号，及其位置
        :param text:
        :return:
        """
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                i = i + 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1
    # 用栈来保存括号
    st = SStack()
    for pr, i in parentheses(text):
        if pr in open_parens:
            st.push(pr)
        elif st.pop() != opposite[pr]:
            print("匹配失败")
            return False
        else:
            print("匹配成功")

    return True
    # for ch in text:


flag = check_parens('322[sff{()}lll]')
print(flag)