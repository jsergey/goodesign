class Authors:
    def __init__(self, commits):
        self.commits = commits

    def count_authors(self):
        authors = set([])
        for entry in self.commits:
            authors.add(entry.author)
        return len(authors)

    def count_authors_by_files(self):
        number_of_authors = {}
        for commit in self.commits:
            author = commit.author
            for entry in commit.get_files():
                file = entry.get_name()
                if file in number_of_authors.keys():
                    number_of_authors[file].add(author)
                else:
                    number_of_authors[file] = {author}
        return number_of_authors
