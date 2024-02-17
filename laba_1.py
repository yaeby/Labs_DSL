class DFA : 

    def __init__(self,Q,Sigma,delta,q0,F) :
        self.Q = Q # set of states
        self.Sigma = Sigma # set of symbols
        self.delta = delta # transition function as a dictionary
        self.q0 = q0 # initial state
        self.F = F # set of final states 
            
    def __repr__(self) :
        return f"DFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"
    
    def run (self,w) :
        q = self.q0
        while w!="" :
            q = self.delta[(q,w[0])]
            w = w[1:]
        return q in self.F    
    
    def minimize(self) :
        # return the minimal DFA
        # the minimisation.pdf which is a section
        # of the lecture notes :
        # Thorsten Altenkirch, Venanzio Capretta, and Henrik Nilsson. 
        # "Languages and Computation." (2019).
        pass
    
D0 = DFA({0,1,2},{"a","b"},
         {(0,"a"):0,(0,"b"):1,
          (1,"a"):2,(1,"b"):1,
          (2,"a"):2,(2,"b"):2},
          0,
          {0,1})

D1 = DFA({0,1,2,3},{"a","b"},
         {(0,"a"):2,(0,"b"):1,
          (1,"a"):0,(1,"b"):3,
          (2,"a"):0,(2,"b"):3,
          (3,"a"):1,(3,"b"):2},
          0,
          {0,3})

# example from minimisation.pdf
# test case : D2.minimize()
D2 = DFA({0,1,2,3,4,5},{"a","b"},
         {(0,"a"):1,(0,"b"):4,
          (1,"a"):2,(1,"b"):3,
          (2,"a"):2,(2,"b"):2,
          (3,"a"):2,(3,"b"):3,
          (4,"a"):5,(4,"b"):4,
          (5,"a"):5,(5,"b"):4},
          0,
          {2,3})

print(D1.run("aabb"))