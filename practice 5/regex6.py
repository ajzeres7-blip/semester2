import re
txt="Cat ran after mouse, it got tired."
result=re.sub(r'[\s|,|.]', ':', txt)
print(result)