def make_memoize(f):
    memory = dict()
    def memorized_fn(*args):
        if args in memory:
            return memory[args]
        memory[args] = f(*args)
        return memory[args]
    return memorized_fn


