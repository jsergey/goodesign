import re
from denalysis.domain.structure import Commit, CommittedFile
import logging
import sqlite3
import os

class GitParser():
    def __init__(self, data):
        self.data = data

    def parse(self):
        db_filename = 'decoupler.db'
        conn = sqlite3.connect(db_filename)
        SQL = """insert into commits (author, hash, commit_date, file, file_path, added, removed)
                 values (:author, :hash, :commit_date, :file, :file_path, :added, :removed)
              """
        cursor = conn.cursor()
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
                logging.debug("New file detected: " + m.group(3) + "(" + m.group(1) + "," + m.group(2) + ")")
                commit.add_file(CommittedFile(m.group(3), m.group(1), m.group(2)))
                cursor.execute(SQL, {"author":commit.author,
                                     "hash":"",
                                     "commit_date":commit.date,
                                     "file":m.group(3),
                                     "file_path": os.path.split(m.group(3))[0],
                                     "added":m.group(1),
                                     "removed":m.group(2)})


        if commit.have_files():
            commits.append(commit)

        conn.commit()

        return commits
