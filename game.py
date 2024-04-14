# Example file showing a circle moving on screen
import pygame
from Ball import Ball

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
startpos = ()
clicked = False
ticks = 0
ball = Ball(pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2), 40)

def isInside(circle_x, circle_y, rad, x, y):
     
    if ((x - circle_x) * (x - circle_x) +
        (y - circle_y) * (y - circle_y) <= rad * rad):
        return True
    else:
        return False
    
def update():
    global ball
    print(ball.velocity)
    ball.position.x += ball.velocity.x
    ball.position.y += ball.velocity.y
    if abs(ball.velocity.x) < 0.01:
        ball.velocity.x = 0
    else:
        ball.velocity.x *= 0.95
    if abs(ball.velocity.y) < 0.01:
        ball.velocity.y = 0
    else:
        ball.velocity.y *= 0.95

def strength_color():
    global ball
    color = "white"
    if abs(ball.position.x - pygame.mouse.get_pos()[0]) > 5 or abs(ball.position.y - pygame.mouse.get_pos()[1]) > 5:
        color = "green"
    if abs(ball.position.x - pygame.mouse.get_pos()[0]) > 80 or abs(ball.position.y - pygame.mouse.get_pos()[1]) > 80:
        color = "orange"
    if abs(ball.position.x - pygame.mouse.get_pos()[0]) > 150 or abs(ball.position.y - pygame.mouse.get_pos()[1]) > 200:
        color = "red"
    
    pygame.draw.line(screen, color, ball.position, pygame.mouse.get_pos())


pygame.draw.circle(screen, "red", pygame.mouse.get_pos(), 10)
while running:
    update()


    screen.fill("green")
    pygame.draw.circle(screen, "white", ball.position , 40)

    if clicked:
        strength_color()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if isInside(ball.position.x, ball.position.y, 40, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    startpos = pygame.mouse.get_pos()
                    clicked = True
                        
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                print(pygame.mouse.get_pos())
                if clicked:
                    clicked = False
                    ball.velocity.x = (ball.position.x - pygame.mouse.get_pos()[0])/25
                    ball.velocity.y = (ball.position.y - pygame.mouse.get_pos()[1])/25




    pygame.display.flip()

    dt = clock.tick(60)

pygame.quit()