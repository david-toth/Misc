import numpy as np
import matplotlib.pyplot as plt

# Simulation-based

n = 100000

die_1 = np.random.randint(1, 7, size=n)
die_2 = np.random.randint(1, 7, size=n)

sum_of_dice = die_1 + die_2

p_sum_is_1 = sum(sum_of_dice == 1)/n
p_sum_is_4 = sum(sum_of_dice == 4)/n
p_sum_less_13 = sum(sum_of_dice < 13)/n

print("Probability sum is equal to 1: {}".format(p_sum_is_1))
print("Probability sum is equal to 4: {}".format(p_sum_is_4))
print("Probability sum is less than 13: {}".format(p_sum_less_13))


# Exact

outcomes = [i+j for i in range(1,7) for j in range(1,7)]

p1 = outcomes.count(1)/len(outcomes)
p4 = outcomes.count(4)/len(outcomes)
p13 = len([i for i in outcomes if i < 13])/len(outcomes)

print("Probability sum is equal to 1: {}".format(p1))
print("Probability sum is equal to 4: {}".format(p4))
print("Probability sum is less than 13: {}".format(p13))
