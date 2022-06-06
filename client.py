from user import User

class Client(User):

    def __init__(self,id , name , age ,id_no ,phone_number):
        super().__init__(id, name, age, id_no)
        self.phone_number = phone_number

    def get_phone_no(self):
        return self.phone_number