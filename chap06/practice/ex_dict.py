d = {'cucumber': 'きゅうり', 'lettuce': 'レタス', 'spinach': 'ホウレンソウ'}
d['cucumber'] = '胡瓜'
d.pop('spinach')
d.setdefault('carrot', 'ニンジン')

for item in d.items():
    print(item)
