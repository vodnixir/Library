class Person():
    def __init__(self):
        self.name = ""
        self.surname = ""
        self.login = ""
        self.password = ""
        self.rights = {addLibrarian: False, addReader: False, delLibrarian: False, delReader: False,
                       addBook: False, delBook: False, checkOutBook: False, takeBook: False}
