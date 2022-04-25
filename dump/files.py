outfile = open("out1.txt", "w")
outfile.write("Example ")
outfile.write("output ")
outfile.write("text file\n")
outfile.write("xyz Coordinates\n")
outfile.write("MODEL\n")
outfile.write("ATOM %3d" % 1)
seq = "n %5.1f%5.1f%5.1f" % (0, 1, 2)
outfile.write(seq)
outfile.write("\n")
outfile.close()
    

