import math

with open('day4Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

total = 0
countArray = []
for game in content:
    card, nums = game.split(':')
    ours, winning = nums.split('|')
    ourNums = ours.strip().split(' ')
    winningNums = winning.strip().split(' ')
    count = 0

    newNums = []
    for num in ourNums:
        if num.strip() != '':
            newNums.append(num.strip())

    for num in set(newNums):
        if num in winningNums:
            count += 1

    if count > 0:
        points = int(math.pow(2, count - 1))
        total += points
    countArray.append(count)

print('part 1: ' + str(total))

scratches = {}
for x in range(len(content)):
    scratches[x+1] = 1

total = 0
for x in range(1, len(content) + 1):
    total += scratches[x]
    wins = countArray[x - 1]
    for y in range(1, wins + 1):
        if y + x < len(content) + 1:
            scratches[y+x] += scratches[x]

print('part 2: ' + str(total))
