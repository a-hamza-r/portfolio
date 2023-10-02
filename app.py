from flask import Flask, render_template
import yaml

app = Flask(__name__)

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file);
    return data;

basic = read_yaml('data/basic.yml');

@app.route('/')
def index():
    return render_template('index.html', data=basic);

@app.route('/publications')
def publications():
    return render_template('publications.html', data=basic);

@app.route('/projects')
def projects():
    return render_template('projects.html', data=basic);

@app.route('/contact')
def contact():
    return render_template('contact.html', data=basic);

@app.route('/cv')
def cv():
    return render_template('cv.html', data=basic);

@app.route('/experience')
def experience():
    return render_template('experience.html', data=basic);

if __name__ == '__main__':
    app.run(debug=True);
