from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b'''
            <body>
                <button> click me </button>
            </body> ''')

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        res = self.rfile.read(content_length)
        print(res)
        self.send_response(201)
        self.send_header("Content_type", "application/json")
        self.end_headers()
        # json_data = json.loads(res)
        response = {"Data added": "user_data"}
        self.wfile.write(json.dumps(response).encode('utf-8'))

def run(server_class=HTTPServer, handler_class = SimpleRequestHandler, port=8080):
    server_address = ('127.0.0.1', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting HTTP server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
