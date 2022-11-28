# Write a function called `choose_func` which takes a list of nums and 2 callback functions.
# If all nums inside the list are positive, execute the first function on that list and return the result of it.
# Otherwise, return the result of the second one

def choose_func(nums: list, func1, func2):
    try:
        if len(list(filter(lambda x: x > 0, nums))) == len(nums):
            return func1(nums)
        else:
            return func2(nums)
    except:
        print(Exception.__doc__)
        return Exception.__name__

# Assertions

nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

def main():
    assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25], 'Bad work for first condition!!!'
    print(f'Good work for first condition!!!')
    assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5], 'Bad work for second condition!!!'
    print(f'Good work for second condition!!!')

if __name__ == '__main__':
    main()
