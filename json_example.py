import json
# data = [
#     {
#         "name": "A",
#         "parents": []
#     },
#     {
#         "name": "B",
#         "parents": ["A", "C"]
#     },
#     {
#         "name": "C",
#         "parents": ["A"]
#     }
# ]

def search(parent):
    childs = []
    for child in dict_extend.keys():
        if (parent in dict_extend[child]) and (child not in childs):
            childs.append(child)
            tmp = search(child)
            for x in tmp:
                if x not in childs:
                    childs.append(x)
    return childs

# data_json = json.dumps(data, indent=4, sort_keys=True)
data_json = input()
dict_extend = dict()
data_again = json.loads(data_json)
for x in data_again:
    dict_extend[x["name"]] = x["parents"]
result = dict()
for parent in sorted(dict_extend.keys()):
    if parent not in result.keys():
        kol = search(parent)
        print(parent + " : " + str(len(kol)+1))