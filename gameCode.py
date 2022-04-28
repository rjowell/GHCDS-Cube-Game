import pygame,random
pygame.init()

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Cuber.io Game")

cubeSize = 20

#RGB Colors
yellow = (255,255, 0)
white = (255,255,255)
myColor = (255,0,0)
randomColor = (45, 252, 222);
bgColor = (0,100,200);

food = [random.randrange(1,500),random.randrange(1,500), 10, 10]
Bfood = [random.randrange(1,500),random.randrange(1,500), 10, 10]


speed = 5

cubeX = 250
cubeY = 250
cubeSize = 20

run = True

while run:

  window.fill(bgColor)
  pygame.display.update()







'''
(100,50,200)

(10,200,70)


R ed
G reen
B lue

C yan
M agenta
Y ellow
K Black

'''