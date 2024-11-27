from http.server import BaseHTTPRequestHandler, HTTPServer
import json

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]
products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Smartphone", "price": 500}
]

class CRUDHandler(BaseHTTPRequestHandler):
    def __set_headers(self, status = 200):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def __path_parser(self):
        parsed_path = self.path.strip("/").split("/")
        return parsed_path
    
    def do_GET(self):
        parsed_path = self.__path_parser()
        if len(parsed_path) == 1:
            if parsed_path[0] == "users":
                self.__set_headers()
                self.wfile.write(json.dumps(users).encode())
            elif parsed_path[0] == "products":
                self.__set_headers()
                self.wfile.write(json.dumps(products).encode())
            else:
                self.__set_headers(400)
                self.wfile.write(json.dumps({"error": "path not  found"}).encode())
        elif len(parsed_path) == 2:
            self.__set_headers()
            resource, resource_id = parsed_path

            result = next(u for u in eval(resource) if u["id"] == int(resource_id))
            self.wfile.write(json.dumps(result).encode())
        else:
            self.__set_headers(404)
            self.wfile.write(json.dumps({"error": "not found"}).encode())

    
    def do_POST(self):
        parsed_path = self.__path_parser()
        if len(parsed_path) == 1:
            self.__set_headers()
            content_length = int(self.headers["Content-Length"])
            body = json.loads(self.rfile.read(content_length))
            resource = parsed_path[0]
            new_id = max([u['id'] + 1 for u in eval(resource)]) if eval(resource) else 1
            body.update({'id': new_id})
            eval(resource).append(body)
            self.wfile.write(json.dumps(eval(resource)).encode())
            

    def do_PUT(self):
        parsed_path = self.__path_parser()
        if len(parsed_path) == 2:
            resource, resource_id = parsed_path
            resource_id = int(resource_id)
            resource_list = None

            if resource == "users":
                resource_list = users
            elif resource == "products":
                resource_list = products
            else: 
                self.__set_headers(400)
                self.wfile.write(json.dumps({"error": "found"}).encode())
                
            
            content_length = int(self.headers["Content-Length"])
            body = json.loads(self.rfile.read(content_length))

            for item in resource_list:
                if item["id"] == resource_id:
                    item.update(body)
                    self.__set_headers(200)
                    self.wfile.write(json.dumps(item).encode())
                    return
            
            self.__set_headers(404)
            self.wfile.write(json.dumps({"error": "not found"}).encode())

        else:
            self.__set_headers(400)
            self.wfile.write(json.dumps({"error": "wrong path"}).encode())

    
    def do_DELETE(self):
        parsed_path = self.__path_parser()
        if len(parsed_path) == 2:
            resource, resource_id = parsed_path
            resource_id = int(resource_id)
            resource_list = None

            if resource == "users":
                resource_list = users
            elif resource == "products":
                resource_list = products
            else:
                self.__set_headers(400)
                self.wfile.write(json.dumps({"error": "invlaid resource"}).encode())

            for item in resource_list:
                if item["id"] == resource_id:
                    resource_list.remove(item)
                    self.__set_headers(204)
                    self.wfile.write(json.dumps({"message":"deleted"}).encode())

            
            self.__set_headers(404)
            self.wfile.write(json.dumps({"error":"not found"}).encode())
        else:
            self.__set_headers(400)
            self.wfile.write(json.dumps({"error":"wrong path"}).encode())


    
def run(server_class = HTTPServer, server_handler = CRUDHandler, port = 8080):
    server_address = ("127.0.0.1", port)

    httpd = server_class(server_address, server_handler)

if __name__ == "__main__":
    run()



