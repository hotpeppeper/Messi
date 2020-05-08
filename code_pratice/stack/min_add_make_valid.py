'''
no.921
给定一个由 '(' 和 ')' 括号组成的字符串 S，我们需要添加最少的括号（ '(' 或是 ')'，可以在任何位置），以使得到的括号字符串有效。
'''


def min_add_make_valid(S):
    stack_ = list()
    pot = {')': '('}
    for s in S:
        if not stack_:
            stack_.append(s)
        else:
            if pot.get(s, '#') == stack_[-1]:
                stack_.pop()
            else:
                stack_.append(s)
    return len(stack_)

ss = ['())', '(((', '()', '()))((']
for s in ss:
    print(min_add_make_valid(s))