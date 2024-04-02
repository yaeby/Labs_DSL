import re

string = '1(0|1)*2(3|4){5}36'
regex = r'([*?+]|\{\d+\})|(\(.*?\)|[A-Za-z0-9])'
# regex =r'\((.*?)\)([*+?]|{\d*,?\d*})'
# regex = r'\((.*?)\)((?:[*+?]|{\d*,?\d*}))|([A-Za-z0-9]+)'
matches = re.findall(regex, string)
print(matches)
