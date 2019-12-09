import re


a = re.findall(r"\bS\w+", "The rain in Spainghas Stanbul Gholam asgharSsmdS")

print(a)


b = re.sub(r"\s", '', "The rain in Spainghas Stanbul Gholam asgharSsmdS")
print(b)

print(re.search(r"\s", "username: Gholi Akbar Khan"))
