a = ['10,12,14,13,15']
b = ['2,0,3,2,1']

wins = 0
looses = 0
draws = 0

for i in range(str(a)):

    if a[i] < b[i]:
        print('a wins')