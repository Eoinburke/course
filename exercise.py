plr1 = [10,6,8,9,7,12,7]
plr2 = [7,6,9,5,2,8,11]


wins = 0

ties = 0

losses = 0

for plr1, plr2 in zip(plr1, plr2):
        if plr1 < plr2:
            losses += 1
            print('Player 2 wins' + ' with'  plr2[0] + ' beating' plr1[0])

        elif plr1 > plr2:
             wins += 1
             print('Player 1 wins')

        else:
            plr1 == plr2
            ties += 1
            print('Draw')

    

