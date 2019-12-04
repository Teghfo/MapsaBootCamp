class Book:

    def __init__(self, name, author, international,   category, bookId):
        self.name = name
        self.author = author
        self.category = category
        self.bookId = bookId
        self.status = True
        self.rent = None
        self.international = international
        self.motarjem = None

    def rentBook(self, member):
        pass

    def setMotarjem(self, motarjem):
        if self.international:
            self.motarjem = motarjem

# Todo method?   attribute?     class??
