from flask import Flask, render_template
from os import path
import yaml

app = Flask(__name__)

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file);
    return data;

basic_path = path.join(app.root_path, 'data', 'basic.yml')
_basic = read_yaml(basic_path);

@app.route('/')
def index_process():
    return render_template('index.html', basic=_basic);

@app.route('/publications')
def publications_process():
    publications_path = path.join(app.root_path, 'data', 'publications.yml')
    _publications = read_yaml(publications_path)['publications'];
    for publication in _publications:
        authors = publication['authors'];
        authors_citation = '';
        for index, author in enumerate(authors):
            author_name = author.split(' ');
            if (index == publication['your_position']):
                author_citation = '<b>' + author_name[0][0] + '. ' + author_name[1] + '</b>, ';
            else:
                author_citation = author_name[0][0] + '. ' + author_name[1] + ', ';
            authors_citation += author_citation;
        authors_citation = authors_citation[:-2];
        publication['citation'] = authors_citation + ', "' + publication['title'] + '" in ' + publication['venue'] + ', ' + str(publication['year']) + '.';
    return render_template('publications.html', publications=_publications, basic=_basic);

@app.route('/projects')
def projects_process():
    return render_template('projects.html', basic=_basic);

@app.route('/contact')
def contact_process():
    return render_template('contact.html', basic=_basic);

@app.route('/cv')
def cv_process():
    return render_template('cv.html', basic=_basic);

@app.route('/experience')
def experience_process():
    experience_path = path.join(app.root_path, 'data', 'experience.yml')
    _teachings = read_yaml(experience_path)['teachings'];
    _jobs = read_yaml(experience_path)['jobs'];
    return render_template('experience.html', basic=_basic, teachings=_teachings, jobs=_jobs);

@app.route('/static/<path:filename>')
def files_process(filename):
    file_path = path.join(app.root_path, 'static',  filename)
    return app.send_static_file(file_path);

if __name__ == '__main__':
    app.run(debug=True);
