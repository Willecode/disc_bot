# Tictactoe game class. Works but isn't polished.
class tictactoe:

    def __init__(self):
        # Initialize an empty board
        self.gameboard = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.turn = 'x'
        self.infotext = self.turn + " vuoro"


    def make_move(self, tag, x_coord, y_coord):

        if self.turn != tag:
            self.infotext = self.turn + " needs to play their turn"
        elif self.gameboard[int(x_coord)][int(y_coord)] != '-' \
            or (int(x_coord) > 2 and int(x_coord) < 0) \
            or (int(y_coord) > 2 and int(y_coord) < 0):
            self.infotext = "Illegal move"
        else:
            self.gameboard[int(x_coord)][int(y_coord)] = tag
            if self.turn == 'x':
                self.turn = 'o'
            else:
                self.turn = 'x'

        board_str = ""
        for i in range(3):
            for j in range(3):
                board_str += self.gameboard[i][j]
            board_str += "\n"

        winner = self.check_if_win()
        if winner != "none":
            self.infotext = winner + " won!"
            self.win()

        return [board_str, self.infotext]

    def check_if_win(self):
    # Return: "none" if nobody won
    #          name of winning tag if someone won
        # Check columns
        for column in self.gameboard:
            if column[0] == column[1] and column[0] == column[2]\
                    and column[0] != "-":
                return column[0]

        # Check rows
        for i in range(2):
            if self.gameboard[0][i] == self.gameboard[1][i] and \
                self.gameboard[0][i] == self.gameboard[2][i] and \
                    self.gameboard[0][i] != "-":
                        return self.gameboard[0][i]

        # Check diagonals
        if self.gameboard[0][0] != "-" \
            and self.gameboard[0][0] == self.gameboard[1][1] \
            and self.gameboard[0][0] == self.gameboard[2][2]:
                return self.gameboard[0][0]

        if self.gameboard[0][2] != "-" \
            and self.gameboard[0][2] == self.gameboard[1][1] \
            and self.gameboard[0][2] == self.gameboard[2][0]:
                return self.gameboard[0][2]
        return 'none'

    def win(self):
        self.gameboard = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        return


ttt = tictactoe()
ttt.make_move('x', 2, 0)
ttt.make_move('x', 1, 1)
ttt.make_move('x', 0, 2)