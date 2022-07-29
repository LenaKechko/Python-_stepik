# import sys
#
# for line in sys.stdin:
#     line = line.rstrip()
#     if line.count("cat") >= 2:
#         print(line)

# import sys
# import re
#
# for line in sys.stdin:
#     line = line.strip()
#     pattern = r".*(\bcat\b).*"
#     if re.match(pattern, line):
#         print(line)

# import sys
# import re
#
# for line in sys.stdin:
#     line = line.strip()
#     pattern = r".*z.{3}z.*"
#     if re.match(pattern, line):
#         print(line)

# import sys
# import re
#
# for line in sys.stdin:
#     line = line.strip()
#     pattern = r".*\\.*"
#     if re.match(pattern, line):
#         print(line)

# import sys
# import re
#
# for line in sys.stdin:
#     line = line.strip()
#     pattern = r"\b(.+)\1\b"
#     if re.match(pattern, line):
#         print(line)

# import sys
# import re
#
# pattern = r"human"
# for line in sys.stdin:
#     line = line.strip()
#     print(re.sub(pattern, "computer", line))

# import sys
# import re
#
# pattern = r"[Aa]+\b"
# for line in sys.stdin:
#     line = line.strip()
#     print(re.sub(pattern, "argh", line, count=1))

# import sys
# import re
#
# pattern = r"\b(\w)(\w)"
# for line in sys.stdin:
#     line = line.strip()
#     print(re.sub(pattern, r"\2\1", line))

# import sys
# import re
#
# pattern = r"((\w)\2+)"
# for line in sys.stdin:
#     line = line.strip()
#     print(re.sub(pattern, r"\2", line))
