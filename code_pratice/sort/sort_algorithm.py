#  插入排序

def insert_sort(array):
    if not array:
        return
    # 从数组的第二个元素开始循环，直到最后一个元素
    for i in range(1, len(array)):
        key_item = array[i]

        # 初始化变量， 用于寻找元素的位置
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

    