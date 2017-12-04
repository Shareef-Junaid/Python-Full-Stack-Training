

file = open("testfile.txt", "w+")
file.write("Hello World\n")
file.write("Testing file write\n")
#file.append("A")

file.seek(0)
print(file.read())
file.close()
