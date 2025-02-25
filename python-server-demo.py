import http.server
import socketserver

PORT = 8080

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)  # Send HTTP status code 200 (OK)
        self.send_header("Content-type", "text/html")  # Set the content type
        self.end_headers()  # End the headers

        # Write the response body
        self.wfile.write(b"<html><body>")
        self.wfile.write(b"<h1>Openshift Virt Demo</h1>")
        self.wfile.write(b"<p>This is a demo web server</p>")
        self.wfile.write(b"</body></html>")

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()

