with open('day10Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]


start = ()
for y in range(len(content)):
    for x in range(len(content[0])):
        if content[y][x] == 'S':
            start = (y, x)

print(start)

right = False
left = False
top = False
bottom = False


visited = {start:0}
visiting = [] # tuple[0] coordinates tuple[1] entering from direction

if start[0] != 0 and (content[start[0] -1][start[1]] == '|' or content[start[0] -1][start[1]] == '7' or content[start[0] -1][start[1]] == 'F'):
    visiting.append(((start[0]-1, start[1]), 'B', 1))
if start[1] != 0 and (content[start[0]][start[1] - 1] == '-' or content[start[0]][start[1] - 1] == 'L' or content[start[0]][start[1] - 1] == 'F'):
    visiting.append(((start[0], start[1] - 1), 'R', 1))
if start[0] != len(content) - 1 and (content[start[0] + 1][start[1]] == '|' or content[start[0] + 1][start[1]] == 'L' or  content[start[0] + 1][start[1]] == 'J'):
    visiting.append(((start[0] + 1, start[1]), 'T', 1))
if start[1] != len(content[0]) - 1 and (content[start[0]][start[1] + 1] == '-' or content[start[0]][start[1] + 1] == 'J' or content[start[0]][start[1] + 1] == '7'):
    visiting.append(((start[0], start[1] + 1), 'L', 1))


ans = -1
while len(visiting) > 0:

    visit = visiting.pop(0)
    if visit[0] in visited.keys():
        ans = visited[visit[0]]
        break

    visited[visit[0]] = visit[2]

    y = visit[0][0]
    x = visit[0][1]
    dist = visit[2] + 1

    if visit[1] == 'B':
        if content[y][x] == '|':
            visiting.append(((y-1, x), 'B', dist))
        elif content[y][x] == '7':
            visiting.append(((y, x-1), 'R', dist))
        else: # F
            visiting.append(((y, x+1), 'L', dist))
    if visit[1] == 'T':
        if content[y][x] == '|':
            visiting.append(((y+1, x), 'T', dist))
        elif content[y][x] == 'L':
            visiting.append(((y, x+1), 'L', dist))
        else: # J
            visiting.append(((y, x-1), 'R', dist))
    if visit[1] == 'L':
        if content[y][x] == '-':
            visiting.append(((y, x + 1), 'L', dist))
        elif content[y][x] == 'J':
            visiting.append(((y - 1, x), 'B', dist))
        else: # 7
            visiting.append(((y + 1, x), 'T', dist))
    if visit[1] == 'R':
        if content[y][x] == '-':
            visiting.append(((y, x - 1), 'R', dist))
        elif content[y][x] == 'F':
            visiting.append(((y + 1, x), 'T', dist))
        else: # L
            visiting.append(((y - 1, x), 'B', dist))



print(ans)

# did not come up with this myself read some tips online apparently if you just go from left to right
# and count how many vertical things you find
# if verticals are odd and you encounter an empty space its inside the shape. idk
enclosed = 0
for i in range(len(content)):
    inside = False
    for j in range(len(content[0])):
        if (i,j) in visited:
            if content[i][j] in '|LJ':
                inside = not inside
            continue
        if inside: enclosed += 1
print(enclosed)