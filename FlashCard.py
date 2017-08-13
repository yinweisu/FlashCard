# -*- coding：utf-8 -*-
import pygame
import re
from pygame.locals import *
from sys import exit

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 640
FONT_SIZE = 70
FONT = 'ZiTi.ttf'
END = '大吉大利，今晚吃鸡！'
file_name = 'words.txt'
save_file_name = 'saving.txt'
word_regex = re.compile(r'([a-zA-Z\-]+)\s*(.*)')

# init
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('背单词咯')

# reload index
try:
    f = open(save_file_name, 'r')
    line_index = int(f.readline())
except Exception as e:
    line_index = 0
# get the word
f = open(file_name, 'r')
lines = f.readlines()
f.close()
text = word_regex.match(lines[line_index]).groups()
word = text[0]
translation = text[1]
translation_flag = False



# main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            f = open(save_file_name, 'w')
            f.write(str(line_index))
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_1:
                translation_flag = not translation_flag
            elif event.key == K_RIGHT:
                line_index += 1
                if line_index < len(lines):
                    text = word_regex.match(lines[line_index]).groups()
                    word = text[0]
                    translation = text[1]
                    translation_flag = False
                else:
                    line_index = len(lines)
                    word = END
                    translation = END
            elif event.key == K_LEFT:
                line_index -= 1
                if line_index >= 0:
                    text = word_regex.match(lines[line_index]).groups()
                    word = text[0]
                    translation = text[1]
                    translation_flag = False
                else:
                    line_index = 0
                    text = word_regex.match(lines[line_index]).groups()
                    word = text[0]
                    translation = text[1]
                    translation_flag = False

    screen.fill([255, 255, 255])
    word_font = pygame.font.Font(FONT, FONT_SIZE)
    if translation_flag:
        word_text = word_font.render(translation, True, (0, 0, 0))

    else:
        word_text = word_font.render(word, True, (0, 0, 0))
    text_rect = word_text.get_rect()
    text_rect.midbottom = [(SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2)]
    screen.blit(word_text, text_rect)
    pygame.display.update()

