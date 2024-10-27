from flask import Flask, render_template

app = Flask(__name__)

@app.route('/healthz')
def index():
  return render_template('card.html')
if __name__ == "__main__":
    app.run()