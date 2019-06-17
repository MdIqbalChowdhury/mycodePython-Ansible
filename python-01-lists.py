#!/usr/bin/python3
"""" Author : md.iqbal.chowdhury@verizon.com ||  Learning about lists"""

def main():
    mylist = ["verizon" , "att"] # creatig a list (init)
    
    print( mylist) 
    print( mylist[0])

    mylist.append("tmob") # add to the END of the list
                          # using a METHOD
    print(mylist)
    print(mylist[2])
    print(mylist[-1]) # it will display from backward

    if mylist[2] == 'tmob':
        print("tmob is in the list!")

    if 'tmob' in mylist:
        print("tmob is someplace in the lists!")
main()

