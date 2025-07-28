import pygame
from puzzleboard import init_board
from numpiecemove import move_zero_to
from gamefin import is_board_solved,shuffle_board
from boardprint import draw_board_gui,get_screen_size,init_pygame

def manage_events(board:list[list[int]])->bool:
    key_map={pygame.K_UP:"down",pygame.K_DOWN:"up",pygame.K_LEFT:"right",pygame.K_RIGHT:"left"}
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            return False
        elif event.type==pygame.KEYDOWN:
            if event.key in key_map:
                move_zero_to(board,key_map[event.key])
                if is_board_solved(board):
                    return False
                
    return True

if __name__=="__main__":
    n_rows,n_cols=4,8
    board=init_board(n_rows,n_cols)
    shuffle_board(board,seed=None)
    scr_size=get_screen_size(n_rows,n_cols)
    screen,font,clock=init_pygame(scr_size)
    running=True

    while running:
        running=manage_events(board)
        screen.fill((0,0,0))
        draw_board_gui(board,screen,font)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()