import os
from flask import Flask, request, jsonify, Response
from xml.sax.saxutils import escape
import core as c
app = Flask(__name__)
HERE = os.path.dirname(os.path.abspath(__file__))
def wrap(fn):
    def view():
        try: return jsonify(fn(request.get_json(silent=True) or {}))
        except Exception as e: return jsonify(error=str(e)), 500
    view.__name__ = "v_" + fn.__name__
    return view
for name in ["chat", "state", "decide", "reset", "telegram"]:
    app.add_url_rule("/api/" + name, view_func=wrap(getattr(c, "api_" + name)), methods=["GET", "POST"])
@app.route("/api/whatsapp", methods=["POST"])
def whatsapp():  # Twilio WhatsApp webhook
    st = c.load(None)
    reply, _, _ = c.handle(st, "wa" + c.norm(request.form.get("From", "x")), request.form.get("Body", ""))
    c.save(st)
    return Response(f"<Response><Message>{escape(reply)}</Message></Response>", mimetype="text/xml")
@app.route("/")
def home():
    return open(os.path.join(HERE, "public", "index.html"), encoding="utf-8").read()
