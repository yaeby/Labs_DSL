class Command:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def commands():
        print("")
        print("h - Help")
        print("g - Generate strings")
        print("f - Check appartanence")
        print("exit - End program")
        print("")

    def command_1(self):
        print("")
        command = int(input("Insert the number of words: "))
        print("")
        return command  

    def command_2(self):
        print("")
        command = str(input("Insert the word: "))
        print("")
        return command