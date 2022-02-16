import pygame as pg
import os
from rich import print


pg.init()
screen=pg.display.set_mode((800,600))
clock = pg.time.Clock()

letters = [chr(i) for i in range(65,91)]
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
                    word=word.upper().strip()
                    replaced=word
                    maintext="_ " * (len(word))
                    status=1

        word_surf = largefont.render(word.capitalize(),False,"Orange")
        screen.blit(word_surf,(center[0]-word_surf.get_width()/2,center[1]-word_surf.get_height()/2+40))

    
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
                    replaced=replaced.replace(word[j],'0',1)
                    maintext=maintext[:2*j]+event.unicode.upper()+maintext[2*j+1:]

        main = largefont.render(maintext,False,"Pink")
        text_surf = myfont.render(text,False,(0,128,128))
        screen.blit(main,(center[0]-main.get_width()/2,center[1]-main.get_height()/2))
        screen.blit(text_surf,(0,0))
    
    clock.tick(60)
    pg.display.flip()
    