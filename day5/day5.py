with open('day5Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

class Complex:

    def __init__(self, deststart, sourcestart, range):

        self.dest = deststart
        self.source = sourcestart
        self.range = range

class SeedRange:

    def __init__(self, start, range):

        self.start = start
        self.range = range


seedsStrings = content[0].split(': ')[1].split(' ')
seeds = [int(x) for x in seedsStrings]
print(seeds)
seedRanges = []
for x in range(0, len(seeds), 2):
    seedRanges.append(SeedRange(seeds[x], seeds[x+1]))

mapsMaps = []
currMap = []
linenum  = 2
highest = 0
while linenum < len(content):
    line = content[linenum]
    if len(line) == 0:
        mapsMaps.append(currMap)
        currMap = []
    elif line[0].isdigit():
        comps = line.split(' ')
        currMap.append(Complex(int(comps[0]), int(comps[1]), int(comps[2])))

    linenum += 1

mapsMaps.append(currMap)

lowestlocation = 11111111111111111111
for seed in seeds:
    val = seed
    for mapping in mapsMaps:
        print('new map')
        for obj in mapping:
            if obj.source <= val < obj.source + obj.range:
                val = obj.dest + (val - obj.source)
                print('new val : ' + str(val))
                break
    if val < lowestlocation:
        print('new lowest ' + str(val))
        lowestlocation = val


print('part 1: ' + str(lowestlocation))



location = -1
found = False
while not found:
    location += 1
    val = location


    c = len(mapsMaps) - 1
    while c >= 0:
        for obj in mapsMaps[c]:
            if obj.dest <= val < obj.dest + obj.range:
                val = obj.source + (val - obj.dest)
                break
        c -= 1

    for seedRange in seedRanges:
        if seedRange.start <= val < seedRange.start + seedRange.range:
            found = True

print('part 2: ' + str(location))
