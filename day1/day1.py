with open('day1Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

total = 0

for line in content:
    left = 0
    right =len(line) - 1
    found = False
    while not found:
        if line[left].isdigit():
            found = True
        else:
            left += 1

    found = False
    while not found:
        if line[right].isdigit():
            found = True
        else:
            right -= 1

    num = int('' + str(line[left]) + str(line[right]))
    total += num

print('part 1 ' + str(total))


numLetters = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

total = 0
for line in content:
    left = 0
    right =len(line) - 1
    found = False
    leftVal, rightVal = -1, -1
    while not found:
        if line[left].isdigit():
            leftVal = int(line[left])
            found = True

        for x in range(len(numLetters)):
            lenlett = len(numLetters[x])
            if left + 1 - lenlett >= 0:
                strs = line[left - lenlett + 1:left + 1]
                if strs == numLetters[x]:
                    found = True
                    leftVal = x + 1
        left += 1

    found = False
    while not found:
        if line[right].isdigit():
            found = True
            rightVal = int(line[right])

        for x in range(len(numLetters)):
            lenlett = len(numLetters[x])
            if right + lenlett <= len(line):

                strs = line[right: lenlett + right]
                if strs == numLetters[x]:
                    found = True
                    rightVal = x + 1
        right -= 1

    num = int(str(leftVal) + str(rightVal))
    total += num

print('part 2 ' + str(total))
