# modify the string by reversing portions of it whenever the character 'i'

def string_modification(input):
    out = ""
    right_part= ""
    left_part = ""
    end_pointer = 0
    for index,char in enumerate(input):
        if char == 'i':
            right_part+=input[end_pointer:index:][::-1]
            end_pointer = index+1
    left_part = input[end_pointer::]
    out = right_part + left_part
    return out

print(string_modification("stringify"))

# if stringify -> "rtsgnfy"


# def string_modification(input):
#     out = ""
#     for char in input:
#         if char != 'i':
#             out += char
#         else:
#             out = out[::-1]
#     return out
# print(string_modification("stringify"))

# if stringify -> "gnstriify"