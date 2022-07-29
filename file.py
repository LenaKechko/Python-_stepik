'''
f = open("test.txt", "r")
#x = f.read()
#x = x.splitlines()
#print(repr(x))
# x = f.readline().rstrip()
# print(repr(x))
# x = f.readline()
# print(repr(x))
for line in f:
    line = line.rstrip()
    print(repr(line))
x = f.read()
print(repr(x))

f.close()

f = open("test1.txt", "w")
#f.write("Hello\n")
#f.write("world")
lines = ["Lines1", "Lines2", "Lines3"]
contents = "\n".join(lines)
f.write(contents)
f.close()

f = open("test_append.txt", "a")
f.write("Hello\n")
f.close()

with open("test.txt") as f:
    for line in f:
        line = line.rstrip()
        print(line)

with open("test.txt") as f, open("test_copy.txt", "w") as w:
    for line in f:
        w.write(line)


with open("dataset_24465_4.txt") as f:
    lines = f.read().splitlines()
with open("result.txt", "w") as g:
    while len(lines) != 0:
        line = lines.pop()
        g.write(line + "\n")


import os
import os.path
import shutil


print(os.getcwd())
print(os.listdir(".idea"))

print(os.path.exists("file.py"))
print(os.path.exists("random.py"))
print(os.path.exists(".idea"))

print(os.path.isdir("file.py"))
print(os.path.isdir(".idea"))

print(os.path.abspath("file.py"))



shutil.copy("test1.txt", "test_copy.txt")
#shutil.copytree("tests", "tests/tests")
for current_dir, dirs, files in os.walk("."):
    print(current_dir, dirs, files)
'''

import os.path
import re

for current_dir, dirs, files in os.walk("main"):
    fl = False
    for file in files:
        if re.match('.+\.py', file):
            fl = True
            break
    if fl:
        print(current_dir)