

def del_dumplicate(s):
    if len(s) == 0 or len(s) == 1:
        return s

    stack_ = list()
    for i in s:
        if stack_ and i == stack_[-1]:
            stack_.pop()
        else:
            stack_.append(i)

    return ''.join(stack_)

ss = ['abbaca', 'aaabbca', 'abcacbacb', 'abcbbcb', 'aaaaaaaaaa', 'abbaabbcca']
for s in ss:
    print(del_dumplicate(s))