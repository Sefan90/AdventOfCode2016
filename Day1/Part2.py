from collections import defaultdict

def walk(hasbeen,moved,rot,new):
    for i in range(1,new+1):
        if rot == 0:
            if hasbeen[str(moved[0]-moved[2]+i)+" "+str(moved[1]-moved[3])] == True:
                return hasbeen, (moved[0]-moved[2]+i)+(moved[1]-moved[3])
            hasbeen[str(moved[0]-moved[2]+i)+" "+str(moved[1]-moved[3])] = True
        if rot == 1:
            if hasbeen[str(moved[0]-moved[2])+" "+str(moved[1]-moved[3]+i)] == True:
                return hasbeen, (moved[0]-moved[2])+(moved[1]-moved[3]+i)
            hasbeen[str(moved[0]-moved[2])+" "+str(moved[1]-moved[3]+i)] = True
        if rot == 2:
            if hasbeen[str(moved[0]-moved[2]-i)+" "+str(moved[1]-moved[3])] == True:
                return hasbeen, (moved[0]-moved[2]-i)+(moved[1]-moved[3])
            hasbeen[str(moved[0]-moved[2]-i)+" "+str(moved[1]-moved[3])] = True
        if rot == 3:
            if hasbeen[str(moved[0]-moved[2])+" "+str(moved[1]-moved[3]-i)] == True:
                return hasbeen, (moved[0]-moved[2])+(moved[1]-moved[3]-i)
            hasbeen[str(moved[0]-moved[2])+" "+str(moved[1]-moved[3]-i)] = True
    return hasbeen, None

def part2():
    coords = open("input.txt","r").read().strip().split(", ")
    rot = 0
    moved = [0,0,0,0]
    hasbeen = defaultdict(lambda: False)
    _break = False
    output = 0

    while True:
        for c in coords:
            if c[0] == "R":
                rot -= 1
                if rot == -1:
                    rot = 3
            else:
                rot = (rot+1)%4
            hasbeen, output = walk(hasbeen,moved,rot,int(c[1:]))
            moved[rot] += int(c[1:])
            if output != None:
                _break = True
                break
        if _break == True:
            break

    print(abs(output))

part2()