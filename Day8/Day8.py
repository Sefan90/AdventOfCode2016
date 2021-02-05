lines = open("input.txt","r").readlines()
screenw = 50#7
screenh = 6#3
screen = [[" " for _ in range(screenw)] for _ in range(screenh)]
for line in lines:
    if "rect" in line:
        w = int(line.split()[1].split("x")[0])
        h = int(line.split("x")[1])
        for i in range(w):
            for j in range(h):
                screen[j][i] = "#"
    elif "row" in line:
        r = int(line.split("=")[1].split()[0])
        t = int(line.split()[4])
        for i in range(t):
            tmp = screen[r][screenw-1]
            for j in range(screenw-1):
                tmp2 = screen[r][j]
                screen[r][j] = tmp
                tmp = tmp2
            screen[r][screenw-1] = tmp
    elif "column" in line:
        c = int(line.split("=")[1].split()[0])
        t = int(line.split()[4])
        for i in range(t):
            tmp = screen[screenh-1][c]
            for j in range(screenh-1):
                tmp2 = screen[j][c]
                screen[j][c] = tmp
                tmp = tmp2
            screen[screenh-1][c] = tmp
litcells = 0
for line in screen:
    print(line)
    for c in line:
        if c == "#":
            litcells += 1
print(litcells)
