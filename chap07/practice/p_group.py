import re


data = 'お問い合わせは support@example.com まで'
ptn = re.compile(r'[a-z0-9.!#$%&\'*+/=?^_{|}~-]+@[a-z0-9-]+(?:\.[a-z0-9-]+)*', re.IGNORECASE)
print(ptn.sub(r'<a href="mailto:\g<0>">\g<0></a>', data))
