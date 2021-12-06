###--- Day 6: Lanternfish ---
###Hacked together in python By AndrewH
###2021/12/06

#CONST
NEWFISH = 8
RESETFISH = 6

def TickDown(di):
    return {k - 1: v for k, v in di.items()}
#enddef

def Spawn(di):
    copy = {k:v for k, v in di.items()}

    if -1 in di:
        if NEWFISH in copy:
            copy[NEWFISH] = di[-1] + copy[NEWFISH]
        else:
            copy[NEWFISH] = di[-1]

    return copy
#enddef

def Reset(di):
    copy = {k:v for k, v in di.items() if k != -1}

    if -1 in di:
        if RESETFISH in copy:
            copy[RESETFISH] += di[-1]
        else:
            copy[RESETFISH] = di[-1]
    return copy
#enddef

def Sum(di):
    return sum(di.values())
#enddef

inputFish = input('Enter Input Array:').split(',')
pool = {int(x): inputFish.count(x) for x in set(inputFish)}
cycles = int(input('Enter number of days to process:'))

print('Initial state: {0}'.format(pool))

for day in range(0, cycles):
    pool = TickDown(pool)
    pool = Spawn(pool)
    print('After {0} Days: {1}'.format(day+1, pool))
    pool = Reset(pool)
#endfor

print('Total fish after {0} days: {1}'.format(cycles, Sum(pool)))
      
