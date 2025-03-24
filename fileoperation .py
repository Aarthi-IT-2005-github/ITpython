# Writing to a the file is sample.txt
file = open("sample.txt", "w")
file.write("hai I am Aarthi\n")
file.close()
# Read to check the write connent or return to the file
file = open("sample.txt", "r")
print(file.read())
file.close()
# Appending
file = open("sample.txt", "a")
file.write("I am a college student.\n")
file.close()
# Reading again to check weather the appending done or not
file = open("sample.txt", "r")
print(file.read())
file.close()
#finally close the file
