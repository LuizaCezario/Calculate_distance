from flask import Blueprint, render_template, request
import requests, re
import geopy.distance 

calculate_route = Blueprint('calculate_route', __name__, static_folder='static', template_folder='coordinates/templates')


@calculate_route.route('/', methods=['POST', 'GET'])
def api():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        num1 = request.form['coordinates']
        result = calculate_distance(num1)
        return render_template('index.html', result=result)


def calculate_distance(p2):
    if (validate_coordinates(p2) == True):
        p2 = re.sub(r"\s+", "", p2)
        if p2 in ('37.842762,55.774558',
        '37.842789,55.76522',
        '37.842627,55.755723',
        '37.841828,55.747399',
        '37.841217,55.739103',
        '37.840175,55.730482',
        '37.83916,55.721939',
        '37.837121,55.712203',
        '37.83262,55.703048',
        '37.829512,55.694287',
        '37.831353,55.68529',
        '37.834605,55.675945',
        '37.837597,55.667752',
        '37.839348,55.658667',
        '37.833842,55.650053',
        '37.824787,55.643713',
        '37.814564,55.637347',
        '37.802473,55.62913',
        '37.794235,55.623758',
        '37.781928,55.617713',
        '37.771139,55.611755',
        '37.758725,55.604956',
        '37.747945,55.599677',
        '37.734785,55.594143',
        '37.723062,55.589234',
        '37.709425,55.583983',
        '37.696256,55.578834',
        '37.683167,55.574019',
        '37.668911,55.571999',
        '37.647765,55.573093',
        '37.633419,55.573928',
        '37.616719,55.574732',
        '37.60107,55.575816',
        '37.586536,55.5778',
        '37.571938,55.581271',
        '37.555732,55.585143',
        '37,37.545132,55.587509',
        '37.526366,55.5922',
        '37.516108,55.594728',
        '37.502274,55.60249',
        '37.49391,55.609685',
        '37.484846,55.617424',
        '37.474668,55.625801',
        '37.469925,55.630207',
        '37.456864,55.641041',
        '37.448195,55.648794',
        '37.441125,55.654675',
        '37.434424,55.660424',
        '37.42598,55.670701',
        '37.418712,55.67994',
        '37.414868,55.686873',
        '37.407528,55.695697',
        '37.397952,55.702805',
        '37.388969,55.709657',
        '37.383283,55.718273',
        '37.378369,55.728581',
        '37.374991,55.735201',
        '37.370248,55.744789',
        '37.369188,55.75435'):
            return "The coordinates are inside MKAD"
        else:
            p1 = (55.751244, 37.618423) 
            distance = geopy.distance.distance(p1, p2).km 
            print(distance)
            return distance
    else:
        return "Latitude must be in the [-90; 90] range and Longitude must be in the [-180; 180] range."

def validate_coordinates(p2):
    p2 = p2.split(sep = ",")
    p2[0] = float(p2[0])
    p2[1] = float(p2[1])
    print(p2)
    if (-90<=p2[0] and p2[0]<=90 and -180<=p2[1] and p2[1]<=180):
        return True
    else:
        return False
