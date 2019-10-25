import math
import string
import random
from time import perf_counter_ns, perf_counter

def swap(l, s, e):
    t = l[s]
    l[s] = l[e]
    l[e] = t

    return l


def reverse(s):
    ret_val = []
    size = len(s)

    for i in range(len(s), 0, -1):
        ret_val.append(s[i - 1])

    return ''.join(ret_val)

def reverse_v2(s):
    ret_val = []
    half_size = math.floor(len(s) / 2)
    start = 0
    end = len(s) - 1
    l = list(s)

    for i in range(half_size):
        l = swap(l, start, end)

        start += 1
        end -= 1

    return ''.join(l)

def main():
    max_size = 100000
    s = ''.join(random.choice(string.ascii_letters) for i in range(max_size))

    start = perf_counter()
    reverse(s)
    end = perf_counter()
    print(f'With reverse v1, it took {end - start} s')

    start = perf_counter()
    reverse_v2(s)
    end = perf_counter()
    print(f'With reverse v2, it took {end - start} s')


if __name__ == "__main__":
    main()