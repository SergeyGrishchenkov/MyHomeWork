# Write a function that takes on an input random ints (between 1 and 10) and returns the longest consecutive
# run and the length of that run of elements of the list.
# Ex. 	def task1(1,2,3,4,4,4,4,4,4,5,6,7,4,2,2,5) -> 6, 4
# 	def task1(1) -> 1, 1
# 	def task1() -> 0, None
import random
def longest_consecutive(count = 30):
    our_tuple = [random.randint(1, 10) for item in range(count + 1)]
    our_set = set(our_tuple)
    our_dic = {}
    for item in our_set:
        our_dic[item] = our_tuple.count(item)
    max_value = max(our_dic.values())
    # на случае, если нескольно ключей с максимальным value, формируем новый словарь
    final_dict = {key: value for key, value in our_dic.items() if value == max_value}
    return final_dict


if __name__ == "__main__":
    count = 1000
    test_results = longest_consecutive(count)
    print(f'For tuple with lengh {count} we have longest consecutive for such numbers:')
    for key, value in test_results.items():
        print(f' -> {key}, {value}')