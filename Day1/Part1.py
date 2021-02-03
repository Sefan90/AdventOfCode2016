coords = open("testinput.txt","r").read().strip().split(", ")
rot = 0
moved = [0,0,0,0]

for c in coords:
    if c[0] == "R":
        rot -= 1
        if rot == -1:
            rot = 3
    else:
        rot = (rot+1)%4
    moved[rot] += int(c[1:])

print(moved[0],moved[1],moved[2],moved[3])
print(abs(moved[0]-moved[2])+abs(moved[1]-moved[3]))