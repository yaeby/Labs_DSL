from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA

dfa = DFA(states={"q0"}, input_symbols={"i0"}, transitions={"q0": {"i0": "q0"}}, initial_state="q0",
          final_states={"q0"})
VisualDFA(states=dfa.states, input_symbols=dfa.input_symbols, transitions=dfa.transitions,
          initial_state=dfa.initial_state, final_states=dfa.final_states).show_diagram(view=True, filename=DFA)