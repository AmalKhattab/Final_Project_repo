class Book:
    def __init__(self, id, title, author, description, status: bool):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.status = status

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_status(self):
        if self.status:
            return "Active"
        else:
            return "In-active"