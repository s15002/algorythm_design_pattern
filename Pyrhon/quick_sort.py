LIST_COUNT = 1000
LOOP_COUNT = 10000
MAX_NUM = 10000

def data_generate():
    import random
    return [random.randint(1, MAX_NUM) for _ in range(LIST_COUNT)]

#最初のquick_sort
def quick_sort_1st(data):
    if len(data) < 1:
        return data

    pivot = data[0]
    left = []
    right = []
    for x in range(1, len(data)):
        if data[x] <= pivot:
            left.append(data[x])
        else:
            right.append(data[x])

    left = quick_sort_1st(left)
    right = quick_sort_1st(right)

    return left + [pivot] + right


#参考:「良いもの、悪いもの」
def quick_sort_2nd(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    data_rest = data[1:]

    return quick_sort_2nd([lt for lt in data[1:] if lt < data[0]]) + data[0:1] + quick_sort_2nd([ge for ge in data[1:] if ge >= data[0]])


# 経過時間
if __name__ == '__main__':
    import time
    import sys

    #1st
    start = time.time()

    for _ in range(LOOP_COUNT):
        data = data_generate()
        quick_sort_1st(data)
        print('.', end='')
        sys.stdout.flush()

    end = time.time()
    print()
    print('quick_sort_1st:', (end - start))

    #2nd
    start = time.time()

    for _ in range(LOOP_COUNT):
        data = data_generate()
        quick_sort_2nd(data)
        print('.', end='')
        sys.stdout.flush()

    end = time.time()
    print()
    print('quick_sort_2nd:', (end - start))