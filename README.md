Culture Ship Name Picker
===============================

version number: 0.0.1
author: Signal

Overview
--------

 Get random ship names from Ian Banks' Culture novels

Installation / Usage
--------------------

To install use pip:

    $ pip install shipnames


Or clone the repo:

    $ git clone https://github.com/signalrock/shipnames.git
    $ python setup.py install

Usage
-----

    shipnames.py [-l | -s] [-a] [<amount>]

    Options:
        -h --help   Show this screen
        -l          Lowercase
        -s          Slugify (spaces and punctuation become hyphens and lowercase)
        -a          Show all in alphabetical order

Example
-------

    ~: python shipnames.py 3

    Cargo Cult
    Nervous Energy
    Highpoint


    ~: python shipnames.py 5 -s

    subtle-shift-in-emphasis
    unacceptable-behaviour
    now-we-try-it-my-way
    reasonable-excuse
    its-character-forming