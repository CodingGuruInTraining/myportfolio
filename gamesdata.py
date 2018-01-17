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
            'futurework': 'Add levels of difficulty, Make different brick patterns, Implement online database',
            'github': 'https://github.com/mark-fox/Breakout',
            'piclink': 'http://i38.photobucket.com/albums/e120/foxm47/breakout_zpsh9n2bz03.gif',
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
            'design': ''
        }
    ]
    return gamesList