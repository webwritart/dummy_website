from flask import render_template, Blueprint


main = Blueprint('main', __name__, static_folder='static', template_folder='template')


@main.route('/')
def home():
    return render_template('index.html')
