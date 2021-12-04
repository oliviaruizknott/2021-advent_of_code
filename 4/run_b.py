# CLASSES
##########
class Board(object):
    """docstring for Board."""

    def __init__(self, id, data):
        super(Board, self).__init__()
        self.id = id
        self.data = data
        self.rows = []
        self.columns = []
        self.all_values = []
        self.all_cells = self.generate_cells(data)

    def __str__(self):
        return f"""
            Board ({self.id}):

            {self.rows[0].cells}
            {self.rows[1].cells}
            {self.rows[2].cells}
            {self.rows[3].cells}
            {self.rows[4].cells}
        """

    def __repr__(self):
        return f"Board ({self.id}): {self.all_values}"

    def generate_cells(self, data):
        all_cells = []
        all_values = []
        rows = []
        columns = []

        for row in data:
            new_row_data = []
            for cell in row:
                all_values.append(cell)
                new_cell = Cell(cell)
                all_cells.append(new_cell)
                new_row_data.append(new_cell)

            rows.append(Line(new_row_data))

        for idx in range(len(rows[0].cells)):
            new_column_data = [row.cells[idx] for row in rows]
            columns.append(Line(new_column_data))

        self.all_values = all_values
        self.rows = rows
        self.columns = columns
        return all_cells

    def mark_number(self, num):
        if num in self.all_values:
            [cell for cell in self.all_cells if cell.num == num][0].marked = True
            print(f"{num} has been marked on board {self.id}")

    def check_for_win(self):
        row_wins = any([row.check_for_win() for row in self.rows])
        column_wins = any([column.check_for_win() for column in self.columns])

        return row_wins or column_wins

    def score(self):
        score = sum([cell.num for cell in self.all_cells if not cell.marked])
        print(f"The sum of the unmarked cells is {score}.")
        return score


class Line(object):
    """docstring for Line."""

    def __init__(self, cells):
        self.cells = cells

    def __str__(self):
        return f"Line: {self.cells}"

    def __repr__(self):
        return f"Line: {self.cells}"

    def check_for_win(self):
        return all([cell.marked for cell in self.cells])


class Cell(object):
    """docstring for Cell."""

    def __init__(self, num):
        self.num = num
        self.marked = False

    def __str__(self):
        return f"Cell: {self.num}, {self.marked}"

    def __repr__(self):
        return f"Cell: {self.num}, {self.marked}"

# FUNCTIONS
###########
def strip(string):
    return int(string.strip())

def process_inputs(inputs):
    drawn_numbers = list(map(strip, inputs.pop(0).split(',')))

    board_data = format_data_for_boards(inputs)
    boards = make_boards(board_data)

    return drawn_numbers, boards

# I want the data structured like:
# [
#   [
#       (22, 13, 17, 11, 0),
#       (8, 2, 23, 4, 24),
#       (21, 9, 14, 16, 7),
#       (6, 10, 3, 18, 5),
#       (1, 12, 20, 15, 19),
#   ],
#   [
#       ...
#   ]
# ]
def format_data_for_boards(data):
    boards = []
    board = []

    for row in data:
        if row == '\n':
            boards.append(board)
            board = []
            continue
        else:
            stripped_row = row.strip().replace('  ', ' ')
            formatted_row = tuple(map(strip, stripped_row.split(' ')))
            board.append(formatted_row)

    # put the last board in the boards list
    boards.append(board)
    # filter out any "empty" boards
    boards = list(filter(None, boards))
    return boards

def make_boards(data):
    boards = [Board(idx, board) for idx, board in enumerate(data)]
    return boards

def mark_and_check_winner(num, boards):
    boards_that_won = []
    for board in boards:
        board.mark_number(num)
        if board.check_for_win():
            print(f"Board {board.id} has won!")

            board_score = board.score()
            final_score = num * board_score

            print(f"The final score is: {final_score}")
            boards_that_won.append(board)

    for board in boards:
        if board in boards_that_won:
            boards.remove(board)

# PROCESS DATA
##############
file = open('input.txt', 'r')
inputs = file.readlines()

drawn_numbers, boards = process_inputs(inputs)

# LOGIC
#######
for num in drawn_numbers:
    mark_and_check_winner(num, boards)

# 8 has been marked on board 78
# Board 78 has won!
# The sum of the unmarked cells is 321.
# The final score is: 2568
