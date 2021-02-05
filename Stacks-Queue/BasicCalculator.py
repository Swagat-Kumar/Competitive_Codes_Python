class Solution:
    def calculate(self, s: str) -> int:
        def precedence(op):
            if op == '-' or op == '+':
                return 1
            return 0

        def applyOperation(a, b, op):
            return {
                '+': lambda x, y: x+y,
                '-': lambda x, y: y-x
            }.get(op)(a, b)

        def evaluate(expression):
            i = 0
            values = []
            operations = []
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
                                operations.pop()
                            else:
                                values.append(a)
                            break
                        b = values.pop()
                        op = operations.pop()
                        values.append(applyOperation(a, b, op))
                    operations.pop()
                    i += 1
                else:
                    while len(operations) != 0 and precedence(operations[-1]) >= precedence(expression[i]):
                        a = values.pop()
                        if len(values) == 0:
                            if operations[-1] == '-':
                                values.append(-a)
                                operations.pop()
                            else:
                                values.append(a)
                            break
                        b = values.pop()
                        op = operations.pop()
                        values.append(applyOperation(a, b, op))
                    operations.append(expression[i])
                    i += 1
            while len(operations) != 0:
                a = values.pop()
                if len(values) == 0:
                    if operations[-1] == '-':
                        values.append(-a)
                        operations.pop()
                    else:
                        values.append(a)
                    break
                b = values.pop()
                op = operations.pop()
                values.append(applyOperation(a, b, op))
            return values[-1]
        return evaluate(s)
