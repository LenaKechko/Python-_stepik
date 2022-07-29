'''
import fib
import exceptions

print(exceptions.greet("Student"))
print(fib.fib(5))


import datetime

year, month, day = (int(x) for x in input().split())
date = datetime.date(year, month, day)
days = datetime.timedelta(int(input()))
date = date + days
print(date.year, date.month, date.day)
'''

import simplecrypt
import request

path = "https://stepic.org/media/attachments/lesson/24466/passwords.txt"
passwords = request.get(path).text.split()
with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
for password in passwords:
    try:
        decrypt = simplecrypt.decrypt(password.strip(), encrypted)
        print(decrypt)
        break
    except simplecrypt.DecryptionException:
        continue
