 
def run_1():
    print(max([sum(map(int, [i for i in elf.split('\n') if i != ''])) for elf in open('input.txt', 'r').read().split('\n\n')]))


def run_2():
    with open('input.txt', 'r') as f:
        data = f.readlines()

    elf_cal_list = []
    cur_cal_counter = 0
    for line in data:
        if line == '\n':
            elf_cal_list.append(cur_cal_counter)
            cur_cal_counter = 0
            continue

        cur_cal_counter += int(line)

    elf_cal_list.sort()
    print(sum(elf_cal_list[-3:]))

if __name__ == '__main__':
    run_1()
    run_2()
