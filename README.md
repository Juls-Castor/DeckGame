# DeckGame
---

Please design and code up a Python app to represent a standard deck of 52 playing cards. The app should have the capability to track the 52 cards, a mechanism to deal cards, and a mechanism to shuffle the deck of card.

Setup
-------------------------------------------------------------------------------

1. Clone python-docs-samples and change directory to the sample directory you want to use.

```
$ git clone https://github.com/Juls-Castor/DeckGame.git
```

2. The dependencies used for this Python code seems to be included in Python 3.6.5+, this program can be run intalling [pip](https://pip.pypa.io/en/stable/) and [virtualenv](https://virtualenv.pypa.io/en/latest/) if you do not already have them.

3. Create a virtualenv. This sample is compatible with Python 3.6.5+.
```
$ virtualenv env
$ source env/bin/activate
```

Sample
-------------------------------------------------------------------------------
To run this sample:

```
$ python main.py 4 3

usage: main.py [PLAYERS] [CARDS]

Init a deck of 52 cards, they are shuffled and they are dealt to P players.

positional arguments:
  PLAYERS     Number of players to deal cards.
  CARDS       Number of cards to deal per player

optional arguments:
  -h, --help  show this help message and exit
```
