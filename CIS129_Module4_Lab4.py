# Module 4 Lab-4
# Christian Garcia
# 10/10/2024
# The program calculates a store bonus and employee bonus based on total store sales
# The main function
def main():
    monthlySales = getSales() # monthly sales amount
    print("monthlySales", monthlySales)
    storeAmount = calcStoreBonus(monthlySales) # store bonus amount
    print("storeAmount",storeAmount)
    salesIncrease = getIncrease() # percent of sales increase
    empAmount = calcEmpBonus(salesIncrease) # employee bonus amount
    print("salesIncrease", salesIncrease) 
    printBonus(storeAmount, empAmount) 
# call to getSales(prompt)
# call to getIncrease(prompt)
# call to calcStoreBonus(monthlySales)
# call to calcEmpBonus(salesIncrease)
# call to printBonus(storeAmount,empAmount)
# This function gets the monthly sales
def getSales():
    monthlySales = float(input("Enter the amount of monthly sales:"))
    return monthlySales
 
# This function gets the percent of increase in sales
def getIncrease():
    salesIncrease = float(input('Enter percent of sales increase with no decimal. Such as 5 for 0.05, 3 for 0.03 and so on:'))
    salesIncrease = salesIncrease / 100
    return salesIncrease
# This function determines the storeAmount bonus
def calcStoreBonus(monthlySales):
    if monthlySales >= 110000:
        storeAmount = 6000
    elif  monthlySales >= 100000:
        storeAmount= 5000
    elif  monthlySales >= 90000:
        storeAmount = 4000
    elif  monthlySales >= 80000:
        storeAmount = 3000
    else:
        storeAmount = 0
    return storeAmount
# This function determines the empAmount bonus
def calcEmpBonus(salesIncrease):
    if salesIncrease >= 0.05:
      empAmount = 75
    elif salesIncrease >= 0.04:
      empAmount = 50
    elif salesIncrease >= 0.03:
      empAmount = 40
    else: 
      empAmount = 0
    return empAmount
# This function prints the bonus information
def printBonus(storeAmount,empAmount ):
    print("The store bonus amount is $",storeAmount )
    print("The employee bonus amount is $",empAmount )
    if (storeAmount == 6000 ) and (empAmount == 75 ):
        print('Congrats! You have reached the highest bonus amounts possible!')
 
# calls main
main()
