# use command line argument
import sys
print("Hello, my name is", sys.argv[1])
# if we don't put the value then click on enter then so me this error
""" Traceback (most recent call last):
  File "C:\Users\RITAM JASH\HarvardX CS50P PYTHON\sys_8.py", line 2, in <module>
    print("Hello, my name is", sys.argv[1])
                               ~~~~~~~~^^^
IndexError: list index out of range """


# solve this error useing try & except
import sys
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")


# if we put too much value so then how we can handel the error
import sys
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello, my name is", sys.argv[1])


# TAW using the shortest way to solve the problem
# cheack for the error
import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
# print name tag
print("Hello, my name is", sys.argv[1])


# # TAW we can put infintite value exception file name [1: ]
import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
for sys in sys.argv[1: ]:
    print("Hello, my name is", sys)


# packegs cowsay
import cowsay
import sys
if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])


# using cowsay packege using trex
import cowsay
import sys
if len(sys.argv) == 2:
    cowsay.trex("Hello, " + sys.argv[1])


# TAW
import cowsay
import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
if len(sys.argv) == 3:
    sys = sys.argv[1: ]
    cowsay.cow(f"Hello, {sys}")

# TAW
import cowsay
import sys
if len(sys.argv) == 3:
    sys = sys.argv[1: ]
    cowsay.trex(f"Hello, {sys}")