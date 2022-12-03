def load_input():
    with open('input.txt', mode='r') as file:
        content = file.read()
        return content.split('\n')

# A = Rock = X 1
# B = Paper = Y 2
# C = Scissors = Z 3


def simulation(opponent: str, you: str):
    result = 0
    result += win(opponent, you)

    if result == 0:
        result += draw(opponent, you)

    if result == 0:
        result = lose(opponent, you)

    return result


def win(opponent: str, you: str):
    if opponent == 'A' and you == 'Y':
        return 8
    elif opponent == 'B' and you == 'Z':
        return 9
    elif opponent == 'C' and you == 'X':
        return 7
    else:
        return 0


def draw(opponent: str, you: str):
    if opponent == 'A' and you == 'X':
        return 4
    elif opponent == 'B' and you == 'Y':
        return 5
    elif opponent == 'C' and you == 'Z':
        return 6
    else:
        return 0


def lose(opponent: str, you: str):
    if opponent == 'A' and you == 'Z':
        return 3
    elif opponent == 'B' and you == 'X':
        return 1
    elif opponent == 'C' and you == 'Y':
        return 2
    else:
        return 0


def main():
    rounds = load_input()
    final_score = 0
    for round in rounds:
        outcomes = round.split(' ')
        opponent = outcomes[0]
        you = outcomes[1]
        final_score += simulation(opponent, you)

    print(final_score)


if __name__ == '__main__':
    main()
