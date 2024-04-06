import random
import re
from infinity_constant import LIMIT

class Regex:
    def __init__(self):
        pass

    '''
    Returns a list of sets with the elements and conditions of an regex

    For regex (a|b)(c|d)E+G? matches will be: 
    [('', '(a|b)'), ('', '(c|d)'), ('', 'E'), ('+', ''), ('', 'G'), ('?', '')]
    '''
    def get_matches(self, regex: str) -> list:
        matches = re.findall(r'([*?+]|\{\d+\})|(\(.*?\)|[A-Za-z0-9])', regex)
        return matches
    
    '''
    Sequence of processing regular expression
    Prints step by step what are doing first, second and so on.
    '''
    def process_regex(self, regex: str) -> None:
        step = 1
        matches = self.get_matches(regex)
        # print(matches)
        print(f"\nSequence of processing the following regular expression: {regex}")
        for i in range(len(matches)):
            expression = matches[i][1]
            if i == len(matches)-1:
                condition = ''
            else:
                condition = matches[i + 1][0]

            if expression and condition:
                print("Step " + str(step) + ":")
                print(f'Looking at {expression}{condition}')
                step += 1
            elif expression:
                print("Step " + str(step) + ":")
                print(f'Looking at {expression}')
                step += 1
    
    '''
    Additional for def generate_string

    Checks each condition (for example: *, +, ? or none)
    and generates the substring, returning it to string
    '''
    def generate_substring(self, expression: str, condition: str) -> str:
        substring = ''

        if expression.startswith('(') and expression.endswith(')'):
            elements = expression[1:-1].split('|')
        else:
            elements = expression

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

    '''
    Generates valid combinations of symbols conform a given regular expressions
    '''
    def generate_string(self, regex: str) -> str:
        generated_string = ""
        matches = self.get_matches(regex)

        for i in range(len(matches)):
            expression = matches[i][1]
            if i == len(matches)-1:
                condition = ''
            else:
                condition = matches[i + 1][0]
            # print(expression, condition)

            if expression and condition:
                generated_string += self.generate_substring(expression, condition)
                
            elif expression:
                generated_string += self.generate_substring(expression, '')

        return generated_string
