def load_input():
    with open('inputs.txt', mode='r') as file:
        content = file.readlines()
        return content


def main():
    pairs = load_input()
    overlaps = 0
    for pair in pairs:
        elf_ids: list = pair.split(',')
        elf_one: list = elf_ids[0].split('-')
        elf_two: list = elf_ids[1].split('-')
        elf_one_low_limit: int = int(elf_one[0])
        elf_one_high_limit: int = int(elf_one[1])
        elf_two_low_limit: int = int(elf_two[0])
        elf_two_high_limit: int = int(elf_two[1])

        if elf_one_low_limit <= elf_two_low_limit and elf_one_high_limit >= elf_two_high_limit:
            overlaps += 1
        elif elf_one_low_limit >= elf_two_low_limit and elf_one_high_limit <= elf_two_high_limit:
            overlaps += 1

    print(overlaps)


if __name__ == '__main__':
    main()
