# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****

def hollow_square(n):
    result = ""
    
    for row in range(n):
        for col in range(n):
            if row == 0 or row == n - 1 or col == 0 or col == n - 1:
                result += "*"
            else:
                result += " "
        if row != n - 1:
            result += "\n"

    return result



# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""

    for row in range(1, n + 1):
        for col in range(1, 1 + row):
            result += str(col)
        if row != n:
            result += "\n"
    
    return result

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total

# Example for n = 4:
#    *
#   ***
#  ***** 
# *******
def centered_star_pyramid(n):
    result = ""
    for i in range(1, n + 1):
        spaces = n - i
        stars = 2 * i - 1
        result += " " * spaces + "*"
        if i != n:
            result += "\n"

    return result
