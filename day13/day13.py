with open('day13Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]


puzzles = []

puzzle = []
for line in content:
    if line == '':
        puzzles.append(puzzle)
        puzzle = []
    else:
        puzzle.append(line)

puzzles.append(puzzle)


verticalLinesLeft = 0
horizontalLinesAbove = 0
verticalLinesLeftPart2 = 0
horizontalLinesAbovePart2 = 0
for puzzle in puzzles:

    width = len(puzzle[0])
    height = len(puzzle)
    #Check for vertical
    for x in range(width - 1):
        incorrect = 0
        left = x
        right = x+1

        while left >= 0 and right < width and incorrect <= 1:
            for y in range(height):
                if puzzle[y][left] != puzzle[y][right]:
                    incorrect += 1

            left -= 1
            right += 1

        if incorrect == 0:
            verticalLinesLeft += x + 1
        if incorrect == 1:
            verticalLinesLeftPart2 += x + 1

    # Check for horizontal
    for y in range(height - 1):
        incorrect = 0
        top = y
        bottom = y + 1

        while top >= 0 and bottom < height and incorrect <= 1:
            for x in range(width):
                if puzzle[top][x] != puzzle[bottom][x]:
                    incorrect += 1

            top -= 1
            bottom += 1

        if incorrect == 0:
            horizontalLinesAbove += y + 1
        if incorrect == 1:
            horizontalLinesAbovePart2 += y + 1


print(horizontalLinesAbove * 100 + verticalLinesLeft)
print(horizontalLinesAbovePart2 * 100 + verticalLinesLeftPart2)
