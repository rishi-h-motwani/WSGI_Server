from flask import (
    Flask,

    render_template,
)
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    
    return render_template('index.html')

@app.route('/about/', methods=['GET'])
def about():

    return render_template('about.html')

@app.route('/projects/', methods=['GET'])
def projects():

    return render_template('projects.html')


app = app.wsgi_app