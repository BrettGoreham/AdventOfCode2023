with open('day8Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]


path = content[0]
placeMap = {}

part2 = []

for x in range(2, len(content)):
    line = content[x]
    place, pair = line.split(' = ')
    xx = pair.strip().split(', ')
    left = xx[0][1:]
    right = xx[1][:-1]
    placeMap[place] = [left, right]
    if place[2] == 'A':
        part2.append(place)

pathlen = len(path)
found = False
count = 0
curr = 'AAA'
while not found:
    check = count
    count += 1
    dir = path[check % pathlen]
    if dir == 'L':
        curr = placeMap[curr][0]
    else:
        curr = placeMap[curr][1]

    if curr == 'ZZZ':
        found = True

print(count)

pathlen = len(path)
found = False
count = 0


for x in part2:
    count = 0
    zIndex = []
    while len(zIndex) < 4:
        check = count
        count += 1
        dir = path[check % pathlen]
        if dir == 'L':
            x = placeMap[x][0]
        else:
            x = placeMap[x][1]

        if x[2] == 'Z':
            zIndex.append(count)
    print(zIndex)

#UseLowestCommonDenominator after this.^