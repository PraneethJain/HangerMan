import pygame as pg
import os
from rich import print
from time import sleep


pg.init()
pg.display.set_caption("Hanger Man")
screen=pg.display.set_mode((800,600))
clock = pg.time.Clock()
bg=pg.image.load(os.path.join("Assets","bg.jpg")).convert_alpha()
scale=2
bg=pg.transform.scale(bg,(bg.get_width()/scale,bg.get_height()/scale))
bg_pos = screen.get_width()/2-bg.get_width()/2, screen.get_height()/2-bg.get_height()/2+150

letters = [chr(i) for i in range(65,91)]
text = ''
word = ''
myfont = pg.font.Font(os.path.join("Fonts","dpcomic.ttf"),50)
largefont = pg.font.Font(os.path.join("Fonts","dpcomic.ttf"),70)
start_surf = largefont.render("Enter word and press enter",False,'Blue')
center = screen.get_width()/2,screen.get_height()/2

attempts_left=7
status=0
while True:
    
    if pg.event.get(pg.QUIT): raise SystemExit
    screen.fill("Black")
    screen.blit(bg,bg_pos)
    
    events = pg.event.get()
    
    if status==0:
        screen.blit(start_surf,(center[0]-start_surf.get_width()/2,center[1]-start_surf.get_height()/2-200))
        for event in events:
            if event.type==pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    word=word[:-1]
                else:
                    word+=event.unicode
                if event.key == pg.K_RETURN:
                    word=word.upper().strip()
                    replaced=word
                    maintext="_ " * (len(word))
                    status=1

        word_surf = largefont.render(word.capitalize(),False,"Orange")
        screen.blit(word_surf,(center[0]-word_surf.get_width()/2,center[1]-word_surf.get_height()/2-100))

    
    if status==1:
        
        guessed = text.upper().strip()
        for i,letter in enumerate(letters):
            if letter in guessed:
                if letter in word:
                    surf=myfont.render(letter,False,"Green")
                    screen.blit(surf,(17+i*screen.get_width()/27,screen.get_height()-50))
                else:
                    surf=myfont.render(letter,False,"Red")
                    screen.blit(surf,(17+i*screen.get_width()/27,screen.get_height()-50))
            else:
                surf=myfont.render(letter,False,"White")
                screen.blit(surf,(17+i*screen.get_width()/27,screen.get_height()-50))
        
        for event in events:
            if event.type==pg.KEYDOWN and event.key != pg.K_BACKSPACE: text += event.unicode
            if event.type==pg.KEYDOWN:
                if event.unicode.upper()!='' and event.unicode.upper() in replaced:
                    j = replaced.find(event.unicode.upper())
                    while replaced.count(word[j])!=0:
                        j = replaced.find(event.unicode.upper())
                        replaced=replaced.replace(word[j],'0',1)
                        maintext=maintext[:2*j]+event.unicode.upper()+maintext[2*j+1:]
                else:
                    attempts_left -= 1

        main = largefont.render(maintext,False,"Pink")
        text_surf = myfont.render(text,False,(0,128,128))
        attempts=myfont.render(f'Attemps Left: {attempts_left}',False,"Purple")
        screen.blit(main,(center[0]-main.get_width()/2,center[1]-main.get_height()/2))
        screen.blit(text_surf,(0,0))
        screen.blit(attempts,(screen.get_width()-attempts.get_width(),attempts.get_height()/2))
        
        if attempts_left == 0:
            game_over = largefont.render("The word was: ",False,"Red")
            pg.display.flip()
            sleep(1)
            status=2
            
        if set(guessed)==set(word):
            you_win = largefont.render("You Win!",False,"White")
            pg.display.flip()
            sleep(1)
            status=3
            
    if status==2:
        screen.blit(word_surf,(center[0]-word_surf.get_width()/2,center[1]-word_surf.get_height()/2))
        screen.blit(game_over,(center[0]-game_over.get_width()/2,center[1]-game_over.get_height()/2-80))
    
    if status==3:
        screen.blit(you_win,(center[0]-you_win.get_width()/2,center[1]-you_win.get_height()/2))
    
    
    clock.tick(60)
    pg.display.flip()
    