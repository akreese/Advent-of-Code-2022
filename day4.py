# open file 
input = open('day4.txt')

# iterate through txt
counter = 0
# first_check = False
# second_check = False
for line in input:
    stripped_line = line.strip()
    split_line = stripped_line.split(",")
    # name variable or group for partner 1 and partner 2
    first_half = split_line[0].split("-")
    second_half = split_line[1].split("-")
    length_of_first = (int(first_half[1]) - int(first_half[0])) + 1
    length_of_second = (int(second_half[1]) - int(second_half[0])) + 1
    first_check = False
    second_check = False
    if length_of_first > length_of_second:
        if int(second_half[0]) in range(int(first_half[0]), int(first_half[1])+1) and int(second_half[1]) in range(int(first_half[0]), int(first_half[1])+1):
            counter += 1
    if length_of_second > length_of_first:
        if int(first_half[0]) in range(int(second_half[0]), int(second_half[1])+1) and int(first_half[1]) in range(int(second_half[0]), int(second_half[1])+1):
            counter += 1
    if length_of_second == length_of_first:
        if first_half == second_half:
            counter += 1

print(counter)



counter_2 = 0
for line in input:
    stripped_line = line.strip()
    split_line = stripped_line.split(",")
    # name variable or group for partner 1 and partner 2
    first_half = split_line[0].split("-")
    second_half = split_line[1].split("-")
    for i in range(int(first_half[0]), int(first_half[1])+1):
       if i in range(int(second_half[0]), int(second_half[1])+1):
        counter_2 += 1
        break
            
print(counter_2)