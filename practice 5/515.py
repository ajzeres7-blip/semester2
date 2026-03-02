import re
txt=input()
def double_d(match):
    return match.group(0)*2
result=re.sub(r"\d",double_d,txt)
print(result)