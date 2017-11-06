from denalysis.parsers.parser_git import GitParser
from denalysis.analysis.code_age import CodeAge
from denalysis.analysis.authors import Authors
import logging
import sys

logging.basicConfig(level = logging.ERROR, stream=sys.stdout)

#git log --all --numstat --date=short --pretty=format:'--%h--%ad--%aN' --no-renames
file = open("../test.log", "r", encoding="UTF-8")
lines = file.read().split("\n")

commits = GitParser(lines).parse()
for commit in commits:
    print(commit)

print("\n--------\n Code Age")

aging = CodeAge(commits).code_age()
for entry in aging.keys():
    print(entry + '\t\t' + aging[entry])

print("\n--------\n Total Num of authors")

authors = Authors(commits)
print(str(authors.count_authors()))

print("\n--------\n Num of authors")

authors_to_files = authors.count_authors_by_files()
for entry in authors_to_files.keys():
    print (entry + '\t\t' + str(len(authors_to_files[entry])) + '\t' + str(authors_to_files[entry]))


# [entry
#  [revision]
#  [author]
#  [date]
#  [changes
#    [file ...]]]