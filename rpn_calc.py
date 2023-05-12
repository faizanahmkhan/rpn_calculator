# stack data structure
# evaluating the experession left to right, push each value onto the stack
# when it reaches an operator, pop the previous values, then perform the operation
# push result onto stack


import math
import operator
import sys

# Define the operators to begin with

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "avg": lambda a, b: (a + b) / 2,
    "mod": lambda a, b: a % b
}


