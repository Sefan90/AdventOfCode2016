def test(l):
    bracket = False
    tls = False
    for i in range(len(l)-3):
        if l[i] in ["[","]"]:
            bracket = not bracket
        elif l[i] == l[i+3] and l[i+1] == l[i+2] and not l[i] == l[i+1] == l[i+2] == l[i+3]:
            if bracket:
                return 0
            else:
                tls = True
    if tls:
        return 1
    else:
        return 0

def part1():
    lines = open("input.txt","r").readlines()
    supportTLS = 0
    for line in lines:
        supportTLS += test(line)
    print(supportTLS)

part1()