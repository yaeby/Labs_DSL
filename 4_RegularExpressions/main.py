import re
import random

def generate_substring(expresion:str, condition:str) -> str:
    substring = ''

    if expresion.startswith('(') and expresion.endswith(')'):
        elements = expresion[1:-1].split('|')
    else:
        elements = expresion

    if condition.startswith('{') and condition.endswith('}'):
        count = int(condition[1:-1])
        for _ in range(count):
            substring += random.choice(elements)
    elif condition == '*':
        count = random.randint(0, 5)
        for _ in range(count):
            element = random.choice(elements)
            substring += element
    elif condition == '+':
        count = random.randint(1, 5)
        for _ in range(count):
            element = random.choice(elements)
            substring += element
    elif condition == '?':
        if random.choice([True, False]):
            substring = random.choice(elements)
    else:
        substring = random.choice(elements)

    return substring

def generate_string(regex:str) -> str:
    generated_string = ""
    matches = re.findall(r'([*?+]|\{\d+\})|(\(.*?\)|[A-Za-z0-9])', regex)
    # print(matches)
    for i in range(len(matches)):
        expresion = matches[i][1]
        if i == len(matches)-1:
            condition = ''
        else:
            condition = matches[i + 1][0]
        # print(expresion, condition)

        if expresion and condition:
            # Code for the first condition
            # print("Both sets are not empty.")
            generated_string += generate_substring(expresion, condition)
            
        elif expresion:
            # Code for the second condition
            # print("Current set is not empty.")
            generated_string += generate_substring(expresion, '')

    return generated_string
                                                                                                                                                                                                 
# Test the function with the provided regular expressions
regexes = [
    '(a|b)(c|d)E+G?',
    'P(Q|R|S)T(UV|W|X)*Z+',
    '1(0|1)*2(3|4){5}36'
]

for regex in regexes:
    print("\nGenerated string for regex '{}':".format(regex))
    for i in range(0,5):
        print(generate_string(regex))
