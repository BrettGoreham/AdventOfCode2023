from  functools import cmp_to_key
# rank
# 5 = 0
# 4 = 1
# full house = 2
# 3 = 3
# 2 pair = 4
# 1 pair = 5
# else 6
class Game:
    def __init__(self, hand, bid):

        self.hand = hand
        self.bid = bid
        self.rank = get_rank_from_hand(self.hand)


with open('day7Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]



def get_rank_from_hand(hand):
    all_freq = {}

    for i in hand:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

    max_val = max(all_freq.values())

    if max_val == 5:
        return 0
    if max_val == 4:
        return 1
    if max_val == 3:
        for x in all_freq.values():
            if x == 2:
                return 2
        return 3
    if max_val == 2:
        count2 = 0
        for x in all_freq.values():
            if x == 2:
                count2 += 1
        if count2 == 2:
            return 4
        else:
            return 5

    return 6


def compare(item1, item2):
    if item1.rank < item2.rank:
        return -1
    elif item1.rank > item2.rank:
        return 1
    else:
        for x in range(len(item1.hand)):
            val1 = get_card_value(item1.hand[x])
            val2 = get_card_value(item2.hand[x])
            if val1 > val2:
                return -1
            elif val1 < val2:
                return 1
        return 0


def get_card_value(letter:str):
    if letter.isdigit():
        return int(letter)
    elif letter == 'T':
        return 10
    elif letter == 'J':
        return 11
    elif letter == 'Q':
        return 12
    elif letter == 'K':
        return 13
    elif letter == 'A':
        return 14


hands = []
bids = []
for line in content:
    hands.append(Game(line.split()[0], int(line.split()[1])))


hands = sorted(hands, key=cmp_to_key(compare), reverse=True)

total = 0
count = 1
for hand in hands:
    total += hand.bid * count
    count += 1

print('part 1: ' + str(total))


class Game2:
    def __init__(self, hand, bid):

        self.hand = hand
        self.bid = bid
        self.rank = get_rank_from_hand2(self.hand)


with open('day7Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]


def get_rank_from_hand2(_hand):
    all_freq = {}
    jokers = 0

    for i in _hand:
        if i == 'J':
            jokers += 1
        else:
            if i in all_freq:
                all_freq[i] += 1
            else:
                all_freq[i] = 1
    max_val = 0
    if len(all_freq) > 0:
        max_val = max(all_freq.values())

    if max_val + jokers == 5 or jokers == 5:
        return 0
    if max_val + jokers == 4 or jokers == 4:
        return 1
    if max_val + jokers == 3 or jokers == 3:
        count2 = 0
        for x in all_freq.values():
            if x == 2:
                count2 += 1

        if count2 == 2 and jokers == 1:
            return 2
        if max_val == 3 and (jokers == 1 or jokers == 2 or count2 == 1):
            return 2

        return 3
    if max_val + jokers == 2 or jokers == 2:
        if jokers == 2:
            return 4
        elif jokers == 0:
            count2 = 0
            for x in all_freq.values():
                if x == 2:
                    count2 += 1
            if count2 == 2:
                return 4
        return 5

    return 6


def compare2(item1, item2):
    if item1.rank < item2.rank:
        return -1
    elif item1.rank > item2.rank:
        return 1
    else:
        for x in range(len(item1.hand)):
            val1 = get_card_value2(item1.hand[x])
            val2 = get_card_value2(item2.hand[x])
            if val1 > val2:
                return -1
            elif val1 < val2:
                return 1
        return 0


def get_card_value2(letter: str):
    if letter.isdigit():
        return int(letter)
    elif letter == 'T':
        return 10
    elif letter == 'J':
        return 0
    elif letter == 'Q':
        return 12
    elif letter == 'K':
        return 13
    elif letter == 'A':
        return 14


hands = []
bids = []
for line in content:
    hands.append(Game2(line.split()[0], int(line.split()[1])))


hands = sorted(hands, key=cmp_to_key(compare2), reverse=True)

total = 0
count = 1
for hand in hands:
    total += hand.bid * count
    count += 1

print('part 2: ' +str(total))