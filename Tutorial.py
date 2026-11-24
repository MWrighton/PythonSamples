print('Hello World')

# Read = default setting for open
# Text = default setting for open
# No need to specify
file = open("TestTextFile.txt")
print(file.read())

# This displays a blank line because the pointer is at the end
print(file.readline())

# Done with the file, don't forget to close it
file.close()

# Using 'with' - should auto-close the file
with open("TestTextFile.txt") as file2:
  print(file2.read())
