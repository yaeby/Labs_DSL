from DFA import DFA 
from Grammar import Grammar
from Command import Command

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


Command.commands()

while True:
    
    command = input("Insert command: ")
    if command == 'h':
        Command.commands()

    elif command == 'g':
        number_of_words = Command.command_1()
        words = []
        while (len(words) < number_of_words):
            word = D0.generate_string()
            if word not in words:
                words.append(word)
        print(*map(str, words), sep='\n')
        print("")       

    elif command == 'f':
        word = Command.command_2()
        print(D1.run(word))
        print("")

    elif command == "exit":
        print("Program finished.")
        break