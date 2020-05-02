

class LargerNum(str):
    def __lt__(x, y):
        return x+y > y+x

def max_number(nums):
    num = map(str, nums)
    largest_num = ''.join(sorted(num, key=LargerNum))
    if largest_num[0] == '0':
        return '0'
    else:
        return largest_num


if __name__ == "__main__":
    a = [[10,2], [3,30,34,5,9], [4,5,6,7,8,9], [10, 29, 76]]
    for i in a:
        print(max_number(i))