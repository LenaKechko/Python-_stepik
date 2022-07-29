def search(parent, child):
    if child in dict_extend.keys() and (child == parent or parent in dict_extend[child]):
        return "Yes"
    elif child in dict_extend.keys():
        for x in dict_extend[child]:
            search(parent, x)
            if search(parent, x) == "Yes":
                return "Yes"
    return "No"

n = int(input())
dict_extend = {}
for i in range(n):
    tmp = input()
    if ":" in tmp:
        key, value = tmp.split(":")
        value = value.split()
    else:
        key = tmp
        value = []
    key = key.strip()
    if key in dict_extend.keys():
        dict_extend[key].extend(value)
    else:
        dict_extend[key]= value
q = int(input())
result = []
for i in range(q):
    parent, child = input().split()
    result.append(search(parent, child))
for x in result:
    print(x)