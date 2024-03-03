class Print:

    def print_grammar(regular_grammar):
        for non_terminal, production_rhs_list in regular_grammar.items():
            for production_rhs in production_rhs_list:
                print(f"{non_terminal} -> {production_rhs}")