import pygame

#board dimensions
HEIGHTL,WIDTHB=850,800
HEIGHT,WIDTH=800,800
ROWS,COLS=8,8
SQ_SIZE=HEIGHT//ROWS

#colors
WHITE=(255,255,255)
WOODEN=(255, 215, 179)
MIDNIGHT=(43, 27, 23)
BLACK=(12, 4, 4) 
GREY=(128,128,128)
RED=(255,0,0) 
TIE=(111,111,111)

CROWN = pygame.transform.scale(pygame.image.load('Images/king.png'),(40, 25)) #load image of crown and resize

BLACK_CELLS = pygame.transform.scale(pygame.image.load('Images/black.png'),(HEIGHT,WIDTH))
WHITE_CELLS = pygame.transform.scale(pygame.image.load('Images/white.png'),(SQ_SIZE,SQ_SIZE))

