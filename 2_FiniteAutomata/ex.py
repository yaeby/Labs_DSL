def is_deterministic(states, alphabet, transition_function, initial_state, final_states):
    # Check if there are duplicate transitions for the same state and symbol
    transitions = set()
    for state in states:
        for symbol in alphabet:
            if (state, symbol) in transitions:
                return False
            next_states = transition_function.get((state, symbol), [])
            if len(next_states) != 1:
                return False
            transitions.add((state, symbol))

    # Check if all states have transitions for all symbols in the alphabet
    for state in states:
        for symbol in alphabet:
            if (state, symbol) not in transitions:
                return False

    return True

# Example usage:
states = {'q0', 'q1', 'q2', 'q3', 'q4'}
alphabet = {'a', 'b'}
transition_function = {
    ('q0', 'a'): ['q1'],
    ('q0', 'b'): ['q0'],
    ('q1', 'a'): ['q2'],
    ('q1', 'b'): ['q1'],
    ('q2', 'a'): ['q4'],
    ('q2', 'b'): ['q3'],
    ('q3', 'a'): ['q1'],
    ('q3', 'b'): ['q4'],
    ('q4', 'a'): ['q4'],
    ('q4', 'b'): ['q4'],
}
initial_state = 'q0'
final_states = {'q0''q4'}

result = is_deterministic(states, alphabet, transition_function, initial_state, final_states)
print("Is Deterministic:", result)
