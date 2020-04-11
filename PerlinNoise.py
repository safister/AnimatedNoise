#Run this and let it render as many frames as you want, and then run VideoCompiler.py to make an mp4
import math as m
import noise
import numpy as np
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame as p
import random as r
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (0,30)
p.init()
p.display.set_caption('Pygame')

def Clamp(min, max, number):
    while number < min or number > max:
        if number < min:
            number += 20
        else:
            number -= 20
    return number

def CreateColors():
    #Color scheme from https://flatuicolors.com/palette/us
    colors = [
    (85, 239, 196),
    (129, 236, 236),
    (116, 185, 255),
    (162, 155, 254),
    (223, 230, 233),
    
    (0, 184, 148),
    (0, 206, 201),
    (9, 132, 227),
    (108, 92, 231),
    (178, 190, 195),
    
    (255, 234, 167),
    (250, 177, 160),
    (255, 118, 117),
    (253, 121, 168),
    (99, 110, 114),
    
    (253, 203, 110),
    (225, 112, 85),
    (214, 48, 49),
    (232, 67, 147),
    (45, 52, 54)
    ]
    #For black and white
    #colors = [
    #(0,0,0),
    #(255,255,255)
    #]*10
    r.shuffle(colors)
    return colors

def CreateMap():
    #Amount of detail
    octaves = 6
    #Size
    scale = 100
    shape = (1920,1080)
    
    #Generate a 2d array with values from -1 to 1
    world = np.zeros((shape[1],shape[0]))
    for y in range(shape[1]):
        for x in range(shape[0]):
            #Perlin noise
            world[y][x] = noise.pnoise2(y/scale, x/scale, octaves=octaves, persistence=0.5, lacunarity=2, repeatx=1024, repeaty=1024, base=0)
            #Shader noise
            #world[y][x] = noise.snoise2(y/scale, x/scale, octaves=octaves, persistence=0.5, lacunarity=2, repeatx=1024, repeaty=1024, base=0)
    return world

def Draw(colors, frame, offset, world):
    #Used to normalize height values, so if its from -0.8 to 0.8, it scales it
    coeff = 1/world.max()
    
    #Color all pixels
    for y in range(len(world)):
        for x in range(len(world[0])):
            #Height of pixel from 0-20
            h = (world[y][x]*coeff + 1)*10 + offset
            
            colorIndex = Clamp(0, 19, int(h))
            w.set_at((x,y), colors[colorIndex])
        p.display.update()
    p.image.save(w, "Render/" + str(frame) + ".png")


colors = CreateColors()
clock = p.time.Clock()
frame = 0
offset = -20
w = p.display.set_mode((1920,1080))
world = CreateMap()

Draw(colors, frame, offset, world)

stop = False
while not stop:
    offset += 0.1
    frame += 1
    Draw(colors, frame, offset, world)
    
    for event in p.event.get():
        if event.type == p.QUIT:
            stop = True
        if event.type == p.KEYDOWN:
            keys = p.key.get_pressed()
            if keys[p.K_SPACE]:
                colors = CreateColors()
                world = CreateMap()
                Draw(colors, frame, offset, world)

p.quit()
quit()