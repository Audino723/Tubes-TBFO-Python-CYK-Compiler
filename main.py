from cyk import cyk_algorithm
from CFG2CNF import read_grammar
from tokenizer import tokenize_file
from CFG2CNF import convert_grammar

terminal = ['import', 'from', 'as', 'True', 'False', 'def', 'None', 'with', 'case', 'return', 'continue', 'break', 'pass', 'raise', 'in', 'class', 'append', '+', '-', '+', '*', '/', '%', 'and', 'or', 'not', '=', '>', '<', 'if', 'else', 'elif','while', 'for', 'word', 'const', 'input', 'is',':', ',', '.', '[', ']', '(', ')', '}', '{',  "'", '"', "'''", '#', 'range', 'print', '!', 'open', 'write', 'num', 'self', 'len', 'IOERROR', 'ValueError', 'ZeroDivisionError', 'ImportError', 'NameError', 'TypeError']
terminal_rule = ['NUM', 'BOOL', 'ALPHABET', 'QUOTE_MARK', 'POINT', 'IF', 'ELIF', 'ELSE', 'IMPORT', 'FROM', 'AS', 'DEF', 'NONE', 'WITH', 'RETURN', 'CONTINUE', 'BREAK', 'PASS', 'RAISE', 'IN', 'CLASS', 'APPEND', 'LEN','MINUS', 'PLUS', 'MUL', 'DIV', 'MOD', 'AND', 'OR', 'NOT', 'EQUAL', 'WHILE', 'FOR', 'INPUT', 'IS','COLON', 'COMMA', 'OP_SQ_BRACK', 'CS_SQ_BRACK', 'OP_BRACK', 'CS_BRACK', 'GREATER', 'LESS', 'DQUOTE_MARK', 'HASHTAG', 'RANGE', 'PRINT', 'EXC_MARK', 'OPEN', 'SELF', 'RELATION_OPERATOR',  'OP_CURLY_BRACK', 'CS_CURLY_BRACK']

import os

def Tes_Case():
    convert_grammar('cfg_revise.txt', terminal, terminal_rule)
    grammar = read_grammar('cnf.txt')

    for filename in os.listdir("TesCase"):
        if filename.endswith(".py"): 
            print(filename)
            input_file = os.path.join('TesCase', filename)
            tokenized_input = tokenize_file(input_file, terminal)
            cyk_algorithm(grammar, tokenized_input)
            print()
            
def Tes_Satu():
    convert_grammar('cfg_revise.txt', terminal, terminal_rule)
    grammar = read_grammar('cnf.txt')

    input_file = input('Masukkan nama file: ')
    tokenized_input = tokenize_file(input_file, terminal)
 
    # print("=============Tokenized Input==========")
    # print(tokenized_input)
    cyk_algorithm(grammar, tokenized_input, stat = False)


def Tes_Banyak():
    convert_grammar('cfg_revise.txt', terminal, terminal_rule)
    grammar = read_grammar('cnf.txt')

    input_file = ["TesCase/TC01.py", "TesCase/TC02.py",
                  "TesCase/TC03.py", "TesCase/TC04.py", "TesCase/TC05.py", "TesCase/TC06.py", "TesCase/TC07.py", "TesCase/TC08.py", "TesCase/TC09.py", "TesCase/TC10.py"]

    for file in input_file:
        tokenized_input = tokenize_file(file, terminal)
        print(file)
        cyk_algorithm(grammar, tokenized_input, stat=False)
    

if __name__ == '__main__':
    Tes_Satu()