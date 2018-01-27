from flask import Flask, render_template

# Imports static data files.
from gamesdata import gamesFunction
from languagedata import langFunction
from resumedata import resumeFunction
from projectsdata import projectsFunction


app = Flask(__name__)

# Retrieves data lists from static files.
gamesData = gamesFunction()
langData = langFunction()
resumeData = resumeFunction()
projData = projectsFunction()


# Home page route.
@app.route('/')
def homepage():
    return render_template('homepage.html')



# Games page route.
@app.route('/games')
def gamesPage():
    return render_template('games.html', items = gamesData)



# Projects page route.
@app.route('/projects')
def projectsPage():
    return render_template('projects.html', items = projData)



# Resume page route.
@app.route('/resume')
def resumePage():
    return render_template('resume.html', data = resumeData)



# Languages page route.
@app.route('/languages')
def languagesPage():
    return render_template('languages.html', items = langData)



# Contact page route.
@app.route('/contact')
def contactPage():
    return render_template('contact.html')



# Runs app.
if __name__ == '__main__':
    app.run()
