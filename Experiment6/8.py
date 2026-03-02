all_same = lambda d: len({v for v in d.values()}) == 1

data = {'a': 10, 'b': 10, 'c': 10}

print(all_same(data))