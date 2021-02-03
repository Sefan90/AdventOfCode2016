import hashlib
def part2():
    line = open("input.txt","r").readline()
    password = ["","","","","","","",""]
    index = 0
    while "" in password:
        hash_ = hashlib.md5((line+str(index)).encode('utf-8')).hexdigest()
        if hash_[0:5] == "00000":
            if hash_[5].isnumeric() and int(hash_[5]) in range(8):
                if password[int(hash_[5])] == "":
                    password[int(hash_[5])] = hash_[6]
        index += 1
    print(password)

part2()