"""Practice with dictionaries."""

__author__ = "730394836"


def invert(old: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values."""
    new: dict[str, str] = dict()
    for key in old:
        count: int = 0
        new[old[key]] = key
        for item in old:
            if old[key] == old[item]:
                count += 1
            if count >= 2:
                raise KeyError("You cant have two keys or values twice.")
    return new


def favorite_color(ppl: dict[str, str]) -> str:
    """Returns most frequent color."""
    red: int = 0
    orange: int = 0
    yellow: int = 0
    green: int = 0
    blue: int = 0
    purple: int = 0
    pink: int = 0
    if ppl == {}:
        return "No favorite colors."
    for person in ppl:
        if ppl[person] == "red":
            red += 1
        if ppl[person] == "orange":
            orange += 1
        if ppl[person] == "yellow":
            yellow += 1
        if ppl[person] == "green":
            green += 1
        if ppl[person] == "blue":
            blue += 1
        if ppl[person] == "purple":
            purple += 1
        if ppl[person] == "pink":
            pink += 1
    if red == 1 and orange == 1 and yellow == 1 and green == 1 and blue == 1 and purple == 1 and pink == 1:
        return "No favorite colors."
    if red > orange and red > yellow and red > green and red > blue and red > purple and red > pink:
        return "red"
    if orange > red and orange > yellow and orange > green and orange > blue and orange > purple and orange > pink:
        return "orange"
    if yellow > orange and yellow > red and yellow > green and yellow > blue and yellow > purple and yellow > pink:
        return "yellow"
    if green > orange and green > yellow and green > red and green > blue and green > purple and green > pink:
        return "green"
    if blue > orange and blue > yellow and blue > green and blue > red and blue > purple and blue > pink:
        return "blue"
    if purple > purple > orange and purple > yellow and purple > green and purple > blue and purple > red and purple > pink:
        return "purple"
    return "pink"


def count(lis: list[str]) -> dict[str, int]:
    """Counts the number of times an item appears in the list."""
    dic: dict[str, int] = {}
    i: int = 0
    if lis == []:
        return dic
    while i < len(lis):
        if lis[i] in dic:
            dic[lis[i]] += 1
        else:
            dic[lis[i]] = 1
        i += 1
    return dic
