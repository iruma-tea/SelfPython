import csv

data = [
    ['山田太郎', '160-9999', '東京都新宿区東町 1-1-1'],
    ['鈴木次郎', '107-1111', '東京都港区西町 2-2-2'],
    ['佐藤花子', '150-2222', '東京都渋谷区南町 3-3-3']
]

with open('./chap07/address.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
    writer.writerows(data)
