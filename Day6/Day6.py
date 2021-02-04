from collections import Counter

lines = open("input.txt","r").readlines()
part1 = ""
part2 = ""
for i in range(len(lines[0].strip())):
    text = ""
    for line in lines:
        text += line[i]
    part1 += Counter(text).most_common(1)[0][0]
    lfc = Counter(text)
    part2 += min(lfc, key = lfc.get)
print(part1)
print(part2)
