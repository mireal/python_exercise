import re

p = re.compile(r'[a-z,A-Z,0-9,$#@]')
test_str = u"DFSdsffdFDfd5342#@!%"
re.fullmatch()
print(re.findall(p, test_str))
