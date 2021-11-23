from cyk import cyk_algorithm
from CFG2CNF import read_grammar
from tokenizer import tokenize_file

if __name__ == '__main__':
    grammar = read_grammar('cfg_revise.txt')
    #print(grammar)
    #input_file = input('Enter the input file to validate: ')
    input_file = "input.py"

    tokenized_input = tokenize_file(input_file)
    print(tokenized_input)

    cyk_algorithm(grammar, tokenized_input)
    #python_cyk_algorithm(grammar, 'terminal.txt', input_file)
