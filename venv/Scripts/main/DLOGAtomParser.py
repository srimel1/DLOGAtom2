import ply.yacc as yacc
from DLOGAtomLexer import tokens

start = 'Atomstart'
def p_Atomstart(p):
    '''Atomstart : NAME LPAREN args RPAREN'''
    print("parsed:", p[1], p[2], p[3])

def p_args_1(p):
    'args : args COMMA arg'
    p[0] = [p[1]] , [p[3]]
    line = p.lineno(2)  # line number of the COMMA token
    arg = p.lexpos(2)  # Position of the ARG token


def p_args_2(p):
    'args : arg'
    p[0] = p[1]


def p_arg_3(p):
    'arg  : NUMBER'
    p[0] = ['num', p[1]]


def p_arg_4(p):
    'arg  : STRING'
    p[0] = ['str', p[1]]


def p_arg_5(p):
    'arg  : NAME'
    p[0] = ['var', p[1]]


def p_error(p):
     if p:
          print("Syntax error at token", p.type)
          # Just discard the token and tell the parser it's okay.
          parser.errok()
     else:
          print("Syntax error at EOF")


# def p_error(p):
#     if p:
#         print("Syntax error at '%s'" % p.value)
#     else:
#         print("Syntax error at EOI")


# def p_statement_print_error(p):
#     'statement : NAME LPAREN error RPAREN'
#     print("Syntax error in print statement. Bad expression")

#parser = yacc.yacc(tabmodule='fooparsetab')
parser = yacc.yacc(start = 'Atomstart')





