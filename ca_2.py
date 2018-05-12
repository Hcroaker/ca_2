"""
Griffith Universiy Harrison Croaker 2018 (C)

"""

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x // y,
    "*": lambda x, y: x * y,
    "%": lambda x, y: int(x % y),
    "&": lambda x, y: int(x & y),
    "|": lambda x, y: int(x | y),
    "^": lambda x, y: int(x ^ y)
}

def doCalculations(expression, operator):
    found = True
    calculations = []
    while found:
        found = False
        for i in range(len(expression)):
            if expression[i]==operator:
                found = True;
                print(expression)
                answer = operations[operator](int(expression[i-1]), int(expression[i+1]))
                expression = expression[:i-1] + [str(answer)] + expression[i+2:len(expression)]
                calculations.append(expression)
                break;
    return calculations

def evaluate(expression):
    expression = expression.split(" ")
    print(expression)
    operations = ["/", "%", "*", "+", "-", "&", "^", "|"]
    for operator in operations:
        res = doCalculations(expression, operator)
        if res:
            expression = res[-1]
    return expression[0]

expression = "28 * 9 + 5"
print(eval(expression))
answer = evaluate(expression)
print(answer)
