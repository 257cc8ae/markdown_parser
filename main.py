# this file is open the markdown file and preview server
import socketserver
import http.server


def main():
    PORT = 8000
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"server is starting: http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    main()