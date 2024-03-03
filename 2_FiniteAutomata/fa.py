class FiniteAutomata:
    def __init__(self,Q,Sigma,delta,q0,F) :
            self.Q = Q # set of states
            self.Sigma = Sigma # set of symbols
            self.delta = delta # transition function as a dictionary
            self.q0 = q0 # initial state
            self.F = F # set of final states 

    def is_deterministic(self):
        # Check if the initial state is defined
        if self.q0 not in self.Q:
            return False

        # Check if all transitions are defined for each state and input symbol
        for state in self.Q:
            for symbol in self.Sigma:
                if state not in self.delta or symbol not in self.delta[state]:
                    return False

        # Check if transitions are deterministic
        seen_transitions = set()
        for state in self.Q:
            for symbol in self.Sigma:
                next_states = self.delta[state][symbol]

                # If a transition for the same symbol from the same state has been seen before, not deterministic
                for next_state in next_states:
                    if (state, symbol, next_state) in seen_transitions:
                        return False

                    seen_transitions.add((state, symbol, next_state))

        return True
    
    def nfa_to_regular_grammar(self):
        # Initialize the productions list
        productions = []

        # Add productions for each transition
        for state in self.Q:
            for symbol in self.Sigma:
                if state in self.delta and symbol in self.delta[state]:
                    next_states = self.delta[state][symbol]
                    for next_state in next_states:
                        if next_state not in self.F:
                            # For non-final states, add a production A -> aB where A is the current state,
                            # a is the input symbol, and B is the next state
                            productions.append((state, f"{symbol}{next_state}"))
                        else:
                            # For final states, add a production A -> a where A is the current state
                            productions.append((state, symbol))

        # Convert the productions list to a dictionary format
        grammar = {}
        for production in productions:
            non_terminal, production_rhs = production
            if non_terminal not in grammar:
                grammar[non_terminal] = []
            grammar[non_terminal].append(production_rhs)

        return grammar
    
    def dfa_to_regular_grammar(self):
        # Initialize the productions list
        productions = []

        # Add productions for each transition
        for state in self.Q:
            for symbol in self.Sigma:
                if state in self.delta and symbol in self.delta[state]:
                    next_state = self.delta[state][symbol]
                    if next_state not in self.F:
                        # For non-final states, add a production A -> aB where A is the current state,
                        # a is the input symbol, and B is the next state
                        productions.append((state, f"{symbol}{next_state}"))
                    else:
                        # For final states, add a production A -> a where A is the current state
                        productions.append((state, symbol))

        # Convert the productions list to a dictionary format
        grammar = {}
        for production in productions:
            non_terminal, production_rhs = production
            if non_terminal not in grammar:
                grammar[non_terminal] = []
            grammar[non_terminal].append(production_rhs)

        return grammar