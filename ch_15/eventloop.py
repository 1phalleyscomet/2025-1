import pygame
from folder import in_dir

def init_pygame(scr_size: tuple[int,int],font_size:int=30):
    pygame.init()
    pygame.display.set_caption("puzzle")
    screen=pygame.display.set_mode(scr_size)
    font=pygame.font.Font(in_dir/"ariblk.ttf",size=font_size)
    clock=pygame.time.Clock()
    return screen,font,clock

if __name__=="__main__":
    width,height=800,100
    screen,font,clock=init_pygame((width,height),15)
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            screen.fill((255,255,255))
            center=width/2,height/2
            text_img=font.render(f"{event=}",True,(0,0,0))
            text_bbox=text_img.get_rect(center=center)
            screen.blit(text_img,text_bbox)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()