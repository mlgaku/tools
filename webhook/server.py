import os
import hmac
from json import loads
from http.server import HTTPServer, BaseHTTPRequestHandler

class HTTPHandler(BaseHTTPRequestHandler):
    def _send_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._send_headers()
        self.wfile.write(b'Meow..Meow...')

    def do_POST(self):
        post_data = self.rfile.read(int(self.headers['Content-Length']))

        secret = config.get('ENFORCE_SECRET', '')
        if secret:
            header_signature = self.headers['X-Hub-Signature']
            if header_signature is None:
                return

            sha_name, signature = header_signature.split('=')
            if sha_name != 'sha1':
                return

            mac = hmac.new(secret.encode(), msg=post_data, digestmod='sha1')
            if not hmac.compare_digest(str(mac.hexdigest()), str(signature)):
                return

        os.system('bash scripts/%s.sh >> log.txt &' % loads(post_data.decode('utf-8'))['repository']['name'])

        self._send_headers()
        self.wfile.write(b'Ok')

with open('.env', 'r') as f:
    config = loads(f.read())

httpd = HTTPServer(('127.0.0.1', 8782), HTTPHandler)
httpd.serve_forever()
