num = '123321'
def second_half(num):
    sum = 0
    result = False
    for i in range(len(num)//2):
        sum = sum +(int(num) % 10)
        num = int(num)//10
    return sum
def first_half(num):
    rum = 0
    index = 0
    while index < len(num) / 2:
        rum = rum + int(num[index])
        index += 1
    return rum
def is_happy_ticket(num):
    if first_half(num) == second_half(num):
        return True
    return False
print(is_happy_ticket(num))