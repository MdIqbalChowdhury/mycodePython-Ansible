#!/usr/bin/python3
""" Author : Iqbal  || learning about dict"""

def main():
    webster = {"apple" : "red" , "leaf" : "green", "grape" : "purple"}
    #webster = dict()
    print(webster)
    print(webster["apple"])


    switches = { "cisco" : "ios", "juniper" : "junos",\
            "arista" : " eos"}
    print(switches["cisco"])

    switches["hp"] = "hpos"

    print(switches)
    

    print(switches.values()) # produce all values
    print(switches.keys()) # product all keys
    print (dir(switches))

main()

