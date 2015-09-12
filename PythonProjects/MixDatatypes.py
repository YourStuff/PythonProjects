'''
Created on Sep 11, 2015

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
    print("The sum of the list: ")
    print(thesum)
    print("This is your whole list: ")
    print(sList)  
  
def ulist():
    userlist = []
    user = 0
    thesum1 = 0
    while True:
        user = raw_input("Enter your data")
        if user=="exit":
            break
        userlist.append(user)
        
        try:
            i = int(user)
            thesum1 = thesum1 + i
        
        except ValueError:
            i = 0
    print("This is your whole list: ")
    print(userlist)
    print("Your total is: ")
    print(thesum1)
alist()
ulist()