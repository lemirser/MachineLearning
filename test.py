from functools import reduce


def multiply_by2(li: list) -> list:
    return li * 2


def odd_only(li: list) -> list:
    return li % 2 != 0


def accumulator(acc: int, item: int) -> int:
    return acc + item


my_list = [2, 4, 6, 8]
new_list = [1, 2, 3, 4, 5, 6]
my_set = {i for i in range(0, 10)}
user_info = ["name", "age", "gender"]
user_details = ["dru", 10, "male"]


user_info2 = ["name", "age", "gender"]
user_details2 = [["dru", 10, "male"], ["test", 30, "male"]]
new_det = {}

# map computes the iterable and return the output based on the condition of the  given function
# print(list(map(multiply_by2, [1, 2, 3])))

# filter return all the True value based on the condition of the given function
# print(list(filter(odd_only, [1, 2, 3, 4, 5])))

# zip combines iterable into a tuple inside a list
# print(list(zip(my_list, new_list)))

# reduce
# print(reduce(accumulator, my_list, 0))

# list comprehensions
# print([["".join(i + str(item)) for i in "hello"] for item in new_list])

# set comprehension
my_set = {i for i in range(0, 10)}
# print(my_set)

# dictionary comprehension
my_dict = {key: value ** 2 for key, value in enumerate(range(0, 10))}
user = {k: v for k, v in zip(user_info, user_details)}
# print(my_dict)
# print(user)


for index, row in enumerate(user_details2):
    for item in user_info2:
        new_det[index] = dict(name=row[0], age=row[1], gender=row[2])

print(new_det)

my_dict = {num: num * 2 for num in [1, 2, 3]}
print(my_dict)

some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

duplicates = {i for i in some_list if some_list.count(i) > 1}
print(duplicates)
