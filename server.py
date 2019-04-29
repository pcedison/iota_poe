import SimpleHTTPServer
import SocketServer
from send import transfer

PORT = 8000

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_POST(self):
      content_len = int(self.headers.getheader('content-length', 0))
      post_body = self.rfile.read(content_len)
      txn_hash = transfer(post_body)
      self.wfile.write(txn_hash)

Handler = ServerHandler
httpd = SocketServer.TCPServer(("0.0.0.0", PORT), Handler)
print "serving at port", PORT
httpd.serve_forever()
