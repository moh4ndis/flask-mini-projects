from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/<name>')
def home(name):
    return f"Hello, {escape(name)}!"

if __name__ == '__main__':
    app.run(debug=True)
