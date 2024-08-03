def make_logger(level):
    def logger(message):
        return str(level + " " + message)
    return logger

print(make_logger("error")("overflow"))
