keypad = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k','l'], ['m','n','o'], ['p','q','r','s'],['t','u','v',],['w','x','y','z']]
stringTyped = input()
possibility = []
for i in (keypad[int(stringTyped[0])-2]): 
    for j in (keypad[int(stringTyped[1])-2]):
        # print(keypad[int(stringTyped[0])-1][i],keypad[int(stringTyped[1])-1][j])
        possibility.append(i+j)
print(possibility)