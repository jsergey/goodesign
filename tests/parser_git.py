import unittest
from datetime import datetime
from denalysis.parsers.parser_git import GitParser


class TestGitParser(unittest.TestCase):
    def test_alone_commit_count(self):
        data = ['--2a40d01--2017-07-30--Sergey', '1	1	README.md', ]
        self.assertEqual(len(GitParser(data).parse()), 1)

    def test_two_commits_count(self):
        data = ['--2a40d01--2017-07-30--Sergey', '1	1	README.md',
                '--2a40d01--2017-07-30--Sergey', '1	1	README2.md']
        self.assertEqual(len(GitParser(data).parse()), 2)

    def test_alone_commit_data(self):
        data = ['--2a40d01--2017-07-30--Sergey', '1	1	README.md', ]

        commit = GitParser(data).parse()[0]

        self.assertEqual(commit.author, 'Sergey')
        self.assertEqual(commit.rev, '2a40d01')
        self.assertEqual(commit.date, datetime.strptime('2017-07-30', "%Y-%m-%d").date())

        self.assertEqual(len(commit.files), 1)

        file = commit.files.pop()
        self.assertEqual(file.name, 'README.md')
        self.assertEqual(file.lines_added, '1')
        self.assertEqual(file.lines_removed, '1')

    def test_empty_commit_doesnt_count(self):
        data = ['--2a40d01--2017-07-30--Sergey', '1	1	README.md',
                '--2a40d21--2017-07-22--Sergey',
                '--2a40d31--2017-07-23--Sergey']
        self.assertEqual(len(GitParser(data).parse()), 1)
