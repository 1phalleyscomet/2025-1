import pygame
from puzzleboard import init_board
from eventloop import init_pygame

def get_screen_size(n_rows:int,n_cols:int,box_size:int=100)->tuple[int,int]:
    return n_cols*box_size,n_rows*box_size

def draw_board_gui(board:list[list[int]],screen:pygame.surface.Surface,font:pygame.font.Font,box_size:int=100):
    for row in range(len(board)):
        for col in range(len(board[row])):
            number=board[row][col]
            if number !=0:
                bbox=pygame.Rect(col*box_size,row*box_size,box_size,box_size)
                pygame.draw.rect(screen,(255,255,255),bbox)
                pygame.draw.rect(screen,(200,200,200),bbox,1)
                text_img=font.render(f"{number}",True,(0,0,0))
                text_bbox=text_img.get_rect(center=bbox.center)
                screen.blit(text_img,text_bbox)

if __name__=="__main__":
    n_rows,n_cols=4,8
    board=init_board(n_rows,n_cols)
    scr_size=get_screen_size(n_rows,n_cols)
    screen,font,clock=init_pygame(scr_size)
    running=True
    
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        screen.fill((0,0,0))
        draw_board_gui(board,screen,font)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()