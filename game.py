class Player:
    def __init__(self, name, game_piece):
        self.name = name
        self.game_piece = game_piece


class Move:
    def __init__(self, author, position):
        self.author = author
        self.position = position


class Board:
    current_display = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

    def __init__(self, moves=[]):
        self.moves = moves

    def display(self):
        clean_display = ""

        for row in self.current_display:
            clean_display += " ".join(row) + "\n"

        print(clean_display)

    def update_display(self, move):
        row = move.position[0]
        column = move.position[1]
        self.current_display[row][column] = move.author.game_piece


    def add_move(self, move):
        self.moves.append(move)
        self.update_display(move)


class Game:
    started_at = None
    finished_at = None
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2



# Game Play
harry = Player("Harry", "X")
hermione = Player("Hermione", "O")

my_board = Board()
my_game = Game(my_board, harry, hermione)

first_move = Move(harry, [0,2])
my_board.add_move(first_move)

second_move = Move(hermione, [1,1])
my_board.add_move(second_move)

third_move = Move(harry, [2,2])
my_board.add_move(third_move)

fourth_move = Move(hermione, [0,0])
my_board.add_move(fourth_move)

fifth_move = Move(harry, [1,2])
my_board.add_move(fifth_move)

my_board.display()