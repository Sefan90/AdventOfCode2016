lines = open("input.txt","r").readlines()
IPs = set()
for l in lines:
    IPs |= set(range(int(l.split("-")[0]),int(l.split("-")[1])+1))
print(IPs)
for i in range(4294967295):
    if i not in IPs:
        print(i)
        break

#2162801 low