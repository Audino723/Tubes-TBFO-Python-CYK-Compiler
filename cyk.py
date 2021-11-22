from CFG2CNF import read_grammar
from CFG2CNF import read_terminal

def cyk_algorithm(grammar, tokenized_input = []):

    tokenized_input = ['a', 'b', 'a', 'a']
    cyk_Table = [[[] for j in range(i)] for i in range(len(tokenized_input), 0, -1)]

    print(cyk_Table)
    #Inisialisasi baris pertama
    for i, token in enumerate(tokenized_input):
        for rule in grammar:
            if rule[1] == token:
                cyk_Table[0][i].append(rule[0])
    
    print(cyk_Table)

    #Mengisi sisa table
    print(grammar)
    for i in range(1, len(cyk_Table)):
        for j in range(len(cyk_Table[i])):
            for k in range(i):
                left_cell = cyk_Table[k][j]
                right_cell = cyk_Table[i-k-1][k+j+1]

                if (left_cell != [] and right_cell != []):
                    for left in left_cell:
                        for right in right_cell:
                            target = []
                            target.append(left)
                            target.append(right)
                            for rule in grammar:
                                if rule[1:3] == target and rule[0] not in cyk_Table[i][j]:
                                    cyk_Table[i][j].append(rule[0])
                
                # print(f"{i} {j} {k}")
                # print(left_cell)
                # print(right_cell)
                # print(cyk_Table[i][j])
                # print("--------------")
        
    #Check if accepted
    print("---------Final-----------")
    print(cyk_Table)
    print(grammar[0][0])
    print(cyk_Table[-1][0][0])
    for item in cyk_Table[-1][0]:
        if (item == grammar[0][0]):
            print("Accepted")
            break
    else:
        print("Good bye")
    


if __name__ == '__main__':
    grammar = read_grammar('cnfTest.txt')
    print(grammar)
    #input_file = input('Enter the input file to validate: ')
    input_file = "TesCase\TC08.py"

    cyk_algorithm(grammar)
    #python_cyk_algorithm(grammar, 'terminal.txt', input_file)

