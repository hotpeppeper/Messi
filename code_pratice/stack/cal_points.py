

def cal_points(ops):
    stack_ = list()
    for i in ops:
        if i == 'C':
            if stack_:
                stack_.pop()
        elif i == 'D':
            stack_.append(2 * stack_[-1])
        elif i == '+':
            stack_.append(stack_[-1] + stack_[-2])
        else:
            stack_.append(int(i))

    return sum(stack_)

s = [["5","2","C","D","+"], ["5","-2","4","C","D","9","+","+"]]
for i in s:
    print(cal_points(i))