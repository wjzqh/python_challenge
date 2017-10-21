import urllib
from PIL import Image
from cStringIO import StringIO
def splitOE(source):
    results = []
    width, height = source.size
    results = [Image.new(source.mode, (width//2, height//2))
               for dummy in range(4)]
    for x in range(width):
        for y in range(height):
            target = results[x%2 + (y%2<<1)]
            target.putpixel((x//2, y//2), source.getpixel((x, y)))
    return results
url = 'http://huge:file@www.pythonchallenge.com/pc/return/cave.jpg'
odd_even = splitOE(Image.open(StringIO(urllib.urlopen(url).read())))
for result in odd_even:
    result.show()