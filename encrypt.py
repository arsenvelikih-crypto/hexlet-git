
text = 'python'
# способ решения задачи через список

text_list = list(text)
def encrypted(text):
    for i in range(1, len(text_list), 2):
        current_char = text_list.pop(i)
        text_list.insert(i-1, current_char)
    print("".join(text_list))
print(encrypted(text))


# способ решения задачи без списков

def encrypt(text):
    new_text = ""
    i = 0
    for i in range(1, len(text), 2):
        new_text += (text[i] + text[i - 1])
        if len(text) % 2 != 0:
            return new_text + text[-1]
    return new_text