input = open('day1.txt')

elf_dict = {}
elf_num = 0

for line in input:
    
    if line.strip() == '':      
        elf_num+=1
    else:
        if elf_num  not in elf_dict:
            elf_dict[elf_num] = []
        elf_dict[elf_num].append(int(line.strip()))

max_value = 0
max_elf = 0
sum_list = []
descending_list = []
for elf in elf_dict:
    elf_list = elf_dict[elf]
    sum_value = sum(elf_list)
    sum_list.append(sum_value)
    if sum_value > max_value:
        max_value = sum_value
        max_elf = elf

print(max_elf+1, max_value)
reversed_list = list(reversed(sorted((sum_list))))
sum = reversed_list[0] + reversed_list[1] + reversed_list[2]
print(sum)
