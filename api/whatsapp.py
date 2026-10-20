import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
from xml.sax.saxutils import escape
import _core as c
class handler(BaseHTTPRequestHandler):
    def do_POST(self):  # Twilio WhatsApp webhook (form-encoded)
        f = parse_qs(self.rfile.read(int(self.headers.get("Content-Length") or 0)).decode())
        st = c.load(None); reply, _, _ = c.handle(st, "wa" + c.norm(f.get("From", ["x"])[0]), f.get("Body", [""])[0]); c.save(st)
        b = f"<Response><Message>{escape(reply)}</Message></Response>".encode()
        self.send_response(200); self.send_header("Content-Type", "text/xml"); self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)
