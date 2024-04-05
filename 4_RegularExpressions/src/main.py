import re
import random
from infinity_constant import LIMIT

def processing_regex(matches: list[any]) -> None:
    print(matches)

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
        count = random.randint(0, LIMIT)
        for _ in range(count):
            element = random.choice(elements)
            substring += element
    elif condition == '+':
        count = random.randint(1, LIMIT)
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
with open('input.txt', 'r') as input_file:
    regexes = input_file.readlines()

with open('output.txt', 'w') as output_file:
    for regex in regexes:
        output_file.write("\nGenerated strings for regex '" + regex.strip() + "' :\n") 
        for i in range(0, 5):
            output_file.write(generate_string(regex) + '\n')

regex = regexes[1]
#TODO: Get matches and generated string 2 different functions