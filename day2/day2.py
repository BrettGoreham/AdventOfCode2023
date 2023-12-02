with open('day2Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

red = 12
green = 13
blue = 14

total = 0
totalPower = 0
for line in content:
    gameText, gameString = line.split(':')
    games = gameString.split(';')
    possible = True
    minRed, minGre, minBlue = 0, 0, 0
    for game in games:
        game = game.strip()
        colors = game.split(', ')
        redTot, greTot, blueTot = 0, 0, 0

        for color in colors:
            num, name = color.split(' ')
            if name[0] == 'r':
                redTot += int(num)
            elif name[0] == 'g':
                greTot += int(num)
            elif name[0] == 'b':
                blueTot += int(num)

        if redTot > red or greTot > green or blueTot > blue:
            possible = False

        if redTot > minRed:
            minRed = redTot
        if greTot > minGre:
            minGre = greTot
        if blueTot > minBlue:
            minBlue = blueTot

    power = minRed * minBlue * minGre
    totalPower += power
    if possible:
        total += int(gameText.split(' ')[1])

print('part 1 ' + str(total))
print('part 2 ' + str(totalPower))
