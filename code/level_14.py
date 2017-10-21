from PIL import Image
src = Image.open('..\\data\\wire.png')
dst = Image.new(src.mode, (100, 100))
x, y, idx = -1, 0, 0            # back a step
steps = [1,0, 0,1, -1,0, 0,-1]
while idx < 10000:
    nx, ny = x + steps[0], y + steps[1]
    if 0 <= nx < 100 and 0 <= ny < 100 \
            and dst.getpixel((nx, ny)) == (0, 0, 0):
        x, y = nx, ny
        dst.putpixel((x, y), src.getpixel((idx, 0)))
        print x,y
        idx += 1
    else:
        steps = steps[2:] + steps[:2] # turn
dst.show()