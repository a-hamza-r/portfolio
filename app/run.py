from flask import Flask, render_template
from os import path
from flask_frozen import Freezer
import yaml

app_dir = path.dirname(path.abspath(__file__))
data_path = path.join(app_dir, 'data')

app = Flask(__name__);
freezer = Freezer(app);

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file);
    return data;


basic_path = path.join(data_path, 'basic.yml')
_basic = read_yaml(basic_path);

@app.route('/')
def index_process():
    return render_template('index.html', basic=_basic);


@app.route('/publications/')
def publications_process():
    publications_path = path.join(data_path, 'publications.yml')
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


@app.route('/projects/')
def projects_process():
    project_path = path.join(data_path, 'projects.yml')
    _projs = read_yaml(project_path);
    _research_projs = _projs['research'];
    _dev_projs = _projs['development'];
    return render_template('projects.html',
            research_projs=_research_projs, dev_projs=_dev_projs, basic=_basic);


@app.route('/contact/')
def contact_process():
    return render_template('contact.html', basic=_basic);


@app.route('/cv/')
def cv_process():
    cv_path = path.join(data_path, 'cv.yml')
    _cv = read_yaml(cv_path);
    _educations = _cv['education'];
    _presentations = _cv['presentations'];
    _reviews = _cv['reviews'];
    _awards = _cv['awards'];
    _skills = _cv['skills'];
    experience_path = path.join(data_path, 'experience.yml')
    _experiences = read_yaml(experience_path);
    _teachings = _experiences['teachings'];
    _jobs = _experiences['jobs'];
    publications_path = path.join(data_path, 'publications.yml')
    _publications = read_yaml(publications_path)['publications'];
    projects_path = path.join(data_path, 'projects.yml')
    _research = read_yaml(projects_path)['research'];
    _development = read_yaml(projects_path)['development'];
    return render_template('cv.html',
                           educations=_educations, teachings=_teachings, jobs=_jobs,
                           publications=_publications, presentations=_presentations,
                           research_projs=_research, dev_projs=_development,
                           reviews=_reviews, skills=_skills, basic=_basic);


@app.route('/experience/')
def experience_process():
    experience_path = path.join(data_path, 'experience.yml')
    _experiences = read_yaml(experience_path);
    _teachings = _experiences['teachings'];
    _jobs = _experiences['jobs'];
    return render_template('experience.html',
                           basic=_basic, teachings=_teachings, jobs=_jobs);


@app.route('/static/<path:filename>')
def files_process(filename):
    return app.send_static_file(filename);

@app.route('/projects/<tag>/')
def project_process(tag):
    project_path = path.join(data_path, 'projects.yml')
    _projs = read_yaml(project_path);
    _research_projs = _projs['research'];
    _dev_projs = _projs['development'];
    for _proj in _research_projs:
        if (_proj['tag'] == tag):
            return render_template('project.html', proj=_proj, basic=_basic);
    for _proj in _dev_projs:
        if (_proj['tag'] == tag):
            return render_template('project.html', proj=_proj, basic=_basic);

@freezer.register_generator
def project_process():
    project_path = path.join(data_path, 'projects.yml')
    _projs = read_yaml(project_path);
    _research_projs = _projs['research'];
    _dev_projs = _projs['development'];
    for project in _research_projs:
        yield {"tag": project["tag"]};
    for project in _dev_projs:
        yield {"tag": project["tag"]};

