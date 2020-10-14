import numpy as np

p = 0.6
q = 0.4
k = 2
trials = 10000
n4 = 0

for i in range(trials):
    fortune = k

    while (fortune > 0) and (fortune < 100):
        result = 1 if np.random.binomial(1,p,1) else -1
        fortune += result

    if fortune >= 100:
        n4 += 1

print(n4/trials)
