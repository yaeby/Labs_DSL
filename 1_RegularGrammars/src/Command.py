class Command:

    @staticmethod
    def commands():
        print("")
        print("h - Help")
        print("g - Generate strings")
        print("f - Check appartanence")
        print("exit - End program")
        print("")

    @staticmethod
    def command_1():
        print("")
        number_of_words = input("Insert number of words: ")
        print("")
        return int(number_of_words)

    @staticmethod
    def command_2():
        print("")
        word = str(input("Insert word: "))
        print("")
        return word