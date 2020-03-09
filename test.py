def multiply_by2(li: list) -> list:
    return li * 2


def odd_only(li: list) -> list:
    return li % 2 != 0


my_list = ["a", "b", "c", "d", "e"]
new_list = [1, 2, 3, 4, 5]

# map computes the iterable and return the output based on the condition of the  given function
print(list(map(multiply_by2, [1, 2, 3])))

# filter return all the True value based on the condition of the given function
print(list(filter(odd_only, [1, 2, 3, 4, 5])))

# zip combines iterable into a tuple inside a list
print(list(zip(my_list, new_list)))
