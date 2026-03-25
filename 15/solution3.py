with open('input3.txt', 'r') as f:
    directions = f.read()
f.close()

history = [(0,0)]

for i in range(len(directions)):
    last = history[-1]
    if directions[i]=='v':
        history.append((last[0],last[1]-1))
    elif directions[i]=='^':
        history.append((last[0],last[1]+1))
    elif directions[i]=='>':
        history.append((last[0]+1,last[1]))
    elif directions[i]=='<':
        history.append((last[0]-1,last[1]))

print(len(set(history)))
