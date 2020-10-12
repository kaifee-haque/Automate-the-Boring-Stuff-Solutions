#! python3
"""Using a given number of trials, calculates the probability that a streak of
6 heads or 6 tails will occur in a series of 100 coin tosses."""


import random


def streaks_in_list():
    """Determines whether or not a streak of 6 heads of 6 tails occurs in
    a given series.

    returns:
        A boolean indicating the presence of a streak.
    """
    
    flip_list = []
    for i in range(100):
        flip_list.append(random.choice(["H", "T"]))

    #For each item in the list of tosses, up until the 94th item, determines
    #whether or not the next 5 tosses produced the same result (making a streak).
    
    for i in range(95):
        for j in range(6):
            if flip_list[i + j] != flip_list[i]:
                return False
            if j == 5:
                return True


def percent_of_streaks(trials):
    """Calls the streaks_in_list function for each trial and determines the
    probability of a streak occurring.

    Args:
        trials: An integer representing the number of trials to perform.

    Returns:
        The probability of a streak of 6 occurring in a series of 100 coin tosses.
    """
    streaks = 0
    for i in range(trials):
        if streaks_in_list() == True:
            streaks += 1
    return streaks / trials


print(f"Chance of streak: {percent_of_streaks(10000) * 100}%")
