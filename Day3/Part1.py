lines = open("input.txt","r").readlines()
possible = 0
for l in lines:
    n = [int(i) for i in l.split()]
    test = True
    for i in range(len(n)):
        if n[i-2]+n[i-1]<=n[i]:
            test = False
    if test == True:
        possible += 1
print(possible)