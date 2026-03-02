import re
txt=["a", "ab", "abb", "abbb", "b", "aa", "ba"]
for m in txt:
    if re.match(r"^ab{2,3}$",m):
        print(f'{m} Match')
    else:
        print(f'{m} No Match')
