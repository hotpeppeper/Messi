'''
给出一个区间的集合，请合并所有重叠的区间。
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
'''

def merge(interval):
    interval.sort(key=lambda x: x[0])

    merged = list()
    for inter in interval:
        if not merged or inter[0] > merged[-1][1]:
            #  当前区间与上一个区间没有重合
            merged.append(inter)
        else:
            # 存在重合，则合并
            merged[-1][1] = max(merged[-1][1], inter[1])

    return merged


if __name__ == "__main__":
    ll = [[[1,3],[2,6],[8,10],[15,18]], [[1,4],[4,5]]]
    for l in ll:
        print(merge(l))