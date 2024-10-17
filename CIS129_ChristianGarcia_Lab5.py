# Christian Garcia
# 10/17/2024
# Program allows a grocery store to keep track of how many bottles are collected 

def getBottles():
    #return the total number of bottles for the week
    no_of_days=7
    totalBottles=0
    todayBottles=0
    counter=0
    while counter<7:
        print("Enter number of bottles returned for day "+str((counter+1))+":")
        todayBottles=int(input())
        counter+=1
        totalBottles+=todayBottles
    print(totalBottles)  
    return totalBottles
        
   
def calcPayout(totalBottles):
    #return total payment for the week
    payout_per_bottle=0.10
    totalPayout=0 
    totalPayout=totalBottles*payout_per_bottle
    return totalPayout

totalBottles=0
counter=1 
todayBottles=0
totalPayout=0
keepGoing='y'
while keepGoing=='y':
    totalBottles=getBottles()
    totalPayout=calcPayout(totalBottles)
    #displaying the output to the user
    print(totalPayout)
    print("Do you want to enter another week's worth of data?")
    keepGoing=input("Enter y or N")