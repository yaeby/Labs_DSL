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
    
    def fa_to_regular_grammar(self):
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

    def epsilon_closure(self, state):
        closure = set()
        stack = [state]

        while stack:
            current_state = stack.pop()
            closure.add(current_state)

            if '' in self.delta.get(current_state, {}):
                epsilon_transitions = self.delta[current_state]['']
                stack.extend(state for state in epsilon_transitions if state not in closure)

        return frozenset(closure)

    def nfa_to_dfa(self):
        dfa_states = set()
        dfa_transitions = {}
        dfa_initial_state = self.epsilon_closure(self.q0)
        dfa_final_states = set()

        queue = [dfa_initial_state]
        processed_states = set()

        while queue:
            current_states = queue.pop()
            if current_states in processed_states:
                continue

            dfa_states.add(current_states)

            for symbol in self.Sigma:
                next_states = set()
                for state in current_states:
                    epsilon_transitions = self.delta.get(state, {}).get('', set())
                    next_states.update(self.delta.get(state, {}).get(symbol, set()))
                    next_states.update(self.epsilon_closure(state) for state in epsilon_transitions)

                next_states_closure = frozenset(next_states)
                dfa_transitions.setdefault(current_states, {})[symbol] = next_states_closure

                if next_states_closure not in dfa_states:
                    queue.append(next_states_closure)

            processed_states.add(current_states)

        for dfa_state in dfa_states:
            if dfa_state.intersection(self.F):
                dfa_final_states.add(dfa_state)

        return {
            'states': dfa_states,
            'input_symbols': self.Sigma,
            'transitions': dfa_transitions,
            'initial_state': dfa_initial_state,
            'final_states': dfa_final_states
        }
    
    