with open('day14Input.txt') as f:
    content = f.readlines()
content = [list(x.strip()) for x in content]

cycles = []
total = 0
#north
for cycle in range(200):
    print(cycle + 1)
    #north
    for x in range(len(content[0])):
        for y in range(len(content)):
            if content[y][x] == 'O':
                roll = y-1
                done = False
                while not done and roll >= 0:
                    if content[roll][x] == '.':
                        roll -= 1
                    else:
                        done = True

                if roll + 1 != y:
                    content[roll+1][x] = 'O'
                    content[y][x] = '.'


    #west
    for y in range(len(content)):
        for x in range(len(content[0])):
            if content[y][x] == 'O':
                roll = x - 1
                done = False
                while not done and roll >= 0:
                    if content[y][roll] == '.':
                        roll -= 1
                    else:
                        done = True

                if roll + 1 != x:
                    content[y][roll + 1] = 'O'
                    content[y][x] = '.'


    # south
    for x in range(len(content[0])):
        for y in range(len(content) - 1, - 1,  -1):
            if content[y][x] == 'O':
                roll = y + 1
                done = False
                while not done and roll <= len(content) - 1:
                    if content[roll][x] == '.':
                        roll += 1
                    else:
                        done = True

                if roll - 1 != y:
                    content[roll - 1][x] = 'O'
                    content[y][x] = '.'

    # west
    for y in range(len(content)):
        for x in range(len(content[0]) - 1, -1,  -1):
            if content[y][x] == 'O':
                roll = x + 1
                done = False
                while not done and roll <= len(content[0]) - 1:
                    if content[y][roll] == '.':
                        roll += 1
                    else:
                        done = True

                if roll - 1 != x:
                    content[y][roll - 1] = 'O'
                    content[y][x] = '.'


    total = 0
    for x in range(len(content[0])):
        for y in range(len(content)):
            if content[y][x] == 'O':
                total += len(content) - y

    cycles.append(total)

print(cycles)
# Dont know how to programatically find cycles correctly insert shrug emoji
# find cycle in pattern then cycles - indexs of cycle starts % cycle length = index of answer in cycle.
# my input cycles after a while to the same 0 numbers of and the last one i printed starts at 199
# 96003, 95985, 95971, 95962, 95961, 95981, 96001, 96020, 96014,
# 1000000000 - 199 % 9 = 0 = 96003
