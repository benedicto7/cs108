infile = open("out.txt", "r")
infile.readline()
infile.readline()
infile.readlines()
infile.readline()
infile.close()

infile = open("out.txt", "r")
for line in infile:
   print(line)
infile.close()

infile = open("out.txt", "r")
for i in range(3):
   infile.readline()
line = infile.readline()
line
print(line[0])
print(line[0:5])
words = line.split()
words
print(words[0])
infile.close()