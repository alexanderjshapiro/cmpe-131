from flask import Flask

name = 'Alex'
city_names = ["New York", "Paris", "Milano", "London"]

app = Flask(__name__)


@app.route("/")
def home():
    html = f"""
    <html>
    <head>
        <title>CMPE 131 Homework 3</title>
    </head>
    <body>
        <h1>Welcome {name}!</h1>
        <a href="www.google.com">not google</a>
        <ul>"""

    for city_name in city_names:
        html += f"<li>{city_name}</li>\n"

    html += """
        </ul>
    </body>
    </html>
    """
    return html
