import pygame, sys, os
from pygame.locals import *
import settings 

pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()


screen = pygame.display.set_mode(settings.SIZE)

# load samples
class noteSamples:
    def __init__(self,noteName):
        self.note = pygame.mixer.Sound(f'samples/{noteName}.wav')
        self.note.set_volume(0.2)

whiteNotes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
blackNotes = ['Db', 'Eb', 'Gb', 'Ab', 'Bb']

whiteNote_samples = []
for noteName in whiteNotes:
    whiteNote_samples.append(noteSamples(noteName))
    whiteNote_samples[0]

blackNote_samples = []
for noteName in blackNotes:
    blackNote_samples.append(noteSamples(noteName))

# draw piano
whiteKey_colors = {i: settings.colorWHITE for i in range(8)} 
blackKeys_colors = {i: settings.colorRED for i in range(6)} 
#pygame.font.init()
#my_font = pygame.font.SysFont('Arial', 30)

def draw_piano():
    for i in range(7):
        pygame.draw.rect(screen, 
            whiteKey_colors[i], 
            pygame.Rect(settings.pad*i + settings.x, settings.y, settings.keyWidth, settings.keyHeight))

        #text_surface = my_font.render(whiteNotes[i], False, (settings.colorBLACK))
        #screen.blit(text_surface, (settings.pad*i + settings.x, settings.y))

        i += 1

    k = 0
    for i in range(5):
        if i >= 2:
            i += 1
        if i >= 6:
            i += 1

        pygame.draw.rect(screen, 
            blackKeys_colors[k], 
            pygame.Rect(settings.pad*i + settings.keyWidth/2 + settings.x, settings.y, settings.keyWidth, settings.keyHeight*0.6))

        #text_surface = my_font.render(blackNotes[k], False, (settings.colorBLACK))
        #screen.blit(text_surface, (settings.pad*i + settings.keyWidth/2 + settings.x, settings.y))

        i += 1
        k += 1
        
# Check for key presses
whiteKeys_askii = {K_a: 0, K_s: 1, K_d: 2, K_f: 3, K_g: 4, K_h: 5, K_j: 6}
blackKeys_askii = {K_w: 0, K_e: 1, K_t: 2, K_y: 3, K_u: 4}

def check_for_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            for key, value in whiteKeys_askii.items():
                if event.key == key:
                    whiteKey_colors[value] = settings.colorBLUE
                    whiteNote_samples[value].note.play()

            for key, value in blackKeys_askii.items():
                if event.key == key:
                    blackKeys_colors[value] = settings.colorBLUE
                    blackNote_samples[value].note.play()

        if event.type == KEYUP:
            for key, value in whiteKeys_askii.items():
                if event.key == key:
                    whiteKey_colors[value] = settings.colorWHITE
                    whiteNote_samples[value].note.fadeout(150)

            for key, value in blackKeys_askii.items():
                if event.key == key:
                    blackKeys_colors[value] = settings.colorRED
                    blackNote_samples[value].note.fadeout(150)

clock = pygame.time.Clock()
# game loop
while True:
    clock.tick(120)
    check_for_events()
    screen.fill(settings.colorBLACK)
    draw_piano()
    pygame.display.update()



