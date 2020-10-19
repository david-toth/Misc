################################################################################
#                               Urn Game Simulator                             #
#                                                                              #
# Given three urns (A, B, C) with some number of balls in each earn (a, b, c), #
# you randomly select one of the three urns with equal probability (p = 1/3).  #
# Then, you take one ball from this urn and add it to one of the remaining urns#
# where the selection of the second urn is also uniform (p=0.5 for each).      #
# The game ends when any of the urns is empty.                                 #
#                                                                              #
# GOAL: Compute mean number of steps until game is over.                       #
################################################################################
import numpy as np

def pick_urn(urns):
    """
    Randomly chooses an urn from a list
    of urn names, where the probability
    of choosing an urn is uniform over all
    urns.
    """
    p = [1/len(urns) for i in urns]
    urn = np.random.choice(urns, p=p)
    
    return urn

def play_game(n, a, b, c):
    """
    Simulates the urn game over n trials.
    Starting values for each earn are given by
    a, b, and c for urns A, B, and C, respectively.
    """
    steps_taken = np.empty(n)
    
    for i in range(n):
        empty = False
        it = 0
        urns = {'A': a, 'B': b, 'C': c}
        
        while not empty:
            it += 1
            pick = pick_urn(list(urns.keys()))
            pick2 = pick_urn([i for i in urns.keys() if i != pick])

            urns[pick] -= 1
            urns[pick2] += 1
            
            if any(v == 0 for v in urns.values()):
                empty = True
                steps_taken[i] = it

    return steps_taken.mean()

def main():
    num_trials = int(1e4)
    a = b = c = 4
    mean_steps = play_game(num_trials, a, b, c)
    print("Mean number of steps: ", mean_steps)

if __name__ == "__main__":
    main()

    
