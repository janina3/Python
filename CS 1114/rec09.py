#!/usr/bin/python

'''
Programmer: Janina Soriano
Username: js7187

This program creates a shopping list for the designated shopper.

Constraints: None

Assumptions: None

'''

AVAILABLE_FOOD = ["milk", "chocolate covered cherries", "apple", "orange", "banana", "corn on the cob", "kampyo sushi", "asparagus", "avacado", "alfalfa", "acorn squash", "almond package", "arugala bunch", "artichoke", "applesauce", "wasabi", "udon noodles", "tunafish can", "apple juice", "avocado sushi", "bruscetta", "bagel", "barley", "bisque", "bluefish", "bread", "broccoli", "buritto", "babaganoosh", "cabbage", "chocolate cake", "red velvet cake", "strawberry short cake", "carrots", "celery", "cheese", "catfish", "chowder", "clams", "coffee", "corn", "crab", "curry", "cereal", "chimichanga", "dumpling", "donut", "egg", "enchilada", "eggroll", "english muffin", "edimame", "eelSushi", "o toro sashimi", "fajita", "falafel", "fondu", "french toast", "french dip", "garlic", "ginger", "gnocchi", "granola", "grape", "green bean", "guacamole", "gumbo", "grits", "graham crackers", "halibut", "honey", "huenos rancheros", "hash browns", "hummus", "chocolate ice cream", "strawberry ice cream", "cherry garcia ice cream", "puri", "veggie kurma", "jambalaya", "kale", "ketchup", "kiwi", "kidney beans pckg", "great northern beans pckg", "lobster", "linguine", "lasagna", "pepperoni pizza", "mushroom pizza", "pancakes", "quesadilla", "quiche", "spinach", "spaghetti", "tater tots", "toast", "waffles", "walnuts", "peanuts", "hazelnuts", "cranberries", "yogurt", "ziti", "zucchini", "canteloupe", "figs", "salt", "pepper", "nutmeg", "yucca", "shichimi"]

ADD_SHOPPING_LIST = '1'
CREATE_WONT_BUY_LIST = '2'
DISPLAY_IN_ORDER = '3'
QUIT_AND_PRINT = '4'

def getMenuChoice():
    choice = str(raw_input(
        '''Enter a number to choose an action:
            1. Add shopping list
            2. Create won't buy list
            3. Display in order
            4. Quit and print
                            '''))
    return(choice)
                            

def handleMenuChoice(wontBuy, shoppingList, finalList, choice):
    '''Runs a function depending on the menu choice'''
    if(choice == CREATE_WONT_BUY_LIST):
        (wontBuy) = wontBuyList(wontBuy)
    elif(choice == ADD_SHOPPING_LIST):
        (shoppingList) = getShoppingList(wontBuy, shoppingList)
    elif(choice == DISPLAY_IN_ORDER):
        (finalList) = getFinalList(shoppingList, finalList)
    else:
        print("Error. Try again.")
        
    
        

def wontBuyList(wontBuy):
    '''Asks the user for a list of food the family won't buy'''
#    wontBuy = []
    while True:
        item = str(raw_input("What food items won't you buy? "))
        item = item.lower()
        if(item == "done"):
            break
        if(AVAILABLE_FOOD.count(item) == 0):
            print("Sorry, that food is not available. Please enter another food item: ")
        else:
            wontBuy.append(item)
        
    return(wontBuy)

def getShoppingList(wontBuy, shoppingList):
    '''Enters items into shopping list if it is in AVAILABLE_FOOD and not in wontBuy'''
#    shoppingList = []
    while True:
        item = str(raw_input("What food items would you like to buy? "))
        item = item.lower()
        if(item == "done"):
            break
        if(AVAILABLE_FOOD.count(item) == 0):
            print("Sorry, that food is not available. Please enter another food item: ")
        elif(wontBuy.count(item) != 0):
            print("Sorry, that food item is in your won't buy list. Please enter another food item: ")
        else:
            shoppingList.append(item)
        
    return(shoppingList)

def getFinalList(shoppingList, finalList):
    '''Creates the final list'''
#    finalList = []
    for item in shoppingList:
        quantity = shoppingList.count(item)
        if(quantity > 1):
            for i in range(quantity):
                shoppingList.remove(item)
        itemAndNum = [item, quantity]
        finalList.append(itemAndNum)
    print(finalList)        
    return(finalList)
                 
def printList(finalList):
    print("-- FAMILY SHOPPING LIST --")
    print("FOOD  QUANTITY TO BUY")
    print("---------------------")
    for item in finalList:  
        print(item)

def main():
    wontBuy = []
    shoppingList = []
    finalList = []
    (choice) = getMenuChoice()
    while True:
        if(choice == QUIT_AND_PRINT):
            printList(finalList)
            break
        handleMenuChoice(wontBuy, shoppingList, finalList, choice)
        choice = getMenuChoice()
        

#   (wontBuy) = wontBuyList()
#   (shoppingList) = getShoppingList(wontBuy)
#   (finalList) = getFinalList(shoppingList)
#   printList(finalList)
  
    
    

if __name__ == '__main__':
    main()
            
