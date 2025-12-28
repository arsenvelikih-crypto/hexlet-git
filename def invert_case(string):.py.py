
def invert_case(string):
    result = ''
    for char in string:
        if char == char.upper():
            result = result + char.lower()
        else:
            result = result + char.upper()
    return result
string = 'hEllo, wORLd'
print(invert_case(string))
