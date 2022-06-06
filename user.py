class User:

    def __init__(self, id , name , age , id_no):
        self.id = id
        self.full_name = name
        self.age = age
        self.id_no = id_no


    def get_id(self):
        return self.id

    def get_name(self):
        return self.full_name

    def get_age(self):
        return self.age

    def get_id_no(self):
        return self.id_no