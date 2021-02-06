def part2():
    line = open("input.txt","r").readline()
    para = False
    while "(" in line:
        text = ""
        i = 0
        while i < len(line.strip()):
            if line[i] == "(":
                para = True
            elif para:
                times = int(line[i:len(line)].split("x")[1].split(")")[0])
                chars = int(line[i:len(line)].split("x")[0])
                moved = len(str(times))+len(str(chars))+2
                for _ in range(times):
                    text += line[i+moved:i+moved+chars]
                i += moved+chars-1
                para = False
            else:
                text += line[i]
            i += 1
        line = text
    print(len(text))

part2()