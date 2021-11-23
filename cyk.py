def cyk_algorithm(grammar, tokenized_input = []):

    cyk_Table = [[[] for j in range(i)] for i in range(len(tokenized_input), 0, -1)]

    #Inisialisasi baris pertama
    #for rule in grammar:
        #print(rule[1])
    for i, token in enumerate(tokenized_input):
        for rule in grammar:
            if rule[1] == token and rule[0] not in cyk_Table[0][i]:
                cyk_Table[0][i].append(rule[0])
    print()
    print(cyk_Table)

    #Mengisi sisa table
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
    for table in cyk_Table:
        print(table)
        print("==========================================")
    for item in cyk_Table[-1][0]:
        if (item == "BLOCK_CODE"):
            print("Accepted")
            break
    else:
        print("Good bye")
    


