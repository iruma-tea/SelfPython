try:
    num = input('数値を入力してください：')
    print('２倍すると...', float(num) + 2)
except ValueError as ex:
    print('エラー発生:', ex)
