import pygame
import subprocess as sb


pygame.init()

work_desk = pygame.display.set_mode((1800, 800))
my_pc = pygame.image.load('work_desk/my_pc.png')
window = pygame.image.load('work_desk/windows.png').convert()
pygame.display.set_caption("Windows Python")     #name progect
icon = pygame.image.load('work_desk/logo.png').convert_alpha()  #icon
pygame.display.set_icon(icon)
 


running = True

while running:

    work_desk.blit(window, (0,0))
    work_desk.blit(my_pc, (10,10))
    pygame.draw.rect(work_desk, (58, 53, 53),(0, 870, 1800, 400))

    keys = pygame.key.get_pressed()

    for ev in pygame.event.get():
        if ev == pygame.MOUSEBUTTONDOWN:
            sb.call('explorer')

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()