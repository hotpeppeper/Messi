'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
输入: "()[]{}"
输出: true

'''

def is_valid(s: str) -> bool:
    if len(s) == 0:
        return True
    if len(s) % 2 != 0:
        return False

    pat = {'(': ')', '[': ']', '{': '}'}
    stack_ = list()
    b_push = False
    for i in s:
        if i in pat:
            stack_.append(i)
            b_push = True
            continue
        if len(stack_) != 0 and i == pat.get(stack_[-1]):
            stack_.pop()
    res = len(stack_) == 0
    return b_push & res

def is_valid2(s: str) -> bool:
    if len(s) == 0:
        return True
    if len(s) % 2 != 0:
        return False
    pat = {')': '(', '}': '{', ']': '['}
    stack_ = list()
    for i in s:
        if i in pat:
            top_ele = stack_.pop() if stack_ else 'q'
            if pat[i] != top_ele:
                return False
        else:
            stack_.append(i)
    return not stack_


barkets = ['"}]}()){{)[{[(]"', '(])', '()[]{}', '(]', '([{}])', '([{}][])', '])']
for b in barkets:
    print(type(b))
    print(is_valid(b))