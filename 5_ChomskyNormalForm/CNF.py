import helper

class CNF:
    left, right = 0, 1

    def __init__(self, modelPath='model.txt'):
        self.K, self.V, self.Productions = helper.loadModel(modelPath)
        self.variablesJar = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W", "X", "Y", "Z"]

    def isUnitary(self, rule, variables):
        if rule[self.left] in variables and rule[self.right][0] in variables and len(rule[self.right]) == 1:
            return True
        return False

    def isSimple(self, rule):
        if rule[self.left] in self.V and rule[self.right][0] in self.K and len(rule[self.right]) == 1:
            return True
        return False

    def START(self):
        self.V.append('S0')
        self.Productions = [('S0', [self.V[0]])] + self.Productions

    def TERM(self):
        newProductions = []
        dictionary = helper.setupDict(self.Productions, self.V, terms=self.K)
        for production in self.Productions:
            if self.isSimple(production):
                newProductions.append(production)
            else:
                for term in self.K:
                    for index, value in enumerate(production[self.right]):
                        if term == value and not term in dictionary:
                            dictionary[term] = self.variablesJar.pop()
                            self.V.append(dictionary[term])
                            newProductions.append((dictionary[term], [term]))
                            production[self.right][index] = dictionary[term]
                        elif term == value:
                            production[self.right][index] = dictionary[term]
                newProductions.append((production[self.left], production[self.right]))
        self.Productions = newProductions

    def BIN(self):
        result = []
        for production in self.Productions:
            k = len(production[self.right])
            if k <= 2:
                result.append(production)
            else:
                newVar = self.variablesJar.pop(0)
                self.V.append(newVar + '1')
                result.append((production[self.left], [production[self.right][0]] + [newVar + '1']))
                for i in range(1, k - 2):
                    var, var2 = newVar + str(i), newVar + str(i + 1)
                    self.V.append(var2)
                    result.append((var, [production[self.right][i], var2]))
                result.append((newVar + str(k - 2), production[self.right][k - 2:k]))
        self.Productions = result

    def DEL(self):
        newSet = []
        outlaws, self.Productions = helper.seekAndDestroy(target='e', productions=self.Productions)
        for outlaw in outlaws:
            for production in self.Productions + [e for e in newSet if e not in self.Productions]:
                if outlaw in production[self.right]:
                    newSet = newSet + [e for e in helper.rewrite(outlaw, production) if e not in newSet]
        self.Productions = newSet + ([p for p in self.Productions if p not in newSet])

    def unit_routine(self, rules):
        unitaries, result = [], []
        for aRule in rules:
            if self.isUnitary(aRule, self.V):
                unitaries.append((aRule[self.left], aRule[self.right][0]))
            else:
                result.append(aRule)
        for uni in unitaries:
            for rule in rules:
                if uni[self.right] == rule[self.left] and uni[self.left] != rule[self.left]:
                    result.append((uni[self.left], rule[self.right]))
        return result

    def UNIT(self):
        i = 0
        result = self.unit_routine(self.Productions)
        tmp = self.unit_routine(result)
        while result != tmp and i < 1000:
            result = self.unit_routine(tmp)
            tmp = self.unit_routine(result)
            i += 1
        self.Productions = result

    def transform(self):
        self.START()
        self.TERM()
        self.BIN()
        self.DEL()
        self.UNIT()
        print(helper.prettyForm(self.Productions))
        print(len(self.Productions))
        open('out.txt', 'w').write(helper.prettyForm(self.Productions))