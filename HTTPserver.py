import http.server
import socketserver

socketserver.TCPServer.allow_reuse_address = True

PORT = 8080

page = """<html>
  <head>
    <title>Hello World</title>
  </head>
  <body>Hello World</body>
</html>"""

class myHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/hello":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(page.encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()


Handler = http.server.SimpleHTTPRequestHandler

with http.server.HTTPServer(("127.0.0.1", PORT), myHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()