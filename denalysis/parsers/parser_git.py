import re
from denalysis.domain.structure import Commit, CommittedFile
import logging

class GitParser():
    def __init__(self, data):
        self.data = data

    def parse(self):
        commits = []
        commit = Commit()

        logging.debug("GitParser::start parsring")
        for nextLine in self.data:
            logging.debug("Processing line: " + nextLine)
            if nextLine == '' or nextLine == '\n':
                logging.debug("Line is empty, skipping")
                pass
            elif bool(re.match('--', nextLine, re.IGNORECASE)):
                logging.debug("Commit metadata detected")
                if commit.have_files():
                    logging.debug("Append commit to storage")
                    commits.append(commit)
                    commit = Commit()
                m = re.compile('--(.*)--(.*)--(.*)').match(nextLine)
                logging.debug("Author: " + m.group(3) +
                              ", revision: " + m.group(1) +
                              ", date: " + m.group(2))
                commit.set_data(m.group(3), m.group(1), m.group(2))

            else:
                m = re.compile('(\d*)\s*(\d*)\s*(.*)').match(nextLine)
                logging.debug("New file detected: " + m.group(3) + "(" + m.group(1) +"," + m.group(2) + ")")
                commit.add_file(CommittedFile(m.group(3), m.group(1), m.group(2)))

        if commit.have_files():
            commits.append(commit)

        return commits
