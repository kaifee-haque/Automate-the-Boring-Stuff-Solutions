import random

def streaks_in_list():
    flip_list = []
    counter = 0
    for i in range(100):
        flip_list.append(random.choice(["H", "T"]))
    for i in range(95):
        for j in range(6):
            if flip_list[i + j] != flip_list[i]:
                return False
            if j == 5:
                return True

def percent_of_streaks(trials):
    streaks = 0
    for i in range(trials):
        if streaks_in_list() == True:
            streaks += 1
    return streaks / trials

print(f"Chance of streak: {percent_of_streaks(10000) * 100}%")
