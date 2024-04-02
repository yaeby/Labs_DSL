import re
import random

def generate_string(regex):
    generated_string = ""
    matches = re.findall(r'([*?+]|\{\d+\})|\((.*?)\)|([A-Za-z0-9])', regex)
    print(matches)
    # for i in range(len(matches)):
    #     match = matches[i]
    #     next_match = matches[i+1]
    #     if match[2] or match[3]:
    #         if next_match[0]:

    #         elif next_match[2]:
    #         else:


    # for match in matches:
    #     if match[0]  or :
    #         generated_string += random.choice(match[0].split('|'))
    #     elif match[1]:
    #         generated_string += random.choice(match[1].split(','))
    #     # elif match[2]:
    #     #     generated_string += match[2]
    # return generated_string
                                                                                                                                                                                                 
# Test the function with the provided regular expressions
regexes = [
    '(a|b)(c|d)E+G?',
    'P(Q|R|S)T(UV|W|X)*Z+',
    '1(0|1)*2(3|4){5}36'
]

for regex in regexes:
    print("Generated string for regex '{}':".format(regex))
    for i in range(0,5):
        print(generate_string(regex))
