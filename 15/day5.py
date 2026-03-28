
VOWELS = "aeiou"
BANS = ["ab", "cd", "pq", "xy"]

def good(word):
    rule1 = False
    rule2 = False
    prev = ''
    counter = 0
    for char in word:
        if char in VOWELS:
            counter += 1
            rule1 = counter > 2
        test = f"{prev}{char}"
        if test in BANS:
            return False
        if char == prev:
            rule2 = True
        prev = char
    return rule1 and rule2

def good2(word):
    # 1. pair of letters >= 2x
    # 2. letter pair separated by letter check
    rule1 = False
    rule2 = False
    copy = ' '
    sep = ' '
    for i, char in enumerate(word):
        pair = f"{sep}{char}"
        left = word[i+1:]
        if pair in left:
            rule1 = True

        if copy == char and sep != char:
            rule2 = True
        copy = sep
        sep = char
        if rule1 and rule2:
            return True
    return rule1 and rule2


with open("input5.txt", "r") as file:
    counter = 0
    for word in file:
        counter += int(good2(word.rstrip()))

print(counter)
