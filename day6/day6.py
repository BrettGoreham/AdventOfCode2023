class Game:
    def __init__(self, time, record):

        self.time = time
        self.record = record

with open('day6Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

lengths = content[0].split(':')[1].strip().split()
records = content[1].split(':')[1].strip().split()

games = []
for x in range(len(lengths)):
    games.append(Game(int(lengths[x]), int(records[x])))

wins = []
for game in games:
    win = 0
    timeUsed = 1
    while timeUsed < game.time:
        timeleft = game.time - timeUsed
        distance = timeUsed * timeleft
        if distance > game.record:
            win += 1
        timeUsed += 1
    wins.append(win)

print(wins)
total = 1
for x in wins:
    total *= x

print(total)

time = ''
distance = ''

for game in games:
    time += str(game.time)
    distance += str(game.record)

game = Game(int(time),int(distance))
win = 0
middle = int(game.time / 2)
timeUsed = middle

while timeUsed > 0:
    timeleft = game.time - timeUsed
    distance = timeUsed * timeleft
    if distance > game.record:
        win += 1
    elif win > 0:
        break
    timeUsed -= 1

timeUsed = middle+1
while timeUsed < game.time:
    timeleft = game.time - timeUsed
    distance = timeUsed * timeleft
    if distance > game.record:
        win += 1
    else:
        break
    timeUsed += 1

print(win)