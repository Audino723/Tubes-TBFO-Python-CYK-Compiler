filename = 'cfg_revise.txt'
terminalfile = open(filename, "r")
terminaltemp = terminalfile.readlines()
terminalfile.close()

terminal = []
for line in terminaltemp:
    linenew = line.replace("\n", "")
    linenew = linenew.split(" ")
    if (linenew[0] not in terminal):
        terminal.append(linenew[0])

print(terminal)