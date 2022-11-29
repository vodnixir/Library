import json
import sys
import unittest

sys.path.insert(0, 'classes')
import libraryManager
import database


class TestLibraryManager(unittest.TestCase):
    def setUp(self) -> None:
        self.manager = libraryManager.LibraryManager()
        self.adminCredentials = {"login": "admin", "password": "000000"}
        self.tmpbase = database.Database()
        self.tmpbase.load()

    def testBaseDel(self):
        self.manager.db.clearDB()
        self.assertEqual(0, len(self.manager.db.data["readers"]) if "readers" in self.manager.db.data else 0)
        # база пуста

    def testLogin(self):
        self.manager.db.clearDB()
        login = "reader"
        password = "123456"
        badLogin = "notReader"
        badPassword = "not123456"
        # логин для несуществующего пользователя на пустой базе
        answer = self.manager.analyseCmd(
            json.dumps({"cmd": "login", "credentials": {"login": login, "password": password}}))
        self.assertEqual(answer, {'msg': 'Login failed', 'result': 'fail'})
        # добавляем пользователя
        answer = self.manager.analyseCmd(json.dumps({"cmd": "addReader", "credentials": self.adminCredentials,
                                                     "usercredentials": {"login": login, "password": password}}))
        self.assertEqual(answer, {'msg': 'Reader added', 'result': 'success'})
        # проверка существующего пользователя
        answer = self.manager.analyseCmd(
            json.dumps({"cmd": "login", "credentials": {"login": login, "password": password}}))
        self.assertEqual(answer, {'msg': 'Successful login', 'result': 'success'})
        # проверка невалидного пароля на заполненой базе
        answer = self.manager.analyseCmd(
            json.dumps({"cmd": "login", "credentials": {"login": login, "password": badPassword}}))
        self.assertEqual(answer, {'msg': 'Login failed', 'result': 'fail'})
        # проверка невалидного пользователя на заполненой базе
        answer = self.manager.analyseCmd(
            json.dumps({"cmd": "login", "credentials": {"login": badLogin, "password": password}}))
        self.assertEqual(answer, {'msg': 'Login failed', 'result': 'fail'})


    def testUser(self):
        self.manager.db.clearDB()
        login = "thirdReader"
        password = "qwerty"
        # проверяем что пользователя еще не существует
        answer = self.manager.analyseCmd(
            json.dumps({"cmd": "login", "credentials": {"login": login, "password": password}}))
        self.assertEqual(answer, {'msg': 'Login failed', 'result': 'fail'})
        # добавляем пользователя
        answer = self.manager.analyseCmd(json.dumps({"cmd": "addReader", "credentials": self.adminCredentials,
                                                     "usercredentials": {"login": login, "password": password}}))
        self.assertEqual(answer, {'msg': 'Reader added', 'result': 'success'})
        # проверяем что пользователь теперь существует
        answer = self.manager.analyseCmd(
            json.dumps({"cmd": "login", "credentials": {"login": login, "password": password}}))
        self.assertEqual(answer, {'msg': 'Successful login', 'result': 'success'})
        # удаляем экспериментальнгого пользователя
        answer = self.manager.analyseCmd(
            json.dumps({"cmd": "delUser", "credentials": self.adminCredentials, "usercredentials": {"login": login}}))
        self.assertEqual(answer, {'msg': 'User deleted', 'result': 'success'})
        # проверяем что пользователь точно удален
        answer = self.manager.analyseCmd(
            json.dumps({"cmd": "login", "credentials": {"login": login, "password": password}}))
        self.assertEqual(answer, {'msg': 'Login failed', 'result': 'fail'})

    def brokenJsonTest(self):
        self.manager.db.clearDB()
        answer = self.manager.analyseCmd({})
        self.assertEqual(answer, {'msg': 'Login failed', 'result': 'fail'})
        answer = self.manager.analyseCmd({"cmd": "login"})
        self.assertEqual(answer, {'msg': 'Login failed', 'result': 'fail'})
        answer = self.manager.analyseCmd({"cmd": "addUser"})
        self.assertEqual(answer, {'msg': 'Login failed', 'result': 'fail'})
        answer = self.manager.analyseCmd({"cmd": "NotACommand"})
        self.assertEqual(answer, {'msg': 'Login failed', 'result': 'fail'})
        # добавляем пользователя
        answer = self.manager.analyseCmd(json.dumps({"cmd": "addReader", "credentials": self.adminCredentials,
                                                     "usercredentials": {"login": login, "password": password}}))
        self.assertEqual(answer, {'msg': 'Reader added', 'result': 'success'})
        answer = self.manager.analyseCmd({})
        self.assertEqual(answer, {'msg': 'Login failed', 'result': 'fail'})
        answer = self.manager.analyseCmd({"cmd": "login"})
        self.assertEqual(answer, {'msg': 'Login failed', 'result': 'fail'})
        answer = self.manager.analyseCmd({"cmd": "addUser"})
        self.assertEqual(answer, {'msg': 'Login failed', 'result': 'fail'})
        answer = self.manager.analyseCmd({"cmd": "NotACommand"})
        self.assertEqual(answer, {'msg': 'Login failed', 'result': 'fail'})

    # def testAuthor(self):
    #     self.manager.db.clearDB()
    #     #проверка добавления автора
    #     answer = self.manager.analyseCmd(
    #         json.dumps({"cmd": "addAuthor", "credentials": {"login": login, "password": password}}))
    #     self.assertEqual(answer, {'msg': 'Login failed', 'result': 'fail'})

    def testBook(self):
        self.manager.db.clearDB()
        login = "librarian"
        password = "qwerty"
        librarianCredentials = {"login": login, "password": password}
        # добавление библиотекаря для добавления книг
        answer = self.manager.analyseCmd(
                    json.dumps({"cmd": "addLibrarian", "credentials": self.adminCredentials,
                                                     "usercredentials": {"login": login, "password": password}}))
        self.assertEqual(answer, {'msg': 'Librarian added', 'result': 'success'})
        # добавление книги в базу
        answer = self.manager.analyseCmd(
            json.dumps({"cmd": "addBook", "credentials": librarianCredentials,
                        "book": {"Title": "Dead Souls"}, "author": {"Name": "Nikolay", "Surname": "Gogolь"}}))
        self.assertEqual({'msg': 'Book added', 'result': 'success'}, answer)

    def tearDown(self) -> None:
        self.manager.db = self.tmpbase
        self.manager.db.save()


if __name__ == "__main__":
    unittest.main(verbosity=1)
