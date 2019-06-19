#!/usr/bin/python3
""" learning about json and pythn"""

import json

def main():
    with open("got.json", "r") as gameofthrone:
        #myjson = gameofthrone.read()
        mygot = json.load(gameofthrone)
    
    
    print(mygot, end='\n\n\n')
    print("", sep=' ', end='\n')
    
    print( "URL:" , mygot['url']) 
    print(mygot['born'])
    print(mygot['father'])
    
    print(mygot['tvSeries'])
    print(mygot['tvSeries'][0])
    print(mygot['tvSeries'][1])


    print(len(mygot['tvSeries']))
    for season in mygot['tvSeries']:
        print(season)
    print('\n')
    for alias in mygot["aliases"]:
        print(alias)

   
    print(mygot['playedBy'][0])
    
    print(mygot.get('larry'))
    #print(mygot['aliases[0]')
    print(type(mygot))
    #print(myjson)
    #print(type(myjson))

main()
