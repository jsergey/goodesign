import re

file = open("test.log", "r", encoding="UTF-8")
lines = file.read().split("\n")

commits = []
changes = []
commit = {}

for nextLine in lines:
    if nextLine == '' or nextLine == '\n':
        pass
    elif bool(re.match('--', nextLine, re.IGNORECASE)):
        if len(commit) != 0:
            commit['changes'] = changes
            commits.append(commit)
            commit = {}
            changes = []
        m = re.compile('--(.*)--(.*)--(.*)').match(nextLine)
        commit['rev'] = m.group(1)
        commit['date'] = m.group(2)
        commit['author'] = m.group(3)
    else:
        m = re.compile('(\d*)\s*(\d*)\s*(.*)').match(nextLine)
        changes.append({'file' : m.group(3), 'added': m.group(1), 'deleted': m.group(2)})

print(commits)
# [entry
#  [revision]
#  [author]
#  [date]
#  [changes
#    [file ...]]]