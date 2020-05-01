'''
给出一个无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
'''

def merge(intervals, newInterval):
    intervals.append(newInterval)
    intervals.sort(key=lambda x: x[0])

    merged = list()
    for inter in intervals:
        if not merged or merged[-1][1] < inter[0]:
            merged.append(inter)
        else:
            merged[-1][1] = max(merged[-1][1], inter[1])

    return merged


if __name__ == "__main__":
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]

    print(merge(intervals, newInterval))