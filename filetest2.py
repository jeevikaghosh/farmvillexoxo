im


writable = ['500', [(1,1,1)], ]

newFile = ""

for elem in writable:
    newFile += (elem + "\n")

# Writing
with open(username.txt, 'w') as file:
    file.write(newFile)
    file.close()

# Reading
with open(filename) as file:
    file = file.split("\n")
    for i in xrange(len(file)):
        self.money = file[0]
