'''
Here's a short & sweet way to get the whole job done, exploiting that regexps have a natural way to say 
"find the longest sequence starting at the current position consisting of repetitions of the current digit".
The "(\d)" matches a digit as group #1, and the "\1" matches the same thing as group #1. Group #0, or m.group(0), is the entire string.
s = '1211@abc456@def'
for m in re.finditer(r"(\d)(\1*)", s):
	print m.group(0),m.group(1),m.group(2)
'''
import re
#finditer返回一个MatchObject类型的iterator,所以我们需要迭代并通过MatchObject的方法group输出
#group(0):母串中与模式pattern匹配的子串,group(1)是与patttern中第一个group匹配成功的子串，group(2)是第二个，依次类推
#匹配项不加括号包围，不计入匹配结果中
#\1的意思是匹配第1个分组的内容，比如\d匹配到的是1，那么\1就是指匹配具体的数值1，\1*就是匹配n个数值1
def describe(s):
	str2 = ""
	for m in re.finditer(r"(\d)(\1*)",s):
		str1 = str(len(m.group(0))) + m.group(1)
		str2 = str2 + "".join(str1)
	return str2
#	return "".join([str(len(m.group(0))) + m.group(1)
#									for m in re.finditer(r"(\d)\1*", s)])
s = "1"
for dummy in range(30):
	s = describe(s)
print len(s)  # prints 5808