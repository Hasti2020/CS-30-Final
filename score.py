###############################################################################
'''
This module manages  and andles the high score system. It will read the high 
score from 'Scores.txt' and updates it if the player gets a score higher
than their old one. It Keeps track of the best score across battle.
'''
###############################################################################
# Imports and Global Variables-------------------------------------------------
ScoreFile = "Scores.txt"
high_score = 0

def getScore():
    '''
    Reads the high score from the score file and updates the high_score .
    '''
    global high_score
    with open(ScoreFile, 'r') as file:
        high_score = int(file.read())

def newScore(newest_score):
    '''
    Writes the newest high score to the score file.
    '''
    with open(ScoreFile, 'w') as file:
        file.write(newest_score)