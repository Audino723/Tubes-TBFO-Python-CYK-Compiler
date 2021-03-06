from cyk import cyk_algorithm, line_error_checker
from CFG2CNF import read_grammar
from tokenizer import tokenize_file
from CFG2CNF import convert_grammar

terminal = ['import', 'from', 'as', 'True', 'False', 'def', 'None', 'with', 'case', 'return', 'continue', 'break', 'pass', 'raise', 'in', 'class', 'append', '+', '-', '+', '*', '/', '%', 'and', 'or', 'not', '=', '>', '<', 'if', 'else', 'elif','while', 'for', 'word', 'const', 'input', 'is',':', ',', '.', '[', ']', '(', ')', '}', '{',  "'", '"', "'''", '#', 'range', 'print', '!', 'open', 'write', 'num', 'self', 'len', 'IOERROR', 'ValueError', 'ZeroDivisionError', 'ImportError', 'NameError', 'TypeError']

terminal_rule = ['NUM', 'BOOL', 'ALPHABET', 'QUOTE_MARK', 'POINT', 'IF', 'ELIF', 'ELSE', 'IMPORT', 'FROM', 'AS', 'DEF', 'NONE', 'WITH', 'RETURN', 'CONTINUE', 'BREAK', 'PASS', 'RAISE', 'IN', 'CLASS', 'APPEND', 'LEN','MINUS', 'PLUS', 'MUL', 'DIV', 'MOD', 'AND', 'OR', 'NOT', 'EQUAL', 'WHILE', 'FOR', 'INPUT', 'IS','COLON', 'COMMA', 'OP_SQ_BRACK', 'CS_SQ_BRACK', 'OP_BRACK', 'CS_BRACK', 'GREATER', 'LESS', 'DQUOTE_MARK', 'HASHTAG', 'RANGE', 'PRINT', 'EXC_MARK', 'OPEN', 'SELF', 'RELATION_OPERATOR',  'OP_CURLY_BRACK', 'CS_CURLY_BRACK']

import os

def Tes_Case():
    convert_grammar('cfg.txt', terminal, terminal_rule)
    grammar = read_grammar('cnf.txt')

    for filename in os.listdir("TesCase"):
        if filename.endswith(".py"): 
            print(filename)
            input_file = os.path.join('TesCase', filename)
            tokenized_input = tokenize_file(input_file, terminal)
            cyk_algorithm(grammar, tokenized_input)
            print()

def python_checker():
    # Coverting CFG to CNF
    convert_grammar('cfg.txt', terminal, terminal_rule)
    grammar = read_grammar('cnf.txt')

    # Converting file into tokens
    input_file = input('Masukkan nama file: ')
    tokenized_input, tokenized_lines = tokenize_file(input_file, terminal)
    
    # Result and Line Checker
    check_table, isAccepted = cyk_algorithm(grammar, tokenized_input, stat = False)
    line_error_checker(check_table, tokenized_lines, isAccepted)

if __name__ == '__main__':
    python_checker()