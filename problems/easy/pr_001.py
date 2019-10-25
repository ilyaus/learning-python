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

            print("{} + {} = {}".format(numbers[i], numbers[j], sum))

            if sum == k:
                return True

    return False

def fn_one_pass(numbers, k):
    """
    
    """

def main():
    numbers = [10, 15, 3, 7]
    k = 17

    print(fn(numbers, k))


if __name__ == "__main__":
    main()
