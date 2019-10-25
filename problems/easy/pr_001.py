from random import randrange
from time import perf_counter

"""
Given a list of numbers and a number k, 
return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, 
return true since 10 + 7 is 17.

Can you do this in one pass?
"""

def fn(numbers, k):
    start = 0
    end = len(numbers)

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            sum = numbers[i] + numbers[j]

            if sum == k:
                return True

    return False

def fn_one_pass(numbers, k):
    d = dict()

    for i in range(len(numbers)):
        d[k - numbers[i]] = numbers[i]

        if k - numbers[i] in d:
            return True


def main():
    max_count = 10000000
    
    numbers = [randrange(max_count) for i in range(max_count)]
    k = randrange(max_count + max_count)

    start = perf_counter()
    print(fn(numbers, k))
    end = perf_counter()

    print(f'Using two for loops, it took {end - start} sec')

    start = perf_counter()
    print(fn_one_pass(numbers, k))
    end = perf_counter()

    print(f'Using dictionary, it took {end - start} sec')

if __name__ == "__main__":
    main()
