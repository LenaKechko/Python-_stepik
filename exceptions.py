'''
try:
    x = [1, 2, "hello", 7]
    x.sort()
    print(x)
except TypeError:
    print("Type error :(")

print("I can catch")

def f(x, y):
    try:
        return x / y
    except TypeError:
        print("Type error")
    except ZeroDivisionError:
        print("Zero division :(")

f(5, 0)

def g(x, y):
    try:
        return x / y
    except (TypeError, ZeroDivisionError) as e:
        print(type(e))
        print(e)
        print(e.args)

g(5, 0)
g(5, [])

def e(x, y):
    try:
        return x / y
    except:
        print("Error")

e(5, 0)
e(5, [])

try:
    15 / 0
except ZeroDivisionError:
    print("Division by zero")

print(ZeroDivisionError.mro())

def divide(x,y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero")
    else:
        print("result is", result)
    finally:
        print("finally")

divide(2, 1)
divide(2, 0)
#divide(2, [])

try:
    foo()
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except AssertionError:
    print("AssertionError")

def result_fun(myError, stack):
    parent_error = extended_error[myError]
    if parent_error == "":
        return False
    for x in stack:
        if x in parent_error:
            return True
    for x in parent_error:
        if result_fun(x, stack) is True:
            return True
    return False

n = int(input())
extended_error = {}
for i in range(n):
    tmp = input()
    if ":" in tmp:
        key, value = tmp.split(":")
        value = value.split()
    else:
        key = tmp
        value = ''
    key = key.strip()
    if key in extended_error.keys():
        extended_error[key].extend(value)
    else:
        extended_error[key] = value
m = int(input())
error = []
for i in range(m):
    error.append(input())
for i in range(1, len(error)):
    if result_fun(error[i],error[:i]) == True:
        print(error[i])

extended_error = {'ArithmeticError': '','ZeroDivisionError': 'ArithmeticError', 'OSError': '', 'FileNotFoundError': 'OSError', 'MyError':'ZeroDivisionError'}
error = ['ArithmeticError', 'OSError', 'MyError', 'ZeroDivisionError', 'FileNotFoundError']
print(extended_error)
print(error)

def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise ValueError(name + " is inappropriate name")

print(greet("Anton"))
print(greet("anton"))

def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise ValueError(name + " is inappropriate name")

while True:
    try:
        name = input("Please enter your name: ")
        greeting = greet(name)
        print(greeting)
    except ValueError:
        print("Please try again")
    else:
        break


class BadName(Exception):
    pass
def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise BadName(name + " is inappropriate name")

print(greet("Anton"))
print(greet("anton"))

class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x > 0:
            super(PositiveList, self).append(x)
        else:
            raise NonPositiveError
'''
class BadName(Exception):
    pass
def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise BadName(name + " is inappropriate name")

print("Import is execution")