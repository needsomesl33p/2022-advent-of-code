from typing import List


def load_input() -> List:
    with open('inputs.txt', 'r') as file:
        return file.readlines()


def eval_line(tree: int, line: List):
    counter = 0
    if line:
        for near_tree in line:
            near_tree = int(near_tree)
            if tree > near_tree:
                counter += 1
            else:
                counter += 1
                break

    return counter


def multiply_trees(*args):
    score = 1
    unblocked_trees = [tree for tree in args if tree > 0]
    for tree in unblocked_trees:
        score *= tree

    return score


def transform_matrix(rows: List) -> List:
    matrix: List[List] = [[] for i in range(len(rows))]
    for line in rows:
        for index, tree in enumerate(line.rstrip()):
            matrix[index].append(tree)

    return matrix


def main():
    rows: List[str] = load_input()
    columns: List[List] = transform_matrix(rows)
    scores: List[int] = []

    for y, row in enumerate(rows):
        row = row.rstrip()
        for x, tree in enumerate(row):
            tree = int(tree)
            column = columns[x]
            trees_on_left = row[:x][::-1]
            trees_on_right = row[x+1:]
            trees_above = column[:y][::-1]
            trees_below = column[y+1:]

            score = multiply_trees(eval_line(tree, trees_on_left), eval_line(tree, trees_on_right),
                eval_line(tree, trees_above), eval_line(tree, trees_below))
            scores.append(score)
    
    print(max(scores))

if __name__ == '__main__':
    main()
