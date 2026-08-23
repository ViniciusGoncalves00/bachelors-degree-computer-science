class Report:

    # ========================================================
    # ANÁLISE LÉXICA / SINTÁTICA
    # ========================================================

    @staticmethod
    def print_tokens(tokens):

        print()
        print("=" * 60)
        print("ANÁLISE LÉXICA / SINTÁTICA")
        print("=" * 60)

        print(
            f"{'NUM':<6}"
            f"{'TOKEN':<20}"
            f"{'LEXEMA'}"
        )

        print("-" * 60)

        for num, token in enumerate(tokens, start=1):

            print(
                f"{num:<6}"
                f"{token.type.name:<20}"
                f"{token.lexeme}"
            )

    # ========================================================
    # TABELA DE SÍMBOLOS
    # ========================================================

    @staticmethod
    def print_symbols(symbol_table):

        print()
        print("=" * 60)
        print("TABELA DE SÍMBOLOS")
        print("=" * 60)

        print(
            f"{'Identificador':<18}"
            f"{'Endereço MEPA':<18}"
            f"{'Tipo Presumido':<18}"
            f"{'Escopo'}"
        )

        print("-" * 75)

        for symbol in symbol_table.symbols.values():

            print(
                f"{symbol.name:<18}"
                f"{symbol.address:<18}"
                f"{symbol.type:<18}"
                f"{symbol.scope}"
            )

    # ========================================================
    # CÓDIGO INTERMEDIÁRIO
    # ========================================================

    @staticmethod
    def print_code(code):

        print()
        print("=" * 60)
        print("GERAÇÃO DE CÓDIGO INTERMEDIÁRIO")
        print("=" * 60)

        for instruction in code:
            print(instruction)