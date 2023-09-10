import copy


def initial_state():
    return ((7, 2, 4, 5, 0, 6, 8, 3, 1), 1, 1)


def is_goal(s):
    return s[0] == (1, 2, 3, 4, 5, 6, 7, 8, 0)


def successors(s):
    _, r, c = s
    new_r, new_c = r-1, c
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r+1, c
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r, c-1
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r, c+1
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1


def is_valid(r, c):
    return 0 <= r <= 2 and 0 <= c <= 2


def move_blank(s, new_r, new_c):
    board, r, c = s
    new_board = list(board)
    new_board[r*3 + c] = new_board[new_r*3 + new_c]
    new_board[new_r*3 + new_c] = 0
    return (tuple(new_board), new_r, new_c)

def h3(s):
    # Define the goal state for comparison
    goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    board, _, _ = s
    total_misplaced = 0

    # Iterate through each tile in the board
    for i in range(9):
        if board[i] != goal_state[i]:
            # Calculate the row and column for both the current state and goal state
            current_row, current_col = divmod(i, 3)
            goal_row, goal_col = divmod(goal_state.index(board[i]), 3)
            # Calculate the Manhattan distance (sum of row and column differences)
            row_diff = abs(current_row - goal_row)
            col_diff = abs(current_col - goal_col)
            total_misplaced += row_diff + col_diff

    return total_misplaced
