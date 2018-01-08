from flask import Flask, render_template
from gamesdata import gamesFunction
from languagedata import langFunction

app = Flask(__name__)

gamesData = gamesFunction()
langData = langFunction()


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/games')
def gamesPage():
    return render_template('games.html', items = gamesData)


@app.route('/projects')
def projectsPage():
    return render_template('projects.html')


@app.route('/resume')
def resumePage():
    return render_template('resume.html')


@app.route('/languages')
def languagesPage():
    return render_template('languages.html', items = langData)


@app.route('/contact')
def contactPage():
    return render_template('contact.html')



if __name__ == '__main__':
    # TODO Remove debug once finished.
    app.run(debug=True)
