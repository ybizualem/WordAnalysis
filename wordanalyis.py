infile = open("crosswords.txt(1)","r")
for line in infile:
    word = line[:len(line)-1]
    print(word)