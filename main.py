import json
import sys
sys.path.insert(0, 'classes')
import libraryManager


def main():
    manager = libraryManager.LibraryManager()
    txt = input()
    answer = manager.analyseCmd(txt)
    print(json.dumps(answer))


if __name__ == "__main__":
    main()

