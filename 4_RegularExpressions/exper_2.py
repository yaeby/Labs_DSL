import re
import random

def generate_string(regex):
    generated_string = ""
    matches = re.findall(r'(\{.*?\})|([*?+])|\((.*?)\)|([A-Za-z0-9])', regex)
    
    for i in range(len(matches)):
        current_set = matches[i]
        
        # Check if the next set is empty at index 0 or 1
        if i + 1 < len(matches) and not matches[i + 1][0] and not matches[i + 1][1]:
            if current_set[2]:  # If the set is non-empty at index 2
                generated_string += random.choice(current_set[2].split('|'))
            elif current_set[3]:  # If the set is non-empty at index 3
                generated_string += current_set[3]
        
        # Check if the next set is non-empty at index 2
        elif i + 1 < len(matches) and matches[i + 1][1] == '+':
            # Generate random numbers of the element from 1 to 5
            count = random.randint(1, 5)
            generated_string += current_set[2] * count
        
        # Check if the next set is non-empty at index 2 and the element is '?'
        elif i + 1 < len(matches) and matches[i + 1][1] == '?':
            # Decide randomly whether to include the element
            if random.choice([True, False]):
                generated_string += current_set[2]
        
        # Check if the next set is non-empty at index 2 and the element is '*'
        elif i + 1 < len(matches) and matches[i + 1][1] == '*':
            # Generate random numbers of the element from 0 to 5
            count = random.randint(0, 5)
            generated_string += current_set[2] * count
            
        # Check if the next set is non-empty at index 2 and the element is '{'
        elif i + 1 < len(matches) and matches[i + 1][1] == '{':
            # Extract min and max count from the curly braces
            min_count, max_count = map(int, matches[i + 1][0].strip('{}').split(','))
            count = random.randint(min_count, max_count)
            generated_string += current_set[2] * count
        
        # Check if the next set is non-empty at index 2 and the element is '}'
        elif i + 1 < len(matches) and matches[i + 1][1] == '}':
            continue
        
    return generated_string

# Test the function with the provided regular expression
regex = r'1(0|1)*2(3|4){5}36'
print("Generated string for regex '{}':".format(regex))
print(generate_string(regex))
