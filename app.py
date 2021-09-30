from flask import Flask
from blueprint import calculate_route

app = Flask(__name__)
app.register_blueprint(calculate_route, url_prefix='/')
app.register_blueprint(calculate_route, url_prefix='/api')


@app.route('/')
def index():
    return "This is an example app"