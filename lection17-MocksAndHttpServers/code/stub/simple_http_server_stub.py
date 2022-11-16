#!/usr/bin/env python3

import json
import os
import random
from http.server import BaseHTTPRequestHandler, HTTPServer


class AgeStubHandleRequests(BaseHTTPRequestHandler):
    data = None

    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        location = self.path.split('/')
        if len(location) == 3 and location[1] == 'get_age' and isinstance(location[2], str):
            self._set_headers(200)
            self.wfile.write(json.dumps(random.randint(18, 105)).encode())
        else:
            self._set_headers(500)
            self.wfile.write(b'error')


if __name__ == '__main__':
    host = os.environ.get('STUB_HOST', '127.0.0.1')
    port = int(os.environ.get('STUB_PORT', 4444))

    server = HTTPServer((host, port), RequestHandlerClass=AgeStubHandleRequests)
    server.allow_reuse_address = True

    server.serve_forever()
