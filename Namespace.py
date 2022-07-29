n = int(input())
structure = {'global': []}
result = []

def create(namespace, parent):
    structure[parent].append(namespace)
    structure[namespace] = []

def add(namespace, var):
    structure[namespace].append(var)

def get(namespace, var):
    if var in structure[namespace]:
        return namespace
    for parent in structure.keys():
        if namespace in structure[parent]:
            return get(parent, var)
    return None

for i in range(n):
    command, namespace, tmp = map(str, input().split())
    if command == 'add':
        add(namespace, tmp)
    elif command == 'create':
        create(namespace, tmp)
    else:
        result.append(get(namespace, tmp))
for x in result:
    print(x)