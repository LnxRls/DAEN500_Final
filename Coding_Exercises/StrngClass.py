"""
Basic string class to define a getter and a string methods
"""


class StrClass:
    def __init__(self):
        self.text = None

    def getString(self):
        return input("please offer some input")

    def printString(self):
        print(self.getString().upper())


def main():
    strng = StrClass()

    strng.printString()


if __name__ == "__main__":
    main()
