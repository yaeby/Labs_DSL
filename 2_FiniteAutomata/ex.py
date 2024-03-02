def is_deterministic(states, input_symbols, transitions, initial_state, final_states):
    # Check if the initial state is defined
    if initial_state not in states:
        return False

    # Check if all transitions are defined for each state and input symbol
    for state in states:
        for symbol in input_symbols:
            if state not in transitions or symbol not in transitions[state]:
                return False

    # Check if transitions are deterministic
    seen_transitions = set()
    for state in states:
        for symbol in input_symbols:
            next_state = transitions[state][symbol]

            # If a transition for the same symbol from the same state has been seen before, not deterministic
            if (state, symbol) in seen_transitions:
                return False

            seen_transitions.add((state, symbol, next_state))

    return True

def fa_to_regular_grammar(states, input_symbols, transitions, initial_state, final_states):
    # Initialize the productions list
    productions = []

    # Add productions for each transition
    for state in states:
        for symbol in input_symbols:
            next_state = transitions[state][symbol]
            if next_state not in final_states:
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

# Example usage with the provided FA representation
states = {'q0', 'q1', 'q2'}
input_symbols = {'0', '1'}
transitions = {
    'q0': {'0': 'q0', '1': 'q1'},
    'q1': {'0': 'q0', '1': 'q2'},
    'q2': {'0': 'q2', '1': 'q1'},
}
initial_state = 'q0'
final_states = {'q1'}

result = is_deterministic(states, input_symbols, transitions, initial_state, final_states)

if result:
    print("The Finite Automaton is deterministic.")
else:
    print("The Finite Automaton is not deterministic.")

regular_grammar = fa_to_regular_grammar(states, input_symbols, transitions, initial_state, final_states)
print(regular_grammar)
# Print the resulting regular grammar with '|' symbol
for non_terminal, production_rhs_list in regular_grammar.items():
    production_strings = [f"{non_terminal} -> {' | '.join(production_rhs_list)}"]
    print("\n".join(production_strings))