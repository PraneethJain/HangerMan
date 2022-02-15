import pygame as pg
import os
import rich

pg.init()
screen=pg.display.set_mode((800,600))
clock = pg.time.Clock()

text = ''
word = ''
myfont = pg.font.Font(os.path.join("Fonts","dpcomic.ttf"),50)
largefont = pg.font.Font(os.path.join("Fonts","dpcomic.ttf"),70)
start_surf = largefont.render("Enter word and press enter",False,'Blue')
center = screen.get_width()/2,screen.get_height()/2

status=0
while True:
    
    if pg.event.get(pg.QUIT): raise SystemExit
    screen.fill((0,0,0))
    
    events = pg.event.get()
    
    if status==0:
        screen.blit(start_surf,(center[0]-start_surf.get_width()/2,center[1]-start_surf.get_height()/2-50))
        for event in events:
            if event.type==pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    word=word[:-1]
                else:
                    word+=event.unicode
                if event.key == pg.K_RETURN:
                    status=1
        word_surf = largefont.render(word,False,"Orange")
        screen.blit(word_surf,(center[0]-word_surf.get_width()/2,center[1]-word_surf.get_height()/2+40))

    
    if status==1:
        for event in events:
            if event.type==pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    text=text[:-1]
                else:
                    text += event.unicode
            
        text_surf = myfont.render(text,False,(0,128,128))
        screen.blit(text_surf,(0,0))
    
    clock.tick(60)
    pg.display.flip()
    