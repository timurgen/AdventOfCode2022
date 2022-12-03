
# x 1
# y 2
# z 3
# lost 0
# draw 3
# won 6
# op
# A - rock
# B - paper
# C - scissors
# me 
# X - rock
# Y - paper
# Z - scissors

# won - need to return 6
# Z - B -> 90 - 66 == 24
# Y - A -> 89 - 65 == 24
# X - C -> 88 - 67 == 21

# draw - need to return 3
# always 23

#loose - need to return 0
# Z - A -> 90 - 65 == 25
# Y - C -> 89 - 67 == 22
# X - B -> 88 - 66 == 22


# A = 65
# B = 66
# C = 67

# X = 88 - loose
# Y = 89 - draw
# Z = 90 - win

lines = open('input.txt', 'r').readlines()

# part 1
def get_round_outcome(op, me):
    result = ord(me) - ord(op)
    return 3 if result == 23 else 6 if result in [21, 24] else 0

total_score = 0
print(sum([get_round_outcome(c[0], c[1]) + (-87 + ord(c[1])) for line in lines if (c := tuple(line.strip().split(" ")))]))



# part 2
def pick_draw(op_choice):
    return chr(ord('Y') + (-66 + ord(op_choice)))

def pick_loose(op_choice):
    return 'X' if op_choice == 'B' else 'Y' if op_choice == 'C' else 'Z'

def pick_win(op_choice):
    return 'X' if op_choice == 'C' else 'Y' if op_choice == 'A' else 'Z'

sum = 0
for line in lines:
    op_choice, my_choice = tuple(line.strip().split(" "))
    if my_choice == 'Y':
        my_choice = pick_draw(op_choice)
    elif my_choice == 'X':
        my_choice = pick_loose(op_choice)
    else:
        my_choice = pick_win(op_choice)

    sum += get_round_outcome(op_choice, my_choice) + (-87 + ord(my_choice))

print(sum)    
    

