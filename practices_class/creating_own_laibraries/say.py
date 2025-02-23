# call the hello function
from practices_class.creating_own_laibraries.saying import hello
import sys


if len(sys.argv) == 2:
    hello(sys.argv[1])


# call the goodbye function
from practices_class.creating_own_laibraries.saying import goodbye
import sys

if len(sys.argv) == 2:
    goodbye(sys.argv[1])