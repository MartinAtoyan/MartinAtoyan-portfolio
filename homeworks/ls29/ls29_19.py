def mean(data):
    return sum(data) / len(data)


def median(data):
    if len(data) % 2 == 0:
        sorted_data = sorted(data)
        mid1 = data[(len(data) - 1) // 2]
        mid2 = data[len(data) // 2]
        return (mid1 + mid2) / 2
    elif len(data) % 2 != 0:
        return data[len(data) // 2]


def mode(data):
    dict = {}
    for i in data:
        if not i in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    lst = list(dict.values())
    max_count = max(lst)
    return max_count

def analyze_data(data, operation):

    dict_of_func = {
        "mean" : mean,
        "median" : median,
        "mode" : mode
    }

    if operation in dict_of_func.keys():
        return dict_of_func[operation](data)

lst = [1, 2, 3, 4, 5]

print(analyze_data(lst, "mean"))
print(analyze_data(lst, "median"))
print(analyze_data(lst, "mode"))

