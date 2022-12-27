from typing import List


def load_input() -> List:
    with open('inputs.txt', 'r') as file:
        return file.readlines()


def search_in_line(tree_line: List, coordinates: set, y_coordinate: int, mode: str) -> None:
    left_visible_tree = int(tree_line[0])
    right_visible_tree = int(tree_line[-1])
    tree_line = tree_line[1:-1]
    line_len = len(tree_line)

    for index, tree_height in enumerate(tree_line):
        backward_idx = line_len - index - 1
        l_inner_tree = int(tree_height)
        r_inner_tree = int(tree_line[backward_idx])
        if left_visible_tree < l_inner_tree:
            coordinate = (index, y_coordinate) if mode == 'row' else (
                y_coordinate, index)
            coordinates.add((coordinate))
            left_visible_tree = l_inner_tree
        if right_visible_tree < r_inner_tree:
            coordinate = (backward_idx, y_coordinate) if mode == 'row' else (
                y_coordinate, backward_idx)
            coordinates.add((coordinate))
            right_visible_tree = r_inner_tree


def transform_matrix(forest: List) -> List:
    matrix: List[List] = [[] for i in range(len(forest))]
    for line in forest:
        for index, tree in enumerate(line.rstrip()):
            matrix[index].append(tree)

    return matrix


def walkthrough_forest(forest: List, mode: str, coordinates: set) -> None:
    y_coordinate: int = 0

    for tree_line in forest[1:-1]:
        if mode == 'row':
            tree_line = tree_line.rstrip()
        search_in_line(tree_line, coordinates, y_coordinate, mode)
        y_coordinate += 1


def main():
    coordinates: set = set()
    forest: List[str] = load_input()
    matrix: List[List] = transform_matrix(forest)
    width: int = len(forest[0].rstrip())
    height: int = len(forest)
    # corner trees have to be subtracted
    outer_tree_number: int = 2 * (width + height) - 4

    walkthrough_forest(forest, 'row', coordinates)
    walkthrough_forest(matrix, 'column', coordinates)

    print(f'{outer_tree_number} : {len(coordinates)} : {outer_tree_number + len(coordinates)}')


if __name__ == '__main__':
    main()
