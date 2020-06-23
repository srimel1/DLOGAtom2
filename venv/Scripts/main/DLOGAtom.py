from DLOGAtomParser import parser
from DLOGAtomLexer import lexer
from DLOGAtomLexer import num_count


def read_input():
    result = ''
    while True:
        data = input('DLOGAtom: ').strip()
        if ')' in data:
            i = data.index(')')
            result += data[0:i + 1]
            break
        else:
            result += data + ' '
    return result


def main():

    while True:
        #reads from standard input
        data = read_input()
        #prints what was entered in standard input
        print(data)
        #feeds the input to the lexer
        lexer.input(data)
        answer = parser.parse(data)
        
        print(answer)

        if answer is not None:
            print(answer)




        #prints the tokens from the lexer
        # while True:
        #     tok = lexer.token()
        #     if not tok:
        #         break  # No more input
        #     print(tok)

        #enter exit; in standard input to exit the program

        # tree = parser.parse(data)
        #
        # if data == 'exit;':
        #     break
        # try:
        #     #parse the input
        #     tree = parser.parse(data)
        # except Exception as inst:
        #     print(inst.args[0])
        #     continue
        #
        # #prints the parse tree
        # print(parser.parse(data))

        # print(num_count)


main()


