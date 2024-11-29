# 1.) Recursive Printing
def print_numbers(n):
    if n > 0:
        print_numbers(n - 1)
        print(n)
# A sample function call for testing
print_numbers(10)
#======================================

# 2.) Recursive Multiplication
def multiply(x, y):
    if x == 0 or y == 0:
        return 0
    else:
        return x + multiply(x, y-1)
# Sample function call inside of a print statement for testing
print(multiply(5, 3))
#======================================

# 3.) Recursive Lines
def print_asterisks(n):
    if n > 0:
        print_asterisks(n - 1)
        print('*' * n)
# A sample function call for testing
print_asterisks(5)
#======================================

# 4.) Largest list item
def find_list_largest(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        largest_value = find_list_largest(lst[1:])
        return lst[0] if lst[0] > largest_value else largest_value

# Sample list for testing
list_test = [1, 2, 4, 7, 11, 6, 3]
print(find_list_largest(list_test))
#======================================

# 5.) Recursive List Sum
def sum_list(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

# Sample list for testing
sample_list = [1, 3, 5, 2, 12, 7, 9, 2, 4]
print(sum_list(sample_list)) 
#======================================

# 6.) Sum of numbers
def sum_up_to(n):
    if n <= 0:
        return 0
    else:
        return n + sum_up_to(n - 1)

# Sample function call for testing
print(sum_up_to(8))