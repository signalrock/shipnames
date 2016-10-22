#! /usr/bin/env python
# coding=utf-8
"""
\n\n

List random Culture ship names

Usage:
    shipnames.py [-l | -s] [-a] [<amount>]

Options:
    -h --help   Show this screen
    -l          Lowercase
    -s          Slugify (spaces and punctuation become hyphens and lowercase)
    -a          Show all in alphabetical order

\n\n
"""

from docopt import docopt
from wikitables import import_tables
from random import shuffle
from slugify import slugify

def process(arguments):
    if arguments['<amount>']:
        amount = int(arguments['<amount>'])
    else:
        amount = 1
    tables = import_tables('List of spacecraft in the Culture series')
    l=[]
    for table in tables[:-1]:
        for row in table.rows:
            try:
                l.append(row['Name'])
            except KeyError:
                pass
    l=[i.value.replace('*','').strip(' ') for i in l]
    if arguments['-l']:
        l = [i.lower() for i in l]
    if arguments['-s']:
        l = [slugify(u"%s" % i) for i in l]
    shuffle(l)
    if arguments['-a']:
        l.sort()
        amount = len(l)
    print
    for i in l[:amount]:
        print i
    print

if __name__ == '__main__':
    arguments = docopt(__doc__)
    process(arguments)
