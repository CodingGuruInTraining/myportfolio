def projectsFunction():
    projectsList = [
        {
            'id': 1,
            'name': 'Portfolio (this one!)',
            'description': 'I created this portfolio website from scratch. What better way to show one\'s '
                           'webpage-making skills than to actually make one! It may not be the flashiest, '
                           'but it is my own.',
            'languages': 'Python/Flask, HTML, CSS',
            'challenges': 'Designing the look and styling website',
            'futurework': 'Adding future projects',
            'github': '',
            'piclink': '',
            'design': 'This website was created using Python Flask for the "server" part and, of course, '
                      'HTML/CSS for the visual side. I stored most of the data in separate .py files so '
                      'it would be easier to add and update as needed. This allowed me to loop over the '
                      'data when adding to the HTML page, which was preferred. The majority of the pages '
                      'follow a single layout, which includes a navigation bar.'
        },
        {
            'id': 2,
            'name': 'What Would You Do For A Dollar? (working title)',
            'description': 'This is meant to be a website for exchanging simple services among a community. '
                           'The idea is that if someone does not want to do something (i.e. shovel the '
                           'driveway, pickup dry-cleaning, fix bicycle, etc.) they can post their task here '
                           'and anyone can commit to doing it. The exchange is between the two parties involved '
                           'and the task owner can offer anything they feel fit (i.e. bag of marbles, red '
                           'paperclip, autographed baseball, etc.).',
            'languages': 'Python/Flask, SQLAlchemy, HTML, CSS',
            'challenges': 'Implementing WTForms Login system',
            'futurework': 'Creating custom users with a public profile page, Implementing a points system '
                          'for leveling up one\'s account, Adding location and filters',
            'github': 'https://github.com/mark-fox/WhatWouldYouDoForADollar_v0.1',
            'piclink': 'https://farm5.staticflickr.com/4611/39752491732_52da87b8d9_o.png',
            'design': 'This website was created using Python Flask along with SQLAlchemy. The table grabs '
                      'all entries from the database and displays them whiling also linking each entry to '
                      'its own page. Newly created tasks are added to the database upon submission.'
        },
        {
            'id': 3,
            'name': 'Speed Typing Tester',
            'description': 'There may not be much to this app, but it was one of my first big JavaScript '
                           'projects and it taught me a lot about the language. The app uses a Ron '
                           'Swanson quote API to generate a random string for the user to type as fast and '
                           'as accurate as they can. Once completed, the user\'s score is displayed and '
                           'added to a MLab database to be shown in the homepage table.',
            'languages': 'JavaScript, HTML, CSS',
            'challenges': 'Reacting to keypress events, Calculating results/stats',
            'futurework': 'Improve Login system strength, Correct the calculations issue',
            'github': 'https://github.com/mark-fox/Speed_Typing_Tester_v0.2',
            'piclink': 'https://farm5.staticflickr.com/4604/25910868898_573c942bb5_o.gif',
            'design': 'The app has a very basic login system, which uses the entered username to populate '
                      'related entries in the high-score table. Client-side JavaScript is used to detect '
                      'keystrokes and react to them. Pressing the wrong key will prevent further entries '
                      'until the error is corrected. Upon completion, the entry is submitted to the server '
                      'to perform the calculations, add them to the database, and display the results. ',
            'onlinelink': 'https://speedtypetest.herokuapp.com/'
        }
    ]
    return projectsList
