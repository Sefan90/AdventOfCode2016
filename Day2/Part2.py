lines = open("input.txt","r").readlines()
coords = [2,0]
code = ""
keypad = [[" "," ","1"," "," "],[" ","2","3","4"," "],["5","6","7","8","9"],[" ","A","B","C"," "],[" "," ","D"," "," "]]
incorrectcords = [[0,0],[0,1],[0,3],[0,4],[1,0],[1,4],[3,0],[3,4],[4,0],[4,1],[4,3],[4,4]]

for l in lines:
    for c in l:
        if c == "U" and coords[0] != 0 and [coords[0]-1,coords[1]] not in incorrectcords:
            coords[0] -= 1
        elif c == "D" and coords[0] != 4 and [coords[0]+1,coords[1]] not in incorrectcords:
            coords[0] += 1
        elif c == "L" and coords[1] != 0 and [coords[0],coords[1]-1] not in incorrectcords:
            coords[1] -= 1
        elif c == "R" and coords[1] != 4 and [coords[0],coords[1]+1] not in incorrectcords:
            coords[1] += 1
    code += keypad[coords[0]][coords[1]]
print(code)