def read_grammar(filename):
# Membaca file grammar, production rule tiap baris akan diubah menjadi bentuk list 
# Contoh : Production rule berbentuk A -> B C D akan diubah menjadi ['A', 'B', 'C', 'D'].
# Production rule yang memiliki dua bentuk atau lebih akan dipisah menjadi 2 list atau lebih 
# Contoh: A -> B | C akan diubah menjadi bentuk ['A', 'B'] dan ['A', 'C']
# Fungsi akan mengembalikan list of list yang berisi production rule tiap baris
    file = open(filename, 'r')
    filelines = file.readlines()
    file.close()

    grammar = []
    
    for line in filelines:
        rule = line.replace(" ->", "").split()
        grammar.append(rule)

    for rule in grammar:
        # Memisahkan rule yang berbentuk X -> Y | Z menjadi X -> Y dan X -> Z
        try:
            or_idx = rule.index("|")

        except ValueError:
            # Apabila sebuah nonterminal tidak mengandung 2 production rule yang berbeda
            or_idx = -1

        if (or_idx != -1):
            insertion_idx = grammar.index(rule) + 1
            nonterm = rule[0]
            rule_branch = [nonterm]
            for i in range(or_idx + 1, len(rule)):
                rule_branch.append(rule[i])
            for j in range(or_idx, len(rule)):
                rule.pop()
            grammar.insert(insertion_idx, rule_branch)
    
    return grammar
    # return [x.replace("->", "").split() for x in filelines]

def convert_large_rules(grammar):
# I. S. grammar merupakan list of list Production Rule suatu CFG
# F. S. Menangani production rule yang memiliki 2 variabel atau lebih
#       Contoh: A -> BCD diubah menjadi A -> BX dan X -> CD
#       Dalam bentuk list: ['A', 'B','C','D'] diubah menjadi ['A','B','X'], ['X','C','D']
    addition = 1
    y = 0
    while y < len(grammar):
        rule_index = y + 1
        if (len(grammar[y]) - 1) > 2:
            new_rule = []
            for i in range(2, len(grammar[y])):
                new_rule.append(grammar[y][i])
            for j in range(2, len(grammar[y])):
                grammar[y].pop()
            new_nonterm = new_rule[0] + "_deriv"
            for checkrule in grammar:
                if checkrule[0] == new_nonterm:
                    new_nonterm += "{}".format(addition)
                    addition += 1
                    break
            grammar[y].append(new_nonterm)
            new_rule.insert(0, new_nonterm)
            if new_rule not in grammar:
                grammar.insert(rule_index, new_rule)
        y += 1

def convert_unit_productions(grammar, terminal, terminal_rule):
# I. S. grammar berbentuk list of list Production Rule suatu CFG
# F. S. Menangani grammar yang memiliki unit production
#       Contoh: Terdapat production Rule A -> B dan B -> C D akan diubah 
#       menjadi A -> C D di mana B merupakan suatu variabel.
#       Dalam bentuk list: ['A', 'B'] dan ['B','C','D'] menjadi
#       ['A','C','D'].
    
    #terminal, terminal_rule = read_terminal('terminal.txt')
    terminal = ['import', 'from', 'as', 'True', 'False', 'def', 'None', 'with', 'case', 'return', 'continue', 'break', 'pass', 'raise', 'in', 'class', '+', '-', '+', '*', '/', '%', 'and', 'or', 'not', '=', '>', '<', 'if', 'else', 'elif','while', 'for', 'word', 'const', 'input', ':', ',', '.', '[', ']', '(', ')', "'", '"', "'''", '#', 'range', 'print', '!', 'open', 'write', 'num', 'self', 'len', 'IOERROR', 'ValueError', 'ZeroDivisionError', 'ImportError', 'NameError', 'TypeError']
    terminal_rule = ['NUM', 'BOOL', 'ALPHABET', 'QUOTE_MARK', 'POINT', 'IF', 'ELIF', 'ELSE', 'IMPORT', 'FROM', 'AS', 'DEF', 'NONE', 'WITH', 'RETURN', 'CONTINUE', 'BREAK', 'PASS', 'RAISE', 'IN', 'CLASS', 'MINUS', 'PLUS', 'MUL', 'DIV', 'MOD', 'AND', 'OR', 'NOT', 'EQUAL', 'WHILE', 'FOR', 'INPUT', 'COLON', 'COMMA', 'OP_SQ_BRACK', 'CS_SQ_BRACK', 'OP_BRACK', 'CS_BRACK', 'GREATER', 'LESS', 'DQUOTE_MARK', 'HASHTAG', 'RANGE', 'PRINT', 'EXC_MARK', 'OPEN', 'SELF', 'RELATION_OPERATOR']

    j = 0
    while j < len(grammar):
        if ((len(grammar[j]) == 2) and (grammar[j][1] in terminal_rule)):
            idx_terminal_rule = search_rule(grammar, grammar[j][1])
            insertion_idx = j + 1
            addition = 0
            for i in idx_terminal_rule:
                new_rule = []
                for termnonterm in grammar[i + addition]:
                    new_rule.append(termnonterm)
                new_rule[0] = grammar[j][0]
                grammar.insert(insertion_idx, new_rule)
                addition += 1
            grammar.remove(grammar[j])
            
        elif ((len(grammar[j]) == 2) and (grammar[j][1] not in terminal)):
            unit_production = grammar[j][1]
            idxs_unit_production = search_rule(grammar, unit_production)
            insertion_idx = j + 1
            addition = 0
            for i in idxs_unit_production:
                new_rule = []
                for termnonterm in grammar[i + addition]:
                    new_rule.append(termnonterm)
                new_rule[0] = grammar[j][0]
                grammar.insert(insertion_idx, new_rule)
                addition += 1
            grammar.remove(grammar[j])
        j += 1


def search_rule(grammar, rule_nonterm):
# Mengembalikan index dari rule dengan variabel yang dicari dalam grammar
# dalam bentuk list. Contoh: [2, 5, 7].
# Diasumsikan variabel tersedia dalam grammar
    idx_rule = []
    for i in range(0, len(grammar)):
        if grammar[i][0] == rule_nonterm:
            idx_rule.append(i)

    return idx_rule



def write_to_file(grammar):
# I. S. grammar berbentuk list of list Production Rule suatu CFG
# F. S. Menuliskan grammar dalam bentuk dalam file .txt
#       List ['A','B','C'] akan ditulis sebagai A -> B C

    for rule in grammar:
        for line in grammar:
            if rule[0] == line[0] :
                if (grammar.index(rule) != grammar.index(line)):
                    rule.append("|")
                    for i in range(1, len(line)):
                        rule.append(line[i])
                    grammar.remove(line)
            


    # filename = input("Enter the output file name: ")
    # file = open('filename', 'w')
    file = open('cnf.txt', 'w')
    for rule in grammar:
        file.write(rule[0])
        file.write(" ->")
        for i in range(1, len(rule)):
            file.write(" {}".format(rule[i]))
        file.write("\n")
    file.close()


def convert_grammar(filename):
# I. S. filename merupakan suatu file berisi production rule suatu CFG
# F. S. Menulis suatu file dengan nama ditentukan user yang berisi bentuk CNF 
#       sesuai dengan langkah-langkah penyederhanaan CFG menjadi CNF dari 
#       file CFG yang menjadi parameter
    grammar = read_grammar(filename)
    for rule in grammar:
        if (len(rule) == 0):
            grammar.remove(rule)
    
    convert_unit_productions(grammar)
    convert_large_rules(grammar)
    write_to_file(grammar)

if __name__ == '__main__':
    # filename = input("Enter the Context Free Grammar file to convert: ")
    # convert_grammar(filename)
    convert_grammar('cfg_revise.txt')

