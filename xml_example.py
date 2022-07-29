from xml.etree import ElementTree

def fun(root, kol = 1):
    kol += 1
    for child in root:
        color_dict[child.attrib["color"]] += kol
        fun(child, kol)

data = input()

root = ElementTree.fromstring(data)

color_dict = {"red": 0, "green": 0, "blue": 0}
color_dict[root.attrib["color"]] += 1
fun(root)
print(color_dict["red"], color_dict["green"], color_dict["blue"])
