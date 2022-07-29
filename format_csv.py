import csv

result = dict()
with open("Crimes.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if "2015" in row["Date"]:
            if row["Primary Type"] in result.keys():
                result[row["Primary Type"]] += 1
            else:
                result[row["Primary Type"]] = 1

i = sorted(result.values()).pop()
for key in result.keys():
    if result[key] == i:
        print(key)