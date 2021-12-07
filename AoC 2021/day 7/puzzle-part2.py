#Something about crabs and submarines
#part 2
#AndrewH 
#2021/12/07

import timeit

start = timeit.timeit()


class csub:
    def __init__(self, position):
        self.position = position
        self.costs = {position : 0}

    def cost_to_pos(self, target):
        if self.position == target:
            return 0
        else:
            distance = abs(self.position - target)
            return (distance / 2) * (distance + 1)
#endclass

def avg(l):
    return int(sum(l) / len(l))
#enddef

def BSearchBestPath(lowInput, highInput, data):
    midTgt = avg([lowInput, highInput])

    lowTgt = lowInput
    highTgt = highInput

    lCost = sum([sub.cost_to_pos(lowTgt) for sub in data])
    hCost = sum([sub.cost_to_pos(highTgt) for sub in data])

    nLow = lowTgt if lCost < hCost else midTgt
    nHigh = midTgt if lCost < hCost else highTgt

    if nLow != nHigh:
        return BSearchBestPath(nLow, nHigh, data)
    else:
        return lowTgt
#enddef

inputFile = open('input.txt').read()
data = [ int(v) for v in inputFile.split(',')]

optIndex = BSearchBestPath(min(data), max(data), [csub(s) for s in data])

print('Optimal position is {0}, which costs {1} fuel'.format(optIndex, int(sum([csub(s).cost_to_pos(optIndex) for s in data]))))

end = timeit.timeit()

print('Completed in {} ms'.format(round(end-start, 4)))