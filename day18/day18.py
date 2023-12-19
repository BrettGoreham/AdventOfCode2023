with open('day18Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]


vertices1 = list()
lengthTotal1 = 0
x1 = 0
y1 = 0

vertices2 = list()
lengthTotal2 = 0
x2 = 0
y2 = 0

for line in content:
    direc, length, color = line.split()

    if direc == 'R':
        x1 += int(length)
    if direc == 'L':
        x1 -= int(length)
    if direc == 'U':
        y1 -= int(length)
    if direc == 'D':
        y1 += int(length)

    vertices1.append((x1, y1))
    lengthTotal1 += int(length)

    numDirec = color[7]
    length2 = int(color[2:7], 16)
    if numDirec == '0':
        x2 += length2
    if numDirec == '2':
        x2 -= length2
    if numDirec == '3':
        y2 -= length2
    if numDirec == '1':
        y2 += length2

    vertices2.append((x2, y2))
    lengthTotal2 += length2


shoelace_area1 = abs(sum(
    (v1[0] + v2[0]) * (v1[1] - v2[1]) / 2
    for v1, v2 in zip(vertices1, vertices1[1:])
))

print('part 1: ' + str(int(shoelace_area1 + lengthTotal1 / 2 + 1)))

shoelace_area2 = abs(sum(
    (v1[0] + v2[0]) * (v1[1] - v2[1]) / 2
    for v1, v2 in zip(vertices2, vertices2[1:])
))

print('part 2: ' + str(int(shoelace_area2 + lengthTotal2 / 2 + 1)))

