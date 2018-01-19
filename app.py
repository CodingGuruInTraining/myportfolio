from flask import Flask, render_template
from gamesdata import gamesFunction
from languagedata import langFunction
from resumedata import resumeFunction
from projectsdata import projectsFunction


app = Flask(__name__)

gamesData = gamesFunction()
langData = langFunction()
resumeData = resumeFunction()
projData = projectsFunction()


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/games')
def gamesPage():
    return render_template('games.html', items = gamesData)


@app.route('/projects')
def projectsPage():
    return render_template('projects.html', items = projData)


@app.route('/resume')
def resumePage():
    return render_template('resume.html', data = resumeData)


@app.route('/languages')
def languagesPage():
    return render_template('languages.html', items = langData)


@app.route('/contact')
def contactPage():
    return render_template('contact.html')



if __name__ == '__main__':
    # TODO Remove debug once finished.
    app.run(debug=True)
