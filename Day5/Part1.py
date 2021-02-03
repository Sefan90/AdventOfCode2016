import hashlib
def part1():
    line = open("input.txt","r").readline()
    password = ""
    index = 0
    while len(password) < 8:
        hash_ = hashlib.md5((line+str(index)).encode('utf-8')).hexdigest()
        if hash_[0:5] == "00000":
            password += hash_[5]
        index += 1
    print(password)

part1()