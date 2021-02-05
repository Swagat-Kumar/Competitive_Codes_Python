def precedence(op):
    if op == '-' or op == '+':
        return 1
    elif op == '*':
        return 2
    elif op == '/':
        return 3
    else:
        return 0


def applyOperation(a, b, op):
    return {
        '+': lambda a, b: a+b,
        '-': lambda a, b: a-b,
        '*': lambda a, b: a*b,
        '/': lambda a, b: a/b,
    }.get(op)(a, b)


def evaluate(expression):
    i = 0
    values = []
    operations = []
    try:
        while i < len(expression):
            if expression[i] == ' ':
                i += 1
            elif expression[i] == '(':
                operations.append('(')
                i += 1
            elif expression[i].isdigit():
                val = 0
                while i < len(expression) and expression[i].isdigit():
                    val = val*10+int(expression[i])
                    i += 1
                values.append(val)
            elif expression[i] == ')':
                while len(operations) != 0 and operations[-1] != '(':
                    a = values.pop()
                    if len(values) == 0:
                        if operations[-1] == '-':
                            values.append(-a)
                        else:
                            values.append(a)
                        break
                    b = values.pop()
                    op = operations.pop()
                    values.append(applyOperation(b, a, op))
                operations.pop()
                i += 1
            else:
                while len(operations) != 0 and precedence(operations[-1]) > precedence(expression[i]):
                    a = values.pop()
                    if len(values) == 0:
                        if operations[-1] == '-':
                            values.append(-a)
                        else:
                            values.append(a)
                        break
                    b = values.pop()
                    op = operations.pop()
                    values.append(applyOperation(b, a, op))
                operations.append(expression[i])
                i += 1
        while len(operations) != 0:
            a = values.pop()
            if len(values) == 0:
                if operations[-1] == '-':
                    values.append(-a)
                else:
                    values.append(a)
                break
            b = values.pop()
            op = operations.pop()
            values.append(applyOperation(b, a, op))
        if values[-1] % 1 == 0:
            return int(values[-1])
        else:
            return values[-1]
    except:
        return 'ERROR'


expression = input()
print(evaluate(expression))
