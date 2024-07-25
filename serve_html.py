import http.server
import socketserver

PORT = 8000

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple HTML Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a simple HTML page served by a Python script.</p>
</body>
</html>
"""

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(html_content, "utf8"))

handler = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
