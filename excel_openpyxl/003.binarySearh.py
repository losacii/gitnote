import time

def binarySearch(arr, x, left=0, right=0):
    right = len(arr) - 1

    while left <= right:

        mid = int(left + (right - left) / 2)

        if arr[mid] == x:
            print('found {} in position {}'.format(x, mid))
            return mid

        elif arr[mid] < x:
            left = mid + 1
            print("range set to {} ~ {}".format(left, right))

        elif arr[mid] > x:
            right = mid - 1
            print("range set to {} ~ {}".format(left, right))

    return -1

def binarySearch1(arr, x, left=0, right=0):
    # step count, time count
    step = 0
    start_time = time.time()

    if right == 0:
        right = len(arr) - 1

    while left <= right:
        step += 1

        mid = int(left + (right - left) / 2)

        if arr[mid] == x:
            print('step {}: found {} in position {}, time consumed {:.3f}'.format(step, x, mid, time.time() - start_time))
            return mid

        elif arr[mid] < x:
            left = mid + 1
            print("set range to {} ~ {}".format(left, right))

        elif arr[mid] > x:
            right = mid - 1
            print("set range to {} ~ {}".format(left, right))

    return -1

res = binarySearch1(range(2048000), 1299, 5, 3000)
print("result:", res)
