# python -m SimpleHTTPPutServer 8080
import SimpleHTTPServer
import BaseHTTPServer

from urlparse import urlparse

class SputHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_PUT(self):
        # print self.headers
        length = int(self.headers["Content-Length"])
        path = self.translate_path(self.path)
        query = urlparse(self.path).query
        append = 0
        if query:
            query_components = dict(qc.split("=") for qc in query.split("&"))
            append = query_components["append"]
        mode = "ab" if append == "1" else "wb"
        print "append=", append, "mode=", mode
        with open(path, mode) as dst:
            dst.write(self.rfile.read(length))
        self.send_response(200)

if __name__ == '__main__':
    SimpleHTTPServer.test(HandlerClass=SputHTTPRequestHandler)
