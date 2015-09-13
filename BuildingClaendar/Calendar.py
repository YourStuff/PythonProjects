'''
Created on Sep 12, 2015

@author: isja
'''

def main():
    for i in range(1, 5) :
        n = int(input("Input the number of days in the month (28-31): "))
        if n<=31:
            while True:
                d = int(input("Input the starting day (0=Sun, 1=Mon,...): "))
                if  d<=7:
                    
                    for i in range(d):
                        print("  ", end=" ")
                    i = 1
                    
                    while i<=n:
                        if i<10:
                            print(" " + str(i), end=" ")
                        else:
                            print(i, end=" ")
                        if (i + d) % 7 == 0:
                            print("")
                        i = i + 1
                    print(" ")
                    break
                else:
                    print("please enter a valid weekdays less than 7 ")
        
        else:
            print("Please enter a valid month between (28 - 31)")
    while True:
        year = int(input("Enter a year: ")) 
    
        if year % 4 == 0 and year %100 != 0 or year % 400 == 0:
    
            print ("Is a leap-year")
    
        else:
            print ("Is not a leap-year")  
main()

