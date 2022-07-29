'''
s = input()
a = input()
b = input()
count = 0
while True:
    if (a in s) and (a in b):
        print("Impossible")
        break
    elif a in s:
        s = s.replace(a, b)
        count += 1
    else:
        print(count)
        break
'''

s = input()
t = input()
count = 0
start = 0
while True:
    try:
        index = s.index(t,start)
        count += 1
        start = index + 1
    except ValueError:
        break
print(count)
