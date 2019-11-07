def countApplesAndOranges(s, t, a, b, apples, oranges):
    appleCount = 0
    orangeCount = 0
    for appl in apples:
        if(appl+a >= s and appl+a <= t):
            appleCount += 1

    for orng in oranges:
        if(orng+b <= t and orng + b >= s):
            orangeCount += 1

    print(appleCount)
    print(orangeCount)
