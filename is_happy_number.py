def sum_of_square_digits(number):
    return sum(int(x) ** 2 for x in str(number))


# BEGIN (write your solution here)
def is_happy_number(num):
    i = 0
    result = 0
    while i <= 10:
        result = sum_of_square_digits(num)
        num = result
        i += 1
        if result == 1:
            return True
    return False
