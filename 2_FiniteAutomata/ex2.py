from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA

from automata.fa.nfa import NFA
from visual_automata.fa.nfa import VisualNFA

new_dfa = VisualDFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q0', '1': 'q2'},
        'q2': {'0': 'q2', '1': 'q1'},
    },
    initial_state='q0',
    final_states={'q1'}
)

print(new_dfa.table)
new_dfa.show_diagram(view=True)
#print(new_dfa.input_check("1001"))
new_dfa.show_diagram("1001", view=True)
# minimal_dfa = VisualDFA.minify(new_dfa)
# minimal_dfa.show_diagram(view=True)
# nfa = VisualNFA(
#     states={"q0", "q1", "q2"},
#     input_symbols={"0", "1"},
#     transitions={
#         "q0": {"": {"q2"}, "1": {"q1"}},
#         "q1": {"1": {"q2"}, "0": {"q0", "q2"}},
#         "q2": {},
#     },
#     initial_state="q0",
#     final_states={"q0"},
# )

# nfa_eliminated = VisualNFA.eliminate_lambda(nfa)
# print(nfa_eliminated.table)