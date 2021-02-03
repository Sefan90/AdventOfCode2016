lines = open("input.txt","r").readlines()
coords = [1,1]
code = ""

for l in lines:
    for c in l:
        if c == "U" and coords[0] != 0:
            coords[0] -= 1
        elif c == "D" and coords[0] != 2:
            coords[0] += 1
        elif c == "L" and coords[1] != 0:
            coords[1] -= 1
        elif c == "R" and coords[1] != 2:
            coords[1] += 1
    code += str(coords[0]*3+coords[1]+1)
print(code)