import os
import random
from readchar import key,readkey
from puzzleboard import draw_board,init_board
from numpiecemove import move_zero_to

def is_board_solved(board:list[list[int]])->bool:
    n_rows=len(board)
    n_cols=len(board[0])
    return board==init_board(n_rows,n_cols)

def clear_terminal(board:list[list[int]]):
    os.system("cls"if os.name=="nt"else"clear")
    draw_board(board)

def shuffle_board(board: list[list[int]],seed:int=None):
    random.seed(seed)
    for _ in range(10_000):
        direction=random.choice(["up","down","right","left"])
        move_zero_to(board,direction)

if __name__=="__main__":
    n_rows=n_cols=3
    board=init_board(n_rows,n_cols)
    shuffle_board(board,seed=None)
    clear_terminal(board)
    key_map={key.UP:"down",key.DOWN:"up",key.LEFT:"right",key.RIGHT:"left"}
    while True:
        key_in = readkey()
        if key_in in key_map:
            move_zero_to(board,key_map[key_in])
        clear_terminal(board)

        if is_board_solved(board):
            print(f"clear")
            break