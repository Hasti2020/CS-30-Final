ScoreFile = "Scores.txt"
high_score = 0

def getScore():
    global high_score
    with open(ScoreFile, 'r') as file:
        high_score = int(file.read())

def newScore(newest_score):
    with open(ScoreFile, 'w') as file:
        file.write(newest_score)