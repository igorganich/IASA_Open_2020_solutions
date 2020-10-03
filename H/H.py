from string import ascii_letters

OPERANDS = set(ascii_letters)
OPERATORS = set('+-*/')
OPEN_BRACKET = '('
CLOSE_BRACKET = ')'


class Expression:
    def __init__(self, op, r, l):
        self.op = op
        self.l = l
        self.r = r


def _get_op_precedence(op):
    if op in '*/':
        return 2
    elif op in '+-':
        return 1
    else:
        return 0


def _get_right_op_precedence(op):
    if op == '/':
        return 4
    elif op == '*':
        return 3
    elif op == '-':
        return 2
    elif op == '+':
        return 1
    else:
        return 0


def infix_to_postfix(expression):
    stack = []
    postfix = []
    for token in expression:
        if token in OPERANDS:
            postfix.append(token)
        elif token == OPEN_BRACKET:
            stack.append(token)
        elif token == CLOSE_BRACKET:
            while len(stack) > 0 and stack[-1] != OPEN_BRACKET:
                postfix.append(stack.pop())
            stack.pop()
        elif token in OPERATORS:
            while len(stack) > 0 and stack[-1] != OPEN_BRACKET and _get_op_precedence(token) <= _get_op_precedence(stack[-1]):
                postfix.append(stack.pop())
            stack.append(token)

    while stack:
        postfix.append(stack.pop())
    return ''.join(postfix)


def display(ast):
    infix = []

    def _display(expr):
        if isinstance(expr, str):
            infix.append(expr)
            return expr
        else:
            l = display(expr.l)
            r = display(expr.r)
            if isinstance(expr.l, Expression) and _get_op_precedence(expr.l.op) < _get_op_precedence(expr.op):
                l = '(%s)' % l

            if isinstance(expr.r, Expression) and (_get_right_op_precedence(expr.r.op) < _get_right_op_precedence(expr.op) or (_get_right_op_precedence(expr.r.op) == _get_right_op_precedence(expr.op) and expr.op in '/-') or (isinstance(expr.l, Expression) and expr.l.op == expr.op and (expr.op == '-' or expr.op == '/'))):
                r = '(%s)' % r
            infix.append('%s%s%s' % (l, expr.op, r))
            return '%s%s%s' % (l, expr.op, r)

    return ''.join(_display(ast))


def postfix_to_infix(expression):
    ast = []
    for token in expression:
        if token in OPERANDS:
            ast.append(token)
        elif token in OPERATORS:
            operand_a = ast.pop()
            operand_b = ast.pop()
            ast.append(Expression(token, operand_a, operand_b))

    return display(ast[0])


expression_type = int(raw_input(''))
expression = raw_input('')

print postfix_to_infix(expression) if expression_type == 2 else infix_to_postfix(expression)
