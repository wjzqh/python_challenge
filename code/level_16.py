from PIL import Image
'''
mozart = Image.open("..\\data\\mozart.gif")
mozartpix = mozart.load()
new = Image.new("RGB", [1250, 480])
newpix = new.load()
b = 0
line = []

for y in range(0, 479):
    for x in range(0, 639):
        #the pink pixels are color #195,195 is the index of palette.
        if mozartpix[x, y] != 195:
            line.append(mozartpix[x, y])
        elif len(line) != 0:
            for a in range(0, len(line)):
                newpix[a, b] = line.pop(0)
            b += 1
new.show()
'''
def straighten(source):
    target = source.copy()
    for y in range(source.size[1]):
        line = [source.getpixel((x, y)) for x in range(source.size[0])]
        pink = line.index(195)
        line = line[pink:] + line[:pink]
        for x, pixel in enumerate(line):
            target.putpixel((x, y), pixel)
    return target
out = straighten(Image.open("..\\data\\mozart.gif"))
out.show()