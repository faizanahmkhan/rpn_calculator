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


def evaluate_expression(expression):
    stack = []
    for token in expression.split():
        if token in OPERATORS:
            if len(stack) < 2:
                return "Error: Not enough operands for operator {}".format(token)
            else:
                b, a = stack.pop(), stack.pop()
                try:
                    result = OPERATORS[token](a, b)
                except ZeroDivisionError:
                    return "Error: Division by zero"
                stack.append(result)
        else:
            try:
                stack.append(float(token))
            except ValueError:
                return "Error: Invalid token {}".format(token)
    if len(stack) == 1:
        return stack[0]
    else:
        return "Error: Too many operands"


def main(input_file):
    with open(input_file) as f:
        for line in f:
            expression = line.strip()
            result = evaluate_expression(expression)
            if isinstance(result, str):
                print("{} - {}".format(expression, result))
            else:
                print("{} = {}".format(expression, result))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} input_file".format(sys.argv[0]))
    else:
        main(sys.argv[1])