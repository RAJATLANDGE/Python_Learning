import os

# getcwd
cwd = os.getcwd()                     #current working directory means presesnt working folder
print(cwd)

# chdir = change directory
os.chdir("E:\Python_project\learning_python\datatypes--1")
print(os.getcwd())
os.chdir("E:\Python_project\learning_python\important_module--5")
print(os.getcwd())

# listdir = give the list of folder in given directory
dir_list = os.listdir("E:\Python_project\learning_python\datatypes--1")
print(dir_list)
dir_list = os.listdir(os.getcwd())
print(dir_list)

#mkdir = for making directory in cwd
# os.mkdir("exp_dir")

# makedirs() = for making directorys in cwd         always use makedirs which also use for single directory creation
# os.makedirs("test/test1/test2")
# os.makedirs("sample")

# rmdir = for removing directory in cwd         (always use rmdir) , this only remove empty directory
# os.rmdir("exp_dir")
# os.rmdir("test")         #OSError: [WinError 145] The directory is not empty: 'test'   - that is only empty directory is remove

#removedirs = for removing more than one directory
# os.removedirs("test/test1/test2")
# os.removedirs("sample")

# rename = rename the directory
# os.rename("im26_demo_import.py", "im26_import_demo.py")
# os.rename()

# stat = give the information of given files
stat = os.stat("im26_import_demo.py")
print(stat)
print(stat.st_size)

# environ = is a mapping object that represents the user's environmental variables.
print(os.environ)
print(os.environ.get("os"))

if "win" in os.environ.get("os").lower():
    print("Welcome Windows User")


os.chdir(os.environ.get("HOMEDRIVE")+os.environ.get("HOMEPATH").replace("\\","/"))
print(os.getcwd())

# os.walk = return generator object
tree = os.walk("E:\Python_project\learning_python")
print(tree)

file_name = input("enter file name")
for dir, sub_dirs, file in tree:
    if file_name.lower in [f.lower for f in file]:
        print(f"your file present in {dir}")
else:
    print("your file is not present")


# os.removedirs("d1_string_introduction.py")

path = os.path.join("E:\Python_project\learning_python\important_module", "im26_import_demo.py")
print(path)

data = os.path.split("E:\Python_project\learning_python\important_module\im29_OS_module.py")   # give the file name separately
print(data)
print(data[-1])

print(os.path.isfile("E:\Python_project\learning_python\important_module\im29_OS_module.py"))
print(os.path.isfile("E:\Python_project\learning_python\important_module"))
print("-------")

print(os.path.isdir("E:\Python_project\learning_python\important_module\im29_OS_module.py"))
print(os.path.isdir("E:\Python_project\learning_python\important_module"))
print("----")

print(os.path.exists("E:\Python_project\learning_python\important_module\im29_OS_module.py"))
print(os.path.exists("E:\Python_project\learning_python\important_module"))
print(os.path.exists("E:\Python_project\learning_python\important_mod"))