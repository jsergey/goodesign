import re

#git log --all --numstat --date=short --pretty=format:'--%h--%ad--%aN' --no-renames
file = open("test.log", "r", encoding="UTF-8")
lines = file.read().split("\n")

commits = []
changes = []
commit = {}

authors = set([])

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
        authors.add(commit['author'])
    else:
        m = re.compile('(\d*)\s*(\d*)\s*(.*)').match(nextLine)
        changes.append({'file' : m.group(3), 'added': m.group(1), 'deleted': m.group(2)})

print('Authors: '+ str(len(authors)) + '\n')

number_of_authors = {}

for commit in commits:
    author = commit['author']
    for entry in commit['changes']:
        file = entry['file']
        if(file in number_of_authors.keys()):
            number_of_authors[file].add(author)
        else:
            number_of_authors[file] = set([author])

for entry in number_of_authors.keys():
    print (entry + '\t\t' + str(len(number_of_authors[entry])) + '\t' + str(number_of_authors[entry]))


# [entry
#  [revision]
#  [author]
#  [date]
#  [changes
#    [file ...]]]