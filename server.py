import string, cgi, time
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import piringo

class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
                try:
                        if self.path.endswith(".html"):
                                f = open(curdir + sep + self.path)
                                self.send_response(200)
                                self.send_header('Content-type', 'text/html')
                                self.end_headers()
                                self.wfile.write(f.read())
                                f.close()
                                return

                        if self.path.endswith("circuit.py"):
                                self.send_response(200)
                                self.send_header('Content-type', 'text/html')
                                self.end_headers()
                                self.wfile.write("Running full circle")
                                piringo.piringoFullCircuit()
                                return

                        return

                except IOError:
                        self.send_error(404, 'File not found: %s' % self.path)

def main():
        try:
                server = HTTPServer(('', 8080), MyHandler)
                print 'Started http server...'

                piringo.piringoSetup()

                server.serve_forever()

        except KeyboardInterrupt:
                print '^C received, shutting down'
                server.socket.close()

if __name__ == '__main__':
        main()
