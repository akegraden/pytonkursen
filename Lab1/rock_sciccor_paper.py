# Lab - inlämningsuppgift 1
import inquirer
import random
 
class Game:
 
    def __init__(self, rounds):
        self.rounds = rounds
        self.c_win = 0
        self.u_win = 0
 
    def round(self, u_choice):
        c_choice = random.randrange(0, 3)
        
        self.comp = f"{c_choice}{u_choice}"     # concatenate index of computers random choice resp. users
        self.user = f"{u_choice}{c_choice}"     # concatenate index of users choice with computers
        self.winnerList = ["01", "12", "20"]     # winner combinations
        self.compWinner = self.comp in self.winnerList     # Is computer the winner? (False/True)
        self.userWinner = self.user in self.winnerList     # Is user the winner? (False/True)

        if self.compWinner == True:       # Datorn vann
            self.c_win += 1
            self.winner = "Datorn"
        elif self.userWinner == True:     # Du vann
            self.u_win += 1
            self.winner = "Du"
        else:
           self.winner = "" 

        if self.winner != "":
            print(f'Vinnare denna omgång är {self.winner}')
        else:        
            print('Ingen vann denna omgång')
         
        if self.c_win == self.rounds:
            return 'Datorn'
        elif self.u_win == self.rounds:
            return 'Du'
        else:
            return ''
    
    def show_winner(self, winner):
        self.winner = winner
        print(f'{chr(10)}Slutlig vinnare först till {self.rounds} segrar är {self.winner}! {chr(10)}Grattis!!{chr(10)}')


# - - - - - Game
game = Game(3)
 
# Init question
possible_choices=['Sten', 'Sax', 'Påse']
question = [
    inquirer.List('val',
            message="Välj en av nedan tre alternativ",
            choices=possible_choices,
        ),
]
   
# Enter game loop
while True:
    answers = inquirer.prompt(question)
    result = game.round(possible_choices.index(answers["val"]))
    if result != '':
        # Game over
        result = game.show_winner(result)
        #print(f'Game over! {result} is the winner!')
        break
