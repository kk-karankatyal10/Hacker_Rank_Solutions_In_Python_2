def breakingRecords(scores):
    Large= scores[0]
    Small= scores[0]
    HighScore=0
    LowScore=0
    for i in scores:
        if i> Large:
            Large=i
            HighScore+=1
        elif i< Small:
            Small=i
            LowScore+=1
    return (HighScore,LowScore)
