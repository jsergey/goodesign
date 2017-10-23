import re
from denalysis.domain.structure import Commit, CommittedFile

class GitParser():
    def __init__(self, data):
        self.data = data

    # def parse(self):
    #     commits = []
    #     changes = []
    #     commit = {}
    #
    #     for nextLine in self.data:
    #         if nextLine == '' or nextLine == '\n':
    #             pass
    #         elif bool(re.match('--', nextLine, re.IGNORECASE)):
    #             if len(commit) != 0:
    #                 commit['changes'] = changes
    #                 commits.append(commit)
    #                 commit = {}
    #                 changes = []
    #             m = re.compile('--(.*)--(.*)--(.*)').match(nextLine)
    #             commit['rev'] = m.group(1)
    #             commit['date'] = m.group(2)
    #             commit['author'] = m.group(3)
    #         else:
    #             m = re.compile('(\d*)\s*(\d*)\s*(.*)').match(nextLine)
    #             changes.append({'file': m.group(3), 'added': m.group(1), 'deleted': m.group(2)})
    #
    #     return commits

    def parse(self):
        commits = []
        commit = Commit()

        for nextLine in self.data:
            if nextLine == '' or nextLine == '\n':
                pass
            elif bool(re.match('--', nextLine, re.IGNORECASE)):
                if(commit.have_files()):
                    commits.append(commit)
                    commit = Commit()
                m = re.compile('--(.*)--(.*)--(.*)').match(nextLine)
                commit.set_data(m.group(3), m.group(1), m.group(2))
            else:
                m = re.compile('(\d*)\s*(\d*)\s*(.*)').match(nextLine)
                commit.add_committed_file(CommittedFile(m.group(3), m.group(1), m.group(2)))

        return commits
