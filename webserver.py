from flask import *
from threading import Thread
app = Flask(__name__)
@app.route("/")
def home():
  return 'all is fine'
def run():
  app.run(host='0.0.0.0', port=8080)
def keep_alive():
  t = Thread(target=run)
  t.start()
if __name__ == "__main__":
    app.run(debug=True)