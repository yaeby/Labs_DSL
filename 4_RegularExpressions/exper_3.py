import re
import random

# def generate_new_string(s, length):
#     # Extract groups within parentheses
#     groups = re.findall(r'([A-Za-z0-9])', s)
#     print(groups)
#     # Generate the new string randomly
#     new_string = ''
#     for _ in range(length):
#         chosen_group = random.choice(groups)
#         new_string += ''.join(random.choice(chosen_group) for _ in range(len(chosen_group)))
    
#     return new_string

def generate_new_string(string_list, length):
    generated_string = ''
    for _ in range(length):
        chosen_element = random.choice(string_list)
        generated_string += chosen_element
    return generated_string

# Test with your examples
s1 = '(0|12)'
s2 = '(UV|W|X)'
# print(generate_new_string(s1, 10))
# print(generate_new_string(s2, 20))

# s1 = s1[1:-1]
list = s1[1:-1].split('|')
print(list)
string = generate_new_string(list, 5)
print(string)

s2 = s2[1:-1]
list = s2.split('|')
print(list)
string = generate_new_string(list, 10)
print(string)

set = ('', '1')
s = set[1]
if s:
    print("Strng is not empty: " + s)
else:
    print("string is empty")

str = ['EVC', 'EV', 'EF']
substring = ''
substring += random.choice(str) * 10
print(substring)