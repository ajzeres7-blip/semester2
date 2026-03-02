import re
txt="today is fu_ll moo_n"
x=re.compile(r'[a-z]+_[a-z]+').findall(txt)
print(x)