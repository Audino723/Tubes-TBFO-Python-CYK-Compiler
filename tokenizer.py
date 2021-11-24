def varname_checker(word):
    # Check variable name using finite automaton

    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    valid_prefix = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm',
                    'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', '_']

    if(word[0] in valid_prefix):
        return 'word'
    else:
        if(word[0] in number):
            for i in range(1, len(word)):
                if(word[i] not in number):
                    return 'undef'

            return 'num'
        else:
            return 'undef'


def tokenize_file(filePath, terminal):
    file = open(filePath, 'r')
    lines = file.readlines()
    file.close()

    # Part 1: Ubah raw input jadi array of string
    replaced = [('(', ' ( '), (')', ' ) '), ('[', ' [ '), (']', ' ] '), ('{', ' { '), ('}', ' } '), (':', ' : '), ('+', ' + '), ('-', ' - '), (
        '*', ' * '), ('/', ' / '), ('%', ' % '), ('=', ' = '), ('<', ' < '), ('>', ' > '), (',', ' , '), ('.', ' . '), ('"', ' " '), ("'", " ' "), ("#", " # "), ('\n', '')]

    tokens = []

    for i in range(len(lines)):
        for k, v in replaced:
            lines[i] = lines[i].replace(k, v)

        lines[i] = lines[i].split(" ")
        for j in range(len(lines[i])):
            tokens.append(lines[i][j])
        tokens.append('endline')

    tokens = ' '.join(tokens).split()

    # Part 2: Ubah array of string jadi array of modified string tergantung terminal

<<<<<<< HEAD
    #print(tokens)
=======
    # print(tokens)
>>>>>>> 02a2cf99c9c0590b1685c35192e0f88604eebe47

    for token in tokens:
        if(token != 'endline'):
            if token not in terminal:
                # Berarti token bukan keyword
                idx = tokens.index(token)
                converted = varname_checker(token)
                tokens.insert(idx, converted)
                tokens.remove(token)
            elif token == '#':
                # Berarti komen one liner
                idx = tokens.index(token)
                idxEnd = idx+1
                while (tokens[idxEnd] != 'endline'):
                    idxEnd+=1
                del tokens[idx:idxEnd]
                
            elif token == "'":
                idx = tokens.index(token)
                if (tokens[idx + 1] == "'") and (tokens[idx + 2] == "'"):
                    # Berarti komen multi-liner
                    idxEnd = idx+3
                    while(not((tokens[idxEnd] == "'") and (tokens[idxEnd+1] == "'") and (tokens[idxEnd+2] == "'")) and idxEnd < len(tokens)-1):
                        idxEnd += 1

                    if(idxEnd == len(tokens)-1):
                        del tokens[idx:]
                        tokens.append('undef')
                    else:
                        del tokens[idx:idxEnd+3]

                else:
                    # Berarti string
                    backslash = False
                    idxEnd = idx+1
                    while(not(tokens[idxEnd]=="'") and idxEnd<len(tokens)-1):
                        if(tokens[idxEnd]=='\\'):
                            backslash=True
                        idxEnd+=1
                    
                    if((idxEnd == len(tokens)-1)):
                        if tokens[idxEnd] != "'":
                            del tokens[idx:]
                            tokens.append('undef')
                        else:
                            del tokens[idx:]
                            if backslash == True:
                                tokens.insert(idx, 'undef')
                            else:
                                tokens.insert(idx, 'word')
                    else:
                        del tokens[idx:idxEnd+1]
                        if backslash==True:
                            tokens.insert(idx, 'undef')
                        else:
                            tokens.insert(idx, 'word')
            elif token == '"':
                idx = tokens.index(token)
                if (tokens[idx + 1] == '"') and (tokens[idx + 2] == '"'):
                    # Berarti komen multiliner
                    idxEnd = idx+3
                    while(not((tokens[idxEnd] == '"') and (tokens[idxEnd+1] == '"') and (tokens[idxEnd+2] == '"')) and idxEnd < len(tokens)-1):
                        if(tokens[idxEnd] == '\\'):
                            backslash = True
                        idxEnd += 1

                    if(idxEnd == len(tokens)-1):
                        del tokens[idx:]
                        tokens.append('undef')
                    else:
                        del tokens[idx:idxEnd+3]
                else:
                    # Berarti string biasa
                    backslash = False
                    idxEnd = idx+1
                    while(not(tokens[idxEnd] == '"') and idxEnd < len(tokens)-1):
                        idxEnd += 1

                    if((idxEnd == len(tokens)-1)):
                        if tokens[idxEnd] != '"':
                            del tokens[idx:]
                            tokens.append('undef')
                        else:
                            del tokens[idx:]
                            if backslash == True:
                                tokens.insert(idx, 'undef')
                            else:
                                tokens.insert(idx, 'word')
                    else:
                        del tokens[idx:idxEnd+1]
                        if backslash == True:
                            tokens.insert(idx, 'undef')
                        else:
                            tokens.insert(idx, 'word')

    while ("endline" in tokens):
        tokens.remove("endline")

    return tokens


# tokenize_file('test.txt')
if __name__ == '__main__':
    terminal = ['import', 'from', 'as', 'True', 'False', 'def', 'None', 'with', 'case', 'return', 'continue', 'break', 'pass', 'raise', 'in', 'class', '+', '-', '+', '*', '/', '%', 'and', 'or', 'not', '=', '>', '<', 'if', 'else', 'elif', 'while',
                'for', 'word', 'const', 'input', ':', ',', '.', '[', ']', '(', ')', "'", '"', "'''", '#', 'range', 'print', '!', 'open', 'write', 'num', 'self', 'len', 'IOERROR', 'ValueError', 'ZeroDivisionError', 'ImportError', 'NameError', 'TypeError']
    print(tokenize_file('test.py', terminal))
