shoppingList = []

def showOptions():
    print("\n")
    print('Options')
    print('1. Add item to the shopping list')
    print('2. View shopping List')
    print('3. Remove item from the shopping list')
    print('4. Quit')

    userChoice = int(input('Enter the number of your choice: '))
    handleUserChoice(userChoice)


def handleUserChoice(choice):
    if choice == 1:
        itemToAdd = input('Enter the item you want to add: ')
        shoppingList.append(itemToAdd)
        print(f"{itemToAdd} has been added to your shopping list")
        showOptions()
    elif choice == 2:
        print('Your shopping list: ')
        if len(shoppingList):
            for item in shoppingList:
                print(item)            
        else:
            print('You have no items in your shopping list')
        showOptions()
    elif choice == 3:  
        itemToRemove = input('Enter the item you want to remove: ')
        shoppingList.remove(itemToRemove)
        showOptions()

    elif choice == 4:
        print('Goodbye!')
        



showOptions()
