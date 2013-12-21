import string, cgi, time
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import piringo

class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()

			if self.path.endswith("/"):
				f = open(curdir + sep + "/index.html")
				self.wfile.write(f.read())
				f.close()
				return

			if self.path.endswith(".html"):
				f = open(curdir + sep + self.path)
				self.wfile.write(f.read())
				f.close()
				return

			if self.path.endswith("slowcircuit"):
				self.wfile.write("Slow circuit")
				piringo.circuit(0.2)
				return

			if self.path.endswith("fastcircuit"):
				self.wfile.write("Fast circuit")
				piringo.circuit(0.05)
				return

			if self.path.endswith("superfastcircuit"):
				self.wfile.write("Super fast circuit")
				piringo.circuit(0.01)
				return

			if self.path.endswith("stars"):
				self.wfile.write("Stars")
				piringo.stars(0.2)
				return

			if self.path.endswith("stars"):
				self.wfile.write("Stars")
				piringo.stars(0.2)
				return

			if self.path.endswith("randomone"):
				self.wfile.write("Random with one pin")
				piringo.randomPins(1, 0.2)
				return

			if self.path.endswith("randomtwo"):
				self.wfile.write("Random with two pins")
				piringo.randomPins(2, 0.2)
				return

			if self.path.endswith("randomthree"):
				self.wfile.write("Random with three pins")
				piringo.randomPins(3, 0.2)
				return

			if self.path.endswith("sequenceone"):
				self.wfile.write("Sequence one")
				piringo.sequenceOne()
				return

			return

		except IOError:
			self.send_error(404, 'File not found: %s' % self.path)

def main():
	try:
		server = HTTPServer(('', 8081), MyHandler)
		print 'Started http server...'

		piringo.setup()

		server.serve_forever()

	except KeyboardInterrupt:
		print '^C received, shutting down'
		server.socket.close()

if __name__ == '__main__':
	main()
