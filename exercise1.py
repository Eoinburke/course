A = [1, 2, 4, 3, 5]
B = [2, 0, 3, 2, 1]

def listComp(listA, listB):
    wins = 0
    ties = 0
    losses = 0


    for a, b in zip(listA, listB):
        if a < b:
            wins += 1
        elif a == b:
            ties += 1
        else:
            losses += 1

    return wins, ties, losses
