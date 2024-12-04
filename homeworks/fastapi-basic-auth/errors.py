class ValidationError(Exception):
    def __init__(self, error="Your data isn't correct"):
        self.error = error
        super().__init__(self.error)
    
class FileError(Exception):
    def __init__(self, error="Your file is missing, corrupted or unreadable."):
        self.error = error
        super().__init__(self.error)

class NotFoundError(Exception):
    def __init__(self, error="Not found"):
        self.error = error
        super().__init__(self.error)