import re
txt='Some_Type_Of_Case'
x=re.split(r'[_]',txt)
print(''.join(x))