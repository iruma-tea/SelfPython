print(all([False, True, False]))
print(any([False, True, False]))
print(not any([False, False, True]))

print(any(['あいう', '', '']))
print(any(['', '', '']))

data = ['さざんか', 'ほうせんか', 'バラ', 'サクラ']
print(any([len(str) > 4 for str in data]))
