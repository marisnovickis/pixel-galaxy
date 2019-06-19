# Container to hold matrix
class Panel:
    def __init__(self, columns, rows):
        self.rows = rows
        self.columns = columns
        self.matrix = [([0] * rows) for j in range(columns)]

    def printPanel(self) :
        for rows in self.matrix:
            panel_row = ' '.join(str(column_val) for column_val in rows)
            print('   ' + panel_row)

    # set matrix horisontaly
    def set_h(self, row, args):
       for column, arg in enumerate(args):
            self.matrix[column][row] = arg

    # set matrix verticaly
    def set_v(self, column, args):
       for row, arg in enumerate(args):
            self.matrix[column][row] = arg


# Representation of whole puzzle layout. Consist of: top panel, left panel and middle board
class Layout:

    def __init__(self, board_size, left_panel_columns, top_panel_rows):
        self.board = Panel(board_size, board_size)
        self.left_panel = Panel(left_panel_columns,board_size)
        self.top_panel = Panel(board_size, top_panel_rows)

    def printLayout(self) :

        SPACER = '       '
        for row_index in range(0, self.top_panel.rows):
            top_panel_row_to_print = ' '.join(str(self.top_panel.matrix[column][row_index]) for column in range(0, self.top_panel.columns))
            top_panel_row_to_print = ' ' + top_panel_row_to_print
            top_panel_row_to_print = top_panel_row_to_print.replace(' 0', '  ', self.top_panel.columns)
            print(' '*(self.left_panel.columns*2-2) + SPACER + top_panel_row_to_print)

        print('')

        for row_index, rows in enumerate(self.board.matrix):
            left_panel_to_print = ' '.join(str(self.left_panel.matrix[column][row_index]) for column in range(0,self.left_panel.columns))
            left_panel_to_print = left_panel_to_print.replace(' 0', '  ', self.left_panel.columns)

            board_row_to_print = ' '.join(str(column_val) for column_val in rows)
            board_row_to_print = board_row_to_print.replace('0', unichr(0x2584))
            print(left_panel_to_print + SPACER + board_row_to_print)
