def has_ten(my_list):
    for item in my_list:
        if item == 10:
            return True

    return False


my_list = [1, 2, 3]
print(has_ten(my_list))
