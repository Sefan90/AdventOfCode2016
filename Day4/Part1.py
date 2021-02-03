from collections import Counter
def test(l):
    for i in range(0,5):
        if l[i-6] not in [i[0] for i in Counter(l[:-10]).most_common(5)]:
            if l[:-10].count(l[i-6]) < Counter(l[:-10]).most_common(5)[i][1]:
                return 0
    return int(l[-10:-7])

def part1():
    lines = open("input.txt","r").readlines()
    sector = 0
    for l in lines:
        sector += test(l.strip().replace("-",""))
    print(sector)

part1()