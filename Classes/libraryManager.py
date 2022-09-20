import database
import reader
import librarian


class LibraryManager():
    def __init__(self):
        self.db = database.Database()
        self.db.load()

    def input(self):
        pass

    def addReader(self, jsonObj):
        answer = self.login(jsonObj)
        if answer["result"] == "success":
            newReader = reader.Reader(jsonObj["usercredentials"]["login"], jsonObj["usercredentials"]["password"])
            if not "readers" in self.db.data:
                self.db.data["readers"] = []
            self.db.data["readers"].append(newReader.__dict__)
            self.db.save()
            answer = self.successAnswer("Reader added")
        return answer

    def addLibrarian(self, jsonObj):
        answer = self.login(jsonObj)
        if answer["result"] == "success":
            newLibrarian = librarian.Librarian(jsonObj["usercredentials"]["login"], jsonObj["usercredentials"]["password"])
            if not "librarians" in self.db.data:
                self.db.data["librarians"] = []
            self.db.data["librarians"].append(newLibrarian.__dict__)
            self.db.save()
            answer = self.successAnswer("Librarian added")
        return answer

    def failAnswer(self, msg):
        answer = {"result": "fail", "msg": msg}
        # print(json.dumps(answer))
        return (answer)

    def successAnswer(self, msg):
        answer = {"result": "success", "msg": msg}
        # print(json.dumps(answer))
        return (answer)

    def login(self, jsonObj):
        if jsonObj["credentials"]["login"] == "admin" and jsonObj["credentials"]["password"] == "000000":
            answer = self.successAnswer("Успешный вход")
        else:
            found = False
            if "readers" in self.db.data:
                for item in self.db.data["readers"]:
                    if item["login"] == jsonObj["credentials"]["login"] and item["password"] == jsonObj["credentials"][
                        "password"]:
                        found = True
                        break
            if not found and "librarians" in self.db.data:
                for item in self.db.data["librarians"]:
                    if item["login"] == jsonObj["credentials"]["login"] and item["password"] == jsonObj["credentials"][
                        "password"]:
                        found = True
                        break
            if found:
                answer = self.successAnswer("Successful login")
            else:
                answer = self.failAnswer("Login failed")
        return (answer)

    def clearDB(self, jsonObj):
        answer = self.login(jsonObj)
        if answer["result"] == "success":
            self.db.clearDB()
        return answer
