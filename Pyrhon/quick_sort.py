LOOP_COUNT = 5000
LIST_COUNT = 1000
MAX_NUM = 10000

def data_generate():
    import random
    return [random.randint(1, MAX_NUM) for _ in range(LIST_COUNT)]

def quick_sort(data):
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

        left = quick_sort(left)
        right = quick_sort(right)

        return left + [pivot] + right


if __name__ == '__main__':
    import time
    import sys

    start = time.time()

    for _ in range(LOOP_COUNT):
        data = data_generate()
        quick_sort(data)
        print('.', end =' ')
        sys.stdout.flush()

    end = time.time()
    print('quick_sort')
    print('elapsed_time', (end-start))
    print('average_time', ((end-start) / 10000))
