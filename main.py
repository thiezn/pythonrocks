from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    html = (
        "<h2>Hello world!!<h2>"
        "<p>nice going, you managed to deploy some code the cool way"
    )
    return html

if __name__ == '__main__':
    app.run()
