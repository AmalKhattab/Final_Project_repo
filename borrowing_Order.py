class Borrowing_Order:
    def __init__(self, id, date, client_id_no, book_id, status):
        super().__init__(id)
        self.date = date
        self.client_id_no = client_id_no
        self.book_id = book_id
        self.status = status

    def get_client_id_no(self):
        return self.client_id_no

    def get_book_id(self):
        return self.book_id

    def get_status(self):
        return self.status