import json
import unittest
import sys
sys.path.insert(0, 'classes')
import libraryManager


class TestLibraryManager(unittest.TestCase):
    def setUp(self) -> None:
        self.manager = libraryManager.LibraryManager()
        self.adminCredentials = {"login": "admin", "password": "000000"}

    def testLogin(self):
        login = "reader"
        password = "123456"
        badLogin = "notReader"
        badPassword = "not123456"
        answer = self.manager.analyseCmd(json.dumps({"cmd": "login", "credentials": {"login": login, "password": password}}))
        self.assertEqual(answer, {'msg': 'Successful login', 'result': 'success'})
        answer = self.manager.analyseCmd(json.dumps({"cmd": "login", "credentials": {"login": login, "password": badPassword}}))
        self.assertEqual(answer, {'msg': 'Login failed', 'result': 'fail'})
        answer = self.manager.analyseCmd(
            json.dumps({"cmd": "login", "credentials": {"login": badLogin, "password": password}}))
        self.assertEqual(answer, {'msg': 'Login failed', 'result': 'fail'})

    def testUser(self):
        login = "thirdReader"
        password = "qwerty"
        # проверяем что пользователя еще не существует
        answer = self.manager.analyseCmd(json.dumps({"cmd": "login", "credentials": {"login": login, "password": password}}))
        self.assertEqual(answer, {'msg': 'Login failed', 'result': 'fail'})
        # добавляем пользователя
        answer = self.manager.analyseCmd(json.dumps({"cmd": "addReader", "credentials": self.adminCredentials , "usercredentials": {"login": login, "password": password}}))
        self.assertEqual(answer, {'msg': 'Reader added', 'result': 'success'})
        # проверяем что пользователь теперь существует
        answer = self.manager.analyseCmd(json.dumps({"cmd": "login", "credentials": {"login": login, "password": password}}))
        self.assertEqual(answer, {'msg': 'Successful login', 'result': 'success'})
        # удаляем экспериментальнгого пользователя
        answer = self.manager.analyseCmd(json.dumps({"cmd": "delUser", "credentials": self.adminCredentials, "usercredentials": {"login": login}}))
        self.assertEqual(answer, {'msg': 'User deleted', 'result': 'success'})
        # проверяем что пользователь точно удален
        answer = self.manager.analyseCmd(json.dumps({"cmd": "login", "credentials": {"login": login, "password": password}}))
        self.assertEqual(answer, {'msg': 'Login failed', 'result': 'fail'})


if __name__ == "__main__":
    unittest.main()

