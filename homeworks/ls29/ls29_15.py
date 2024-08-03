def manipulate_string(s, operation):
    def uppercase(s):
        return s.upper()

    def lowercase(s):
        return s.lower()

    def title(s):
        return s.title()

    def reverse(s):
        return s[::-1]

    dict_of_str_func = {
        "uppercase": uppercase(s),
        "lowercase": lowercase(s),
        "title": title(s),
        "reverse": reverse(s)
    }
    if operation in dict_of_str_func.keys():
        return dict_of_str_func[operation]
    return "String doesn't have this function"


str = "Hello world"
print(manipulate_string(str, "uppercase"))
print(manipulate_string(str, "lowercase"))
print(manipulate_string(str, "title"))
print(manipulate_string(str, "reverse"))
print(manipulate_string(str, "reverokl"))