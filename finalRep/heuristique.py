#! /usr/bin/python3

import requests
from nltk.tag import pos_tag
import sys


maString=' '.join(sys.argv[1:])

def treeTag(uneStr):
    tagged_sent = pos_tag(str(uneStr).split())
    newHaut =[word for word, pos in tagged_sent if pos == 'NNP']
    newHaut = ' '.join(newHaut)
    return(newHaut)

print(treeTag(maString))
