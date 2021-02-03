coords = open("input.txt","r").read().strip().split(", ")
rot = 0
moved = [0,0,0,0]
hasbeen = set()
_break = False

while True:
    for c in coords:
        if c[0] == "R":
            rot -= 1
            if rot == -1:
                rot = 3
        else:
            rot = (rot+1)%4
        moved[rot] += int(c[1:])
        tmp = str(moved[0]-moved[2])+" "+str(moved[1]-moved[3])
        print(tmp)
        if tmp in hasbeen:
            _break = True
            break
        hasbeen.add(tmp)
    if _break == True:
        break

print(moved[0],moved[1],moved[2],moved[3])
print(abs(moved[0]-moved[2])+abs(moved[1]-moved[3]))

#275 high