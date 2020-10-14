import numpy as np
import matplotlib.pyplot as plt

def flip():
    """
    Flip a coin.
    
    Returns 'H' with p=0.5
    and 'T' otherwise.
    """
    if(np.random.binomial(1, 0.5, 1)):
        return "H"

    else:
        return "T"
    
def find_pattern(ntrials):
    """
    Simulates flipping a fair
    coin until the pattern HTH
    appears

    Returns mean number of flips
    to observe pattern, unique flip
    counts with their probability
    masses.
    """
    total = np.empty(ntrials)

    for i in range(ntrials):
        current_count = 0
        pattern = ""

        while True:
            current_count += 1
            pattern += flip()

            if pattern == "HTH":
                total[i] = current_count
                break

            if pattern == "HTT":
                pattern = ""

            if pattern == "HH":
                pattern = pattern[-1]

            if pattern == "T":
                pattern = ""

    vals, counts = np.unique(total, return_counts=True)
    
    return total.mean(), vals, counts/counts.sum()


def main():
    mean_flips, vals, prob = find_pattern(100000)
    print("Mean number of flips until first observe 'HTH' is {}".format(mean_flips))
    plt.bar(vals, prob, edgecolor='black', linewidth=0.8)
    plt.xlim(vals.min(), vals.max())
    plt.xlabel("Number of Flips")
    plt.ylabel("Probability")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
    

                
        
