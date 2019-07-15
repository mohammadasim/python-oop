l = lambda x: x > 5
"""
In the above example lambda is a function that takes x
and returns it only when x > 5
The above can be defined as a function as follows
"""

# def l(x):
#    return x > 5


# print(l(6))

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def alter(values, check):
    return [value for value in values if check(value)]


"""
My understanding of lambda
lambda x: (This is like a function definiation without the key word def.
lambda as a function is taking the input x
x % 2 != 0, is like the body of a normal function
The return of value of the function is whatever is the outcome of the body of the function
Check examples below
"""

print(alter(my_list, lambda x: x % 2 != 0))

# lambda function to finding the square root of a number

sqr_root = lambda x: x ** (1 / 2)

print(sqr_root(49))

# lambda function for finding square of a number

square = lambda x: x ** 2

print(square(55))


def remove_numbers(values, check):
    return [value for value in values if check(value)]


my_input = [1, 2, 3, 'a', 'b', 'c', 'd', 4, 5, 6]

print(remove_numbers(my_input, lambda x: not isinstance(x,int)))

