def test(l):
    text = ""
    brackettext = ""
    bracket = False
    for c in l:
        if c in ["[","]"]:
            bracket = not bracket
            text += " "
            brackettext += " "
        elif bracket:
            brackettext += c
        else:
            text += c
    for i in range(len(text)-2):
        if text[i] == text[i+2] and text[i] != text[i+1] and text[i] != " " and text[i+1] != " ":
            if text[i+1]+text[i]+text[i+1] in brackettext:
                return 1
    return 0

def part2():
    lines = open("input.txt","r").readlines()
    supportTLS = 0
    for line in lines:
        supportTLS += test(line)
    print(supportTLS)

part2()