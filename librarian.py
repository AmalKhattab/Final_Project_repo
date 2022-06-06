from user import User

class Librarian(User):

    def __init__(self, id, name, age, id_no, employement_type):
        super().__init__(id, name, age, id_no)
        self.employement_type = employement_type

    def get_employement_type(self):
        return self.employement_type