n = 8
def is_perfect(n):
    sum = 0
    for i in range(1, int(n//2)+1):
        if n % i == 0:
            sum = sum + i
            if sum == n:
                print(sum)
                return True
    print(sum)
    return False
print(is_perfect(n))