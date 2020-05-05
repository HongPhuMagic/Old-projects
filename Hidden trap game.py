import random
from pip._vendor.distlib.compat import raw_input


def create_board():
    board = [['-', '-', '-', '-', '-', '-', '-'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-'],
             ['B', '-', 'R', 'B', '-', '-', 'R']]
    p = random.randrange(0, 7)
    board[0][p] = 'G'
    return board


def set_traps():
    trap_map = [['-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-']]
    for i in range(2, 6):
        for n in range(0, 6):
            trap_map[i][n] = ' '.join(random.choices(['-', 'T'], [0.8, 0.2], k=1))
    count = 0
    for j in range(2, 6):
        for o in range(0, 6):
            if trap_map[j][o] == 'T':
                count = count + 1
    """print("  0123456")
    print(" +=======+")
    print("0|" + trap_map[0][0] + trap_map[0][1] + trap_map[0][2] + trap_map[0][3] + trap_map[0][4] + trap_map[0][5] +
          trap_map[0][6] + "|0")
    print("1|" + trap_map[1][0] + trap_map[1][1] + trap_map[1][2] + trap_map[1][3] + trap_map[1][4] + trap_map[1][5] +
          trap_map[1][6] + "|1")
    print("2|" + trap_map[2][0] + trap_map[2][1] + trap_map[2][2] + trap_map[2][3] + trap_map[2][4] + trap_map[2][5] +
          trap_map[2][6] + "|2")
    print("3|" + trap_map[3][0] + trap_map[3][1] + trap_map[3][2] + trap_map[3][3] + trap_map[3][4] + trap_map[3][5] +
          trap_map[3][6] + "|3")
    print("4|" + trap_map[4][0] + trap_map[4][1] + trap_map[4][2] + trap_map[4][3] + trap_map[4][4] + trap_map[4][5] +
          trap_map[4][6] + "|4")
    print("5|" + trap_map[5][0] + trap_map[5][1] + trap_map[5][2] + trap_map[5][3] + trap_map[5][4] + trap_map[5][5] +
          trap_map[5][6] + "|5")
    print("6|" + trap_map[6][0] + trap_map[6][1] + trap_map[6][2] + trap_map[6][3] + trap_map[6][4] + trap_map[6][5] +
          trap_map[6][6] + "|6")
    print(" +=======+")
    print("  0123456")"""
    return trap_map, count


def display_board(board):
    print("  0123456")
    print(" +=======+")
    print("0|" + board[0][0] + board[0][1] + board[0][2] + board[0][3] + board[0][4] + board[0][5] + board[0][6] + "|0")
    print("1|" + board[1][0] + board[1][1] + board[1][2] + board[1][3] + board[1][4] + board[1][5] + board[1][6] + "|1")
    print("2|" + board[2][0] + board[2][1] + board[2][2] + board[2][3] + board[2][4] + board[2][5] + board[2][6] + "|2")
    print("3|" + board[3][0] + board[3][1] + board[3][2] + board[3][3] + board[3][4] + board[3][5] + board[3][6] + "|3")
    print("4|" + board[4][0] + board[4][1] + board[4][2] + board[4][3] + board[4][4] + board[4][5] + board[4][6] + "|4")
    print("5|" + board[5][0] + board[5][1] + board[5][2] + board[5][3] + board[5][4] + board[5][5] + board[5][6] + "|5")
    print("6|" + board[6][0] + board[6][1] + board[6][2] + board[6][3] + board[6][4] + board[6][5] + board[6][6] + "|6")
    print(" +=======+")
    print("  0123456")


def validate_moves(cr, cc, nr, nc, c_board):
    v = False
    l = help1(cr, cc, c_board)
    if l == '-':
        v = False
    elif l == 'R':
        if cc == nc and cr != nr:
            v = True
        elif cc != nc and cr == nr:
            v = True
    elif l == 'B':
        if cc != nc and cr != nr:
            v = True
    return v


def check_traps(cr, cc, nr, nc, t_board):
    return 0


def move_general(board):
    for i in range(0, 1):
        for j in range(0, 7):
            if board[i][j] == 'G':
                board[i][j] = '-'

    p = random.randrange(0, 7)
    board[0][p] = 'G'
    return board


def move_soldier(cr, cc, nr, nc, c_board, t_board):
    soldier = help1(cr, cc, c_board)
    c_board[int(cr)][int(cc)] = '-'
    c_board[int(nr)][int(nc)] = soldier

    return c_board


def help1(cr, cc, board):
    soldier = str(board[int(cr)][int(cc)])
    return soldier


def main():
    print("Game starts now >> ")
    board = create_board()
    display_board(board)
    trap_map, count = set_traps()
    print("\nThis board has " + str(count) + " hidden traps!")
    pt = 0
    while True:
        try:
            if pt < 101:
                while True:
                    try:
                        cr, cc = raw_input("\nTo move your soldier enter it's current position <row, col>: ").split(',')
                        if (int(cr) > 6) or (int(cc) > 6):
                            print("Please input valid current position!")
                            continue
                        else:
                            break
                    except ValueError:
                        print("Oops!  That was no valid number.  Try again...")

                while True:
                    try:
                        nr, nc = raw_input("Enter the new position <row, col>: ").split(',')
                        if (int(nr) > 6) or (int(nc) > 6):
                            print("Please input valid new position!")
                            continue
                        if validate_moves(cr, cc, nr, nc, board) == False:
                            print("Invalid move")
                            continue
                        else:
                            break
                    except ValueError:
                        print("Oops!  That was no valid number.  Try again...")

                while True:
                    try:
                        if board[int(cr)][int(cc)] == '-':
                            print("\nThere is no soldier present. ")
                            break
                        else:
                            v_m = validate_moves(cr, cc, nr, nc, board)
                            if v_m:
                                move_soldier(cr, cc, nr, nc, board, trap_map)
                                display_board(board)
                                pt = pt + 2
                                print("Your score: " + str(pt))
                                break
                            elif not v_m:
                                print("The move is invalid! ")
                                break
                    except ValueError:
                        print("Oops!  That was no valid number.  Try again...")
            continue
        except ValueError:
            print("Opps. ")

main()
