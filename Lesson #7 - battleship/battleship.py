# board = []
#
# for i  in range(5):
#   board.append(['O']*5)
# # print(board)
#
# #convert each item in the list to string
#
# for item in board:
#     item = ("".join(item))
#     print (item)

##################################################
# MY SOLUTION :

# board = []
#
# for i in range(5):
#     board.append(['O'] * 5)
#
#
# # print(board)
#
#
# def print_board(board_in):
#     for item in board:
#         item = (''.join(item))
#         print(item)
#
#
# print_board(board)
#####################################################################
# CODE ACADEMY SOLUTION :
# board = []
#
# for i in range(5):
#     board.append(["O"] * 5)
#
#
# def print_board(board_in):
#     for row in board:
#         print (row)
#

#print_board(board)
##################################################
# THE NICE BATTLESHIP BOARD :
board = []

for i in range(5):
    board.append(["O"] * 5)


def print_board(board_in):
    for row in board:
        print(' '.join(row))

print_board(board)