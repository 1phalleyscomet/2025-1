def init_board(n_rows: int=3,n_cols:int=3)->list:
    nums=list(range(1, n_rows*n_cols))+[0]
    return[nums[idx:idx+n_cols] for idx in range(0,n_rows*n_cols,n_cols)]

def draw_board(board: list):
    for row in board:
        print(" ".join(f"{num:>2}" if num !=0 else " " for num in row))
    print("-"*8)

if __name__=="__main__":
    n_rows=n_cols=3
    borad=init_board()
    draw_board(borad)