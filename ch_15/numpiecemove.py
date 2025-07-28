from puzzleboard import draw_board, init_board

def find_zero(board: list[list[int]])->tuple[int,int]:
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col]==0:
                return row,col
            
def move_zero_to(board:list[list[int]],direction:str)->bool:
    row,col=find_zero(board)
    if direction =="up":
        new_row,new_col=row-1,col
    elif direction =="down":
        new_row,new_col=row+1,col
    elif direction =="left":
        new_row,new_col=row,col-1
    elif direction =="right":
        new_row,new_col=row,col+1

    if 0 <= new_row <len(board)and 0<=new_col<len(board[0]):
        zero,not_zero=board[row][col], board[new_row][new_col]
        board[row][col], board[new_row][new_col]=not_zero,zero
        return True
    return False

if __name__=="__main__":
    n_rows=n_cols=3
    board=init_board(n_rows,n_cols)
    draw_board(board)

    for direction in ["up","right","down","left"]:
        result=move_zero_to(board,direction)
        print(f"{direction=},{result=}")
        draw_board(board)