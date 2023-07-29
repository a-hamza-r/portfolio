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

if __name__ == '__main__':
    app.run(debug=True);
