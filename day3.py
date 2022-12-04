# open file 
input = open('day3.txt')
# iterate through each line of text 
common_letters = []
# for line in input:
#     line = list(line.strip())
#     # print(line)
# # split line in half 
#     split_half = len(line)
#     split_half /= 2
#     split_half = int(split_half)
#     first_comp = line[:split_half]
#     second_comp = line[split_half:]
#     # print(first_comp)
#     # print(second_comp)
# # find the common character 
#     for letter in second_comp:
#         if letter in first_comp:
#             common_letters.append(letter)
#             break
# get value of common character               
score_sheet = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52   
    }
# score = 0
# for letter in common_letters:
#     add_score = score_sheet[letter]
#     # add to sum
#     score += add_score
# # return sum
# print(score)

three_line_list = []
second_common_letters = []
temp_list = []
for line in input:
    strip_line = line.strip()
    temp_list.append(strip_line)
    if len(temp_list) == 3:
            three_line_list.append(temp_list)
            temp_list = []

        
        # for l in three_line_list[0]:
        #     if (l in three_line_list[1]) and (l in three_line_list[2]):
        #         second_common_letters.append(l)
        #         break

# print(three_line_list)

for group in three_line_list:
    for letter in group[0]:
        if (letter in group[1]) and (letter in group[2]):
            second_common_letters.append(letter)
            break

# print(counter)
# print(second_common_letters)
# print(len(second_common_letters))
score = 0
for letter in second_common_letters:
    add_score = score_sheet[letter]
    # add to sum
    score += add_score
# return sum
print(score)

