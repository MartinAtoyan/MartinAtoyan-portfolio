def make_config(key, value):
    dict = {}
    def ret_dict():
        nonlocal dict
        dict.update({key: value})
        return dict
    return ret_dict()

print(make_config("name", "james"))
print(make_config("surename", "brown"))