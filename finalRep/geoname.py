#! /usr/bin/python3


import requests
import sys
import json

n=sys.argv[1]
maString=' '.join(sys.argv[2:])

def askGeoname(nRes,str):
    resp=requests.get('http://api.geonames.org/searchJSON?username=beoffre&maxRows='+nRes+'&q='+format(str))
    res=json.loads(resp.text)
    return(resp.text)


print(askGeoname(n,maString))
