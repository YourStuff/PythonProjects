'''
Created on Sep 10, 2015

@author: isja
'''
Mylist = [1, 9, 45, "ism", "dee", 7, 80,34, "sal", "mai"]
def alist():
    sList = []
    
    thesum = 0
    
    for i in Mylist:
        if  isinstance( i, int ):
            thesum = thesum + i
        else :
            sList.append(i)
    print(thesum)
    print(sList)   
def ulist():
    user = 0
    userlist = []
    while True :
        user = raw_input("Please add your elements: ")
        if user == "exit":
            break
        userlist.append(user)
    print(userlist)

alist()
ulist()
