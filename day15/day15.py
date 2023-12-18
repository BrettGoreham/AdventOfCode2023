with open('day15Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

total = 0
for thing in content[0].split(','):
    value = 0
    for c in thing:
        value += ord(c)
        value *= 17
        value = value % 256
    total += value
print('part 1: ' + str(total))


boxes = {}
for thing in content[0].split(','):
    value = 0
    indexOfSign = -1
    for index in range(len(thing)):
        c = thing[index]
        if c == '-' or c == '=':
            indexOfSign = index
            break
        else:
            value += ord(c)
            value *= 17
            value = value % 256
    if thing[indexOfSign] == '-':
        label = thing[:indexOfSign]
        box = boxes.get(value, [])
        indexRemov = -1
        for x in range(len(box)):
            if box[x][0] == label:
                indexRemov = x
                break
        if indexRemov >= 0:
            box.pop(indexRemov)
        boxes[value] = box
    else:
        label = thing[:indexOfSign]
        box = boxes.get(value, [])
        index = -1
        for x in range(len(box)):
            if box[x][0] == label:
                index = x
                box[x] = (label, thing[indexOfSign+1:])
                break
        if index == -1:
            box.append((label, thing[indexOfSign+1:]))

        boxes[value] = box


total = 0
for box in boxes.keys():
    boxval = boxes[box]
    c = 1
    for val in boxval:
        total += (box + 1) * c * int(val[1])
        c += 1

print('part 2: ' + total)

