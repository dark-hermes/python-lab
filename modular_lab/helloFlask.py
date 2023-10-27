from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """Display Hello, Flask! on the web page

    Returns:
        str: Hello, Flask!
    """
    return "<p>Hello, Flask!</p>"

if __name__ == '__main__':
    import doctest
    doctest.testmod()