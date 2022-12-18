#
# 
# 
# 

# Create this hierarchy of directories:
# root - dir10 - dir20
#      - dir11 - dir21 - dir31
#      - dir12

from  day07lib import *

root = Dir(None, "root")

dir10 = Dir(root,"dir10")
root.dirs.append(dir10)
dir11 = Dir(root,"dir11")
root.dirs.append(dir11)
dir12 = Dir(root,"dir12")
root.dirs.append(dir12)

dir20 = Dir(dir10,"dir20")
dir10.dirs.append(dir20)
dir21 = Dir(dir11,"dir21")
dir11.dirs.append(dir21)

dir31 = Dir(dir21,"dir31")
dir21.dirs.append(dir31)

# Now add some files
file11A = File("file11A",100)
file11B = File("file11B",200)

file21A = File("file21A",100)

file31A = File("file31A",100)
file31B = File("file31B",200)
file31C = File("file31C",300)

dir11.files.append(file11A)
dir11.files.append(file11B)
dir21.files.append(file21A)
dir31.files.append(file31A)
dir31.files.append(file31B)
dir31.files.append(file31C)



print(showTree(root))
print(ls(dir11))

