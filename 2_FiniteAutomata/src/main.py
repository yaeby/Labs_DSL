
from fa import FiniteAutomata
from print import Print as p

def main():
    fa = FiniteAutomata(states, input_symbols, transitions, initial_state, final_states)
    result = fa.is_deterministic()

    if result:
        print("\nThe Finite Automaton is deterministic.\n")
        regular_grammar = fa.dfa_to_regular_grammar()
        p.print_grammar(Vn=states, Vt=input_symbols, regular_grammar=regular_grammar)
    else:
        print("\nThe Finite Automaton is not deterministic.\n")
        regular_grammar = fa.nfa_to_regular_grammar()
        p.print_grammar(Vn=states, Vt=input_symbols, regular_grammar=regular_grammar)
        dfa_result = fa.nfa_to_dfa()
        p.graph_dfa(dfa=dfa_result)

if __name__ == "__main__":
    # NFA
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

    #DFA
    # states = {'q0', 'q1', 'q2'}
    # input_symbols = {'0', '1'}
    # transitions = {
    #     'q0': {'0': 'q0', '1': 'q1'},
    #     'q1': {'0': 'q0', '1': 'q2'},
    #     'q2': {'0': 'q2', '1': 'q1'},
    # }
    # initial_state = 'q0'
    # final_states = {'q1'}

    main()