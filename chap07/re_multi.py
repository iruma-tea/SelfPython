import re

msg = '10人のインデアン。\n1年生になったら'
ptn = re.compile(r'^\d*', re.MULTILINE)
results = ptn.findall(msg)

for result in results:
    print(result)
