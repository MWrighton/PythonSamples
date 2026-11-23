print('Hello World')

# Read = default setting for open
# Text = default setting for open
# No need to specify
file = open("TestTextFile.txt")
print(file.read())

# Done with the file, don't forget to close it
file.close()
