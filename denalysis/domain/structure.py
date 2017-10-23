from datetime import datetime


class Commit:

    files = set([])

    def set_data(self, author, rev, date):
        self.author = author
        self.rev = rev
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.files = set([])

    def add_committed_file(self, committed_file):
        self.files.add(committed_file)

    def have_files(self):
        return len(self.files) > 0

    def get_files(self):
        return self.files

    def get_author(self):
        return self.author

    def __str__(self):
        string = self.author + '\t' + self.rev + '\t' + str(self.date) + '\n'
        for file in self.files:
            string += '\t' + format(file)
        return string


class CommittedFile:
    def __init__(self, name, lines_added, lines_removed):
        self.name = name
        self.lines_added = lines_added
        self.lines_removed = lines_removed

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name + '\t' + self.lines_added + '\t' + self.lines_removed + '\n'

    def __repr__(self):
        return self.name + '\t' + self.lines_added + '\t' + self.lines_removed + '\n'
