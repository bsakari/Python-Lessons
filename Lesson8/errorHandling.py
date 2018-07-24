try:
    file = open("king.txt","w")
    file.write("This is my file")

except IOError:
    print("Error: Can't find file or read data")
else:
    print("File Created and writen data successfully")
    file.close()