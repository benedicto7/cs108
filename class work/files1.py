file = open('lines.txt', 'w')
for i in range(0, 100):
    file.write('Lines #' + str(i) + '\n')
file.close()

