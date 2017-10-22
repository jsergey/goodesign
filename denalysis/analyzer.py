import re

from denalysis.parsers import parser_git
from denalysis.analysis import code_age, authors

#git log --all --numstat --date=short --pretty=format:'--%h--%ad--%aN' --no-renames
file = open("../test.log", "r", encoding="UTF-8")
lines = file.read().split("\n")

parser = parser_git.GitParser(lines)
commits = parser.parse()

#for commit in commits:
#    print(commit)

aging = code_age.CodeAge(commits).code_age()

#for entry in aging.keys():
#    print(entry + '\t\t' + aging[entry])

authors = authors.Authors(commits)
print(str(authors.count_authors()))

authors_to_files = authors.count_authors_by_files()
for entry in authors_to_files.keys():
    print (entry + '\t\t' + str(len(authors_to_files[entry])) + '\t' + str(authors_to_files[entry]))


# [entry
#  [revision]
#  [author]
#  [date]
#  [changes
#    [file ...]]]