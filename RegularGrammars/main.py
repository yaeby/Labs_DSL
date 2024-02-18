from DFA import DFA 
from Grammar import Grammar

def commands():
    print("h - Help")
    print("g - Generate strings")
    print("f - Check appartanence")
    print("exit - End program")

def command_1():
    command = int(input("Insert the number of words: "))
    return command  

def command_2():
    command = str(input("Insert the word: "))
    return command   

D0 = Grammar(["S", "I", "J", 'K'],
            ["b", "c", "e", "n", "m"],
            {"S":["cI"], "I":["bJ", "eK", "e"], "J":["nJ", "cS"], "K":["nK", "m"]})

D1 = DFA({0,1,2,3,4},
         {"c","b","n","e","m"},
         {(0,"c"):1,
          (1,"b"):2,(1,"e"):3,
          (2,"n"):2,(2,"c"):0,
          (3,"n"):4,(3,"e"):3,(3,"m"):3,
          (4,"n"):4,(4,"m"):3},
          0,
          {0,3})

print(D0.generate_strings())

print(D1.run("cbccennnnnnm"))


commands()
while True:
    command = input("Insert command: ")
    if command == 'h':
        commands()

    elif command == 'g':
        n = command_1()
        for i in range(n-1):
            print(D0.generate_strings())

    elif command == 'f':
        word = command_2()
        print(D1.run(word))

    elif command == "exit":
        print("Program finished.")
        break