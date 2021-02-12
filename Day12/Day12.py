lines = open("input.txt","r").readlines()
register = [0,0,1,0] #[0,0,0,0]
i = 0
while i < len(lines):
    l = lines[i]
    if "cpy" in l:
        val = l.split()[1]
        reg = l.split()[2]
        if val.isnumeric():
            register[ord(reg)-97]  = int(val)
        else:
            register[ord(reg)-97] = register[ord(val)-97]
    elif "inc" in l:
        register[ord(l.split()[1])-97] += 1
    elif "dec" in l:
        register[ord(l.split()[1])-97] -= 1
    elif "jnz" in l:
        reg = l.split()[1]
        jmp = l.split()[2]
        if reg.isnumeric() and reg != 0:
            i += int(jmp)
        elif register[ord(reg)-97] != 0:
            i += int(jmp)
    if l == lines[i]:
        i += 1
print(register)
print(register[0])