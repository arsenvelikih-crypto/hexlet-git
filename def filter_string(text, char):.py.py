text = 'family'
char = 'm'
def filter_string(text: str, char: str):
    result = ''
    i = 0
    while i < len(text):
        if text[i].lower() != char.lower():
            result += text[i]
        i += 1
    return result


print (filter_string(text, char))