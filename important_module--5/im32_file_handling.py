
# r = read mode
file_obj = open("new team.txt")
print(file_obj.read())
file_obj.close()
print("----------")

with open("new team.txt") as file_obj:                   #using   context manager  #default mode is 'r' mode i.e read mode
                                                         #in context manager no need to close the file it automatically close
    print(file_obj.readline())
    print(file_obj.readline())
    print(file_obj.readlines())                                 #give the given file data in list.
print("---------------")

with open("new team.txt") as file_obj:
    for line in file_obj.readlines():
        print(line.upper())
print("-----------")

with open("new team.txt") as file_obj:
        print(file_obj.read())
print("---------")


# write mode
with open("new_team.txt", "w") as wf:
    wf.write("this will create a new folder with pass name")

with open("new team.txt") as rf:
    with open("new_team12.txt", "w") as wf:
        # wf.write(rf.read())
        # wf.write(rf.readline())
        # wf.write("------------------")
        # wf.write(rf.readline())
        # wf.write("---------------\n")
        # wf.writelines(rf.readlines())
        wf.write("4582266974256633.38888")
        for line in rf.readlines():
            wf.write(line.upper())

# a = appending mode                             # add the item in last of file
with open("new_team12.txt", "a") as af:
       af.write("45822669\n7425663356\n2238888")

# rb, wb, ab binary deals with image and videos
with open("file1619.jpg", "rb") as rf:
    with open("new_file1619.jpg", "wb") as wf:
        wf.write(rf.read())
print("r,wb,ab")
with open("file new1.txt", "w+") as wf:                  # r+ = first read then write
    wf.write("first line\n")                             # w+ = first write then seek, read
    wf.write("second line\n")
    wf.write("third line\n")
    wf.seek(0)
    print(wf.read())


with open("new team.txt","r") as rf:
    with open ("newteam15.txt","w") as wf:
        wf.write(rf.read())
        wf.write("something i write in this file is very very correct and verified")

with open("new_team12.txt","r") as rf:
    with open ("newteam16.txt","w") as wf:
        wf.write(rf.read())


"""
The mode in the open function--3 syntax will tell Python as what operation--2 you want to do on a file.

‘r’ – Read Mode: Read mode is used only to read data from the file.

‘w’ – Write Mode: This mode is used when you want to write data into the file or modify it.
      Remember write mode overwrites the data present in the file.
      
‘a’ – Append Mode: Append mode is used to append data to the file. Remember data will be appended at the end of the file pointer.
‘r+’ – Read or Write Mode: This mode is used when we want to write or read the data from the same file.
‘a+’ – Append or Read Mode: This mode is used when we want to read data from the file or append the data into the same file.
Note: The above-mentioned modes are for opening, reading or writing text files only.

While using binary files, we have to use the same modes with the letter ‘b’ at the end. So that Python can understand that we are interacting with binary files.

‘wb’ – Open a file for write only mode in the binary format.
‘rb’ – Open a file for the read-only mode in the binary format.
‘ab’ – Open a file for appending only mode in the binary format.
‘rb+’ – Open a file for read and write only mode in the binary format.
‘ab+’ – Open a file for appending and read-only mode in the binary format.
"""