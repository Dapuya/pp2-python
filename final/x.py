n = int(input())

data = {}

for i in range(n):
    name, value = input().split()
    value = int(value)

    try:
        data[name] += value
    except KeyError:
        data[name] = value

total = sum(data.values())

data = {
    name: value / total * 100.0
    for name, value in data.items()
}

data_list = list(data.items())

for i in range(len(data_list)):
    for j in range(i + 1, len(data_list)):
        if data_list[i][1] < data_list[j][1]:
            tmp = [*data_list[i]]
            data_list[i] = data_list[j]
            data_list[j] = tmp
        elif data_list[i][1] == data_list[j][1]:
            if data_list[i][0] < data_list[j][0]:
                tmp = [*data_list[i]]
                data_list[i] = data_list[j]
                data_list[j] = tmp

data = dict(data_list)

for name, value in data.items():
    print(name, "%g" % (value) + "%")