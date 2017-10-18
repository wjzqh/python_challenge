from PIL import Image
import re

im = Image.open('..\\data\\oxygen.png')
width = im.size[0]
height = im.size[1]
pixels = im.load()
bar_y = height / 2 # bar is half way down the image

# look at every 7th pixel 
answer = ''
for i in range (0, width, 7):
    p = pixels[i, bar_y] # get a pixel object[x, y] - (r, g, b, a) 
    if(p[0] == p[1] == p[2]): # only look at greyscale pixels (r = g = b)
         print p[0]
         answer = answer + chr(p[0])

print '\n', answer, '\n'

list = re.findall('(\d+)', answer) # find all numbers and put into a list
print ''.join(map(chr, map(int, list))) # int() each, then chr() each