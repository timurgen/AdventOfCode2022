

items = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

with open('input.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

sum_of_priorities = 0

sum_of_badges = 0
cur_group = []

for line in data:
    split_on = len(line) // 2
    # part 1
    first, second = (set(line[:split_on]),line[split_on:])
    recurrent = [char for char in first if char in second]
    sum_of_priorities += sum([items.index(item) +1 for item in recurrent])
    # part 2
    cur_group.append(line)
    if len(cur_group) == 3:
        recurrent = set.intersection(*[set(item) for item in cur_group])
        sum_of_badges += items.index(recurrent.pop()) + 1
        cur_group = []

print(sum_of_priorities)
print(sum_of_badges)

