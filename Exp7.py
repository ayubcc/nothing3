'''
                                          Experiment No : 7
                              Aim: WAP to implement Alpha-Beta Pruning Algorithm.
                                                                           
                                                                          @Learner: TE-CO
                                                                                           Name: PATEL MUSKAN KASIM SHAH.
                                                                                           Roll No: 22DCO04
                                                                                           Batch: 1
                                                                                           Academic Year: 2024
                                                                                           Sem - 6
                                                                                           
# Introduction
Alpha-Beta Pruning optimizes decision-making algorithms, especially in games, by reducing the search space in the game tree. It does so by eliminating branches that are guaranteed to not affect the final decision. This technique dramatically improves the efficiency of algorithms like Minimax, making them suitable for complex games with large decision trees.

# Functions
- Alpha-Beta Pruning is a smart way to make decisions in games.
- It's like trimming branches of a decision tree to save time.
- Keeps track of the best choices so far.
- When it finds a choice that's definitely worse than another, it stops looking.
- This saves time by avoiding unnecessary exploration.
- Makes the decision process faster and more efficient.

## `main()`
The main function orchestrates the program's execution by calling the necessary functions. It retrieves user input for the scores array, calculates the tree depth, and then calls the `minimax` function to find the optimal value. The result is then printed to the console.

# Usage
. Alpha-Beta Pruning is used in the Minimax algorithm to make decisions in games efficiently. It saves time by ignoring branches of the game tree that won't affect the final decision. By keeping track of the best moves found so far, it avoids exploring unpromising paths, leading to faster decision-making.
'''
import math

class Node:
    def __init__(self, value, move=None):
        self.value = value
        self.move = move
        self.children = []

    def is_terminal(self):
        return len(self.children) == 0

    def evaluate(self):
        return self.value

    def generate_children(self):
        return self.children

class Game:
    def __init__(self):
        self.root = Node(0)

    def build_game_tree(self):
        # Example game tree generation
        node_A = Node(5, move="A")
        node_A1 = Node(7, move="A1")
        node_A2 = Node(3, move="A2")
        node_B = Node(2, move="B")
        node_B1 = Node(1, move="B1")
        node_B2 = Node(6, move="B2")
        node_C = Node(8, move="C")
        node_C1 = Node(4, move="C1")
        node_C2 = Node(9, move="C2")

        self.root.children = [node_A, node_B, node_C]
        node_A.children = [node_A1, node_A2]
        node_B.children = [node_B1, node_B2]
        node_C.children = [node_C1, node_C2]

def minimax_alpha_beta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or node.is_terminal():
        return node.evaluate(), None

    if maximizing_player:
        value = -math.inf
        best_move = None
        for child in node.generate_children():
            child_value, _ = minimax_alpha_beta(child, depth - 1, alpha, beta, False)
            if child_value > value:
                value = child_value
                best_move = child.move
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value, best_move
    else:
        value = math.inf
        best_move = None
        for child in node.generate_children():
            child_value, _ = minimax_alpha_beta(child, depth - 1, alpha, beta, True)
            if child_value < value:
                value = child_value
                best_move = child.move
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value, best_move

def visualize(node, depth=0, prefix="Root"):
    print("  " * depth + prefix + " -> Score:", node.value)
    for child in node.children:
        visualize(child, depth + 1, "Move: " + str(child.move))

# Example usage
game = Game()
game.build_game_tree()
score, move = minimax_alpha_beta(game.root, depth=3, alpha=-math.inf, beta=math.inf, maximizing_player=True)
print("Best Score:", score)
print("Best Move:", move)

# print("\nGame Tree Visualization:")
visualize(game.root)

# Output:-

# [Running] python -u "c:\Users\22DCO04\Desktop\sem 6\AI\Exp7.py"
# Best Score: 4
# Best Move: C
# Root -> Score: 0
#   Move: A -> Score: 5
#     Move: A1 -> Score: 7
#     Move: A2 -> Score: 3
#   Move: B -> Score: 2
#     Move: B1 -> Score: 1
#     Move: B2 -> Score: 6
#   Move: C -> Score: 8
#     Move: C1 -> Score: 4
#     Move: C2 -> Score: 9

# [Done] exited with code=0 in 0.13 seconds
