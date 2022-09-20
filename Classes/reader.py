import user


class Reader(user.User):
    def __init__(self, login, password):
        super().__init__(login, password)
        self.rights = {}

