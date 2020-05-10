#! /usr/bin/python3


import re
import sys 


maString=' '.join(sys.argv[1:])

regles=[r"[\(\[]*\s*\d+\s*\D\s*\d+\s*[\)\]]*",                      #res
        r"[\(\[\s]\s*OC\s*[\)\]\s]",                                #oc
        r"\b(ig|instagram|insta)\s*[\:\.\-\s]+\S+",                 #ig
        r"\S*[@\#]\S+",                                             #handles ou hashtags
        r"[\u263a-\U0001ffff]"                                      #emojis
        ]                     



def epurer(titre):
    for regexp in regles:
        titre=re.sub(regexp,'',titre,flags=re.IGNORECASE)
    return(titre)

print(epurer(maString))
