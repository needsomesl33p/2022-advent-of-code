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


def analyze_rucksack(rucksack: str):    
    length = len(rucksack)//2
    first_half = rucksack[:length]
    second_half = rucksack[length:]

    for letter in first_half:
        if letter in second_half:
            return letter


def main():
    rucksacks = load_input()
    lookup_tbl = create_lookup_tables()
    summed = 0

    for rucksack in rucksacks:
        rsack = rucksack.strip()
        letter = analyze_rucksack(rsack)
        value = lookup_tbl[letter]
        summed += value

    print(summed)

if __name__ == '__main__':
    main()
