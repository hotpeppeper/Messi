'''
以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。
输入："/a/./b/../../c/"
输出："/c"

输入："/home//foo/"
输出："/home/foo"
解释：在规范路径中，多个连续斜杠需要用一个斜杠替换。
'''

def simplify_path(path):
    stack_ = list()
    path_char = path.split('/')
    for char in path_char:
        if char == '.' or char == '':
            continue
        if char == '..':
            if stack_:
                stack_.pop()
        else:
            stack_.append(char)

    return '/' + '/'.join(stack_)

path_ = ['/home/', '/../', '/home//foo/', '/a/./b/../../c/', '/a/../../b/../c//.//', '/a//b////c/d//././/..']
for c in path_:
    print(simplify_path(c))