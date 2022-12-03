# The first column: what the opponent going to play
# A for Rock, B for Paper, and C for Scissors
# The second column, you reason, must be what you should play in response: 
# X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

# Point system:
# 1 for Rock, 2 for Paper, and 3 for Scissors) 
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)



# A - rock - only paper wins (Y)
# B - paper only scissor wins (Z)
# C- Scissors - only rock wins (X)
# Open the file


#   X Y Z
# A - O X
# B X - O  
# C O X - 
input = open('day2.txt')

score = 0 
# Iterate through the file
for line in input:
    stripped_line = line.strip()
    list_line = stripped_line.split(' ')
    if list_line[0] == 'A':
        if list_line[1] == 'Y':
                score += 4
        elif list_line[1] == 'X':
                score += 3
        elif list_line[1] == 'Z':
                score += 8
    if list_line[0] == 'B':
        if list_line[1] == 'Y':
                score += 5
        elif list_line[1] == 'X':
                score += 1
        elif list_line[1] == 'Z':
                score += 9
    if list_line[0] == 'C':
        if list_line[1] == 'Y':
                score += 6
        elif list_line[1] == 'X':
                score += 2
        elif list_line[1] == 'Z':
                score += 7


print(score)
# check the winner

# calculate score

# return total score