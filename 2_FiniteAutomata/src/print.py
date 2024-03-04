from visual_automata.fa.dfa import VisualDFA

class Print:

    @staticmethod
    def print_grammar(Vn, Vt, regular_grammar):
        print("Regula Grammar of the given FA:")
        print(f'Vn = {Vn}')
        print(f'Vt = {Vt}')
        print("P = {")
        for non_terminal, production_rhs_list in regular_grammar.items():
            for production_rhs in production_rhs_list:
                print(f"{non_terminal} -> {production_rhs}")
        print("}\n")

    @staticmethod
    def graph_dfa(dfa):
        def map_states_to_characters(states):
            state_mapping = {}
            result = []
            for i, state in enumerate(states):
                char_representation = chr(ord('A') + i)
                state_mapping[state] = char_representation
                result.append(char_representation)
            return set(result), state_mapping

        # Use the function to map frozensets to characters
        dfa_states_representation, state_mapping = map_states_to_characters(dfa['states'])

        # Update the DFA transitions and final states with the mapped characters
        dfa['states'] = dfa_states_representation
        dfa['transitions'] = {
            state_mapping[state]: {
                symbol: state_mapping[next_state] for symbol, next_state in transitions.items()
            } for state, transitions in dfa['transitions'].items()
        }
        dfa['initial_state'] = state_mapping[dfa['initial_state']]
        dfa['final_states'] = {state_mapping[state] for state in dfa['final_states']}

        # Print the updated DFA information
        # print("DFA States:", dfa['states'])
        # print("DFA language:", dfa['input_symbols'])
        # print("DFA Transitions:", dfa['transitions'])
        # print("DFA Initial State:", dfa['initial_state'])
        # print("DFA Final States:", dfa['final_states'])

        graph_dfa = VisualDFA(states=dfa['states'], 
                input_symbols=dfa['input_symbols'], 
                transitions=dfa['transitions'], 
                initial_state=dfa['initial_state'], 
                final_states=dfa['final_states'])

        print("DFA Table:")
        print(graph_dfa.table)
        graph_dfa.show_diagram(filename="DFA")
        print("\nThe DFA was saved with the filename DFA.png")