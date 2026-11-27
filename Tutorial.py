print('Hello World')

print("This will be concatonated with the next sentence without making a new line.", end=" STOP ")
print("This is the next sentence.")

print(1)
print(1+1)
print(1*3)
print(8/2)

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

# Prints the first 5 characters
with open("TestTextFile.txt") as file2:
  print(file2.read(5))

# Create a new file
newFile = open("NewFile.txt", "x")

# Write content to the file
with open("NewFile.txt", "w") as newFile:
  newFile.write("Write content to the file")

with open("NewFile.txt") as newFile:
  print(newFile.read())

# Overwrite the content of the file
with open("NewFile.txt", "w") as newFile:
  newFile.write("Put different text in the file")

with open("NewFile.txt") as newFile:
  print(newFile.read())

# Delete the new file so the sample code can run on subsequent tests 
# without throwing a fit because the 'new' file already exists
# os needs to be imported to delete files
import os
if os.path.exists("NewFile.txt"):
  os.remove("NewFile.txt")
else:
  print("404 - file not found")
