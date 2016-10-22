Culture Ship Name Picker
===============================

version number: 0.0.2
author: Signal

Overview
--------

 Get random ship names from Iain Banks' Culture novels

Installation / Usage
--------------------

Clone the repo:

    $ git clone https://github.com/signalrock/shipnames.git

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