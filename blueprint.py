from flask import Blueprint, render_template
import requests

calculate_route = Blueprint('calculate_route', __name__, static_folder='static', template_folder='coordinates/templates')

@calculate_route.route('/')
def api():
    return render_template("index.html")