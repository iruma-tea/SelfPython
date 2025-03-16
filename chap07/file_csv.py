import csv


with open('./chap07/data.tsv', encoding='utf-8') as file:
    for row in csv.reader(file, delimiter='\t'):
        for cell in row:
            print(cell)
        print('----------')
