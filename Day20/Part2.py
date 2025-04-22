def tmp():
IPs = [True for _ in range(4294967296)]
for l in lines:
    for i in range(int(l.split("-")[0]),int(l.split("-")[1])+1):
        IPs[i] = False
for i in range(len(IPs)):
    if IPs[i] == True:
        print(i)
        break