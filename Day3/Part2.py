def tryTriangles(n):
    for i in range(len(n)):
        if n[i-2]+n[i-1]<=n[i]:
            return 0
    return 1

lines = open("input.txt","r").readlines()
possible = 0
i = 0
while i < len(lines):
    row1 = [int(n) for n in lines[i].split()]
    row2 = [int(n) for n in lines[i+1].split()]
    row3 = [int(n) for n in lines[i+2].split()]
    i += 3
    for r in range(3):
        possible += tryTriangles([row1[r],row2[r],row3[r]])
print(possible)