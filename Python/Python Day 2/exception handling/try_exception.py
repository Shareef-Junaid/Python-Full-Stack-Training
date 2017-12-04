try:
    file = open("testfile.txt", "r")
    file.write("Hello World\n")
except IOError:
    print("can't find the file or read data")
else:
    print("File data written successfully")
    file.close()
