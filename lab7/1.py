import pygame 
import os
import datetime

_image_library = {}
def get_image(path):
    global _image_library 
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace("/",os.sep).replace("\\",os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[canonicalized_path] = image
    return image

def blitRotate(screen , img , pos , angle):
    rotated_img = pygame.transform.rotate(img , angle)
    new_rect = rotated_img.get_rect(center = img.get_rect(center = pos).center)

    screen.blit(rotated_img , new_rect.topleft)

pygame.init()
done = False

screen = pygame.display.set_mode((1200,800))
w , h = screen.get_size()
bg = pygame.transform.scale(get_image(r"C:\Users\zhuma\OneDrive\Рабочий стол\PP2 labs\lab7\images\mickeyclock.jpeg"), (w,h))
pygame.display.set_caption("Mickey's Clock")


angle_min = 0
angle_sec = 0
global topleft
topleft = (w//2 , h//2 )

while not done :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            done = True

    today = datetime.datetime.now()
    minutes = int(datetime.datetime.strftime(today,'%M'))
    seconds = int(datetime.datetime.strftime(today,'%S')) 
    pos = (screen.get_width()/2 , screen.get_height()/2 )
    screen.blit( bg , (0,0) )

    blitRotate(screen , get_image(r"C:\Users\zhuma\OneDrive\Рабочий стол\PP2 labs\lab7\images\leftarm.png") , pos ,angle_sec )
    blitRotate(screen , get_image(r"C:\Users\zhuma\OneDrive\Рабочий стол\PP2 labs\lab7\images\rightarm.png"), pos , angle_min)
    angle_min = -6*minutes-53
    angle_sec = -6*seconds
    pygame.display.flip()