#Something about crabs and submarines
#part 1
#AndrewH 
#2021/12/07

from statistics import median

inputFile = open('input.txt').read()

result = [ int(v) for v in inputFile.split(',')]

med = median(result)

left = [ med - v for v in result if v < med ]
right = [ v - med for v in result if v > med ]

cost = sum(left) + sum(right)

print('The optimal cost is {0} to align to position {1}'.format(int(cost), int(med)))
