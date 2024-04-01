import re

string = r'1(0|1){4}2(3|4){0,5}(3|6)36'
# regex =r'\((.*?)\)([*+?]|{\d*,?\d*})'
regex = r'\((.*?)\)((?:[*+?]|{\d*,?\d*}))'
matches = re.findall(regex, string)
print(matches)
