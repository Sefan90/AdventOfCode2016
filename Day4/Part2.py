from collections import Counter
def test(l):
    for i in range(0,5):
        if l[i-6] not in [i[0] for i in Counter(l[:-10]).most_common(5)]:
            if l[:-10].count(l[i-6]) < Counter(l[:-10]).most_common(5)[i][1]:
                return 0
    return int(l[-10:-7])

def part2():
    lines = open("input.txt","r").readlines()
    for l in lines:
        text = ""
        for c in l[:-10]:
            if c == "-":
                text += " "
            else:
                text += chr(97+(ord(c)-97+int(l.strip().replace("-","")[-10:-7]))%26)
        if test(l.strip().replace("-","")) != 0:
            if 'north' in text:
                print(l.strip().replace("-","")[-10:-7])

part2()