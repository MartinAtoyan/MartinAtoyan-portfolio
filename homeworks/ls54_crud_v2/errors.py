
class ValidationError(Exception):
    def __init__(self, error="Validation error."):
        self.error = error

class FileError(Exception):
    def __init__(self, error="File error."):
        self.error = error

class NotFoundError(Exception):
    def  __init__(self, error="Not found error."):
        self.error = error

