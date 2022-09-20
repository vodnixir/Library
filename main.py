import json
import sys

sys.path.insert(0, 'classes')
import libraryManager


def main():
    manager = libraryManager.LibraryManager()
    txt = input()
    jsonObj = json.loads(txt)
    cmd = jsonObj["cmd"]
    # print(jsonObj["cmd"])
    if cmd == "login":
        answer = manager.login(jsonObj)
    elif cmd == "addReader":
        answer = manager.addReader(jsonObj)
    elif cmd == "addLibrarian":
        answer = manager.addLibrarian(jsonObj)
    elif cmd == "clearDB":
        answer = manager.clearDB(jsonObj)
    else:
        answer = manager.failAnswer("Команда не распознана")
    print(json.dumps(answer))


if __name__ == "__main__":
    main()

