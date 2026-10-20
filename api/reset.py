import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from http.server import BaseHTTPRequestHandler
import _core as c
class handler(BaseHTTPRequestHandler):
    def do_POST(self): c.run(self, c.api_reset)
    def do_GET(self): c.run(self, c.api_reset)
