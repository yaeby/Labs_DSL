class DFA : 

    def __init__(self,Q,Sigma,delta,q0,F) :
        self.Q = Q # set of states
        self.Sigma = Sigma # set of symbols
        self.delta = delta # transition function as a dictionary
        self.q0 = q0 # initial state
        self.F = F # set of final states 
            
    def __repr__(self) :
        return f"DFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"
    
    def check (self,w) :
        q = self.q0
        while w!="" :
            q = self.delta[(q,w[0])]
            w = w[1:]
        return q in self.F        