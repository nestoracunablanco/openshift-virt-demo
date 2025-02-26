import http.server
import socketserver
import logging
import time
import threading

PORT = 8080

logging.basicConfig(
    filename='app.log',  # Log file name
    level=logging.INFO,   # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)

def log_periodically():
    while True:
        logging.info("This is a periodic log message.")
        time.sleep(1)  # Log every second

# Start the logging thread
threading.Thread(target=log_periodically, daemon=True).start()

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

