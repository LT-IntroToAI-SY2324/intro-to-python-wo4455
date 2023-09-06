# We will write a rock paper scissors game in class - Complete it in this file

import random

def game(userChoice):
    if userChoice != 'rock' or userChoice != 'paper' or userChoice != 'scissors':
        return "please input rock, paper, or scissors correctly"
    options = ['rock', 'paper', 'scissors']
    computerChoice = random.choice(options)
    choices = {'player': userChoice, 'computer': computerChoice}
    return choices

print(game(input("Choose rock, paper, or scissors ")))