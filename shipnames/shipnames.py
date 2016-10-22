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
from random import shuffle
from docopt import docopt
from wikitables import import_tables
from slugify import slugify


def process(args):
    """Main body"""
    if args['<amount>']:
        amount = int(args['<amount>'])
    else:
        amount = 1
    tables = import_tables('List of spacecraft in the Culture series')
    names = []
    for table in tables[:-1]:
        for row in table.rows:
            try:
                names.append(row['Name'])
            except KeyError:
                pass
    names = [i.value.replace('*', '').strip(' ') for i in names]
    if args['-l']:
        names = [i.lower() for i in names]
    if args['-s']:
        names = [slugify(u"%s" % i) for i in names]
    shuffle(names)
    if args['-a']:
        names.sort()
        amount = len(names)
    print
    for i in names[:amount]:
        print i
    print


if __name__ == '__main__':
    ARGS = docopt(__doc__)
    process(ARGS)
