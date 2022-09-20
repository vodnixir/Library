import user


class Librarian(user.User):
    def __init__(self, login, password):
        super().__init__(login, password)
        self.rights = {"addUser": True, "lendBook": True, "addBook": True}