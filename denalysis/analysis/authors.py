class Authors:

    def __init__(self, data):
        self.data = data

    def count_authors(self):
        authors = set([])
        for entry in self.data:
            authors.add(entry.get_author())
        return len(authors)

    def count_authors_by_files(self):
        number_of_authors = {}
        for commit in self.data:
            author = commit.get_author()
            for entry in commit.get_files():
                file = entry.get_name()
                if (file in number_of_authors.keys()):
                    number_of_authors[file].add(author)
                else:
                    number_of_authors[file] = set([author])
        return number_of_authors