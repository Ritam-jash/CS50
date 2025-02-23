''' import sys
try:
    print("hello, my name is",sys.argv[1])
except IndexError:
    print("Too few arguments") '''


""" import sys
# cheack for code
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")

# print name tags
else:
    print("hello, my name is", sys.argv[1]) """


""" import sys
# cheack the code
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
# print the name tag
print("hello, my name is", sys.argv[1]) """


#TAW
import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
for arg in sys.argv[1: ]:
    print("hello, my name is", arg)
