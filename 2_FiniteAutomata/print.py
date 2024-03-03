class Print:

    def print_grammar(Vn, Vt, regular_grammar):
        print(f'Vn = {Vn}')
        print(f'Vt = {Vt}')
        print("P = {")
        for non_terminal, production_rhs_list in regular_grammar.items():
            for production_rhs in production_rhs_list:
                print(f"{non_terminal} -> {production_rhs}")
        print("}")