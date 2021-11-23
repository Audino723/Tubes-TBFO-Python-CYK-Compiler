from cyk import cyk_algorithm
from CFG2CNF import read_grammar
from tokenizer import tokenize_file
from CFG2CNF import convert_grammar

terminal = ['import', 'from', 'as', 'True', 'False', 'def', 'None', 'with', 'case', 'return', 'continue', 'break', 'pass', 'raise', 'in', 'class', '+', '-', '+', '*', '/', '%', 'and', 'or', 'not', '=', '>', '<', 'if', 'else', 'elif','while', 'for', 'word', 'const', 'input', ':', ',', '.', '[', ']', '(', ')', "'", '"', "'''", '#', 'range', 'print', '!', 'open', 'write', 'num', 'self', 'len', 'IOERROR', 'ValueError', 'ZeroDivisionError', 'ImportError', 'NameError', 'TypeError']
terminal_rule = ['NUM', 'BOOL', 'ALPHABET', 'QUOTE_MARK', 'POINT', 'IF', 'ELIF', 'ELSE', 'IMPORT', 'FROM', 'AS', 'DEF', 'NONE', 'WITH', 'RETURN', 'CONTINUE', 'BREAK', 'PASS', 'RAISE', 'IN', 'CLASS', 'MINUS', 'PLUS', 'MUL', 'DIV', 'MOD', 'AND', 'OR', 'NOT', 'EQUAL', 'WHILE', 'FOR', 'INPUT', 'COLON', 'COMMA', 'OP_SQ_BRACK', 'CS_SQ_BRACK', 'OP_BRACK', 'CS_BRACK', 'GREATER', 'LESS', 'DQUOTE_MARK', 'HASHTAG', 'RANGE', 'PRINT', 'EXC_MARK', 'OPEN', 'SELF', 'RELATION_OPERATOR']

if __name__ == '__main__':
    # grammar = read_grammar('cfg_revise.txt')
    # print("======CFG Grammar=========")
    # for gra in grammar:
    #     print(gra)

    convert_grammar('cfg_revise.txt', terminal, terminal_rule)
    grammar = read_grammar('cnf.txt')
    # print("======CNF Grammar=========")
    # for gra in grammar:
    #     print(gra)
    #input_file = input('Enter the input file to validate: ')

    input_file = "test.py"
    tokenized_input = tokenize_file(input_file, terminal)

    print("=============Tokenized Input==========")
    print(tokenized_input)

    cyk_algorithm(grammar, tokenized_input)
    #python_cyk_algorithm(grammar, 'terminal.txt', input_file)