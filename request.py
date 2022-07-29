# import requests
# import re
#
# def getUrl(pattern, text):
#     return re.findall(pattern, text)
#
# urlA = input()
# urlB = input()
#
# # urlA = "https://stepic.org/media/attachments/lesson/24472/sample0.html"
# # urlB = "https://stepic.org/media/attachments/lesson/24472/sample2.html"
# pattern = r"a.+href=.+>"
# pattern_url = r"http.+html"
#
# res = requests.get(urlA)
# flag = False
# if res.status_code == requests.codes.ok and re.search(pattern, res.text):
#     urlC = getUrl(pattern_url, res.text)
#     for url in urlC:
#         res = requests.get(url)
#         if res.status_code == requests.codes.ok and re.search(pattern, res.text) and urlB in res.text:
#             flag = True
#             break
# if flag:
#     print("Yes")
# else:
#     print("No")

import requests
import re
import urllib

# url = input()
url = "https://stepic.org/media/attachments/lesson/24471/01"
res = requests.get(url)
pattern = r"<[aA].*?href[ ]*=[ ]*[\"\'].*?[\"\']"
pattern_url = r"href[ ]*=[ ]*[\"\'](\w+:\/\/|\w).*\.\w+.*?"
result_line =[]
for lines in res.text.split("\n"):
    links = re.findall(pattern, lines.strip())
    for link in links:
        match = re.search(pattern_url, link)
        if match is not None:
            line = re.search(r"[\"\'].*", match.group(0)).group(0)
            line = line[1:]
            result_line.append(line)
result = []
for link in result_line:
    parseResult = urllib.parse.urlparse(link)
    if ":" in parseResult.netloc:
        st = parseResult.netloc.split(":")[0]
        if st not in result:
            result.append(st)
    elif parseResult.netloc not in "" and parseResult.netloc not in result:
        result.append(parseResult.netloc)
    elif parseResult.netloc in "" and parseResult.path not in result:
        result.append(parseResult.path)
for link in sorted(result):
    print(link)
