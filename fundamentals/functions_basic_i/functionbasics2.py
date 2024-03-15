# Countdown function
def countdown(n):
    return list(range(n, -1, -1))

# Print and Return function
def print_and_return(arr):
    print(arr[0])
    return arr[1]

# First Plus Length function
def first_plus_length(arr):
    return arr[0] + len(arr)

# Values Greater than Second function
def values_greater_than_second(arr):
    if len(arr) < 2:
        return False
    second_value = arr[1]
    new_list = [val for val in arr if val > second_value]
    print(len(new_list))
    return new_list

# This Length, That Value function
def length_and_value(size, value):
    return [value] * size

# Examples of function calls
print(countdown(5))
print(print_and_return([1, 2]))
print(first_plus_length([1, 2, 3, 4, 5]))
print(values_greater_than_second([5, 2, 3, 2, 1, 4]))
print(values_greater_than_second([3]))
print(length_and_value(4, 7))
print(length_and_value(6, 2))
