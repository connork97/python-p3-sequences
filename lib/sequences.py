#!/usr/bin/env python3

def print_fibonacci(length):
    i = 0
    my_list = []
    my_range = [*range(length)]
    while len(my_list) < len(my_range):
        if (i == 0):
            my_list.append(i)
            i += 1
        elif (i == 1):
            my_list.append(i)          
            i += my_list[-2]
        else:
            i = my_list[-1] + my_list[-2]
            my_list.append(i)
    print(my_list)

print_fibonacci(9)