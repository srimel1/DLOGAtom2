import ply.lex as lex

reserved = {'select': 'SELECT', 'project': 'PROJECT', 'rename': 'RENAME'}

tokens = ['LPAREN', 'NAME', 'RPAREN', 'COMMA', 'NUMBER', 'STRING'] + list(reserved.values())

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_RENAME = r'[rR][eE][nN][aA][mM][eE]'
t_SELECT = r'[sS][eE][lL][eE][cC][tT]'
t_PROJECT = r'[pP][rR][oO][jJ][eE][cC][tT]'

num_count = 0
def t_NUMBER(t):
    r'\d+'
    global num_count
    num_count += 1
    t.value = int(t.value)
    t.type = 'NUMBER'
    return t


def t_NAME(t):
    r'[a-zA-Z][_a-zA-Z0-9]*'
    t.type = reserved.get(t.value.lower(), 'NAME')
    return t


def t_STRING(t):
    r'"[a-zA-Z]+"'
    t.type = reserved.get(t.value.lower(), 'STRING')
    return t

# Ignored characters
t_ignore = " \r\n\t"
t_ignore_COMMENT = r'\#.*'



def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    #     raise Exception('LEXER ERROR')


# lexer = lex.lex(debug = 1)
lexer = lex.lex()
#
# ## Test it out
# data = '''employee(1, 2, "string")'''
#
# # Give the lexer some input
# print("rename[" + data + "]")
# lexer.input(data)
#
# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok:
#         break  # No more input
#     print(tok)
#
#
