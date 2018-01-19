def gamesFunction():
    gamesList = [
        {
            'id': 1,
            'name': 'Breakout',
            'description': 'This is my Breakout/Brick Buster clone game. A player controls a paddle '
                           'at the bottom of the window to bounce a single ball towards a group of '
                           'bricks. Each brick destroyed grants the player points. If the ball falls '
                           'past the paddle, the player loses one of three lives.',
            'languages': 'Java',
            'challenges': 'Making the bricks scale with the window size, which taught me things I can '
                          'apply in future games.',
            'futurework': 'Add levels of difficulty, Make different brick patterns, Implement '
                          'online database',
            'github': 'https://github.com/mark-fox/Breakout',
            'piclink': 'https://farm5.staticflickr.com/4617/39720630382_db5a2e791e_o.gif',
            'design': 'This game uses OOP to separate the different objects and allow for '
                      'custom methods and features. There is a "manager" class that coordinates '
                      'the object method calls as well as the game loop. Objects are drawn onto '
                      'a JFrame and the High Score feature uses a JTable along with a SQLite database '
                      '(temporarily). A single Interface object is used to hold constant magic numbers '
                      'as well as providing a single location for classes to access these values.'
        },
        {
            'id': 2,
            'name': 'Ninja Zombie Scroller (working title)',
            'description': 'This is an Android side scroller game involving a ninja player against '
                           'an endless horde of zombies. Points are awarded to the player for every '
                           'defeated zombie, but the zombies will gain points if they manage to hit '
                           'the player first.',
            'languages': 'Android/Java',
            'challenges': 'First time working with sprite animations and state changes',
            'futurework': 'Adding levels, bosses, more actions, and more',
            'github': 'https://github.com/mark-fox/NinjaZombieScroller_v0.1',
            'piclink': '',
            'design': 'A SurfaceView is used along with a canvas to draw each object to the screen. '
                      'Sprite sheets were used for the characters while the background uses static '
                      'images. Each aspect of the game is drawn with custom scaling values, which '
                      'allows the game to scale with the screen size.'
        },
        {
            'id': 3,
            'name': 'Rock Paper Scissors Lizard Spock',
            'description': 'Here is a classic game of rock paper scissors lizard spock! I '
                           'first learned about this game version while watching an '
                           'episode of The Big Bang Theory. This is my online game version '
                           'that uses web-sockets to allow real-time game results. Any '
                           'number of players can join and play against each other.',
            'languages': 'JavaScript web-sockets, HTML, CSS',
            'challenges': 'Learning how to use web-sockets, Determining active players',
            'futurework': 'Fine-tune active player detection, "Invite Your Friends" link',
            'github': 'https://github.com/mark-fox/RockPaperScissors_v0.2',
            'piclink': 'https://farm5.staticflickr.com/4752/39740894192_db0123526a_o.gif',
            'design': 'With the use of web-sockets, the game is able to stay connected '
                      'with all active players at a time. When a new player joins, they are '
                      'added to the list of users and a message is sent to all other active '
                      'players alerting them of the newcomer. The server uses this count '
                      'to determine whether it has received all player inputs before '
                      'proceeding with the results. Once all players have made their '
                      'selection, the server will determine the winners and display the '
                      'results to everyone. ',
            'gamelink': 'http://rockpaperscissorsv2.herokuapp.com/'
        }
    ]
    return gamesList
