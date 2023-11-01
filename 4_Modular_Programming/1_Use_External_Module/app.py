# Hermawan Sentyaki Sarjito
# J0403231111

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world() -> str:
    """Display Hello, Flask! on the web page

    Returns:
        str: Hello, Flask!
    """
    return "<p>Hello, Flask!</p>"

if __name__ == '__main__':
    app.run()