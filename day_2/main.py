
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


# part 1
def get_round_outcome(op, me):
    result = ord(me) - ord(op)
    return 3 if result == 23 else 6 if result in [21, 24] else 0

total_score = 0
print(sum([get_round_outcome(c[1], c[0]) + (-87 + ord(c[1])) for line in open('input.txt', 'r').readlines() if (c := tuple(line.strip().split(" ")))]))




    
