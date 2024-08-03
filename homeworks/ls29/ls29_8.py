def make_greeting(greeting):
    def fn(name):
        return str(greeting + name)
    return fn

print(make_greeting("Hello ")("James"))

