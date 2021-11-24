def cyk_algorithm(grammar, tokenized_input, stat = False):

    #Inisialisasi CYK Table
    cyk_Table = [[[] for j in range(i)] for i in range(len(tokenized_input), 0, -1)]

    #Array untuk Line Error checker
    check_Table = [False for _ in range(len(tokenized_input))]
    pos_Table = [[set() for j in range(i)] for i in range(len(tokenized_input), 0, -1)]
    pos_Table[0] = [set([i]) for i in range(len(tokenized_input))]

    #Inisialisasi baris pertama
    for i, token in enumerate(tokenized_input):
        for rule in grammar:
            if rule[1] == token and rule[0] not in cyk_Table[0][i]:
                cyk_Table[0][i].append(rule[0])
    
    #Statistik untuk debugging
    if stat:
        print()
        print(cyk_Table[0])
        print(len(cyk_Table[0]))
        print(len(tokenized_input))

    #Mengisi sisa table
    for i in range(1, len(cyk_Table)):
        for j in range(len(cyk_Table[i])):
            for k in range(i):
                left_cell = cyk_Table[k][j]
                right_cell = cyk_Table[i-k-1][k+j+1]

                for left in left_cell:
                    for right in right_cell:
                        targets = []
                        targets.append(left)
                        targets.append(right)
                        
                        #Untuk line checker
                        notDeriv = True
                        for target in targets:
                            if ('deriv' in target):
                                notDeriv = False                            

                        for rule in grammar:
                            if rule[1:3] == targets and rule[0] not in cyk_Table[i][j]:
                                cyk_Table[i][j].append(rule[0])

                                pos_Table[i][j] = pos_Table[i][j].union(pos_Table[k][j])
                                pos_Table[i][j] = pos_Table[i][j].union(pos_Table[i-k-1][k+j+1])

                                if ('deriv' not in rule and notDeriv):
                                    for pos in pos_Table[i][j]:
                                        check_Table[pos] = True
    
    #Check if accepted
    if stat:
        print(check_Table)
        print(len(check_Table))
        print("---------Final-----------")
        for table in cyk_Table:
            print(table)
            print("==========================================")
    for item in cyk_Table[-1][0]:
        if (item == "BLOCK_CODE"):
            print("Accepted")
            isAccepted = True
            break
    else:
        print("Syntax Error")
        isAccepted = False

    return check_Table, isAccepted
    
def line_error_checker(check_table, tokenized_lines, isAccepted):
    if not isAccepted:
        error_lines = []
        for i, isCorrect in enumerate(check_table):
            if not isCorrect and tokenized_lines[i] not in error_lines:
                error_lines.append(tokenized_lines[i])

        print("Possible Error Lines : ", *error_lines)