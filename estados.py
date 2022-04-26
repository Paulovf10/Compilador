class Estados:
    def declaracao(a, b, lin):
        if a[b] == {'Palavra reservada - Função': '#include'}:
            if 'Palavra reservada - Biblioteca' not in a[b + 1]:
                print(f"Error - Declaração, {a[b]} na linha {lin}")


    def tipos(a, b, lin):
        if 'Palavra reservada - Tipo' in str(a[b]):
            if a[b] == {'Palavra reservada - Tipo': 'int'} or a[b] == {'Palavra reservada - Tipo': 'const'} or a[b] == {
                    'Palavra reservada - Tipo': 'double'} or a[b] == {'Palavra reservada - Tipo': 'float'} or a[b] == {
                    'Palavra reservada - Tipo': 'short'} or a[b] == {'Palavra reservada - Tipo': 'long'}:
                if "main" in str(a[b + 1]) or "void" in str(a[b + 1]) :
                    d = 1
                elif "=" in str(a[b + 1]):
                    if "Numero" not in str(a[b + 2]):
                        print(f"Error - Tipos, {a[b]} na linha {lin}", 1)
                else:
                    print(f"Error - Tipos, {a[b]} na linha {lin}")
            elif a[b] == {'Palavra reservada - Tipo': 'char'}:
                if "=" in str(a[b + 1]):
                    if "string" not in str(a[b + 2]):
                        print(f"Error - Tipos, {a[b]} na linha {lin}")

        if a[b] == {'Palavra reservada - Tipo': 'char'}:
            if "String" not in str(a[b + 1]):
                print(f"Erro - Tipos, {a[b]} na linha {lin}")

    def parenteses(a, b, lin):
        if a[b] == {'Delimitador - Inicio': '('}:
            if {'Delimitador - Fim': ')'} not in a:
                print(f"Error - PARENTESES, {a[b]} na linha {lin}")

    def ponto_vir(a, b, lin):

        if a[len(a) - 1] != {'Separador': ';'}:

            flag = 0
            if a[len(a) - 1] == {'Delimitador - Fim': '}'}:
                flag = 1
            if a[len(a) - 1] == {'Delimitador - Inicio': '{'}:
                flag = 1
            if a[len(a) - 1] == {'Delimitador - Fim': ')'}:
                flag = 1
            if 'Biblioteca' in str(a[len(a) - 1]):
                flag = 1
            if flag == 0:
                print(f"Error - ;, {a[b]} na linha {lin}")

    def colchetes(a, b, lin):
        if a[b] == {'Delimitador - Inicio': '['}:
            if a[b + 1] == {'Delimitador - Fim': ']'} and 'Indetificador' in str(a[b - 1]):
                d = 1
            else:
                print(f"Errado - Colchetes, {a[b]} na linha {lin}")

    def loop_for(a, b, lin):
        if a[b] == {'Palavra reservada - Repetição': 'for'}:
            if a[b + 1] != {'Delimitador - Inicio': '('}:
                print(f"Error - For, {a[b]} na linha {lin}")
            if 'Indetificador' not in str(a[b + 2]):
                print(f"Error - For, {a[b]} na linha {lin}")
            if a[b + 5] != {'Separador': ';'}:
                print(f"Error - For, {a[b]} na linha {lin}")
            if 'Operador relacional' not in str(a[b + 7]):
                print(f"Error - For, {a[b]} na linha {lin}")
            if a[b + 9] != {'Separador': ';'}:
                print(f"Error - For, {a[b]} na linha {lin}")

    def operadores_aritimetico(a, b, lin):
        if 'Operador aritimetico' in str(a[b]):
            if ('Indetificador' or 'Numero') not in str(a[b - 1]):
                print(f"Error - Aritimetico, {a[b]} na linha {lin}")
            elif ('Indetificador' or 'Numero') not in str(a[b + 1]):
                print(f"Error - Aritimetico, {a[b]} na linha {lin}")

    def operadores_atribuicao(a, b, lin):
        if a[b] == {'Operador atribuição': '='}:
            if 'Indetificador' not in str(a[b - 1]):
                if 'Tipo' in str(a[b - 1]):
                    d = 1
                elif 'Numero' in str(a[b - 1]):
                    d = 1
                else:
                    print(f"Error - atribuição, {a[b]} na linha {lin}")

    def operadores_logico(a, b, lin):  ##
        if 'Operador logico' in a[b]:
            if 'Indetificador' in str(a[b - 1]):
                d = 1
                if 'Numero' in str(a[b - 1]):
                    d = 1
                elif "String" in str(a[b - 1]):
                    d = 1
                else:
                    print(f"Error - Logico, {a[b]} na linha {lin}")
            else:
                print(f"Error - Logico, {a[b]} na linha {lin}")


    def operadores_relacional(a, b, lin):
        if 'Operador relacional' in a[b]:
            if 'Indetificador' in str(a[b - 1]):
                d = 1
            elif 'Numero' in str(a[b - 1]):
                d = 1
            elif 'String' in str(a[b - 1]):
                d = 1
            else:
                print(f"Error - Relacional, {a[b]} na linha {lin}")
            if 'Indetificador' in str(a[b + 1]):
                d = 1
            elif 'Numero' in str(a[b + 1]):
                d = 1
            elif 'String' in str(a[b + 1]):
                d = 1
            else:
                print(f"Error - Relacional, {a[b]} na linha {lin}")


    def condicioal(a, b, lin):
        if {'Palavra reservada - Condicional': 'if'} == a[b]:
            if a[b + 1] != {'Delimitador - Inicio': '('}:
                print(f"Error- Condicional, {a[b]} na linha {lin}")
            if 'Indetificador' not in str(a[b + 2]):
                print(f"Error - Condicional, {a[b]} na linha {lin}")

    def mais_menos(a, b, lin):
        if {'Operador relacional': '=='} == a[b]:
            if 'Indetificador' not in str(a[b - 1]):
                print(f"Error- mais e menos, {a[b]} na linha {lin}")
            if 'Numero' or 'Indetificador' in str(a[b - 1]):
                d = 1
            else:
                print(f"Error - mais menos, {a[b]} na linha {lin}")

    def chaves(a, b, lin):
        if a[b] == {'Delimitador - Inicio': '{'}:
            i = 1
            flag = 1
            while i < len(a)-1:
                if {'Delimitador - Fim': '}'} == a[i]:
                    flag = 2
                i += 1
            if flag != 2:
                print(f"Error - Chaves, {a[b]} na linha {lin}")
