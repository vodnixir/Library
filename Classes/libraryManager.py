import json

import database
import librarian
import reader
import book


class LibraryManager():
    def __init__(self):
        self.db = database.Database()
        self.db.load()

    def input(self):
        pass

    def _cmdAddReader(self, jsonObj):
        answer = self._cmdLogin(jsonObj)
        if answer["result"] == "success":
            newReader = reader.Reader(jsonObj["usercredentials"]["login"], jsonObj["usercredentials"]["password"])
            if not "readers" in self.db.data:
                self.db.data["readers"] = []
            self.db.data["readers"].append(newReader.__dict__)
            self.db.save()
            answer = self.successAnswer("Reader added")
        return answer

    def _cmdDelUser(self, jsonObj):
        answer = self._cmdLogin(jsonObj)
        if answer["result"] == "success":
            tmpReaderList = []
            if "readers" in self.db.data:
                tmpReaderList = [x for x in self.db.data["readers"] if
                                 (jsonObj["usercredentials"]["login"] == x.get('login'))]
            tmpLibrarianList = []
            if "librarians" in self.db.data:
                tmpLibrarianList = [x for x in self.db.data["librarians"] if
                                    (jsonObj["usercredentials"]["login"] == x.get('login'))]
            if len(tmpReaderList) == 0 and len(tmpLibrarianList) == 0:
                answer = self.successAnswer("User not found")
            else:
                if len(tmpReaderList) != 0:
                    self.db.data["readers"] = [x for x in self.db.data["readers"] if
                                               (jsonObj["usercredentials"]["login"] != x.get('login'))]
                    self.db.save()
                if len(tmpLibrarianList) != 0:
                    self.db.data["librarians"] = [x for x in self.db.data["librarians"] if
                                                  (jsonObj["usercredentials"]["login"] != x.get('login'))]
                    self.db.save()
                answer = self.successAnswer("User deleted")
        return answer

    def _cmdAddLibrarian(self, jsonObj):
        answer = self._cmdLogin(jsonObj)
        if answer["result"] == "success":
            newLibrarian = librarian.Librarian(jsonObj["usercredentials"]["login"],
                                               jsonObj["usercredentials"]["password"])
            if not "librarians" in self.db.data:
                self.db.data["librarians"] = []
            self.db.data["librarians"].append(newLibrarian.__dict__)
            self.db.save()
            answer = self.successAnswer("Librarian added")
        return answer

    def _cmdAddBook(self, jsonObj):
        answer = self._cmdLogin(jsonObj)
        if answer["result"] == "success":
            answer = self.successAnswer("Add failed")
            if self.hasRights(jsonObj, "addBook"):
                if "book" in jsonObj and "title" in jsonObj["book"] and "author" in jsonObj and "name" in jsonObj["author"] and "surname" in jsonObj["author"]:
                    newBook = book.Book(jsonObj["book"], jsonObj["author"])
                    self.db.data["books"].append(newBook.__dict__)
                    self.db.save()
                    answer = self.successAnswer("Book added")
        return answer

    def failAnswer(self, msg):
        answer = {"result": "fail", "msg": msg}
        # print(json.dumps(answer))
        return (answer)

    def successAnswer(self, msg):
        answer = {"result": "success", "msg": msg}
        # print(json.dumps(answer))
        return (answer)

    def _cmdLogin(self, jsonObj):
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

    def hasRights(self, jsonObj, right):
        result = False
        if jsonObj["credentials"]["login"] == "admin" and jsonObj["credentials"]["password"] == "000000":
            result = True
        else:
            found = False
            if "readers" in self.db.data:
                for item in self.db.data["readers"]:
                    if item["login"] == jsonObj["credentials"]["login"] and item["password"] == jsonObj["credentials"][
                        "password"]:
                        found = True
                        if "rights" in item:
                            if right in item["rights"]:
                                if item["rights"][right]:
                                    result = True
                        break
            if not found and "librarians" in self.db.data:
                for item in self.db.data["librarians"]:
                    if item["login"] == jsonObj["credentials"]["login"] and item["password"] == jsonObj["credentials"][
                        "password"]:
                        if "rights" in item:
                            if right in item["rights"]:
                                if item["rights"][right]:
                                    result = True
                        break
        return result

    def _cmdClearDB(self, jsonObj):
        answer = self._cmdLogin(jsonObj)
        if answer["result"] == "success":
            self.db.clearDB()
        return answer

    def analyseCmd(self, txt):
        jsonObj = json.loads(txt)
        cmd = jsonObj["cmd"]
        # print(jsonObj["cmd"])
        if cmd == "login":
            answer = self._cmdLogin(jsonObj)
        elif cmd == "addReader":
            answer = self._cmdAddReader(jsonObj)
        elif cmd == "delUser":
            answer = self._cmdDelUser(jsonObj)
        elif cmd == "addLibrarian":
            answer = self._cmdAddLibrarian(jsonObj)
        elif cmd == "clearDB":
            answer = self._cmdClearDB(jsonObj)
        elif cmd == "addBook":
            answer = self._cmdAddBook(jsonObj)
        else:
            answer = self.failAnswer("Команда не распознана")
        return answer
