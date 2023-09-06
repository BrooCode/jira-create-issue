import http.server
import socketserver

# Specify the port you want to use
port = 8000

# Define the request handler (serves files from the current directory)
handler = http.server.SimpleHTTPRequestHandler

# Create an HTTP server
httpd = socketserver.TCPServer(("", port), handler)

print(f"Serving HTML file on port {port}")

# Start the server
httpd.serve_forever()
