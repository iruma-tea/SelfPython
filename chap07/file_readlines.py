with open('./chap07/sample.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()

for line in data:
    print(line, end='')
