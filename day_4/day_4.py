from operator import and_, or_

with open('input.txt', 'r') as f:
    data = f.readlines()


def range_in_range(a, b, strict= False):
    if not strict:
        return set(range(a[0], a[1]+1)).issubset(range(b[0], b[1]+1))
    return len(set(range(a[0], a[1]+1)).intersection(range(b[0], b[1]+1))) > 0

overlapped_ranges_full = 0
overlapped_ranges_part = 0

for line in data:
    ranges = [list(map(int, elf.split("-"))) for elf in line.strip().split(",")]
    if range_in_range(ranges[0], ranges[1]) or range_in_range(ranges[1], ranges[0]):
        overlapped_ranges_full += 1
    # part 2
    if range_in_range(ranges[0], ranges[1], True) or range_in_range(ranges[1], ranges[0], True):
        overlapped_ranges_part += 1

print(overlapped_ranges_full)
print(overlapped_ranges_part)
