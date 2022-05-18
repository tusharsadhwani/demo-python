def has_ten(my_list):
    return any(item == 10 for item in my_list)

my_list = [1, 2, 3]
print(has_ten(my_list))
