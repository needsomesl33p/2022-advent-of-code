import re


def load_input(file_path):
    with open(file_path, mode='r') as file:
        return [line.rstrip() for line in file]


def transform_stacks(stacks):
    #[A] [C]
    # 0123456
    columns = 9
    matrix = [[] for i in range(columns)]
    step = 4

    for stack_row in stacks:
        next = 1
        iter = len(stack_row) // step + 1
        for i in range(iter):
            crate = stack_row[next]
            if crate != ' ':
                matrix[i].append(crate)
            next += step

    return matrix


def transform_moves(moves):
    instructions = []
    pattern = '[0-9]?[0-9]'
    for move in moves:
        instructions.append(re.findall(pattern, move))

    return instructions


def process_instruction(instruction_set, stack_matrix):
    crate_num = int(instruction_set[0])
    source = int(instruction_set[1]) - 1
    target = int(instruction_set[2]) - 1

    source_stack: list = stack_matrix[source]
    target_stack: list = stack_matrix[target]
    tmp_list: list = source_stack[:crate_num]

    for item in tmp_list:
        source_stack.remove(item)
        target_stack.insert(0, item)


def print_first_letters(stack_matrix):
    for stack in stack_matrix:
        print(stack[0], end='')


def main():
    raw_stacks = load_input('init_stacks.txt')
    raw_moves = load_input('moves.txt')
    stacks = transform_stacks(raw_stacks)
    moves = transform_moves(raw_moves)
    # [print(stack) for stack in stacks]
    # [print(move) for move in moves]
    for instruction_set in moves:
        process_instruction(instruction_set, stacks)

    print_first_letters(stack_matrix=stacks)


if __name__ == '__main__':
    main()
