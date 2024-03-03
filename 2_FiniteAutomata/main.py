import re 
from fa import FiniteAutomata
from print import Print

# Example usage with the provided FA representation
states = {'q0','q1','q2','q3','q4'}
input_symbols = {'a','b'}
transitions = {
    'q0': {'a': {'q1'}},
    'q1': {'b': {'q1','q2'}},
    'q2': {'a': {'q4'},'b': {'q3'}},
    'q3': {'a': {'q1'}},
    'q4': {}
}
initial_state = 'q0'
final_states = {'q4'}

# states = {'q0', 'q1', 'q2'}
# input_symbols = {'0', '1'}
# transitions = {
#     'q0': {'0': 'q0', '1': 'q1'},
#     'q1': {'0': 'q0', '1': 'q2'},
#     'q2': {'0': 'q2', '1': 'q1'},
# }
# initial_state = 'q0'
# final_states = {'q1'}


fa = FiniteAutomata(states, input_symbols, transitions, initial_state, final_states)
result = fa.is_deterministic()

if result:
    print("The Finite Automaton is deterministic.")
    regular_grammar = fa.dfa_to_regular_grammar()
    print(regular_grammar)
else:
    print("The Finite Automaton is not deterministic.")
    regular_grammar = fa.nfa_to_regular_grammar()
    Print.print_grammar(regular_grammar=regular_grammar)

# production_strings = []
# # Print the resulting regular grammar with '|' symbol
# for non_terminal, production_rhs_list in regular_grammar.items():
#     production_string = f"{non_terminal} -> {' | '.join(production_rhs_list)}"
#     production_strings.append(production_string)
#     #print("\n".join(production_strings))
# print(production_strings)

# for i, string in enumerate(production_strings):
#     pattern = re.compile(r'q\d')  # Match any q followed by a digit
#     replacement_letter = chr(ord('A') + i)  # Get the uppercase letter based on index
#     modified_string = pattern.sub(replacement_letter, string)
#     production_strings[i] = modified_string
# print("\n".join(production_strings))
