'''
              EXPERIMENT NO :- 05


                   AIM :- Implementation of Wumpus World
    
                                                                NAME :- SOBAN WAJUDDIN MARUF 
                                                                ROLL NO :- 21CO58
                                                                BATCH :- 03


                                                                


The Wumpus World’s agent is an example of a knowledge-based agent that represents Knowledge representation, reasoning and planning. Knowledge-Based agent links general knowledge with current percepts to infer hidden characters of current state before selecting actions. Its necessity is vital in partially observable environments.

Problem Statement:
The Wumpus world is a cave with 16 rooms (4×4). Each room is connected to others through walkways (no rooms are connected diagonally). The knowledge-based agent starts from Room[1, 1]. The cave has – some pits, a treasure and a beast named Wumpus. The Wumpus can not move but eats the one who enters its room. If the agent enters the pit, it gets stuck there. The goal of the agent is to take the treasure and come out of the cave. The agent is rewarded, when the goal conditions are met. The agent is penalized, when it falls into a pit or being eaten by the Wumpus.
Some elements support the agent to explore the cave, like -The wumpus’s adjacent rooms are stenchy. -The agent is given one arrow which it can use to kill the wumpus when facing it (Wumpus screams when it is killed). – The adjacent rooms of the room with pits are filled with breeze. -The treasure room is always glittery.




'''


import random

class WumpusWorld:
    def __init__(self):
        self.grid_size = 4
        self.agent_position = (0, 0)
        self.wumpus_position = self.generate_random_position()
        self.gold_position = self.generate_random_position(exclude=[self.agent_position, self.wumpus_position])
        self.pit_positions = [self.generate_random_position(exclude=[self.agent_position, self.wumpus_position, self.gold_position]) for _ in range(3)]
        self.game_over = False

    def generate_random_position(self, exclude=[]):
        while True:
            position = (random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1))
            if position not in exclude:
                return position

    def is_valid_position(self, position):
        x, y = position
        return 0 <= x < self.grid_size and 0 <= y < self.grid_size

    def move_agent(self, action):
        x, y = self.agent_position
        if action == 'up':
            x -= 1
        elif action == 'down':
            x += 1
        elif action == 'left':
            y -= 1
        elif action == 'right':
            y += 1
        
        new_position = (x, y)
        if self.is_valid_position(new_position):
            self.agent_position = new_position
        else:
            print("Invalid move!")

    def check_percept(self):
        percepts = []
        if self.agent_position == self.wumpus_position:
            percepts.append("You smell a terrible stench!")
        if self.agent_position == self.gold_position:
            percepts.append("You see a glimmer!")
        for pit_position in self.pit_positions:
            if self.agent_position == pit_position:
                percepts.append("You feel a breeze!")
        return percepts

    def check_game_status(self):
        if self.agent_position == self.wumpus_position:
            print("You were eaten by the wumpus! Game Over!")
            self.game_over = True
        elif self.agent_position == self.gold_position:
            print("You found the gold! You Win!")
            self.game_over = True
        elif self.agent_position in self.pit_positions:
            print("You fell into a pit! Game Over!")
            self.game_over = True

    def print_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if (i, j) == self.agent_position:
                    print("A", end=" ")
                elif (i, j) == self.wumpus_position:
                    print("W", end=" ")
                elif (i, j) == self.gold_position:
                    print("G", end=" ")
                elif (i, j) in self.pit_positions:
                    print("P", end=" ")
                else:
                    print("-", end=" ")
            print()

    def play(self):
        print("Welcome to Wumpus World!")
        while not self.game_over:
            self.print_grid()
            print("Actions: (up, down, left, right)")
            action = input("Enter action: ")
            self.move_agent(action)
            percepts = self.check_percept()
            for percept in percepts:
                print(percept)
            self.check_game_status()

# Play the game
game = WumpusWorld()
game.play()



'''
output:   

Enter action: python -u "/home/aiktc/Desktop/Asif_ai/wumpus.py"
- A - P 
- - P W 
G - - - 
- P - - 
Actions: (up, down, left, right)
Enter action: left
A - - P 
- - P W 
G - - - 
- P - - 
Actions: (up, down, left, right)
Enter action: left
Invalid move!
A - - P 
- - P W 
G - - - 
- P - - 
Actions: (up, down, left, right)
Enter action: left
Invalid move!
A - - P 
- - P W 
G - - - 
- P - - 
Actions: (up, down, left, right)
Enter action: left
Invalid move!
A - - P 
- - P W 
G - - - 
- P - - 
Actions: (up, down, left, right)
Enter action: right
- A - P 
- - P W 
G - - - 
- P - - 
Actions: (up, down, left, right)
Enter action: bottom
- A - P 
- - P W 
G - - - 
- P - - 
Actions: (up, down, left, right)
Enter action: right
- - A P 
- - P W 
G - - - 
- P - - 
Actions: (up, down, left, right)
Enter action: lrft
- - A P 
- - P W 
G - - - 
- P - - 
Actions: (up, down, left, right)
Enter action: left
- A - P 
- - P W 
G - - - 
- P - - 
Actions: (up, down, left, right)
Enter action: right
- - A P 
- - P W 
G - - - 
- P - - 
Actions: (up, down, left, right)
Enter action: down
You feel a breeze!
You fell into a pit! Game Over!





'''