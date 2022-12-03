import string


def load_input():
    with open('inputs.txt', mode='r') as file:
        content = file.readlines()
        return content


def create_lookup_tables():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    low_lookup_tbl = {}
    upper_lookup_tbl = {}
    x = len(uppercase)

    for i in range(0, x):
        low_lookup_tbl[lowercase[i]] = i + 1
        upper_lookup_tbl[uppercase[i]] = i + 27

    low_lookup_tbl.update(upper_lookup_tbl)
    return low_lookup_tbl


def analyze_rucksack(rucksacks: list):
    first_sack = set(rucksacks[0])
    second_sack = set(rucksacks[1])
    third_sack = set(rucksacks[2])

    for letter in first_sack:
        if letter in second_sack and letter in third_sack:
            return letter


def main():
    rucksacks = load_input()
    lookup_tbl = create_lookup_tables()
    summed = 0
    i = 0
    length = len(rucksacks)

    for i in range(0, length, 3):
        target_list = [
            rucksacks[i].strip(),
            rucksacks[i+1].strip(),
            rucksacks[i+2].strip()]
        letter = analyze_rucksack(target_list)
        value = lookup_tbl[letter]
        summed += value

    print(summed)


if __name__ == '__main__':
    main()
