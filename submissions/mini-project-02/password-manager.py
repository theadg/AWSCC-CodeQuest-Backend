import json
baseFilePath = '/Users/badg/Documents/repos/AWSCC-CodeQuest-Backend/backend/day-15'

class userInput:
    def __init__(
            self, 
            name = "", 
            password = "", 
            email = ""
        ):
        self.name = name
        self.password = password
        self.email = email

currentUser = userInput()

# Open File, so it can be easily accessed
with open(f"{baseFilePath}/db.json", 'r+') as file:
    data = json.load(file)

# Add updated data to json file
def updateJsonFile():
    with open(f"{baseFilePath}/db.json", 'w') as file:
            json.dump(data, file, indent=4)    

def getUserInput(isShow = False):
    currentUser.name = input('Name of Website: ')
    currentUser.email = input('Email of Website: ')

    if not isShow:
        currentUser.password = input('Password of Website: ')

# Returns the index of the account
def findIndex(data):
    for index, account in enumerate(data['accounts']):
        if account['name'] == currentUser.name or account['email'] == currentUser.email:
            return index

    return None

# Prints User info
def printUserInfo(user):
    print(f"\nWebsite: {user['name']}")
    print(f"  Email: {user['email']}")
    print(f"  Password: {user['password']}")

# show all
def index():
    for user in data['accounts']:
        printUserInfo(user)

# opening file
def store():
    getUserInput()

    newData = {
        "name": currentUser.name,
        "email": currentUser.email,
        "password": currentUser.password
    }

    # Create or update Record
    userExists = findIndex(data)
    if userExists == None:
        data['accounts'].append(newData)
    else:
        data['accounts'][findIndex(data)] = newData

    updateJsonFile()

def show():
    getUserInput(True)

    with open(f"{baseFilePath}/db.json", 'r+') as file:
        data = json.load(file)

    userExists = findIndex(data)
    if userExists == None:
        print('User does not exist')       
    else:
        userFound = data['accounts'][userExists]
        printUserInfo(userFound)

def delete():
    indexToDelete = 0

    while True:
        try:
            indexToDelete = int(input("Enter the index you want to delete: "))
        except ValueError:
            print("You must enter an integer number")
            continue
        else:
            break
    
    # Guard clause to return if out of range   
    if (indexToDelete > len(data['accounts'])):
        return print("Index out of range")
    
    # Remove account based on index
    data['accounts'].pop(indexToDelete)

    updateJsonFile()

def update():
    getUserInput()

    newData = {
        "name": currentUser.name,
        "email": currentUser.email,
        "password": currentUser.password
    }

    userExists = findIndex(data)
    if userExists == None:
        return print("User not found")
    else:
        data['accounts'][findIndex(data)] = newData

    updateJsonFile()

def endProgram():
    global running
    
    print('Thank you for using the program!')
    running = False

running = True
def printMenu():
    menu = [
        '1 - Add Username and Password',
        '2 - View',
        '3 - Search',
        '4 - Delete',
        '5 - Update',
        '6 - Exit'
    ]

    print('\n\n\n-------PASSWORD MANAGER---------')
    for item in menu:
        print(item)

def handleUserInput(_input):
    global running

    if _input == 1:
        store()
    elif _input == 2:
        index()
    elif _input == 3:
        show()
    elif _input == 4:
        delete()
    elif _input == 5:
        update()
    elif _input == 6:
        endProgram()
    else:
        print('Invalid input')
        

while running:
    printMenu()
    userInput = int(input("Enter a number: "))
    handleUserInput(userInput)



