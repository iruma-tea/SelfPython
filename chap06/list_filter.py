data = [
    'フレンチブルドック',
    'ヨークシャーテリア',
    'ダックスフント',
    'ポメラニアン',
    'コーギー'
]

result = filter(lambda v: len(v) < 8, data)
print(list(result))
