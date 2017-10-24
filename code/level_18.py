import urllib, gzip, difflib, time
from PIL import Image
from cStringIO import StringIO
url = 'http://huge:file@www.pythonchallenge.com/pc/return/deltas.gz'
data = urllib.urlopen(url).read()
l1 = []
l2 = []
for line in gzip.GzipFile(fileobj=StringIO(data)):
    l1.append(line[:53])
    l2.append(line[56:-1])

#ndiff的结果中,-表示l1中存在但是l2中不存在的数据，+则刚好相反,如果是空格开头的，则表示l1与l2中都存在，但是在不同的位置(行)
result = list(difflib.ndiff(l1, l2))

def solve(condition):
    s = [chr(int(group, 16))
         for line in result if line.startswith(condition)
         for group in line[len(condition):].split()]
    Image.open(StringIO("".join(s))).show()

for condition in " +-":
    solve(condition)
    time.sleep(1)  # give time to view
#差分的结果表示成三幅图，分别为hex/bin.html,buffer,fly