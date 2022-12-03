def load_input():
    with open('inputs.txt', mode='r') as file:
        content = file.readlines()
        return content


def process_blocks(snack_supply: list) -> list:
    sum_supply: list = []
    sum_item: int = 0
    for item in snack_supply:
        if item != '\n':
            sum_item += int(item)
        else:
            sum_supply.append(sum_item)
            sum_item = 0

    return sum_supply

def get_top_3_kcal(elfs_with_kcal: list) -> int:
    ranked = sorted(elfs_with_kcal, reverse=True)
    return ranked[0] + ranked[1] + ranked[2]


def main():
    calories = load_input()
    elfs_with_kcals = process_blocks(calories)
    max_kcal = max(elfs_with_kcals)
    top_3_kcal = get_top_3_kcal(elfs_with_kcals)
    print(max_kcal)
    print(top_3_kcal)


if __name__ == '__main__':
    main()
