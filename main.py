class Board(object):

    def __init__(self, size=3):
        self.size = size
        self.board = []
        for i in range(self.size):
            self.board.append([' '] * size)

    def get_value(self, row, col):
        return self.board[row][col]

    def set_value(self, row, col, value):
        if self.board[row][col] == ' ':
            self.board[row][col] = value
        else:
            raise ValueError

    def display(self):
        print ' ',
        for col in range(self.size):
            print '  %s' % col,
        print
        print '  -' + '----' * (self.size)
        for row in range(self.size):
            print '%s |' % row,
            for col in range(self.size):
                print self.get_value(row, col),
                print '|',
            print
            print '  -' + '----' * (self.size)

    @staticmethod
    def get_winners(input_list):
        input_set = set(input_list)
        winners = set()
        if len(input_set) != 1:
            if ' ' in input_set:
               winners.add(' ')
        else:
            if ' ' not in input_set:
               winners = winners.union(input_set)
        return winners

    def winner(self):
        winners = set()
        for i in range(self.size):
            current_row = [None] * self.size
            current_col = [None] * self.size
            for j in range(self.size):
                current_row[j] = self.get_value(i, j)
                current_col[j] = self.get_value(j, i)
            row_winners = self.get_winners(current_row)
            col_winners = self.get_winners(current_col)
            winners = winners.union(row_winners, col_winners)

        left_diagonal = [None] * self.size
        right_diagonal = [None] * self.size

        max_pos = self.size - 1

        for i in range(self.size):
            left_diagonal[i] = self.get_value(i, i)
            right_diagonal[i] = self.get_value(max_pos-i, i)

        left_winners = self.get_winners(left_diagonal)
        right_winners = self.get_winners(right_diagonal)
        winners = winners.union(row_winners, col_winners, left_winners,
                right_winners)

        left_diagonal = set(left_diagonal)
        right_diagonal = set(right_diagonal)
        
        if 'X' in winners:
            return 'X'
        if 'O' in winners:
            return 'O'
        if ' ' in winners:
            return None
        return 'C'

def main_loop():
    letters = {1: 'X', 2: 'O'}
    while True:
        player_number = 1
        board = Board()

        while True:
            board.display()
            print 'Player %s, select next move' % letters[player_number]
            row = raw_input("Row: ")
            col = raw_input("Column: ")

            row = int(row)
            col = int(col)

            # Set value, check winner and switch player, if valid move
            try:
                board.set_value(row, col, letters[player_number])
                winner = board.winner()
                if winner is not None:
                    if winner is 'C':
                        print 'There was a tie!'
                    else:
                        print 'Player %s has won!' % player_number
                    break
                player_number ^= 3
            except ValueError:
                print
                print "You can't pick this square!"
                print

if __name__ == '__main__':
    main_loop()
