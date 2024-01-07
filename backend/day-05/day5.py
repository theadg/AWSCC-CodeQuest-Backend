import random

def getWinner(userChoice, computerChoice):
    winner = ''
    if userChoice.value == computerChoice.value:
        winner = 'It\'s a tie'
    elif userChoice.value == computerChoice.losesTo:
        winner = 'You won'
    elif computerChoice.value == userChoice.losesTo:
        winner = 'Computer won'
    else:
        winner = 'Nobody one'
    return winner

class Choice:
    def __init__(self, value, losesTo, winsTo):
        self.value = value
        self.losesTo = losesTo
        self.winsTo = winsTo

rock = Choice('rock', 'paper', 'scissors')
paper = Choice('paper', 'rock', 'scissors')
scissors = Choice('scissors', 'paper', 'rock')

choices = [
    rock,
    paper,
    scissors
]

computerChoice = random.choice(choices)

userInput = input('Your choice: ').lower()
# find user choice


def getChoice(userInput):
    return next((choice for choice in choices if choice.value == userInput), None)

userChoice = getChoice(userInput)

print(f"Computer Choice: {computerChoice.value}")
print(getWinner(userChoice, computerChoice))




