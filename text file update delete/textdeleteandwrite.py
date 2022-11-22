# Program to show various ways to read and
# write data in a file.
file1 = open("testing.txt","w")
file1.truncate(0)
L = ["This is Chennai \n","This is paris \n","This is Singapore \n"]

# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)
file1.close() #to change file access modes