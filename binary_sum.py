a = '101'
b = '1101'
def binary_sum(a, b):
    c = int(a, 2)
    e = int(b, 2)
    sum = 0
    sum = c + e
    return bin(sum)

print(binary_sum(a, b))
