def check_winner(board, mark):
    return((board.cell_00==mark and board.cell_01== mark and board.cell_02==mark )or #for row1 

            (board.cell_10==mark and board.cell_11==mark and board.cell_12==mark )or #for row2

            (board.cell_20==mark and board.cell_21==mark and board.cell_22==mark )or #for row3

            (board.cell_00==mark and board.cell_10==mark and board.cell_20== mark )or#for Colm1 

            (board.cell_01==mark and board.cell_11==mark and board.cell_21==mark )or #for Colm 2

            (board.cell_02==mark and board.cell_12==mark and board.cell_22==mark )or #for colm 3

            (board.cell_00==mark and board.cell_11==mark and board.cell_22==mark )or #daignole 1

            (board.cell_02==mark and board.cell_11==mark and board.cell_20==mark )) #daignole 2


def is_draw_move(board):
    return (
        board.cell_00 and board.cell_01  and board.cell_02 and 
        board.cell_10 and board.cell_11  and board.cell_12 and 
        board.cell_20 and board.cell_21 and board.cell_22
    ) # checking all the cells, returns True if all cells filled 