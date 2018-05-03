from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    html = "<h1>Hello World!!</h1><p>nice going, you managed to deploy some code the cool way"
    htmlv2 = (
        "<h1>Hello world!!<h1>"
        "<h2>Summary</h2>"
        "<font size='6'>"
        "<b>Python</b> shooting for the stars!<br>"
        "<i>C#</i> The only way is down<br>"
        "<i>PowerShell</i> Staat niet op de kaart... bieb bieb bieb mwueup<br>"
        "</font><br><br>"
        "<img src='https://raw.githubusercontent.com/thiezn/pythonrocks/master/images/programmingpopularity.PNG'>"
    )
    return htmlv2


if __name__ == '__main__':
    app.run()
