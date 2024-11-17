class RequestHandler:
    def __init__(self, url):
        self.url = url

    def extract_param(self, name):
        if "?" not in self.url:
            return None

        query_string = self.url.split("?", 1)[1]

        query_param = query_string.split("&")

        for param in query_param:
            key, value = param.split("=", 1)
            if key == name:
                return value


url = "/search?email=test@example.com&name=JohnDoe"

handler = RequestHandler(url)
email = handler.extract_param("email")
print(email)

