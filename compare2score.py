"""First part is to import necessary modules"""

import os
"""Second part is to read the result of comparation"""
# initialize the score_board
score_board = {}
comp_num = 100 #how many comparation results we have
for i in range(1, comp_num):
# [how many times it loses, how many times it has been tested]
    score_board[str(i)] = [0,0]
 
comp_rds = open("compare.txt","r")
records = comp_rds.readlines()
for record in records:
    win = record[0]
    lose = record[1]
    score_board[lose][0] = score_board[lose][0] + 1
    score_board[win][1] = score_board[win][1] + 1
    score_board[lose][1] = score_board[lose][1] + 1

comp_rds.close()

"""Third part is to write final score into the file named compare.txt """
score = open("score.txt","a")
for i in range(1, comp_num):
    final_score = (1-score_board[str(i)][0]/score_board[str(i)][1])*100
    new_line = str(i) + " " + str(final_score) + "\n"
    score.write(new_line)
score.close()
