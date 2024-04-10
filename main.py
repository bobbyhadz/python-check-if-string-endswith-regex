# Check if string ends with a substring using Regex in Python

import re

string = 'bobbyhadz.com'

match = re.search(r'\.com$', string)
print(match)  # 👉️ <re.Match object; span=(9, 13), match='.com'>

if match is not None:
    print('The string ends with the regex')

    print(match.group())  # 👉️ .com

    print(match.start())  # 👉️ 9
else:
    print('The string does NOT end with the regex')