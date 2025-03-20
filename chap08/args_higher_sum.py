def walk_list(data, func):
    for key, value in enumerate(data):
        func(value, key)


result = 0


def calc_sum(value, key):
    global result
    result += value


data = [105, 53, 27, 87, 33]
walk_list(data, calc_sum)
print(result)
